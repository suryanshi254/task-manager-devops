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
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                sh '''
                source venv/bin/activate
                python manage.py migrate
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                python manage.py test
                '''
            }
        }
    }
}

