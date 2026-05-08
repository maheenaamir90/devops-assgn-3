pipeline {
    agent any

    stages {

        stage('Code Linting') {
            steps {
                echo 'Linting Code'
            }
        }

        stage('Code Build') {
            steps {
                sh 'docker build -t flaskapp .'
            }
        }

        stage('Containerized Deployment') {
            steps {
                sh 'docker stop flaskcontainer || true'
                sh 'docker rm flaskcontainer || true'
                sh 'docker run -d --name flaskcontainer -p 5000:5000 flaskapp'
            }
        }

        stage('Containerized Selenium Testing') {
            steps {
                sh 'docker build -t seleniumtest -f Dockerfile.selenium .'
                sh 'docker run --network host seleniumtest'
            }
        }
    }
}
