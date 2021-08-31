pipeline {

  agent any

  stages {

    stage('Checkout Source') {
      steps {
        git url:'https://github.com/<GITHUB_USERNAME>/<YOUR_WEB_APP_REPO>.git',
        // credentialsId: 'creds_github',
        branch:'master'
      }
    }
    
      stage("Build image") {
            steps {
                script {
                    myapp = docker.build("<YOUR_DOCKER_USERNAME>/helloworld:${env.BUILD_ID}")
                }
            }
        }
    
      stage("Push image") {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                            myapp.push("latest")
                            myapp.push("${env.BUILD_ID}")
                    }
                }
            }
        }

    
    stage('Deploy App') {
      steps {
        script {
          sh 'ansible-playbook deploy.yml'
        }
      }
    }

  }

}
