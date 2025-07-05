pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/suryanshi254/task-manager-devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                sh '''
                . venv/bin/activate
                python manage.py migrate
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                python manage.py test
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ Pipeline failed. Check the console output.'
        }
        success {
            echo '✅ Pipeline completed successfully.'
        }
    }
}

