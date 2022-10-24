# App Creation

## Requirements

1. Make sure you have repository with some Kubernetes manifests
2. Make sure you have a Kubernetes cluster running with ArgoCD installed

## Objectives

1. Using the CLI or the UI, create a a new application with the following properties:
   1. app name: app-demo
   2. project: app-project
   3. repository URL: your repo with some k8s manifests
   4. namespace: default
2. Verify the app was created
3. Sync the app
4. Verify Kubernetes resources were created
5. Delete the app

## Solution

### UI

1. Click on "New App"
   1. Insert application name: `app-demo`
   2. Insert project: `app-project`
   3. Under source put the repository URL to your GitHub repo with Kubernetes manifests
      1. Set the path for your application
   4. Under destination put the address of your Kubernetes cluster and set namespace to `default`
   5. Click on "Create"
2. Click on "Sync" button on the "app-demo" form
   1. Click on "Synchronize"
3. Verify the Kubernetes resources were created
   1. `kubectl get deployments`
4. Delete the app

### CLI

```
argocd app create app-demo \
--project app-project \
--repo https://fake.repo.address \
--path ./some_app_path \
--dest-namespace default \
--dest-server my.kubernetes.cluster

# Check app state
argocd app list
argocd app get app-demo

# Sync app state
argocd app sync app-demo
argocd app wait app-demo

# Verify kubernetes resources were created
kubectl get deployments

# Delete the app
argocd app delete app-demo
```