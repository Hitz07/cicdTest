pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run API Tests') {
            steps {
                sh 'pytest api_tests/ --html=api_report.html'
            }
        }
        stage('Run UI Tests') {
            steps {
                sh 'pytest ui_tests/ --html=ui_report.html'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '*.html', allowEmptyArchive: true
        }
    }
}