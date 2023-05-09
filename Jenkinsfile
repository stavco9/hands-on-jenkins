pipeline {
  agent { label 'generic-agent' }
  options {
    skipDefaultCheckout true
  }
  stages {
    stage('Troubleshoot') {
      steps {
        sh 'sleep 600'
      }
    }
    stage('Build') {
      steps {
        echo 'Building...'
      }
    }
    stage('Test Firefox') {
      parallel {
        stage('Test Firefox') {
          steps {
            sh 'echo \'Testing Firefox\''
          }
        }
        stage('Test Chrome') {
          steps {
            sh 'echo \'Testing Chrome\''
          }
        }
        stage('Test Edge') {
          steps {
            sh 'echo \'Testing Edge\''
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploy'
      }
    }
  }
}
