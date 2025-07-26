pipeline {
    agent { label 'Agent-Vinod' }  // 👈 Use your actual agent label

    environment {
        IMAGE_NAME = 'your-dockerhub-username/reddit-clone'
        CREDENTIAL_ID = 'dockerhub-creds-id' // 👈 your Jenkins DockerHub credentials ID
    }

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/your-username/reddit-clone.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: "${CREDENTIAL_ID}",
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', "${CREDENTIAL_ID}") {
                            dockerImage.push('latest')
                        }
                    }
                }
            }
        }

        stage('Clean Up') {
            steps {
                sh "docker rmi ${IMAGE_NAME}:latest || true"
            }
        }
    }
}
