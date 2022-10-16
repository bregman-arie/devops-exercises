# CKA (Certified Kubernetes Administrator)

- [CKA (Certified Kubernetes Administrator)](#cka-certified-kubernetes-administrator)
  - [Setup](#setup)
  - [Pods](#pods)
    - [Troubleshooting Pods](#troubleshooting-pods)
  - [Namespaces](#namespaces)
  - [Nodes](#nodes)
  - [Services](#services)
  - [ReplicaSets](#replicasets)
    - [Troubleshooting ReplicaSets](#troubleshooting-replicasets)
  - [Deployments](#deployments)
    - [Troubleshooting Deployments](#troubleshooting-deployments)
  - [Scheduler](#scheduler)
  - [Labels and Selectors](#labels-and-selectors)
  - [Taints](#taints)

## Setup

* Set up Kubernetes cluster. Use on of the following
   1. Minikube for local free & simple cluster
   2. Managed Cluster (EKS, GKE, AKS)

* Set aliases

```
alias k=kubectl
alias kd=kubectl delete
alias kds=kubectl describe
alias ke=kubectl edit
alias kr=kubectl run
alias kg=kubectl get
```

## Pods

<details>
<summary>Run a command to view all the pods in the current namespace</summary><br><b>

`kubectl get pods`

Note: create an alias (`alias k=kubectl`) and get used to `k get po`
</b></details>

<details>
<summary>Run a pod called "nginx-test" using the "nginx" image</summary><br><b>

`k run nginx-test --image=nginx`
</b></details>

<details>
<summary>Assuming you have a Pod called "nginx-test", how to remove it?</summary><br><b>

`k delete nginx-test`
</b></details>

<details>
<summary>In what namespace the <code>etcd</code> pod is running? list the pods in that namespace</summary><br><b>

`k get po -n kube-system`

Let's say you didn't know in what namespace it is. You could then run `k get po -A | grep etc` to find the Pod and see in what namespace it resides.
</b></details>

<details>
<summary>List pods from all namespaces</summary><br><b>

`k get po -A`

The long version would be `kubectl get pods --all-namespaces`.
</b></details>

<details>
<summary>Write a YAML of a Pod with two containers and use the YAML file to create the Pod (use whatever images you prefer)</summary><br><b>

```
cat > pod.yaml <<EOL
apiVersion: v1
kind: Pod
metadata:
  name: test
spec:
  containers:
  - image: alpine
    name: alpine
  - image: nginx-unprivileged
    name: nginx-unprivileged
EOL

k create -f pod.yaml
```

If you ask yourself how would I remember writing all of that? no worries, you can simply run `kubectl run some_pod --image=redis -o yaml --dry-run=client > pod.yaml`. If you ask yourself "how am I supposed to remember this long command" time to change attitude ;)
</b></details>

<details>
<summary>Create a YAML of a Pod without actually running the Pod with the kubectl command (use whatever image you prefer)</summary><br><b>

`k run some-pod -o yaml --image nginx-unprivileged --dry-run=client > pod.yaml`
</b></details>

<details>
<summary>How to test a manifest is valid?</summary><br><b>

with `--dry-run` flag which will not actually create it, but it will test it and you can find this way any syntax issues.

`k create -f YAML_FILE --dry-run`
</b></details>

<details>
<summary>How to check which image a certain Pod is using?</summary><br><b>

`k describe po <POD_NAME> | grep -i image`
</b></details>

<details>
<summary>How to check how many containers run in signle Pod?</summary><br><b>

`k get po POD_NAME` and see the number under "READY" column.

You can also run `k describe po POD_NAME`
</b></details>

<details>
<summary>Run a Pod called "remo" with the the latest redis image and the label 'year=2017'</summary><br><b>

`k run remo --image=redis:latest -l year=2017`
</b></details>

<details>
<summary>List pods and their labels</summary><br><b>

`k get po --show-labels`
</b></details>

<details>
<summary>Delete a Pod called "nm"</summary><br><b>

`k delete po nm`
</b></details>

<details>
<summary>List all the pods with the label "env=prod"</summary><br><b>

`k get po -l env=prod`

To count them: `k get po -l env=prod --no-headers | wc -l`
</b></details>

### Troubleshooting Pods

<details>
<summary>You try to run a Pod but see the status "CrashLoopBackOff". What does it means? How to identify the issue?</summary><br><b>

The container failed to run (due to different reasons) and Kubernetes tries to run the Pod again after some delay (= BackOff time).

Some reasons for it to fail:
  - Misconfiguration - mispelling, non supported value, etc.
  - Resource not available - nodes are down, PV not mounted, etc.

Some ways to debug:

1. `kubectl describe pod POD_NAME`
   1. Focus on `State` (which should be Waiting, CrashLoopBackOff) and `Last State` which should tell what happened before (as in why it failed)
2. Run `kubectl logs mypod`
   1. This should provide an accurate output of 
   2. For specific container, you can add `-c CONTAINER_NAME`
3. If you still have no idea why it failed, try `kubectl get events`
4. 
</b></details>

<details>
<summary>What the error <code>ImagePullBackOff</code> means?</summary><br><b>

Most likely you didn't write correctly the name of the image you try to pull and run. Or perhaps it doesn't exists in the registry.

You can confirm with `kubectl describe po POD_NAME`
</b></details>

<details>
<summary>How to check on which node a certain Pod is running?</summary><br><b>

`k get po POD_NAME -o wide`
</b></details>

<details>
<summary>Run the following command: <code>kubectl run ohno --image=sheris</code>. Did it work? why not? fix it without removing the Pod and using any image you want</summary><br><b>

Because there is no such image `sheris`. At least for now :)

To fix it, run `kubectl edit ohno` and modify the following line `- image: sheris` to `- image: redis` or any other image you prefer.
</b></details>

<details>
<summary>You try to run a Pod but it's in "Pending" state. What might be the reason?</summary><br><b>

One possible reason is that the scheduler which supposed to schedule Pods on nodes, is not running. To verify it, you can run `kubectl get po -A | grep scheduler` or check directly in `kube-system` namespace.
</b></details>

## Namespaces

<details>
<summary>List all the namespaces</summary><br><b>

`k get ns`
</b></details>

<details>
<summary>Create a namespace called 'alle'</summary><br><b>

`k create ns alle`
</b></details>

<details>
<summary>Check how many namespaces are there</summary><br><b>

`k get ns --no-headers | wc -l`
</b></details>

<details>
<summary>Check how many pods exist in the "dev" namespace</summary><br><b>

`k get po -n dev`
</b></details>

<details>
<summary>Create a pod called "kartos" in the namespace dev. The pod should be using the "redis" image.</summary><br><b>

If the namespace doesn't exist already: `k create ns dev`

`k run kratos --image=redis -n dev`
</b></details>

<details>
<summary>You are looking for a Pod called "atreus". How to check in which namespace it runs?</summary><br><b>

`k get po -A | grep atreus`
</b></details>

## Nodes

<details>
<summary>Run a command to view all nodes of the cluster</summary><br><b>

`kubectl get nodes`

Note: create an alias (`alias k=kubectl`) and get used to `k get no`
</b></details>

<details>
<summary>Create a list of all nodes in JSON format and store it in a file called "some_nodes.json"</summary><br><b>

`k get nodes -o json > some_nodes.json`
</b></details>

## Services

<details>
<summary>Check how many services are running in the current namespace</summary><br><b>

`k get svc`
</b></details>

<details>
<summary>Create an internal service called "sevi" to expose the app 'web' on port 1991</summary><br><b>
</b></details>

<details>
<summary>How to reference by name a service called "app-service" within the same namespace?</summary><br><b>

app-service
</b></details>

<details>
<summary>How to check the TargetPort of a service?</summary><br><b>

`k describe svc <SERVICE_NAME>`
</b></details>

<details>
<summary>How to check what endpoints the svc has?</summary><br><b>

`k describe svc <SERVICE_NAME>`
</b></details>

<details>
<summary>How to reference by name a service called "app-service" within a different namespace, called "dev"?</summary><br><b>

app-service.dev.svc.cluster.local
</b></details>

<details>
<summary>Assume you have a deployment running and you need to create a Service for exposing the pods. This is what is required/known:

* Deployment name: jabulik
* Target port: 8080
* Service type: NodePort
* Selector: jabulik-app
* Port: 8080
</summary><br><b>

`kubectl expose deployment jabulik --name=jabulik-service --target-port=8080 --type=NodePort --port=8080 --dry-run=client -o yaml -> svc.yaml`

`vi svc.yaml` (make sure selector is set to `jabulik-app`)

`k apply -f svc.yaml`
</b></details>

## ReplicaSets

<details>
<summary>How to check how many replicasets defined in the current namespace?</summary><br><b>

`k get rs`
</b></details>

<details>
<summary>You have a replica set defined to run 3 Pods. You removed one of these 3 pods. What will happen next? how many Pods will there be?</summary><br><b>

There will still be 3 Pods running theoretically because the goal of the replica set is to ensure that. so if you delete one or more Pods, it will run additional Pods so there are always 3 Pods.
</b></details>

<details>
<summary>How to check which container image was used as part of replica set called "repli"?</summary><br><b>

`k describe rs repli | grep -i image`
</b></details>

<details>
<summary>How to check how many Pods are ready as part of a replica set called "repli"?</summary><br><b>

`k describe rs repli | grep -i "Pods Status"`
</b></details>

<details>
<summary>How to delete a replica set called "rori"?</summary><br><b>

`k delete rs rori`
</b></details>

<details>
<summary>How to modify a replica set called "rori" to use a different image?</summary><br><b>

`k edis rs rori`
</b></details>

<details>
<summary>Scale up a replica set called "rori" to run 5 Pods instead of 2</summary><br><b>

`k scale rs rori --replicas=5`
</b></details>

<details>
<summary>Scale down a replica set called "rori" to run 1 Pod instead of 5</summary><br><b>

`k scale rs rori --replicas=1`
</b></details>

### Troubleshooting ReplicaSets

<details>
<summary>Fix the following ReplicaSet definition

```yaml
apiVersion: apps/v1
kind: ReplicaCet
metadata:
  name: redis
  labels:
    app: redis
    tier: cache
spec:
  selector:
    matchLabels:
      tier: cache
  template:
    metadata:
      labels:
        tier: cachy
    spec:
      containers:
      - name: redis
        image: redis
```
</summary><br><b>

kind should be ReplicaSet and not ReplicaCet :)

</b></details>

<details>
<summary>Fix the following ReplicaSet definition

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: redis
  labels:
    app: redis
    tier: cache
spec:
  selector:
    matchLabels:
      tier: cache
  template:
    metadata:
      labels:
        tier: cachy
    spec:
      containers:
      - name: redis
        image: redis
```
</summary><br><b>

The selector doesn't match the label (cache vs cachy). To solve it, fix cachy so it's cache instead.

</b></details>

## Deployments

<details>
<summary>How to list all the deployments in the current namespace?</summary><br><b>

`k get deploy`

</b></details>

<details>
<summary>How to check which image a certain Deployment is using?</summary><br><b>

`k describe deploy <DEPLOYMENT_NAME> | grep image`

</b></details>

<details>
<summary>Create a file definition/manifest of a deployment called "dep", with 3 replicas that uses the image 'redis'</summary><br><b>

`k create deploy dep -o yaml --image=redis --dry-run=client --replicas 3 > deployment.yaml `

</b></details>

<details>
<summary>Remove the deployment `depdep`</summary><br><b>

`k delete deploy depdep`

</b></details>

### Troubleshooting Deployments

<details>
<summary>Fix the following deployment manifest

```yaml
apiVersion: apps/v1
kind: Deploy
metadata:
  creationTimestamp: null
  labels:
    app: dep
  name: dep
spec:
  replicas: 3
  selector:
    matchLabels:
      app: dep
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: dep
    spec:
      containers:
      - image: redis
        name: redis
        resources: {}
status: {}
```
</summary><br><b>

Change `kind: Deploy` to `kind: Deployment`
</b></details>

<details>
<summary>Fix the following deployment manifest

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: dep
  name: dep
spec:
  replicas: 3
  selector:
    matchLabels:
      app: depdep
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: dep
    spec:
      containers:
      - image: redis
        name: redis
        resources: {}
status: {}
```
</summary><br><b>

The selector doesn't match the label (dep vs depdep). To solve it, fix depdep so it's dep instead.
</b></details>

## Scheduler

<details>
<summary>How to schedule a pod on a node called "node1"?</summary><br><b>

`k run some-pod --image=redix -o yaml --dry-run=client > pod.yaml`

`vi pod.yaml` and add:

```
spec:
  nodeName: node1
```

`k apply -f pod.yaml`

Note: if you don't have a node1 in your cluster the Pod will be stuck on "Pending" state.
</b></details>

## Labels and Selectors

<details>
<summary>How to list all the Pods with the label "app=web"?</summary><br><b>

`k get po -l app=web`
</b></details>

<details>
<summary>How to list all objects labeled as "env=staging"?</summary><br><b>

`k get all -l env=staging`
</b></details>

<details>
<summary>How to list all deployments from "env=prod" and "type=web"?</summary><br><b>

`k get deploy -l env=prod,type=web`
</b></details>

## Taints

<details>
<summary>Check if there are taints on node "master"</summary><br><b>

`k describe no master | grep -i taints`
</b></details>

<details>
<summary>Create a taint on one of the nodes in your cluster with key of "app" and value of "web" and effect of "NoSchedule"</summary><br><b>

`k taint node minikube app=web:NoSchedule`
</b></details>