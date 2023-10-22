#!/usr/bin/env groovy

def placeholder(){
    echo "This is placeholder!"
}

def get_vars(){
    // echo "This is placeholder!"
    def ENV_NAME = env.ENV_NAME?:''
}

def artifactory_download(String serevr_id, String pattern, String target, String goal = "*") {
    def retry = 1
    def success = false
    def server = Artifactory.server server_id
    def downloadSpec = """{"files": [{
                            "pattern": "${pattern}",
                            "target": "${target}/",
                            "flat": "true"
                            }]}"""
    // retry 3 times to download file from actifactory
    while ((retry <= 3) && !success) {
        echo "Downloading files from actifactory: ${pattern}, retry: ${retry}"
        try {
            server.download spec: downloadSpec
            def file_exist = sh script: "ls ${target}/${goal}", returnStatus: true
            if (file_exist == 0) {
                echo "Download from artifactory successful!"
                success = true
            } else {
                echo "Download from artifactory failed!"
                retry++
            }
        } catch (Exception e) {
            echo "Download from artifactory failed!"
            currentBuild.result = 'FAILED'
        }
    }
    return success
}

def artifactory_upload(String serevr_id, String target, String pattern) {
    def server = Artifactory.server server_id
    def uploadSpec = """{"files": [{
                            "pattern": "${pattern}",
                            "target": "${target}"
                            }]
                        }"""
    server.upload spec: uploadSpec
}

def run_playbook(cmd) {
    sh """
    set +x
    set -e
    cd tools/ansible
    ansible-playbook ${cmd}
    """
}

def getValueByKeyFromFile(filePath,fileKey) {
    def result
    def target
    try {
        result = sh(script: "set +x && set -e && cat ${filePath} | grep \"${fileKey}: \"", returnStdout: true)
        target = result.substring(result.lastIndexOf(": ") + 2).trim().replace("\"", "")
        return target
    } catch (Exception e) {
        print("No key: " + fileKey)
    }
}

// Return a value of target/vars.yml based on the key
def returnValueFromOpsVault(key){
    value=getValueByKeyFromFile("target/vars.yml",key)
    return value
}

// Return a value of secret based on the key
def returnValueFromVault(key){
    helper.vault_get_key(env.VAULT_TOKEN_ID,env.VAULT_PATH,'vars')
    value=getValueByKeyFromFile("target/vars.yml",key)
    return value
}

// Return a value of secret based on the key from vars target/file
def returnValueFromVaultVars(key){
    value=getValueByKeyFromFile("target/vars.yml",key)
    return value
}

def appendToGroupVars(str_value){
    sh """
    echo '${str_value}' >> tools/ansible/group_vars/all/main.yml
    """
}

// Abort build in Infra is locked in Vault/Keeper
def checkLockedInfra(){
    if (returnValueFromVaultVars('lock_infra')=="true") {
        echo "============= Deployment is locked in Keeper! ============="
        autoCancelled = true
        error('Aborting the build.')
    }
}

def init_vars(token_name) {
    withCredentials([string(
            credentialsId: token_name,
            variable: 'VAULT_TOKEN'
    )]) {
        // get_vars()
        sh """
        set +x && set -e
        unset no_proxy && unset NO_PROXY
        mkdir -p target && rm -rf target/*
        """
        if (ENV_NAME == null || ENV_NAME.isEmpty()) {
            echo "============= Get preloaded environment from the YARN pool ============="
            get_environment('preloaded',VAULT_TOKEN)
            echo "Define ENV_NAME for pipeline"
            ENV_NAME = sh(script: 'set +x && source ./_env_name.txt && echo $ENV_NAME', returnStdout: true).trim()
            println "Environment: " + ENV_NAME
            sh """
            set +x
            export ENV_NAME="$ENV_NAME"
            tools/scripts/init_vars_appliance.sh
            """
        } else {
            sh """
            set +x
            tools/scripts/init_vars_appliance.sh
            """
        }
    }
}

def run_security_scan(token_name, git_repo_name, scan_name, target) {
    withCredentials([string(credentialsId: token_name,variable: 'VAULT_TOKEN')]) {
        sh """
            set +x && set -e
            export git_repo_name=$git_repo_name
            export scan_name=$scan_name
            export scan_target=$target 
            /bin/bash ${WORKSPACE}/$git_repo_name/tools/run.sh
        """
    }
}

def vault_get_key(token_name, String secret_path, String key) {
// Get arbitrary key from vault secret
    withCredentials([string(
            credentialsId: token_name,
            variable: 'VAULT_TOKEN'
    )]) {
        sh """
        set +x && set -e
        echo "Get $key from Vault"
        mkdir -p target
        rm -rf ../../target target/vars.yml
        python3 tools/lib/vault_api.py -s "$JENKINS_GLOBAL_VAULT" -t "$VAULT_TOKEN" -p "$secret_path" -k "$key" > /dev/null
        mv -f ../../target/vars.yml target/"$key".yml
        rm -rf ../../target
        """
    }
}

