## Certified Kubernetes Application Developer (CKAD)

### Core Concepts

### Pods

<details>
<summary>Deploy a pod called web-1985 using the nginx:alpine image</code></summary><br><b>

`kubectl run web-1985 --image=nginx:alpine --restart=Never`
</b></details>

<details>
<summary>How to find out on which node a certain pod is running?</summary><br><b>

`kubectl get po -o wide`
</b></details>

### Namespaces

<details>
<summary>List all namespaces</code></summary><br><b>

kubectl get ns
</b></details>

<details>
<summary>List all the pods in the namespace 'neverland'</code></summary><br><b>

kubectl get po -n neverland
</b></details>

<details>
<summary>List all the pods in all the namespaces</code></summary><br><b>

kubectl get po --all-namespaces
</b></details>
