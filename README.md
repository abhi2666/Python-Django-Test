<h1>Testing of Python-django app as a docker container inside Jenkins</h1>

<h3>Steps Followed</h3>

1. Created a basic python-django app that sends a simply http response - "hello world"
   
![Screenshot (399)](https://github.com/user-attachments/assets/5c8aeee1-71a6-443c-89ad-0930e3aa571d)

2. Created a test case to check if the http response is "hello world" or not. Created a Dockerfile that will be later used by docker to create the image.

![Screenshot (400)](https://github.com/user-attachments/assets/d2680808-4921-4a0b-87f7-ac2a4f034a48)

3. Pushed the code to the github so that jenkins can pull it.

4. Created a Jenkins Pipeline to pull the code from git hub, then build the code and then test the code and generate test result file.
(NO Jenkins file is created..pipeline is directly created inside the jenkins using pipeline script.)

<h3>Pipeline Script</h3>
<p>
  pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "my-test-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/abhi2666/Python-Django-Test.git'
                echo "done collecting the repo !!"
            }
            
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t my-test-app .'
                }
                echo "Building docker image..."
                sh 'docker --version'
            }
        }
        
        // not recommended to run django development server directly on pipeline
        // better to test them directly.
        // stage('build') {
        //     steps {
        //         sh 'python3 --version'
        //         sh 'python3 manage.py runserver'
        //     }
        // }
        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=test-results.xml'
            }
        }

        
        
        stage('Report Test Results') {
            steps {
                junit 'test-results.xml'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

</p>

