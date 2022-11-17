pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [],
                userRemoteConfigs: [[credentialsId: '4b1bb4a4-5bf3-4786-a32a-452f9297827f',
                url: 'https://github.com/RaghavendraVasa/heroku.git']]])
            }
        }
        stage('Execute API Tests') {
            steps {
                bat 'pytest --html=./reports/report.html test_cases'
            }
        }
        stage('Publish Report') {
            steps {
                archiveArtifacts artifacts: 'reports/report.html,reports/assets/style.css', followSymlinks: false
            }
        }
    }
}
