pipeline {
    agent {
        label 'node-2'
    }
    stages {
        stage('pull cases') {
            steps {
				echo 'pull testcases'
            }
        }
        
        stage('run cases') {
            steps {
                sh 'pip3 install -r  requirements.txt'
            }
        }
        stage('generate allure report') {
            steps {
                echo 'generate allure report'
            }
        }
        stage('send email') {
            steps {
                echo 'send email'
            }
        }
        
    }
}