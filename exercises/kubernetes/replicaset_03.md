## ReplicaSet 103

#### Objective

Learn how labels used by ReplicaSets

#### Instructions

1. Create a ReplicaSet with 2 replicas. Make sure the label used for the selector and in the Pods is "type=web"
2. Verify a ReplicaSet was created and there are 2 replicas
3. List the Pods running
4. Remove the label (type=web) from one of the Pods created by the ReplicaSet
5. List the Pods running. Are there more Pods running after removing the label? Why?
6. Verify the ReplicaSet indeed created a new Pod
