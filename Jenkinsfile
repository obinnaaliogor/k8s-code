node {
    def app

    stage('Clone repository') {
      

        checkout scm
    }

    stage('Build image') {
  
       app = docker.build("obinnaaliogor/python-app")
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhubcredentials') {
            app.push("${env.BUILD_NUMBER}")
        }
    }

    
/* stage('8Deployment to Kubernetes'){
sh 'kubectl apply -f deployment.yml'
}
*/

    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest_pythonapp', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}
