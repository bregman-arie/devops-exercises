## Certified Kubernetes Application Developer (CKAD)

### Core Concepts

### Pods

<details>
<summary>Deploy a pod called web-1985 using the nginx:alpine image</code></summary><br><b>

`kubectl run web-1985 --image=nginx:alpine --restart=Never`
</b></details>

### Namespaces

<details>
<summary>List all namespaces</code></summary><br><b>

kubectl get ns
</b></details>

<details>
<summary>List all the pods in the namespace 'neverland'</code></summary><br><b>

kubectl get ns -n neverland
</b></details>

<details>
<summary>List all the pods in all the namespaces</code></summary><br><b>

kubectl get po --all-namespaces
</b></details>