def vault_devices_get(token_name, String secret_path) {
// Get value for the "device" key in vault secret
    withCredentials([string(
            credentialsId: token_name,
            variable: 'VAULT_TOKEN'
    )]) {
        sh """
        set +x && set -e
        echo "Get devices from Vault"
        mkdir -p target
        rm -rf ../../target target/devices.yml
        python3 tools/lib/vault_api.py -s "$JENKINS_GLOBAL_VAULT" -t "$VAULT_TOKEN" -p "$secret_path" -k "devices"
        mv -f ../../target/devices.yml target/devices.yml
        rm -rf ../../target
        """
    }
}

def vault_devices_post(token_name, String secret_path, String devices_value) {
// Update value for "device" key in Vault, with supplied "devices_value" 
    withCredentials([string(
            credentialsId: token_name,
            variable: 'VAULT_TOKEN'
    )]) {
        sh """
        set +x && set -e
        echo "Update devices in Vault"
        python3 tools/lib/vault_api.py -s "$JENKINS_GLOBAL_VAULT" -t "$VAULT_TOKEN" -p "$secret_path" -k "devices" -v "$devices_value"
        rm -rf ../../target
        """
    }
}

def vault_secret_post(token_name, String secret_path, String key_value) {
    withCredentials([string(
            credentialsId: token_name,
            variable: 'VAULT_TOKEN'
    )]) {
        sh """
        set +x && set -e
        echo "Update secret/key in Vault"
        python3 tools/lib/vault_api.py -s "$JENKINS_GLOBAL_VAULT" -t "$VAULT_TOKEN" -p "$secret_path" -v "$key_value"
        rm -rf ../../target
        """
    }
}


def vault_key_value_post(token_name, String secret_path, String key, String key_value) {
// Update in Vault a given Key with the supplied "key_value"
    withCredentials([string(
            credentialsId: token_name,
            variable: 'VAULT_TOKEN'
    )]) {
        sh """
        set +x && set -e
        echo "Update $key in Vault"
        python3 tools/lib/vault_api.py -s "$JENKINS_GLOBAL_VAULT" -t "$VAULT_TOKEN" -p "$secret_path" -k '$key' -v '$key_value'
        echo "Updated $key in Vault"
        rm -rf ../../target
        """
    }
}

def parseProxyString(proxy) {
    def result = [:]
    result.protocol = "http"
    result.host = "localhost"
    result.port = "80"
    def split = "$proxy".split('://')
    result.protocol = "${split[0]}"
    split = "${split[1]}".split(':')
    result.host = "${split[0]}"
    if (split.size() > 1) {
        result.port = "${split[1]}"
    } else if ("https".equalsIgnoreCase(result.protocol)) {
        result.port = "443"
    }
    return result
}

