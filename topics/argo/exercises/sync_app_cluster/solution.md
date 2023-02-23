# Sync App - Cluster

## Requirements

1. Make sure you have a Kubernetes cluster running with ArgoCD installed
1. Make sure you have an app deployed in the cluster and tracked by ArgoCD

## Objectives

1. Verify the app is tracked by ArgoCD and in sync
2. . Make a change to your application by running a `kubectl` command. The change can anything:
   1. Changing the tag of the image
   2. Changing the number of replicas
   3. You can go extreme and delete the resource if you would like :)
3. Check the app state in ArgoCD
4. Sync the app state

## Solution

### UI

1. Click on the app in the UI
   1. Make sure it's in sync and in "healthy" state
2. Make a check in the cluster
   1. `kubectl scale --replicas=0 <DEPLOYMENT_NAME>`
   2. `kubectl get rs <DEPLOYMENT_NAME>`
3. Go back to the UI and check the state of the app
   1. If it's still in sync, make sure to click on "Refresh"
   2. The app should be in "out-of-sync" state
   3. Click on "Sync" and then on "Synchronize"

### CLI 

```
# Check app state and verify it's in sync
argocd app get app-demo

# Run the following k8s commands (or any other commands that will change the state of your app)
kubectl scale --replicas=0 <DEPLOYMENT_NAME>
kubectl get rs <DEPLOYMENT_NAME>

# Check app state again
argocd app get app-demo

# Sync app state
argocd app sync app-demo
argocd app wait app-demo
```