## Certified Kubernetes Administrator (CKA)

#### Basic Commands

<details>
<summary>Which command you run to view your nodes?</code></summary><br><b>

`kubectl get nodes`
</b></details>

<details>
<summary>Which command you run to view all pods running on all namespaces?</code></summary><br><b>

`kubectl get pods --all-namespaces`
</b></details>

<details>
<summary>How to list all namespaces?</code></summary><br><b>

`kubectl get namespaces`
</b></details>

<details>
<summary>How to create a deployment?</code></summary><br><b>

```
cat << EOF | kubectl create -f -
> apiVersion: v1
> kind: Pod
> metadata:
>   name: nginx
> spec:
>   containers:
>   - name: nginx
>     image: nginx
> EOF
```
</b></details>

<details>
<summary>How to print information on a specific pod?</code></summary><br><b>

`kubectl describe pod pod_name`
</b></details>

<details>
<summary>How to delete a pod?</code></summary><br><b>

`kubectl delete pod pod_name`
</b></details>

<details>
<summary>How to check the status of all the components?</code></summary><br><b>
</b></details>