def slack_started(channel = '#jenkins') {
    if ( channel ) {
        wrap([$class: 'BuildUser']) {
            env.BUILD_USER = env.BUILD_USER ?: 'Jenkins' //fix "No such property: BUILD_USER"
            channel.split(",").each { channelItem ->
                slackSend(color: '#FFFF00', channel: "${channelItem}", message: "STARTED by ${BUILD_USER}.\n${env.ACTION} >> ${env.JOB_NAME} - #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
            }
        }
    }
}

def slack_success(channel = '#jenkins') {
    if ( channel ) {
        channel.split(",").each { channelItem ->
            slackSend(color: '#008000', channel: "${channelItem}", message: "SUCCESS\n${env.ACTION} >> ${env.JOB_NAME} - #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        }
    }
}

def slack_unstable(channel = '#jenkins') {
    if ( channel ) {
        channel.split(",").each { channelItem ->
            slackSend(color: '#008000', channel: "${channelItem}", message: "UNSTABLE\n${env.ACTION} >> ${env.JOB_NAME} - #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        }
    }
}


def slack_failure(channel = '#jenkins') {
    if ( channel ) {
        channel.split(",").each { channelItem ->
            slackSend(color: '#FF0000', channel: "${channelItem}", message: "FAILED\n${env.ACTION} >> ${env.JOB_NAME} - #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        }
    }
}


def slack_aborted(channel = '#jenkins') {
    if ( channel ) {
        wrap([$class: 'BuildUser']) {
            channel.split(",").each { channelItem ->
                slackSend(color: '#D0D3D4', channel: "${channelItem}", message: "ABORTED by ${BUILD_USER}.\n${env.ACTION} >> ${env.JOB_NAME} - #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
            }
        }
    }
}

def slack_result(channel = '#jenkins') {
    env.ACTION = env.ACTION ?: "Pipeline"
    switch (currentBuild.currentResult) {
        case 'SUCCESS':
            slack_success(channel)
            break
        case 'FAILURE':
            slack_failure(channel)
            break
        case 'ABORTED':
            slack_aborted(channel)
            break
        case 'UNSTABLE':
            slack_unstable(channel)
            break
        default:
            slack_failure(channel)
            break
    }
}

def slackSendEventError(error, system = null, channelList = ['#pipeline-events-error'], channelCsv = null) {

    // if not provided, get from environment
    if ( ! system ) {
        system = env.SYSTEM?env.SYSTEM:"unknown"
    }

    println "slackSendEventError error ${error} system ${system} channelList ${channelList} channelCsv ${channelCsv}"

    // If channelCsv is provided use it over channelList.
    if ( channelCsv ) {
        println "channelCsv provided: ${channelCsv}"
        channelList = channelCsv.tokenize(",")
    }

    // Always make sure we send the error to #pipeline-events-error
    if ( ! channelList.contains("#pipeline-events-error") ) {
        channelList.add("#pipeline-events-error")
    }

    // Make sure the error is on a separate line
    if ( error ) {
        error = "\n" + error + "\n"
    }

    channelList.each {
        channel ->
            // the BUILD_URL has a trailing /
            def msg = "ERROR ${system} ${error} <${env.BUILD_URL}console|${env.JOB_BASE_NAME}/${env.BUILD_NUMBER}>"
            println "Sending to ${channel}: ${msg}"
            slackSend(color: '#FF0000', channel: "${channel}", message: msg)
    }
}

def slackSendDeviceResetError(component = "unknown", error = "", channelList = ['#pipeline-events-error']) {
    slackSendEventError("Device Reset Failed for ${component} ${error}", null , channelList, null)
}

def slackSendServicePackDeployError(component = "unknown", error = "", channelList = ['#pipeline-events-error']) {
    slackSendEventError("Service Pack Deploy Failed for ${component} ${error}", null , channelList, null)
}

def slackSendServicePackPostDeployError(component = "unknown", error = "", channelList = ['#pipeline-events-error']) {
    slackSendEventError("Service Pack Post-Deploy Failed for ${component} ${error}", null , channelList, null)
}

def slackSendDeviceResetErrorToChannelCsv(component = "unknown", channelCsv, error = "") {
    slackSendEventError("Device Reset Failed for ${component} ${error}", null , [], channelCsv)
}

def slackSendServicePackDeployErrorToChannelCsv(component = "unknown", channelCsv, error = "") {
    slackSendEventError("Service Pack Deploy Failed for ${component} ${error}", null , [], channelCsv)
}

def slackSendServicePackPostDeployErrorToChannelCsv(component = "unknown", channelCsv, error = "") {
    slackSendEventError("Service Pack Post-Deploy Failed for ${component} ${error}", null , [], channelCsv)
}

def print(String msg) {
    println msg
}

def sendConsoleLogToElastic() {
    println "Sending Console Log to Elastic"
    try {
        // if the result send fails, we still pass the build
        logstashSend failBuild: false, maxLines: 200
        println "Console Log is now available at kibana: https://log.infra.example.com/"
    } catch (Exception e) {
        println "Could not send Console Log to Elastic. ${e.toString()}"
    }
}


def get_slack_channel(){
    if ( env.SLACK_CHANNEL ) {
        SLACK_CHANNEL = env.SLACK_CHANNEL
    } else if ( env.slack_channel ) {
        println "WARNING: lower case env.slack_channel is in use. Please change it to env.SLACK_CHANNEL in your Jenkins Job Properties."
        SLACK_CHANNEL = env.slack_channel
    }
    println "SLACK_CHANNEL is ${SLACK_CHANNEL}"
    return SLACK_CHANNEL
}


def vm_deploy(token_name,OVA_FILE,DEPLOY_BIN,CREATE_SNAP) {
    withCredentials([string(credentialsId: token_name,variable: 'VAULT_TOKEN')]) {
        vault_install()
        sh """
        set +x && set -e
        export VAULT_TOKEN=$VAULT_TOKEN
        bash ./tools/scripts/vmware/vm_deployment.sh
        """
    }
}

def vm_delete() {
    script{
        sh'''
        set +x && set -e
        bash ./tools/scripts/vmware/vm_delete.sh
        '''
    }
}

def post_build_success(vault_token_id) {
    if ( env.ENV_NAME.isEmpty() && params.RELOAD_ENVIRONMENT ) {
        script{
            ENV_NAME = sh(script: 'set +x && source ./_env_name.txt && echo $ENV_NAME', returnStdout: true).trim()
            release_environment(vault_token_id,ENV_NAME)
            build_new_project_deployment_generic(ENV_NAME)
        }    
    } else {
        if ( params.RELOAD_ENVIRONMENT ) {
            build_new_project_deployment_generic(env.ENV_NAME)
        }
    }
    archiveArtifacts artifacts: 'target/*', allowEmptyArchive: true
    cleanWs()
}

def post_build_failure(vault_token_id) {
    if ( env.ENV_NAME.isEmpty()) {
        sh"""
        set +x
        # cp ./tools/scripts/vmware/vm_init_vars.env target/vm_init_vars.env || true
        """
        // run_playbook('action_appliance.yml --tags "fetch_logs"')
    }
    post_build_success(vault_token_id)
}

def post_success() {
    archiveArtifacts artifacts: 'target/*', allowEmptyArchive: true
    cleanWs()
}

def get_vault_secret(token_name,ENV_NAME) {
    withCredentials([string(credentialsId: token_name,variable: 'VAULT_TOKEN')]) {
        sh'''
        set +x && set -e
        export VAULT_TOKEN=$VAULT_TOKEN
        ${WORKSPACE}/tools/scripts/vmware/init_vars.sh
        '''
        DEBUG=env.DEBUG?:'false'
        if ( DEBUG == 'true' ) {
            sh """
            set +x
            mkdir -p ${WORKSPACE}/target
            cp ./vm_init_vars.json ${WORKSPACE}/target/ || true
            """
        }
    }
}

def check_file(FILE_PATH) {
    script{
        sh"""
        set +x && set -e
        if [ -f ${FILE_PATH} ]; then
            echo '${FILE_PATH} exists.'
        else 
            echo '${FILE_PATH} does not exist.'
            exit 1
        fi
        """
    }
}

def vault_install() {
    script{
        sh"""
        set +x && set -e
        function install_vault() {
            echo "Installing Vault"
            curl -s -o vault.zip https://releases.hashicorp.com/vault/1.13.2/vault_1.13.2_linux_amd64.zip
            unzip ./vault.zip
            sudo mv vault /usr/local/bin/vault
            rm ./vault.zip
        }
        if ! command -v vault &> /dev/null
        then
            echo "Vault could not be found"
            install_vault
        fi
        """
    }
}

def get_environment(STATE,VAULT_TOKEN) {
    sh"""
    set +x && set -e
    export VAULT_TOKEN="$VAULT_TOKEN"
    ${WORKSPACE}/tools/scripts/vmware/get_env.sh "$STATE"
    """
}

def release_environment(vault_token_id,ENV_NAME) {
    withCredentials([string(
            credentialsId: vault_token_id,
            variable: 'VAULT_TOKEN'
    )]) {
        sh """
        set +x && set -e
        export VAULT_TOKEN=$VAULT_TOKEN
        ${WORKSPACE}/tools/scripts/vmware/release_env.sh $ENV_NAME
        """
        build_new_project_deployment_generic(ENV_NAME)
    }
}

def build_new_project_deployment_generic(ENV_NAME) {
    build job: 'Environments/Tools/new_project-deployment-generic',
        parameters: [string(name: 'ENV_NAME', value: ENV_NAME)],
        propagate: false,
        wait: false
}

def promote(){
    script{
        sh'''
        set +x
        echo "Promote something to repo or artifactory."
        '''
    }
}

def pre_deploy_pool(token_name) {
    withCredentials([string(credentialsId: token_name,
    variable: 'VAULT_TOKEN')]) {
        sh"""
        set +x
        ./tools/scripts/vmware/get_pool_to_preload.sh
        """
        if (fileExists('_array_env.txt')) {
            array_env = readFile('_array_env.txt')
            def env_in_pool = array_env.split(" ")
            for (int i = 0; i < env_in_pool.size(); i++) {
                build_new_project_deployment_generic(env_in_pool[i])
                println env_in_pool[i]
                sh 'sleep 5'          
            }
            currentBuild.description = array_env
        } else {
            echo 'Nothing to preload.'
            currentBuild.description = "null"
        }
    }
}

def get_code_repo(git_repo_url,git_repo_name,git_branch) {
    checkout([$class: 'GitSCM', branches: [[name: git_branch ]],
    doGenerateSubmoduleConfigurations: false,
    extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: git_repo_name]],
    userRemoteConfigs: [[credentialsId: 'project-jenkins-gen-ssh-key',
    url: git_repo_url]]])
        println "Git Repo " + git_repo_url + " cloned in : " + git_repo_name
        println "Git branch : " + git_branch
}

def run_deploy(git_repo_name) {
    script{
        sh"""
        set +x && set -e
        cd "$git_repo_name"/tools/scripts
        ./run_deploy.sh
        """
    }
}

def run_tests(git_repo_name) {
    sh"""
    set +x && set -e
    cd "$git_repo_name"/tools/scripts
    ./run-tests.sh
    """
}

return this
