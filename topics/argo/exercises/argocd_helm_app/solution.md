# ArgoCD Helm App

## Requirements

1. Running Kubernetes cluster
2. ArgoCD installed on the k8s cluster
3. Repository of an Helm chart

## Objectives

1. Create a new app in ArgoCD that points to the repo of your Helm chart

## Solution

```
argocd app create some-app \
--project default \
--repo https://repo-with-helm-chart
--path "./helm" \
--sync-policy auto \
--dest-namespace default \
--dest-server https://kubernetes.cluster
```