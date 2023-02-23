# Argo Rollouts - Canary

## Requirements

1. Running Kubernetes cluster
2. Argo Rollouts CLI
3. Deployed app in a specific version

## Objectives

1. Install Argo Rollouts controller
2. Write a rollout manifest that use canary rollout strategy and apply it
   1. Set it to 6 replicas
   2. Disable auto-promotions
3. Check the rollout list
4. Rollout a new version of your app in any way you prefer
   1. Check the status of the rollout

## Solution

Installation:

1. `kubectl create namespace argo-rollouts`
   1. `kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml`

2. Rollout resource:

```
---
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: some-app
spec:
  replicas: 6
  strategy:
    canary:
      stableService: k8s-service-stable
      canaryService: k8s-service-canary
      trafficRouting:
        ambassador:
          mappings:
            - k8s-mapping
      steps:
      - setWeight: 30
      - pause: {}
      - setWeight: 60
      - pause: {}
      - setWeight: 100
      - pause: {}   
  selector:
    matchLabels:
      app: some-web-app
  template:
    metadata:
      labels:
        app: some-web-app
    spec:
      containers:
      - name: web-app
        image: some/registry/and/image:v1.0
        ports:
        - name: http
          containerPort: 8080
          protocol: TCP
```

3. `kubectl argo rollouts list rollouts`
4. `kubectl argo rollouts set image SOME-APP web-app=some/registry/and/image:v2.0`
   1. `kubectl argo rollouts get rollout some-app --watch`