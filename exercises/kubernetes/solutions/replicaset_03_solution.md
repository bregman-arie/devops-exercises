## ReplicaSet 03 - Solution

1. Create a ReplicaSet with 2 replicas. Make sure the label used for the selector and in the Pods is "type=web"

```
cat >> rs.yaml <<EOL
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: web
  labels:
    app: somewebapp
    type: web
spec:
  replicas: 2
  selector:
    matchLabels:
      type: web
  template:
    metadata:
      labels:
        type: web
    spec:
      containers:
      - name: httpd
        image: registry.redhat.io/rhscl/httpd-24-rhel7
EOL

kubectl apply -f rs.yaml
```

2. Verify a ReplicaSet was created and there are 2 replicas

```
kubectl get rs
# OR a more specific way: kubectl get -f rs.yaml
```

3. List the Pods running and save the output somewhere

```
kubectl get po > running_pods.txt
```

4. Remove the label (type=web) from one of the Pods created by the ReplicaSet

```
kubectl label pod <POD_NAME> type-
```

5. List the Pods running. Are there more Pods running after removing the label? Why?

```
Yes, there is an additional Pod running because once the label (used as a matching selector) was removed, the Pod became independant meaning, it's not controlled by the ReplicaSet anymore and the ReplicaSet was missing replicas based on its definition so, it created a new Pod.
```

6. Verify the ReplicaSet indeed created a new Pod

```
kubectl describe rs web
```
