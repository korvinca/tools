#!/bin/bash

set -e
set +x

export VAULT_ADDR=https://keeper.example.com
export VAULT_NAMESPACE="ops-infra/dev/"
export VAULT_YARN_PATH="secret/dev/new_project/yarn"

function export_json_to_env() {
    INPUT_FILE="${1}"
    check_file "${INPUT_FILE}"
    echo "Convert ${INPUT_FILE} to env vars file"
    VAR_FILE=./vm_init_vars.env
    while IFS=$'\t\n' read -r LINE; do
        echo "${LINE}" >> $VAR_FILE
    done < <(
        <"${INPUT_FILE}" jq \
            --compact-output \
            --raw-output \
            --monochrome-output \
            --from-file \
            <(echo '. | to_entries | map("\(.key)=\(.value|@sh)") | .[]')
    )
}

function install_vault() {
    echo "Install Vault"
    export VAULT_VERSION="1.13.2"
    curl -O -s https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
    unzip ./vault_${VAULT_VERSION}_linux_amd64.zip
    sudo mv vault /usr/local/bin/vault
    rm ./vault_${VAULT_VERSION}_linux_amd64.zip
    vault version
}

function get_vault() {
    if ! command -v vault &> /dev/null
    then
        echo "Vault could not be found"
        install_vault
    fi
    vault version
}

function install_ovftool() {
    echo "Check ovftool"
    if ! command -v ovftool &> /dev/null; then
        echo "ovftool could not be found"
        unset HTTP_PROXY
        unset HTTPS_PROXY
        unset http_proxy
        unset https_proxy
        echo 'Download and install ovftool'
        curl -o ./ovftool.bundle https://maven-master.example.com/artifactory/symphony-release/com/example/project/deployment-artifacts/ops/files/VMware-ovftool-4.4.3-18663434-lin.x86_64.bundle
        sudo sh ./ovftool.bundle --console --required --eulas-agreed
        rm ./ovftool.bundle
    else
        echo "ovftool already installed"
    fi
    ovftool --version
}

function check_file() {
    set +x
    FILE_PATH="${1}"
    if [ -f ${FILE_PATH} ]; then
        echo "${FILE_PATH} exists."
    else 
        echo "${FILE_PATH} does not exist."
        exit 1
    fi
}

function get_file_url() {
    set +x
    FILE_PATH="${1}"
    curl -O -s ${FILE_PATH}
}

function install_govc() {
    echo "Check govc"
    if ! command -v govc &> /dev/null; then
        echo "govc could not be found"
        unset HTTP_PROXY
        unset HTTPS_PROXY
        unset http_proxy
        unset https_proxy
        echo "Download and install govc"
        curl -L -o - http://software.lab.example.com/tools/govc_$(uname -s)_$(uname -m).tar.gz | sudo tar -C /usr/local/bin -xvzf - govc
    else
        echo "govc already installed"
    fi
    govc version
}

function create_snapshot() {
    if [ "$3" == "Cold" ]; then
        echo "Power Off vm"
        govc vm.power -off -k=true  $1
        echo "Create snapshot $2"
        govc snapshot.create -k=true -vm $1 $2
        echo "Power On vm"
        govc vm.power -on -k=true  $1
    else
        echo "Create snapshot of the running VM $2"
        govc snapshot.create -k=true -vm $1 $2
    fi
}

function revert_snapshot() {
    echo "Revert snapshot $2"
    govc snapshot.revert -k=true -vm $1 $2
    if [ "$3" == "Cold" ]; then
        echo "Power On vm"
        govc vm.power -on -k=true  $1
    fi
}

function select_source() {
    response=$(curl -s -o /dev/null -w "%{http_code}" -I "$1")
    if [ "$response" -eq 200 ]; then
        echo "File exists on NAS"
        SELECTED_URL=$1
    else
        echo "File does not exist on NAS"
        response=$(curl -s -o /dev/null -w "%{http_code}" -I "$2")
        if [ "$response" -eq 200 ]; then
            echo "File exists on Artifactory"
            SELECTED_URL=$2
        else
            echo "File does not exist on Artifactory" | exit 1
        fi
    fi
}

function waiting_for_portal() {
    max_attempts=60
    attempt=0

    while [ ${attempt} -lt ${max_attempts} ]; do
        if curl -k "https://${1}/connector/SetupInfo"; then
            break
        fi
        attempt=$((attempt + 1))  
        sleep 10
    done    
}

function __run_on_host_ssh() {
    # ssh -q -i <path_to_private_ssh_key> <user>@<host> <command>
    ssh -q -i $1 $2 $3
}

function waiting_for_host_ssh() {
    local period interval i
    period="$1"
    interval="$2"
    for ((i=0; i<$period; i+=$interval)); do
        if __run_on_host_ssh $3 $4 "hostname"; then
            echo "SSH is available on host."
            return 0
        fi
    echo "Waiting for ssh to be ready..."
    sleep "$interval"
    done
    echo "Waited for $period seconds, but ssh on host not ready yet."
    return 1
}

