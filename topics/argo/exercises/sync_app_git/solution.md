# Sync App - Git

## Requirements

1. Make sure you have repository with some Kubernetes manifests
2. Make sure you have a Kubernetes cluster running with ArgoCD installed


## Objectives

1. Create a new application using the UI or CLI
   1. App Name: app-demo
   2. Project: project-demo
   3. Kubernetes namespace: default
2. Sync the application
3. Verify the application is running by executing `kubectl get deploy` in the `default` namespace
4. Now make a change in your repository to one of the Kubernetes manifests (e.g. update deployment tag)
5. Go back to ArgoCD and check the state of the app
6. Sync the state of the application

## Solution

### UI

1. Click on "New App"
   1. Insert application name: `app-demo`
   2. Insert project: `project-demo`
   3. Under source put the repository URL to your GitHub repo with Kubernetes manifests
      1. Set path of your application
   4. Under destination put the address of your Kubernetes cluster and set namespace to `default`
   5. Click on "Create"
2. Click on the newly created application
   1. Click on the "sync button" and click on "Synchronize"
3. Make a change in your Git repo where the Kubernetes manifests are
   1.  `git add .`
   2.  `git commit -a`
   3.  `git push origin <BRANCH_NAME>`
4.  Go back to ArgoCD UI and check the status of the app
    1.  You should see it's "out-of-sync". If you don't, you may want to click on "Refresh"
    2.  You can also click on "App diff" to see the difference that led to "out-of-sync"
5.  Click on "Sync" and "Synchronize" to sync the application

### CLI 

```
argocd app create app-demo \
--project project-demo \
--repo https://fake.repo.address \
--path ./some_app_path \
--dest-namespace default \
--dest-server my.kubernetes.cluster

# In the Git repo
cd <git repo>
vi <k8s manifest>
git add .
git commit -a
git push origin <BRANCH_NAME>

# Check app state
argocd app get app-demo

# Sync app state
argocd app sync app-demo
argocd app wait app-demo
```