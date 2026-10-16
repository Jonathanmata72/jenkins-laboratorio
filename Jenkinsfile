
pipeline {
    agent any

    stages {
        stage('Preparacion') {
            steps {
                echo 'Iniciando CI desde GitHub'
            }
        }

        stage('Verificacion') {
            steps {
                echo 'Verificando el codigo'
                echo "Commit: ${env.GIT_COMMIT}"
            }
        }

        stage('Pruebas') {
            steps {
                echo 'Simulando pruebas automatizadas'
            }
        }
    }

    post {
        success {
            echo 'Integracion completada'
        }

        failure {
            echo 'Error en la integracion'
        }
    }
}
