def dockerContainer = -1

pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/rachelg1/wog.git']])
            }
        }

        stage('build') {
            steps {
                sh 'docker build -t wog:1.0.0 .'
            }
        }

        stage('run') {
            steps {
                script {
                    dockerContainer = sh(script: 'docker run -d -p 8777:5000 wog:1.0.0',returnStdout: true).trim()
                }
            }
        }

        stage('test') {
            steps {
                sh 'pip3 install selenium'

                script {
                    def result = sh(script: '''
                        #!/bin/bash

                        python_result=$(python3 -c "from tests.e2e import main_function; print(main_function('http://localhost:8777'))")

                        echo $python_result
                    ''', returnStdout: true).trim()

                    if (result == '-1') {
                        error('Test Failed!')
                    }
                }

            }
        }

        stage('finalize') {
            steps {
                sh "docker kill $dockerContainer"

            }
        }
    }
}
