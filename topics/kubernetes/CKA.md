# CKA (Certified Kubernetes Administrator)

- [CKA (Certified Kubernetes Administrator)](#cka-certified-kubernetes-administrator)
  - [Setup](#setup)
  - [Pods](#pods)
    - [Troubleshooting Pods](#troubleshooting-pods)
  - [Namespaces](#namespaces)
  - [Nodes](#nodes)
  - [Services](#services)

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
<summary>Run a command to view all the pods in current namespace</summary><br><b>

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
</b></details>

<details>
<summary>List pods from all namespaces</summary><br><b>

`k get po --all-namespaces`
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
</b></details>

<details>
<summary>What the error <code>ImagePullBackOff</code> means?</summary><br><b>

Most likely you didn't write correctly the name of the image you try to pull and run

You can confirm with `kubectl describe po POD_NAME`
</b></details>

<details>
<summary>How to check on which node a certain Pod is running?</summary><br><b>

`k get po POD_NAME -o wide`
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
<summary>Create an internal service called "sevi" to expose the app 'web' on port 1991</summary><br><b>
</b></details>