#!/usr/bin/env groovy

def started(channel = '#project-jenkins'){
    wrap([$class: 'BuildUser']) {
        slackSend (color: '#FFFF00', channel: "${channel}", message: "STARTED by ${BUILD_USER}.\n${env.ACTION} >> ${env.JOB_NAME} - #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
    }
}
def success(channel = '#project-jenkins'){
    slackSend (color: '#008000', channel: "${channel}", message: "SUCCESS\n${env.ACTION} >> ${env.JOB_NAME} - #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
}
def failure(channel = '#project-jenkins'){
    slackSend (color: '#FF0000', channel: "${channel}", message: "FAILED\n${env.ACTION} >> ${env.JOB_NAME} - #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
}
def aborted(channel = '#project-jenkins'){
    wrap([$class: 'BuildUser']) {
        slackSend (color: '#D0D3D4', channel: "${channel}", message: "ABORTED by ${BUILD_USER}.\n${env.ACTION} >> ${env.JOB_NAME} - #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
    }
}
return this