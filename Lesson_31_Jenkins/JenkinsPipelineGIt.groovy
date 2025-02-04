pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.10'
        TESTS_API_DIR = 'Tests_API'
        TESTS_UI_DIR = 'Tests_UI_Playwright'
    }

    parameters {
        string(name: 'Caption', defaultValue: '=== TESTING ===', description: '')
        booleanParam(name: 'JUNIT', defaultValue: true, description: 'Enable JUnit XML output for reports')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/homework_31']],  //  main  
                    extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'git_dir']],
                    userRemoteConfigs: [[credentialsId: 'git-creds', url: 'git@github.com:barchiso/AQA_Python.git']]
                ])
            }
        }

        stage('Set Up Python') {
            steps {
                script {
                    dir('Lesson_31_Jenkins/qauto') {
                        withPythonEnv('python3') {
                            sh '''
                                echo "Python version:"
                                python --version
                                echo "Pip version:"
                                pip --version
                                echo "${Caption}"
                                pip install -r requirements.txt
                                echo "Installing Playwright browser chromium"
                                python3 -m playwright install chromium
                            '''
                        }
                    }
                }
            }
        }

        stage('Run API Tests') {
            steps {
                script {
                    dir('Lesson_31_Jenkins/qauto') {
                        withPythonEnv('python3') {
                            sh '''
                                echo "${Caption}"
                                if [ -z "${JUNIT}" ]; then
                                    pytest -sv ./${TESTS_API_DIR}/test_requests.py --alluredir=${WORKSPACE}/allure-results
                                else
                                    pytest -sv ./${TESTS_API_DIR}/test_requests.py --alluredir=${WORKSPACE}/allure-results --junit-xml=report_api.xml
                                fi
                            '''
                        }
                    }
                }
            }
        }

        stage('Run UI Tests') {
            steps {
                script {
                    dir('Lesson_31_Jenkins/qauto') {
                        withPythonEnv('python3') {
                            sh '''
                                echo "${Caption}"
                                if [ -z "${JUNIT}" ]; then
                                    pytest -sv ./${TESTS_UI_DIR}/test_registration.py --alluredir=${WORKSPACE}/allure-results
                                else
                                    pytest -sv ./${TESTS_UI_DIR}/test_registration.py --alluredir=${WORKSPACE}/allure-results --junit-xml=report_ui.xml
                                fi
                            '''
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
        success {
              emailext (
                  to: 'xnunrgx@gmail.com',
                  subject: "SUCCESS: Jenkins Test Results",
                  body: "Tests completed. Check Jenkins for details.",
                  mimeType: 'text/html'
              )
          }
          failure {
              emailext (
                  to: 'xnunrgx@gmail.com',
                  subject: "FAILURE: Jenkins Test Results",
                  body: "Tests completed. Check Jenkins for details.",
                  mimeType: 'text/html'
              )
          }
    }
}
