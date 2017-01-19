node {
  stage('Cleanup') {
    deleteDir()
  }

  stage('Checkout') {
    checkout scm
    dir('ci-tools') {
      git 'https://github.com/vexxhost/molecule-ci-tools'
    }
  }

  stage('Lint') {
    parallel (
        ansible: {
            sh 'ansible-lint tests/test.yml'
        },
        yaml: {
            sh 'yamllint .'
        },
        failFast: true
    )
  }

  stage('Test') {
    env.OS_AUTH_URL = 'https://auth.vexxhost.net'
    env.OS_TENANT_NAME = 'jenkins'
    env.OS_USERNAME = 'jenkins'
    sh "ci-tools/setup_config.py"

    withCredentials([string(credentialsId: 'OS_PASSWORD', variable: 'OS_PASSWORD')]) {
      try {
        sh 'molecule syntax'
        sh 'molecule create'
        sh 'molecule converge'
        sh 'molecule idempotence'
        sh 'molecule verify'
        sh 'molecule destroy'
      } catch (Exception e) {
        try {
            sh 'molecule destroy'
        } catch (Exception exc) {}

        throw e;
      }
    }
  }
}
