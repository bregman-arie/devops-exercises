## Certified Kubernetes Administrator (CKA)

### Pods

<details>
<summary>Deploy a pod called web-1985 using the nginx:alpine image</code></summary><br><b>

`kubectl run web-1985 --image=nginx:alpine --restart=Never`
</b></details>

<details>
<summary>How to find out on which node a certain pod is running?</summary><br><b>

`kubectl get po -o wide`
</b></details>

<details>
<summary>Upgrade the current version of kubernetes from 1.25.0 to 1.26.0 exactly using the kubeadm utility. Make sure that the upgrade is carried out one node at a time starting with the controlplane node. To minimize downtime, the deployment gold-nginx should be rescheduled on an alternate node before upgrading each node.
Upgrade controlplane node first and drain node node01 before upgrading it. Pods for gold-nginx should run on the controlplane node subsequently.
</summary><br><b>

+ kubectl drain controlplane --ignore-daemonsets 
+ apt update
+ apt-get install kubeadm=1.26.0-00
+ kubeadm upgrade plan v1.26.0
+ kubeadm upgrade apply v1.26.0
+ apt-get install kubelet=1.26.0-00
+ systemctl daemon-reload
+ systemctl restart kubelet
+ kubectl uncordon controlplane
###### Identify the taint first. 
+ kubectl describe node controlplane | grep -i taint
###### Remove the taint with help of "kubectl taint" command
+ kubectl taint node controlplane node-role.kubernetes.io/control-plane:NoSchedule
###### Verify it, the taint has been removed successfully
+ kubectl describe node controlplane | grep -i taint
+ kubectl drain node01 --ignore-daemonsets
+ apt update
+ apt-get install kubeadm=1.26.0-00
+ kubeadm upgrade node
+ apt-get install kubelet=1.26.0-00
+ systemctl daemon-reload
+ systemctl restart kubelet
+ kubectl uncordon node01
+ kubectl get pods -o wide | grep gold (make sure this is scheduled on node)
</b></details>


