pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo "Building Docker image on branch: ${env.BRANCH_NAME}"
                sh 'docker build -t cloudops-monitor .'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }

            steps {
                echo "Deploying application from main branch"
                sh 'ansible-playbook -i ansible/inventory ansible/deploy.yml'
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully for branch: ${env.BRANCH_NAME}"
        }

        failure {
            echo "Pipeline failed for branch: ${env.BRANCH_NAME}"
        }
    }
}