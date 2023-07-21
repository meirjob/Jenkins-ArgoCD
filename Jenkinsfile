pipeline {
 agent any
    environment {
        AWS_ACCOUNT_ID="777644549717"
        AWS_DEFAULT_REGION="eu-west-1" 
        IMAGE_REPO_NAME="simpleapp"
        IMAGE_TAG="latest"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    }    
 
    stages {
 
        stage('Logging into AWS ECR') {
            steps {
                script {
                    sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                }
 
            }
        }
 
        stage('Cloning Git') {
            steps {
                checkout scm
                //checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/sd031/aws_codebuild_codedeploy_nodeJs_demo.git']]]) 
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
    }
}


// pipeline {
//     agent any
//     options {
//         skipStagesAfterUnstable()
//     }
//     stages {
//          stage('Clone repository') { 
//             steps { 
//                 script{
//                 checkout scm
//                 }
//             }
//         }

//         stage('Build') { 
//             steps { 
//                 script{
//                  app = docker.build("sampleapp")
//                 }
//             }
//         }
//         stage('Test'){
//             steps {
//                  echo 'Empty'
//             }
//         }
//         stage('PushImage') {
//             steps {
//                 script{
//                         docker.withRegistry('https://777644549717.dkr.ecr.eu-west-1.amazonaws.com', 'ecr:eu-west-1:aws-credentials') {
//                             app.push("${env.BUILD_NUMBER}")
//                             app.push("latest")
//                         }
//                 }
//             }
//         }
//     }
// }