pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "itsaliiiiiiii/simple_api"
        VERSION = "latest"
    }

    stages {
        stage('Cloner le projet') {
            steps {
                git 'https://github.com/itsaliiiiiiii/MPDocker.git'
            }
        }

        stage('Construire image Docker') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE:$VERSION .'
                }
            }
        }

        stage('Tester image Docker') {
            steps {
                script {
                    sh 'docker run -d --name test-container -p 8080:80 $DOCKER_IMAGE:$VERSION'
                    sh 'sleep 5' 
                    sh 'curl -I http://localhost:8080' 
                    sh 'docker stop test-container && docker rm test-container'
                }
            }
        }

    }
}
