pipeline {
    agent {
        label env.SLAVE_LABEL
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '100', artifactNumToKeepStr: '100'))
    }
    stages {
        stage('Setup environment') {
            steps {
                script {
                    currentBuild.description = "placeholder"
                    helper = load 'tools/lib/helper.groovy'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    helper.placeholder()
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    helper.placeholder()
                }
            }
        }
    }
    post {
        success {
            script {
                helper.placeholder()
            }
        }
        failure {
            script {
                helper.placeholder()
            }
        }
        aborted {
            cleanWs()
        }
    }
}