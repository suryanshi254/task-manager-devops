pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo '✅ Cloning repository...'
                // Checkout is done automatically in declarative pipeline
            }
        }

        stage('Set up Python Env') {
            steps {
                echo '🐍 Creating virtual environment...'
                sh '''
                    cd backend
                    python3.10 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt || true
                '''
            }
        }

        stage('Run Django Migrations') {
            steps {
                echo '🛠️ Running Django migrations...'
                sh '''
                    cd backend
                    . venv/bin/activate
                    python manage.py migrate
                '''
            }
        }

        stage('Run Django Tests') {
            steps {
                echo '🧪 Running Django tests...'
                sh '''
                    cd backend
                    . venv/bin/activate
                    python manage.py test
                '''
            }
        }

        stage('Run JUnit Tests') {
            steps {
                echo '☕ Running JUnit tests...'
                dir('java-tests') {
                    sh 'mvn test'
                }
            }
        }

        stage('Send Metrics to Graphite') {
            steps {
                echo '📈 Sending custom metrics to Graphite...'
                sh '''
                    cd monitoring
                    . ../backend/venv/bin/activate
                    python metrics_push.py
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo '🐳 Building Docker image...'
                sh 'docker build -t taskmanager:latest .'
            }
        }
    }
}

