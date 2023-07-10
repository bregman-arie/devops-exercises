## ReplicaSet 02 - Solution

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

3. Remove the ReplicaSet but NOT the pods it created

```
kubectl delete -f rs.yaml --cascade=orphan
```

4. Verify you've deleted the ReplicaSet but the Pods are still running

```
kubectl get rs # no replicas
kubectl get po # Pods still running
```

5. Create again the same ReplicaSet, without changing anything

```
kubectl apply -f rs.yaml
```

6. Verify that the ReplicaSet used the existing Pods and didn't create new Pods

```
kubectl describe rs web  # You should see there are no new events and if you list the pods with 'kubectl get po -f rs.yaml` you'll see they have the same names
```
