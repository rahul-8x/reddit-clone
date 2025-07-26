pipeline {
    agent { label 'Agent-Vinod' }

    environment {
        IMAGE_NAME = 'rahul8x/reddit-clone'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t %IMAGE_NAME% ."
                }
            }
        }

        stage('DockerHub Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    bat "docker push %IMAGE_NAME%"
                }
            }
        }
    }
}
