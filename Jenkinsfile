
pipeline {
    agent {
        label 'python'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Codigo descargado desde GitHub'
            }
        }

        stage('Preparar entorno') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Pruebas automatizadas') {
            steps {
                sh '''
                    .venv/bin/python -m pytest \
                        --junitxml=resultados.xml
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'resultados.xml'
        }

        success {
            echo 'Todas las pruebas pasaron'
        }

        failure {
            echo 'Se detectaron errores'
        }
    }
}