function get_latest_bin_from_artifactory() {
    echo "Get file"
    bin_output=$(curl -s 'https://maven-master.example.com/artifactory/cspg-andromeda-snapshot/andromeda/appliance-images/staging/')
    bin_file=$(echo $bin_output | grep Intersight-appliance-bundle-1.0.9- | grep debug.devsigned.bin\"\> | tail -1 | sed 's/\<a href=\"//' | sed 's/\">.*//')
    echo $bin_file
}

function print_log {
    echo "logs: $1"
}

function print_error {
    echo "ERROR: $1"
    exit 1
}

function __keeper_get_secret() {
    data=$(vault kv get -format=json "$1" | jq -r '.data')
    if [ "$?" != "0" ]; then
        print_error "__keeper_get_secret"
    fi
}

function __keeper_put_secret() {
    echo "Update secret: $1"
    test -f ./data.json || print_error "__keeper_put_secret > no data.json"
    vault kv put -format=json "$1" @data.json
}

function yarn_get_environment() {
    cd ${WORKSPACE}/tools/scripts/yarn
    local period interval i
    period="3600"
    interval="60"
    for ((i=0; i<$period; i+=$interval)); do
        # Get free prloaded environment
        cd ${WORKSPACE}/tools/scripts/yarn
        __keeper_get_secret ${VAULT_YARN_PATH}
        echo $data > data.json
        # cat data.json
        python3 yarn.py -s "preloaded" #Script generates file ./_env_name.txt
        if [ -f ./_env_name.txt ] ; then
            source ./_env_name.txt
            echo "\"$1\" environment dedicated: $ENV_NAME"
            cp ./_env_name.txt ${WORKSPACE}/ ||  print_error "No file with environment"
            cd ${WORKSPACE}
            return 0
        else
            print_log "No \"$1\" environment."
        fi
        cd ${WORKSPACE}
        print_log "Waiting for $interval seconds and repeat request"
        sleep "$interval"
    done
    echo "Waited for $period seconds, but no preloaded environment found."
    return 1
}

function yarn_get_environment_from_pool_to_preload() {
    cd ${WORKSPACE}/tools/scripts/yarn
    __keeper_get_secret ${VAULT_YARN_PATH}
    echo $data > data.json
    python3 yarn.py -a "to_be_preloaded"
    if [ -f ./_array_env.txt ] ; then
        # groovy_list=$(ids=$(cat ./_array_env.txt);id="${ids[@]}";echo ${id// /, })
        # echo "def grrovy_list=[ $groovy_list ]" > ${WORKSPACE}/_array_env.groovy
        mv ./_array_env.txt ${WORKSPACE}/
    else
        print_log "All environment is preloaded."
    fi
    cd ${WORKSPACE}
}

function yarn_upadte_lease() {
    cd ${WORKSPACE}/tools/scripts/yarn
    print_log "Update lease for "$1" to \"$2\" status"
    __keeper_get_secret ${VAULT_YARN_PATH}
    echo $data > data.json
    python3 yarn.py -e $1 -s "$2" -l $3
    __keeper_put_secret ${VAULT_YARN_PATH}
    cd ${WORKSPACE}
}

function keeper_add_secret() {
    cat > secret_$ENV_NAME.json << EOF
{
  "ipv4_address": "$ipv4_address",
  "ipv4_gateway": "$ipv4_gateway",
  "ipv4_mask": "$ipv4_mask",
  "network": "$network"
}
EOF
    cp secret_$ENV_NAME.json data.json
    __keeper_put_secret "secret/dev/new_project/$ENV_NAME" && rm ./data.json
}

function keeper_update_yarn() {
    rm -rf data.json
    unixtime=$(date +%s)
    cat > data_yarn.json << EOF
{
  "$ENV_NAME": {
    "args": {"": ""},
    "lease_end_time": $unixtime,
    "leased": 0,
    "pool": "$pool",
    "release": "$release",
    "release_version": "$release_version",
    "state": "$state",
    "type": "$type"
  }
}
EOF
    __keeper_get_secret "$VAULT_YARN_PATH" && echo $data > ./data.json
    data=$(jq -s 'add' ./data_yarn.json ./data.json) && echo $data > ./data.json
    __keeper_put_secret "$VAULT_YARN_PATH" && rm ./data.json
}

function inject_public_key {
    print_log "Check if customer public key exists"
    existing_key=$(ssh ${SSH_TARGET} "bash -c \"grep -w '${SSH_CUSTOMER_PUBLIC_KEY}' ~/.ssh/authorized_keys\" || true")
    if [ -n "${existing_key}" ] && [ "${existing_key}" == "${SSH_CUSTOMER_PUBLIC_KEY}" ]; then
        print_log "Provided customer public key already exists."
    else
        ssh ${SSH_TARGET} "bash -c \"echo '${SSH_CUSTOMER_PUBLIC_KEY}' >> ~/.ssh/authorized_keys\""
        print_log "Provided customer public key added."
    fi
}