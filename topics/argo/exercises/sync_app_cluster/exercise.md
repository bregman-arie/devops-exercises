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

Click [here](solution.md) to view the solution