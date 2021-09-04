## ReplicaSet 01 - Solution

1. Create a ReplicaSet with 2 replicas. The app can be anything.

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

3. Delete one of the Pods the ReplicaSet has created

```
kubectl delete po <POD_NAME>
```

4. If you'll list all the Pods now, what will you see?

```
The same number of Pods. Since we defined 2 replicas, the ReplicaSet will make sure to create another Pod that will replace the one you've deleted.
```

5. Remove the ReplicaSet you've created

```
kubectl delete -f rs.yaml
```

6. Verify you've deleted the ReplicaSet

```
kubectl get rs
# OR a more specific way: kubectl get -f rs.yaml
```
