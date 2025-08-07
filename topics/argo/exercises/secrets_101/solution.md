# ArgoCD Secrets 101

## Requirements

1. Running Kubernetes cluster
2. Application k8s manifests with secrets
3. Kubeseal binary installed

## Objectives

1. Install bitnami sealed controller as ArgoCD app
2. Encrypt secrets and commit them to the repo with the k8s manifests
3. Create an app using the secrets you encrypted

## Solution

1. Click on "New App"
   1. app name: controller
   2. project: default
   3. sync policy: automatic
   4. repository URL: a URL to bitnami sealed controller manifests
   5. namespace: kube-system

2. Run the following for every secret: `kubeseal < some/secret.yml > sealed_secrets/some/encrypted_secret.yaml -o yaml`

3. Click on "New App"
   1. app name: some-app
   2. project: default
   3. sync policy: automatic
   4. repository URL: a URL to k8s manifests (including encrypted secrets)
   5. namespace: default
