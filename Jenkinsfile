pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'docker build -t cloudops-monitor .'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }

            steps {
                sh 'ansible-playbook -i ansible/inventory ansible/deploy.yml'
            }
        }
    }
}