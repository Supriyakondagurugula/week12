pipeline {
    agent any

    stages {

        stage('Run Selenium Tests with pytest') {
            steps {
                echo "Running Selenium Tests using pytest"
                bat 'pip install -r requirements.txt'
                bat 'start /B python app.py'
                bat 'ping 127.0.0.1 -n 5 > nul'
                bat 'pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat 'docker build -t seleniumdemoapp1:v1 .'
            }
        }

        stage('Docker Login') {
            steps {
                bat 'docker login -u supriyamallesh -p Supriya@206'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                bat 'docker tag seleniumdemoapp1:v1 supriyamallesh/seleniumtestimage:v1'
                bat 'docker push supriyamallesh/seleniumtestimage:v1'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}