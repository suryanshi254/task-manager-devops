pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3.10 -m venv venv
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
            echo "❌ Pipeline failed. Check the logs!"
        }
        success {
            echo "✅ Pipeline succeeded."
        }
    }
}

