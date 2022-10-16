# Taints 101

## Objectives

1. Check if one of the nodes in the cluster has taints (doesn't matter which node)
2. Create a taint on one of the nodes in your cluster with key of "app" and value of "web" and effect of "NoSchedule"
   1. Explain what it does exactly
   2. Verify it was applied

## Solution

Click [here](solution.md) to view the solution.

1. `kubectl describe no minikube | grep -i taints`
2. `kubectl taint node minikube app=web:NoSchedule`
   1. Any resource with "app=web" key value will not be scheduled on node `minikube`
   2. `kubectl describe no minikube | grep -i taints`