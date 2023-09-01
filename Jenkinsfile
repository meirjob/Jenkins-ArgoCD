pipeline {
 agent any
    environment {
        AWS_ACCOUNT_ID="777644549717"
        AWS_DEFAULT_REGION="us-east-1" 
        IMAGE_REPO_NAME="simpleapp"
        IMAGE_TAG="${env.BUILD_NUMBER}"// "latest"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    }    
 
    stages {
 
        stage('Logging into AWS ECR') {
            steps {
                script {
                    sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | sudo docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                }
 
            }
        }
 
        stage('Cloning Git') {
            steps {
                checkout scm
            }
        }
 
        // Building Docker images
        stage('Building image') {
            steps{
                script {
                    dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}"
                }
            }
        }
 
        // Uploading Docker images into AWS ECR
        stage('Pushing to ECR') {
            steps{ 
                script {
                    sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
                    sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"
                }
            }
        }

        stage('Trigger ClusterUpdate') {
            steps{
                echo "triggering updateclusterjob"
                build job: 'updatecluster', parameters: [string(name: 'IMAGE_TAG', value: IMAGE_TAG)]
            }
        }
    }
}
