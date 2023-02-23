# Kubernetes

<!-- {% raw %} -->

What's your goal?

* I would like to prepare for CKA certification
  * See [CKA](CKA.md) page
* I would like to learn Kubernetes by practicing both theoritcal and practical material
  * Solve [exercises](#kubernetes-exercises)
  * Solve [questions](#kubernetes-questions)
* I would like to learn parctical Kubernetes
  * Solve [exercises](#kubernetes-exercises)

- [Kubernetes](#kubernetes)
  - [Kubernetes Exercises](#kubernetes-exercises)
    - [Pods](#pods)
    - [Service](#service)
    - [ReplicaSet](#replicaset)
    - [Labels and Selectors](#labels-and-selectors)
    - [Scheduler](#scheduler)
    - [Kustomize](#kustomize)
  - [Kubernetes Questions](#kubernetes-questions)
    - [Kubernetes 101](#kubernetes-101)
    - [Cluster and Architecture](#cluster-and-architecture)
      - [Kubelet](#kubelet)
      - [Nodes Commands](#nodes-commands)
    - [Pods](#pods-1)
      - [Static Pods](#static-pods)
      - [Pods Commands](#pods-commands)
      - [Pods Troubleshooting and Debugging](#pods-troubleshooting-and-debugging)
    - [Labels and Selectors](#labels-and-selectors-1)
    - [Deployments](#deployments)
      - [Deployments Commands](#deployments-commands)
    - [Services](#services)
    - [Ingress](#ingress)
    - [ReplicaSets](#replicasets)
    - [DaemonSet](#daemonset)
      - [DaemonSet - Commands](#daemonset---commands)
    - [StatefulSet](#statefulset)
    - [Storage](#storage)
      - [Volumes](#volumes)
    - [Networking](#networking)
    - [Network Policies](#network-policies)
    - [etcd](#etcd)
    - [Namespaces](#namespaces)
      - [Namespaces - commands](#namespaces---commands)
      - [Resources Quota](#resources-quota)
    - [Operators](#operators)
    - [Secrets](#secrets)
    - [Volumes](#volumes-1)
    - [Access Control](#access-control)
    - [Patterns](#patterns)
    - [CronJob](#cronjob)
    - [Misc](#misc)
    - [Gatekeeper](#gatekeeper)
    - [Policy Testing](#policy-testing)
    - [Helm](#helm)
      - [Commands](#commands)
    - [Security](#security)
    - [Troubleshooting Scenarios](#troubleshooting-scenarios)
    - [Istio](#istio)
    - [Controllers](#controllers)
    - [Scheduler](#scheduler-1)
      - [Node Affinity](#node-affinity)
    - [Taints](#taints)
    - [Resource Limits](#resource-limits)
      - [Resources Limits - Commands](#resources-limits---commands)
    - [Monitoring](#monitoring)
    - [Kustomize](#kustomize-1)
    - [Deployment Strategies](#deployment-strategies)
    - [Scenarios](#scenarios)

## Kubernetes Exercises

### Pods

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| My First Pod | Pods | [Exercise](pods_01.md) | [Solution](solutions/pods_01_solution.md)
| "Killing" Containers | Pods | [Exercise](killing_containers.md) | [Solution](solutions/killing_containers.md)

### Service

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Creating a Service | Service | [Exercise](services_01.md) | [Solution](solutions/services_01_solution.md)

### ReplicaSet

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Creating a ReplicaSet | ReplicaSet | [Exercise](replicaset_01.md) | [Solution](solutions/replicaset_01_solution.md)
| Operating ReplicaSets | ReplicaSet | [Exercise](replicaset_02.md) | [Solution](solutions/replicaset_02_solution.md)
| ReplicaSets Selectors | ReplicaSet | [Exercise](replicaset_03.md) | [Solution](solutions/replicaset_03_solution.md)

### Labels and Selectors

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Labels and Selectors 101 | Labels, Selectors | [Exercise](exercises/labels_and_selectors/exercise.md) | [Solution](exercises/labels_and_selectors/solution.md)
| Node Selectors | Labels, Selectors | [Exercise](exercises/node_selectors/exercise.md) | [Solution](exercises/node_selectors/solution.md)


### Scheduler

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Taints 101 | Taints | [Exercise](exercises/taints_101/exercise.md) | [Solution](exercises/taints_101/solution.md)

### Kustomize

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| common labels | Kustomize | [Exercise](exercises/kustomize_common_labels/exercise.md) | [Solution](exercises/kustomize_common_labels/solution.md)

## Kubernetes Questions

### Kubernetes 101

<details>
<summary>What is Kubernetes? Why organizations are using it?</summary><br><b>

Kubernetes is an open-source system that provides users with the ability to manage, scale and deploy containerized applications.

To understand what Kubernetes is good for, let's look at some examples:

* You would like to run a certain application in a container on multiple different locations and sync changes across all of them, no matter where they run
* Performing updates and changes across hundreds of containers
* Handle cases where the current load requires to scale up (or down)

</b></details>

<details>
<summary>When or why NOT to use Kubernetes?</summary><br><b>

  - If you manage low level infrastructure or baremetals, Kubernetes is probably not what you need or want
  - If you are a small team (like less than 20 engineers) running less than a dozen of containers, Kubernetes might be an overkill (even if you need scale, rolling out updates, etc.). You might still enjoy the benefits of using managed Kubernetes, but you definitely want to think about it carefully before making a decision on whether to adopt it.

</b></details>

<details>
<summary>What are some of Kubernetes features?</summary><br><b>

  - Self-Healing: Kubernetes uses health checks to monitor containers and run certain actions upon failure or other type of events, like restarting the container
  - Load Balancing: Kubernetes can split and/or balance requests to applications running in the cluster, based on the state of the Pods running the application
  - Operators: Kubernetes packaged applications that can use the API of the cluster to update its state and trigger actions based on events and application state changes
  - Automated Rollout: Gradual updates roll out to applications and support in roll back in case anything goes wrong
  - Scaling: Scaling horizontally (down and up) based on different state parameters and custom defined criteria
  - Secrets: you have a mechanism for storing user names, passwords and service endpoints in a private way, where not everyone using the cluster are able to view it

</b></details>

<details>
<summary>What Kubernetes objects are there?</summary><br><b>

  * Pod
  * Service
  * ReplicationController
  * ReplicaSet
  * DaemonSet
  * Namespace
  * ConfigMap
  ...
</b></details>

<details>
<summary>What fields are mandatory with any Kubernetes object?</summary><br><b>

metadata, kind and apiVersion

</b></details>

<details>
<summary>What is kubectl?</summary><br><b>

Kubectl is the Kubernetes command line tool that allows you to run commands against Kubernetes clusters. For example, you can use kubectl to deploy applications, inspect and manage cluster resources, and view logs.

</b></details>

<details>
<summary>What Kubernetes objects do you usually use when deploying applications in Kubernetes?</summary><br><b>

* Deployment - creates the Pods () and watches them
* Service: route traffic to Pods internally
* Ingress: route traffic from outside the cluster

</b></details>

<details>
<summary>Why there is no such command in Kubernetes? <code>kubectl get containers</code></summary><br><b>

Becaused container is not a Kubernetes object. The smallest object unit in Kubernetes is a Pod. In a single Pod you can find one or more containers.

</b></details>

<details>
<summary>What actions or operations you consider as best practices when it comes to Kubernetes?</summary><br><b>

  - Always make sure Kubernetes YAML files are valid. Applying automated checks and pipelines is recommended.
  - Always specify requests and limits to prevent situation where containers are using the entire cluster memory which may lead to OOM issue
  - Specify labels to logically group Pods, Deployments, etc. Use labels to identify the type of the application for example, among other things

</b></details>

### Cluster and Architecture

<details>
<summary>What is a Kubernetes Cluster?</summary><br><b>

Red Hat Definition: "A Kubernetes cluster is a set of node machines for running containerized applications. If you’re running Kubernetes, you’re running a cluster.
At a minimum, a cluster contains a worker node and a master node."

Read more [here](https://www.redhat.com/en/topics/containers/what-is-a-kubernetes-cluster)
</b></details>

<details>
<summary>What is a Node?</summary><br><b>

A node is a virtual or a physical machine that serves as a worker for running the applications.<br>
It's recommended to have at least 3 nodes in a production environment.
</b></details>

<details>
<summary>What the master node is responsible for?</summary><br><b>

The master coordinates all the workflows in the cluster:

* Scheduling applications
* Managing desired state
* Rolling out new updates

</b></details>

<details>
<summary>Describe shortly and in high-level, what happens when you run <code>kubectl get nodes</code></summary><br><b>

1. Your user is getting authenticated
2. Request is validated by the kube-apiserver
3. Data is retrieved from etcd
</b></details>

<details>
<summary>True or False? Every cluster must have 0 or more master nodes and at least 1 worker</summary><br><b>

False. A Kubernetes cluster consists of at least 1 master and can have 0 workers (although that wouldn't be very useful...)

</b></details> 

<details>
<summary>What are the components of the master node (aka control plane)?</summary><br><b>

  * API Server - the Kubernetes API. All cluster components communicate through it
  * Scheduler - assigns an application with a worker node it can run on
  * Controller Manager - cluster maintenance (replications, node failures, etc.)
  * etcd - stores cluster configuration

</b></details>

<details>
<summary>What are the components of a worker node (aka data plane)?</summary><br><b>

  * Kubelet - an agent responsible for node communication with the master.
  * Kube-proxy - load balancing traffic between app components
  * Container runtime - the engine runs the containers (Podman, Docker, ...)

</b></details>

<details>
<summary>Place the components on the right side of the image in the right place in the drawing<br>
<img src="images/cluster_architecture_exercise.png"/>
</summary><br><b>
<img src="images/cluster_architecture_solution.png"/>

</b></details>

<details>
<summary>You are managing multiple Kubernetes clusters. How do you quickly change between the clusters using kubectl?</summary><br><b>

`kubectl config use-context`
</b></details>

<details>
<summary>How do you prevent high memory usage in your Kubernetes cluster and possibly issues like memory leak and OOM?</summary><br><b>

Apply requests and limits, especially on third party applications (where the uncertainty is even bigger)
</b></details>

<details>
<summary>Do you have experience with deploying a Kubernetes cluster? If so, can you describe the process in high-level?</summary><br><b>

1. Create multiple instances you will use as Kubernetes nodes/workers. Create also an instance to act as the Master. The instances can be provisioned in a cloud or they can be virtual machines on bare metal hosts.
2. Provision a certificate authority that will be used to generate TLS certificates for the different components of a Kubernetes cluster (kubelet, etcd, ...)
  1. Generate a certificate and private key for the different components
3. Generate kubeconfigs so the different clients of Kubernetes can locate the API servers and authenticate.
4. Generate encryption key that will be used for encrypting the cluster data
5. Create an etcd cluster
</b></details>

<details>
<summary>Which command will list all the object types in a cluster?</summary><br><b>

`kubectl api-resources`
</b></details>

<details>
<summary>What <code>kubectl get componentstatus</code> does?</summary><br><b>

Outputs the status of each of the control plane components.
</b></details>

#### Kubelet

<details>
<summary>What happens to running pods if if you stop Kubelet on the worker nodes?</summary><br><b>

</b></details>

#### Nodes Commands

<details>
<summary>Run a command to view all nodes of the cluster</summary><br><b>

`kubectl get nodes`

Note: You might want to create an alias (`alias k=kubectl`) and get used to `k get no`
</b></details>

<details>
<summary>Create a list of all nodes in JSON format and store it in a file called "some_nodes.json"</summary><br><b>

`k get nodes -o json > some_nodes.json`
</b></details>

<details>
<summary>Check what labels one of your nodes in the cluster has</summary><br><b>

`k get no minikube --show-labels`
</b></details>

### Pods

<details>
<summary>Explain what is a Pod</summary><br><b>

A Pod is a group of one or more containers, with shared storage and network resources, and a specification for how to run the containers.

Pods are the smallest deployable units of computing that you can create and manage in Kubernetes. 

</b></details>

<details>
<summary>Deploy a pod called "my-pod" using the nginx:alpine image</summary><br><b>

`kubectl run my-pod --image=nginx:alpine`

If you are a Kubernetes beginner you should know that this is not a common way to run Pods. The common way is to run a Deployment which in turn runs Pod(s).

In addition, Pods and/or Deployments are usually defined in files rather than executed directly using only the CLI arguments.
</b></details>

<details>
<summary>What are your thoughts on "Pods are not meant to be created directly"?</summary><br><b>

Pods are usually indeed not created directly. You'll notice that Pods are usually created as part of another entities such as Deployments or ReplicaSets.

If a Pod dies, Kubernetes will not bring it back. This is why it's more useful for example to define ReplicaSets that will make sure that a given number of Pods will always run, even after a certain Pod dies.
</b></details>

<details>
<summary>How many containers can a pod contain?</summary><br><b>

A pod can include multiple containers but in most cases it would probably be one container per pod.

There are some patterns where it makes to run more than one container like the "side-car" pattern where you might want to perform logging or some other operation that is executed by another container running with your app container in the same Pod.
</b></details>

<details>
<summary>What use cases exist for running multiple containers in a single pod?</summary><br><b>

A web application with separate (= in their own containers) logging and monitoring components/adapters is one examples.<br>
A CI/CD pipeline (using Tekton for example) can run multiple containers in one Pod if a Task contains multiple commands.
</b></details>

<details>
<summary>What are the possible Pod phases?</summary><br><b>

  * Running - The Pod bound to a node and at least one container is running
  * Failed/Error - At least one container in the Pod terminated with a failure
  * Succeeded - Every container in the Pod terminated with success
  * Unknown - Pod's state could not be obtained
  * Pending - Containers are not yet running (Perhaps images are still being downloaded or the pod wasn't scheduled yet)
</b></details>

<details>
<summary>True or False? By default, pods are isolated. This means they are unable to receive traffic from any source</summary><br><b>

False. By default, pods are non-isolated = pods accept traffic from any source.
</b></details>

<details>
<summary>True or False? The "Pending" phase means the Pod was not yet accepted by the Kubernetes cluster so the scheduler can't run it unless it's accepted</summary><br><b>

False. "Pending" is after the Pod was accepted by the cluster, but the container can't run for different reasons like images not yet downloaded.
</b></details>

<details>
<summary>True or False? A single Pod can be split across multiple nodes</summary><br><b>

False. A single Pod can run on a single node.
</b></details>

<details>
<summary>You run a pod and you see the status <code>ContainerCreating</code></summary><br><b>
</b></details>

<details>
<summary>True or False? A volume defined in Pod can be accessed by all the containers of that Pod</summary><br><b>

True.
</b></details>

<details>
<summary>What happens when you run a Pod with kubectl?</summary><br><b>

1. Kubectl sends a request to the API server (kube-apiserver) to create the Pod
   1. In the the process the user gets authenticated and the request is being validated.
   2. etcd is being updated with the data
2. The Scheduler detects that there is an unassigned Pod by monitoring the API server (kube-apiserver)
3. The Scheduler chooses a node to assign the Pod to
   1. etcd is being updated with the information
4. The Scheduler updates the API server about which node it chose
5. Kubelet (which also monitors the API server) notices there is a Pod assigned to the same node on which it runs and that Pod isn't running
6. Kubelet sends request to the container engine (e.g. Docker) to create and run the containers
7. An update is sent by Kubelet to the API server (notifying it that the Pod is running)
   1. etcd is being updated by the API server again
</b></details>

<details>
<summary>How to confirm a container is running after running the command <code>kubectl run web --image nginxinc/nginx-unprivileged</code></summary><br><b>

* When you run `kubectl describe pods <POD_NAME>` it will tell whether the container is running:
`Status:       Running`
* Run a command inside the container: `kubectl exec web -- ls`
</b></details>

<details>
<summary>After running <code>kubectl run database --image mongo</code> you see the status is "CrashLoopBackOff". What could possibly went wrong and what do you do to confirm?</summary><br><b>

"CrashLoopBackOff" means the Pod is starting, crashing, starting...and so it repeats itself.<br>
There are many different reasons to get this error - lack of permissions, init-container misconfiguration, persistent volume connection issue, etc.

One of the ways to check why it happened it to run `kubectl describe po <POD_NAME>` and having a look at the exit code

```
 Last State:     Terminated
   Reason:       Error
   Exit Code:    100
```

Another way to check what's going on, is to run `kubectl logs <POD_NAME>`. This will provide us with the logs from the containers running in that Pod.
</b></details>

<details>
<summary>Explain the purpose of the following lines

```
livenessProbe:
  exec:
    command:
    - cat
    - /appStatus
  initialDelaySeconds: 10
  periodSeconds: 5
```
</summary><br><b>

These lines make use of `liveness probe`. It's used to restart a container when it reaches a non-desired state.<br>
In this case, if the command `cat /appStatus` fails, Kubernetes will kill the container and will apply the restart policy. The `initialDelaySeconds: 10` means that Kubelet will wait 10 seconds before running the command/probe for the first time. From that point on, it will run it every 5 seconds, as defined with `periodSeconds`
</b></details>

<details>
<summary>Explain the purpose of the following lines

```
readinessProbe:
      tcpSocket:
        port: 2017
      initialDelaySeconds: 15
      periodSeconds: 20
```
</summary><br><b>

They define a readiness probe where the Pod will not be marked as "Ready" before it will be possible to connect to port 2017 of the container. The first check/probe will start after 15 seconds from the moment the container started to run and will continue to run the check/probe every 20 seconds until it will manage to connect to the defined port.
</b></details>

<details>
<summary>What does the "ErrImagePull" status of a Pod means?</summary><br><b>

It wasn't able to pull the image specified for running the container(s). This can happen if the client didn't authenticated for example.<br>
More details can be obtained with `kubectl describe po <POD_NAME>`.
</b></details>

<details>
<summary>What happens when you delete a Pod?</summary><br><b>

1. The `TERM` signal is sent to kill the main processes inside the containers of the given Pod
2. Each container is given a period of 30 seconds to shut down the processes gracefully
3. If the grace period expires, the `KILL` signal is used to kill the processes forcefully and the containers as well
</b></details>

<details>
<summary>Explain liveness probes</summary><br><b>

Liveness probes is a useful mechanism used for restarting the container when a certain check/probe, the user has defined, fails.<br>
For example, the user can define that the command `cat /app/status` will run every X seconds and the moment this command fails, the container will be restarted.

You can read more about it in [kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes)
</b></details>

<details>
<summary>Explain readiness probes</summary><br><b>

readiness probes used by Kubelet to know when a container is ready to start running, accepting traffic.<br>
For example, a readiness probe can be to connect port 8080 on a container. Once Kubelet manages to connect it, the Pod is marked as ready

You can read more about it in [kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes)
</b></details>

<details>
<summary>How readiness probe status affect Services when they are combined?</summary><br><b>

Only containers whose state set to Success will be able to receive requests sent to the Service.
</b></details>

<details>
<summary>Why it's common to have only one container per Pod in most cases?</summary><br><b>

One reason is that it makes it harder to scale when you need to scale only one of the containers in a given Pod.
</b></details>

<details>
<summary>True or False? Once a Pod is assisgned to a worker node, it will only run on that node, even if it fails at some point and spins up a new Pod</summary><br><b>

True.
</b></details>

<details>
<summary>True or False? Each Pod, when created, gets its own public IP address</summary><br><b>

False. Each Pod gets an IP address but an internal one and not publicly accessible.

To make a Pod externally accessible, we need to use an object called Service in Kubernetes.
</b></details>

#### Static Pods

<details>
<summary>What are Static Pods?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/): "Static Pods are managed directly by the kubelet daemon on a specific node, without the API server observing them. Unlike Pods that are managed by the control plane (for example, a Deployment); instead, the kubelet watches each static Pod (and restarts it if it fails)."
</b></details>

<details>
<summary>True or False? The same as there are "Static Pods" there are other static resources like "deployments" and "replicasets"</summary><br><b>

False.
</b></details>

<details>
<summary>What are some use cases for using Static Pods?</summary><br><b>

One clear use case is running Control Plane Pods -  running Pods such as kube-apiserver, scheduler, etc. These should run and operate regardless of whether some components of the cluster work or not and they should run on specific nodes of the cluster.
</b></details>

<details>
<summary>How to identify which Pods are Static Pods?</summary><br><b>

The suffix of the Pods is the same as the name of the nodes on which they are running
TODO: check if it's always the case.
</b></details>

<details>
<summary>Which of the following is not a static pod?:

* kube-scheduler
* kube-proxy
* kube-apiserver
</summary><br><b>

kube-proxy - it's a DaemonSet (since it has to be presented on every node in the cluster). There is no one specific node on which it has to run.
</b></details>

<details>
<summary>Where static Pods manifests are located?</summary><br><b>

Most of the time it's in /etc/kubernetes/manifests but you can verify with `grep -i static /var/lib/kubelet/config.yaml` to locate the value of `statisPodsPath`.

It might be that your config is in different path. To verify run `ps -ef | grep kubelet` and see what is the value of --config argument of the process `/usr/bin/kubelet`

The key itself for defining the path of static Pods is `staticPodPath`. So if your config is in `/var/lib/kubelet/config.yaml` you can run `grep staticPodPath /var/lib/kubelet/config.yaml`.
</b></details>

<details>
<summary>Describe how would you delete a static Pod
</summary><br><b>

Locate the static Pods directory (look at `staticPodPath` in kubelet configuration file).

Go to that directory and remove the manifest/definition of the staic Pod (`rm <STATIC_POD_PATH>/<POD_DEFINITION_FILE>`)
</b></details>

#### Pods Commands

<details>
<summary>How to check to which worker node the pods were scheduled to? In other words, how to check on which node a certain Pod is running?</summary><br><b>

`kubectl get pods -o wide`
</b></details>

<details>
<summary>How to delete a pod?</summary><br><b>

`kubectl delete pod pod_name`
</b></details>

<details>
<summary>List all the pods with the label "env=prod"</summary><br><b>

`k get po -l env=prod`

To count them: `k get po -l env=prod --no-headers | wc -l`
</b></details>

<details>
<summary>How to list the pods in the current namespace?</summary><br><b>

`kubectl get po`
</b></details>

<details>
<summary>How view all the pods running in all the namespaces?</summary><br><b>

`kubectl get pods --all-namespaces`
</b></details>

#### Pods Troubleshooting and Debugging

<details>
<summary>You try to run a Pod but it's in "Pending" state. What might be the reason?</summary><br><b>

One possible reason is that the scheduler which supposed to schedule Pods on nodes, is not running. To verify it, you can run `kubectl get po -A | grep scheduler` or check directly in `kube-system` namespace.
</b></details>

<details>
<summary>What <code>kubectl logs [pod-name]</code> command does?</summary><br><b>

Prints the logs for a container in a pod.
</b></details>

<details>
<summary>What <code>kubectl describe pod [pod name] does?</code> command does?</summary><br><b>

Show details of a specific resource or group of resources.
</b></details>

<details>
<summary>Create a static pod with the image <code>python</code> that runs the command <code>sleep 2017</code></summary><br><b>

First change to the directory tracked by kubelet for creating static pod: `cd /etc/kubernetes/manifests` (you can verify path by reading kubelet conf file)

Now create the definition/manifest in that directory
`k run some-pod --image=python --command sleep 2017 --restart=Never --dry-run=client -o yaml > statuc-pod.yaml`
</b></details>

### Labels and Selectors

<details>
<summary>Explain Labels</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/): "Labels are key/value pairs that are attached to objects, such as pods. Labels are intended to be used to specify identifying attributes of objects that are meaningful and relevant to users, but do not directly imply semantics to the core system. Labels can be used to organize and to select subsets of objects. Labels can be attached to objects at creation time and subsequently added and modified at any time. Each object can have a set of key/value labels defined. Each Key must be unique for a given object."
</b></details>

<details>
<summary>Explain selectors</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors): "Unlike names and UIDs, labels do not provide uniqueness. In general, we expect many objects to carry the same label(s).

Via a label selector, the client/user can identify a set of objects. The label selector is the core grouping primitive in Kubernetes.

The API currently supports two types of selectors: equality-based and set-based. A label selector can be made of multiple requirements which are comma-separated. In the case of multiple requirements, all must be satisfied so the comma separator acts as a logical AND (&&) operator."
</b></details>

<details>
<summary>Provide some actual examples of how labels are used</summary><br><b>

* Can be used by the scheduler to place certain Pods (with certain labels) on specific nodes
* Used by replicasets to track pods which have to be scaled
</b></details>

<details>
<summary>What are Annotations?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/): "You can use Kubernetes annotations to attach arbitrary non-identifying metadata to objects. Clients such as tools and libraries can retrieve this metadata."
</b></details>

<details>
<summary>How annotations different from labels?</summary><br><b>

[Kuberenets.io](Labels can be used to select objects and to find collections of objects that satisfy certain conditions. In contrast, annotations are not used to identify and select objects. The metadata in an annotation can be small or large, structured or unstructured, and can include characters not permitted by labels.): "Labels can be used to select objects and to find collections of objects that satisfy certain conditions. In contrast, annotations are not used to identify and select objects. The metadata in an annotation can be small or large, structured or unstructured, and can include characters not permitted by labels."
</b></details>

<details>
<summary>How to view the logs of a container running in a Pod?</summary><br><b>

`k logs POD_NAME`
</b></details>

<details>
<summary>There are two containers inside a Pod called "some-pod". What will happen if you run <code>kubectl logs some-pod</code></summary><br><b>

It won't work because there are two containers inside the Pod and you need to specify one of them with `kubectl logs POD_NAME -c CONTAINER_NAME`
</b></details>

### Deployments

<details>
<summary>What is a "Deployment" in Kubernetes?</summary><br><b>

A Kubernetes Deployment is used to tell Kubernetes how to create or modify instances of the pods that hold a containerized application.
Deployments can scale the number of replica pods, enable rollout of updated code in a controlled manner, or roll back to an earlier deployment version if necessary. 

A Deployment is a declarative statement for the desired state for Pods and Replica Sets.
</b></details>

<details>
<summary>How to create a deployment with the image "nginx:alpine"?</code></summary><br><b>

`kubectl create deployment my_first_deployment --image=nginx:alpine`

OR

```
cat << EOF | kubectl create -f -
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:alpine
EOF
```
</b></details>

<details>
<summary>How to verify a deployment was created?</code></summary><br><b>

`kubectl get deployments` or `kubectl get deploy`

This command lists all the Deployment objects created and exist in the cluster. It doesn't mean the deployments are readt and running. This can be checked with the "READY" and "AVAILABLE" columns.
</b></details>

<details>
<summary>How to edit a deployment?</code></summary><br><b>

`kubectl edit deployment <DEPLOYMENT_NAME>`
</b></details>

<details>
<summary>What happens after you edit a deployment and change the image?</summary><br><b>

The pod will terminate and another, new pod, will be created.

Also, when looking at the replicaset, you'll see the old replica doesn't have any pods and a new replicaset is created.
</b></details>

<details>
<summary>How to delete a deployment?</summary><br><b>

One way is by specifying the deployment name: `kubectl delete deployment [deployment_name]`

Another way is using the deployment configuration file: `kubectl delete -f deployment.yaml`
</b></details>

<details>
<summary>What happens when you delete a deployment?</summary><br><b>

The pod related to the deployment will terminate and the replicaset will be removed.
</b></details>

<details>
<summary>What happens behind the scenes when you create a Deployment object?</summary><br><b>

The following occurs when you run `kubectl create deployment some_deployment --image=nginx`

1. HTTP request sent to kubernetes API server on the cluster to create a new deployment
2. A new Pod object is created and scheduled to one of the workers nodes
3. Kublet on the worker node notices the new Pod and instructs the Container runtime engine to pull the image from the registry
4. A new container is created using the image that was just pulled
</b></details>

<details>
<summary>How make an app accessible on private or external network?</summary><br><b>

Using a Service.
</b></details>

<details>
<summary>Can you use a Deployment for stateful applications?</summary><br><b>
</b></details>

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

#### Deployments Commands

<details>
<summary>Create a file definition/manifest of a deployment called "dep", with 3 replicas that uses the image 'redis'</summary><br><b>

`k create deploy dep -o yaml --image=redis --dry-run=client --replicas 3 > deployment.yaml `

</b></details>

<details>
<summary>Delete the deployment `depdep`</summary><br><b>

`k delete deploy depdep`

</b></details>

<details>
<summary>Create a deployment called "pluck" using the image "redis" and make sure it runs 5 replicas</summary><br><b>

`kubectl create deployment pluck --image=redis`

`kubectl scale deployment pluck --replicas=5`
</b></details>

<details>
<summary>Create a deployment with the following properties:

* called "blufer"
* using the image "python"
* runs 3 replicas
* all pods will be placed on a node that has the label "blufer"
</summary><br><b>

`kubectl create deployment blufer --image=python --replicas=3 -o yaml --dry-run=client > deployment.yaml`

Add the following section (`vi deployment.yaml`):

```
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedlingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: blufer
            operator: Exists
```

`kubectl apply -f deployment.yaml`
</b></details>

### Services

<details>
<summary>What is a Service in Kubernetes?</summary><br><b>

"An abstract way to expose an application running on a set of Pods as a network service." - read more [here](https://kubernetes.io/docs/concepts/services-networking/service)

In simpler words, it allows you to add an internal or external connectivity to a certain application running in a container.
</b></details>

<details>
<summary>Place the components in the right placeholders in regards to Kubernetes service<br>
<img src="images/service_exercise.png"/>
</summary><br><b>

<img src="images/service_solution.png"/>

</b></details>


<details>
<summary>How to create a service for an existing deployment called "alle" on port 8080 so the Pod(s) accessible via a Load Balancer?</summary><br><b>

The imperative way:

`kubectl expose deployment alle --type=LoadBalancer --port 8080`
</b></details>

<details>
<summary>True or False? The lifecycle of Pods and Services isn't connected so when a Pod dies, the Service still stays </summary><br><b>

True
</b></details>

<details>
<summary>After creating a service, how to check it was created?</summary><br><b>

`kubectl get svc`
</b></details>

<details>
<summary>What's the default Service type?</summary><br><b>

ClusterIP - used for internal communication.
</b></details>

<details>
<summary>What Service types are there?</summary><br><b>

* ClusterIP
* NodePort
* LoadBalancer
* ExternalName

More on this topic [here](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types)
</b></details>

<details>
<summary>How Service and Deployment are connected?</summary><br><b>

The truth is they aren't connected. Service points to Pod(s) directly, without connecting to the Deployment in any way.
</b></details>

<details>
<summary>What are important steps in defining/adding a Service?</summary><br><b>

1. Making sure that targetPort of the Service is matching the containerPort of the Pod
2. Making sure that selector matches at least one of the Pod's labels

</b></details>

<details>
<summary>What is the default service type in Kubernetes and what is it used for?</summary><br><b>

The default is ClusterIP and it's used for exposing a port internally. It's useful when you want to enable internal communication between Pods and prevent any external access.

</b></details>

<details>
<summary>How to get information on a certain service?</summary><br><b>

`kubctl describe service <SERVICE_NAME>`

It's more common to use `kubectl describe svc ...`

</b></details>

<details>
<summary>What the following command does?

```
kubectl expose rs some-replicaset --name=replicaset-svc --target-port=2017 --type=NodePort
```
</summary><br><b>

It exposes a ReplicaSet by creating a service called 'replicaset-svc'. The exposed port is 2017 (this is the port used by the application) and the service type is NodePort which means it will be reachable externally.
</b></details>

<details>
<summary>True or False? the target port, in the case of running the following command, will be exposed only on one of the Kubernetes cluster nodes but it will routed to all the pods

```
kubectl expose rs some-replicaset --name=replicaset-svc --target-port=2017 --type=NodePort
```
</summary><br><b>

False. It will be exposed on every node of the cluster and will be routed to one of the Pods (which belong to the ReplicaSet)
</b></details>

<details>
<summary>How to verify that a certain service configured to forward the requests to a given pod</summary><br><b>

Run `kubectl describe service` and see if the IPs from "Endpoints" match any IPs from the output of `kubectl get pod -o wide`
</b></details>

<details>
<summary>Explain what will happen when running apply on the following block

```
apiVersion: v1
kind: Service
metadata:
  name: some-app
spec:
  type: NodePort
  ports:
  - port: 8080
    nodePort: 2017
    protocol: TCP
  selector:
    type: backend
    service: some-app
```
</summary><br><b>

It creates a new Service of the type "NodePort" which means it can be used for internal and external communication with the app.<br>
The port of the application is 8080 and the requests will forwarded to this port. The exposed port is 2017. As a note, this is not a common practice, to specify the nodePort.<br>
The port used TCP (instead of UDP) and this is also the default so you don't have to specify it.<br>
The selector used by the Service to know to which Pods to forward the requests. In this case, Pods with the label "type: backend" and "service: some-app".<br>
</b></details>

<details>
<summary>How to turn the following service into an external one?

```
spec:
  selector:
    app: some-app
  ports:
    - protocol: TCP
      port: 8081
      targetPort: 8081
```
</summary><br><b>

Adding `type: LoadBalancer` and `nodePort`

```
spec:
  selector:
    app: some-app
  type: LoadBalancer
  ports:
    - protocol: TCP
      port: 8081
      targetPort: 8081
      nodePort: 32412
```
</b></details>

<details>
<summary>What would you use to route traffic from outside the Kubernetes cluster to services within a cluster?</summary><br><b>

Ingress
</b></details>

<details>
<summary>True or False? When "NodePort" is used, "ClusterIP" will be created automatically?</summary><br><b>

True
</b></details>

<details>
<summary>When would you use the "LoadBalancer" type</summary><br><b>

Mostly when you would like to combine it with cloud provider's load balancer
</b></details>

<details>
<summary>How would you map a service to an external address?</summary><br><b>

Using the 'ExternalName' directive.
</b></details>

<details>
<summary>Describe in detail what happens when you create a service</summary><br><b>

1. Kubectl sends a request to the API server to create a Service
2. The controller detects there is a new Service
3. Endpoint objects created with the same name as the service, by the controller
4. The controller is using the Service selector to identify the endpoints
5. kube-proxy detects there is a new endpoint object + new service and adds iptables rules to capture traffic to the Service port and redirect it to endpoints
6. kube-dns detects there is a new Service and adds the container record to the dns server
</b></details>

<details>
<summary>How to list the endpoints of a certain app?</summary><br><b>

`kubectl get ep <name>`
</b></details>

<details>
<summary>How can you find out information on a Service related to a certain Pod if all you can use is <code>kubectl exec <POD_NAME> -- </code></summary><br><b>

You can run `kubectl exec <POD_NAME> -- env` which will give you a couple environment variables related to the Service.<br>
Variables such as `[SERVICE_NAME]_SERVICE_HOST`, `[SERVICE_NAME]_SERVICE_PORT`, ...
</b></details>

<details>
<summary>Describe what happens when a container tries to connect with its corresponding Service for the first time. Explain who added each of the components you include in your description</summary><br><b>

  - The container looks at the nameserver defined in /etc/resolv.conf
  - The container queries the nameserver so the address is resolved to the Service IP
  - Requests sent to the Service IP are forwarded with iptables rules (or other chosen software) to the endpoint(s).

Explanation as to who added them:

  - The nameserver in the container is added by kubelet during the scheduling of the Pod, by using kube-dns
  - The DNS record of the service is added by kube-dns during the Service creation
  - iptables rules are added by kube-proxy during Endpoint and Service creation
</b></details>

<details>
<summary>Describe in high level what happens when you run <code>kubctl expose deployment remo --type=LoadBalancer --port 8080</code></summary><br><b>

1. Kubectl sends a request to Kubernetes API to create a Service object
2. Kubernetes asks the cloud provider (e.g. AWS, GCP, Azure) to provision a load balancer
3. The newly created load balancer forwards incoming traffic to relevant worker node(s) which forwards the traffic to the relevant containers
</b></details>

<details>
<summary>After creating a service that forwards incoming external traffic to the containerized application, how to make sure it works?</summary><br><b>

You can run `curl <SERIVCE IP>:<SERVICE PORT>` to examine the output.
</b></details>

<details>
<summary>An internal load balancer in Kubernetes is called <code>____</code> and an external load balancer is called <code>____</code></summary><br><b>

An internal load balancer in Kubernetes is called Service and an external load balancer is Ingress
</b></details>

### Ingress

<details>
<summary>What is Ingress?</summary><br><b>

From Kubernetes docs: "Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource."

Read more [here](https://kubernetes.io/docs/concepts/services-networking/ingress/)
</b></details>

<details>
<summary>Complete the following configuration file to make it Ingress

```
metadata:
  name: someapp-ingress
spec:
```
</summary><br><b>
There are several ways to answer this question.

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: someapp-ingress
spec:
  rules:
  - host: my.host
    http:
      paths:
      - backend:
          serviceName: someapp-internal-service
          servicePort: 8080
```
</b></details>


<details>
<summary>Explain the meaning of "http", "host" and "backend" directives

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: someapp-ingress
spec:
  rules:
  - host: my.host
    http:
      paths:
      - backend:
          serviceName: someapp-internal-service
          servicePort: 8080
```
</summary><br><b>

host is the entry point of the cluster so basically a valid domain address that maps to cluster's node IP address<br>
the http line used for specifying that incoming requests will be forwarded to the internal service using http.<br>
backend is referencing the internal service (serviceName is the name under metadata and servicePort is the port under the ports section).
</b></details>

<details>
<summary>Why using a wildcard in ingress host may lead to issues?</summary><br><b>

The reason you should not wildcard value in a host (like `- host: *`) is because you basically tell your Kubernetes cluster to forward all the traffic to the container where you used this ingress. This may cause the entire cluster to go down.
</b></details>

<details>
<summary>What is Ingress Controller?</summary><br><b>

An implementation for Ingress. It's basically another pod (or set of pods) that does evaluates and processes Ingress rules and this it manages all the redirections. 

There are multiple Ingress Controller implementations (the one from Kubernetes is Kubernetes Nginx Ingress Controller).
</b></details>

<details>
<summary>What are some use cases for using Ingress?</summary><br><b>

* Multiple sub-domains (multiple host entries, each with its own service)
* One domain with multiple services (multiple paths where each one is mapped to a different service/application)
</b></details>

<details>
<summary>How to list Ingress in your namespace?</summary><br><b>

kubectl get ingress
</b></details>

<details>
<summary>What is Ingress Default Backend?</summary><br><b>

It specifies what do with an incoming request to the Kubernetes cluster that isn't mapped to any backend (= no rule to for mapping the request to a service). If the default backend service isn't defined, it's recommended to define so users still see some kind of message instead of nothing or unclear error.
</b></details>

<details>
<summary>How to configure a default backend?</summary><br><b>

Create Service resource that specifies the name of the default backend as reflected in `kubectl describe ingress ...` and the port under the ports section.
</b></details>

<details>
<summary>How to configure TLS with Ingress?</summary><br><b>

Add tls and secretName entries.

```
spec:
  tls:
  - hosts:
    - some_app.com
    secretName: someapp-secret-tls
```
</b></details>

<details>
<summary>True or False? When configuring Ingress with TLS, the Secret component must be in the same namespace as the Ingress component</summary><br><b>

True
</b></details>

<details>
<summary>Which Kubernetes concept would you use to control traffic flow at the IP address or port level? </summary><br><b>

Network Policies
</b></details>

<details>
<summary>How to scale an application (deplyoment) so it runs more than one instance of the application?</summary><br><b>

To run two instances of the applicaation?

`kubectl scale deployment <DEPLOYMENT_NAME> --replicas=2`

You can speciy any other number, given that your application knows how to scale.
</b></details>

### ReplicaSets

<details>
<summary>What is the purpose of ReplicaSet?</summary><br><b>

[kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset): "A ReplicaSet's purpose is to maintain a stable set of replica Pods running at any given time. As such, it is often used to guarantee the availability of a specified number of identical Pods."

In simpler words, a ReplicaSet will ensure the specified number of Pods replicas is running for a selected Pod. If there are more Pods than defined in the ReplicaSet, some will be removed. If there are less than what is defined in the ReplicaSet then, then more replicas will be added.
</b></details>

<details>
<summary>What the following block of lines does?

```
spec:
  replicas: 2
  selector:
    matchLabels:
      type: backend
  template:
    metadata:
      labels:
        type: backend
    spec:
      containers:
      - name: httpd-yup
        image: httpd
```
</summary><br><b>

It defines a replicaset for Pods whose type is set to "backend" so at any given point of time there will be 2 concurrent Pods running.
</b></details>

<details>
<summary>What will happen when a Pod, created by ReplicaSet, is deleted directly with <code>kubectl delete po ...</code>?</summary><br><b>

The ReplicaSet will create a new Pod in order to reach the desired number of replicas.
</b></details>

<details>
<summary>True or False? If a ReplicaSet defines 2 replicas but there 3 Pods running matching the ReplicaSet selector, it will do nothing</summary><br><b>

False. It will terminate one of the Pods to reach the desired state of 2 replicas.
</b></details>

<details>
<summary>Describe the sequence of events in case of creating a ReplicaSet</summary><br><b>

* The client (e.g. kubectl) sends a request to the API server to create a ReplicaSet
* The Controller detects there is a new event requesting for a ReplicaSet
* The controller creates new Pod definitions (the exact number depends on what is defined in the ReplicaSet definition)
* The scheduler detects unassigned Pods and decides to which nodes to assign the Pods. This information sent to the API server
* Kubelet detects that two Pods were assigned to the node it's running on (as it constantly watching the API server)
* Kubelet sends requests to the container engine, to create the containers that are part of the Pod
* Kubelet sends a request to the API server to notify it the Pods were created
</b></details>

<details>
<summary>How to list ReplicaSets in the current namespace?</summary><br><b>

`kubectl get rs`
</b></details>

<details>
<summary>Is it possible to delete ReplicaSet without deleting the Pods it created?</summary><br><b>

Yes, with `--cascase=false`.

`kubectl delete -f rs.yaml --cascade=false`
</b></details>

<details>
<summary>What is the default number of replicas if not explicitly specified?</summary><br><b>

1
</b></details>

<details>
<summary>What the following output of <code>kubectl get rs</code> means?

NAME                    DESIRED   CURRENT   READY   AGE
web                     2         2         0       2m23s
</summary><br><b>

The replicaset `web` has 2 replicas. It seems that the containers inside the Pod(s) are not yet running since the value of READY is 0. It might be normal since it takes time for some containers to start running and it might be due to an error. Running `kubectl describe po POD_NAME` or `kubectl logs POD_NAME` can give us more information.
</b></details>

<details>
<summary>True or False? Pods specified by the selector field of ReplicaSet must be created by the ReplicaSet itself</summary><br><b>

False. The Pods can be already running and initially they can be created by any object. It doesn't matter for the ReplicaSet and not a requirement for it to acquire and monitor them.
</b></details>

<details>
<summary>True or False? In case of a ReplicaSet, if Pods specified in the selector field don't exists, the ReplicaSet will wait for them to run before doing anything</summary><br><b>

False. It will take care of running the missing Pods.
</b></details>

<details>
<summary>In case of a ReplicaSet, Which field is mandatory in the spec section?</summary><br><b>

The field `template` in spec section is mandatory. It's used by the ReplicaSet to create new Pods when needed.
</b></details>

<details>
<summary>You've created a ReplicaSet, how to check whether the ReplicaSet found matching Pods or it created new Pods?</summary><br><b>

`kubectl describe rs <ReplicaSet Name>`

It will be visible under `Events` (the very last lines)
</b></details>

<details>
<summary>True or False? Deleting a ReplicaSet will delete the Pods it created</summary><br><b>

True (and not only the Pods but anything else it created).
</b></details>

<details>
<summary>True or False? Removing the label from a Pod that is tracked by a ReplicaSet, will cause the ReplicaSet to create a new Pod</summary><br><b>

True. When the label, used by a ReplicaSet in the selector field, removed from a Pod, that Pod no longer controlled by the ReplicaSet and the ReplicaSet will create a new Pod to compensate for the one it "lost".
</b></details>

<details>
<summary>How to scale a deployment to 8 replicas?</code></summary><br><b>

kubectl scale deploy <DEPLOYMENT_NAME> --replicas=8
</b></details>

<details>
<summary>ReplicaSets are running the moment the user executed the command to create them (like <code>kubectl create -f rs.yaml</code>)</summary><br><b>

False. It can take some time, depends on what exactly you are running. To see if they are up and running, run `kubectl get rs` and watch the 'READY' column.
</b></details>

<details>
<summary>How to expose a ReplicaSet as a new service?</summary><br><b>

`kubectl expose rs <ReplicaSet Name> --name=<Service Name> --target-port=<Port to expose> --type=NodePort`

Few notes:
  - the target port depends on which port the app is using in the container
  - type can be different and doesn't has to be specifically "NodePort"
</b></details>

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

### DaemonSet

<details>
<summary>What's a DaemonSet?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset): "A DaemonSet ensures that all (or some) Nodes run a copy of a Pod. As nodes are added to the cluster, Pods are added to them. As nodes are removed from the cluster, those Pods are garbage collected. Deleting a DaemonSet will clean up the Pods it created."
</b></details>

<details>
<summary>What's the difference between a ReplicaSet and DaemonSet?</summary><br><b>

A ReplicaSet's purpose is to maintain a stable set of replica Pods running at any given time.
A DaemonSet ensures that all Nodes run a copy of a Pod. 
</b></details>

<details>
<summary>What are some use cases for using a DaemonSet?</summary><br><b>

* Monitoring: You would like to perform monitoring on every node part of cluster. For example datadog pod runs on  every node using a daemonset
* Logging: You would like to having logging set up on every node part of your cluster
* Networking: there is networking component you need on every node for all nodes to communicate between them
</b></details>

<details>
<summary>How DaemonSet works?</summary><br><b>

Historically, up 1.12, it was done with NodeName attribute.

Starting 1.12, it's achieved with regular scheduler and node affinity.
</b></details>

#### DaemonSet - Commands

<details>
<summary>How to list all daemonsets in the current namespace?</summary><br><b>

`kubectl get ds`
</b></details>

### StatefulSet

<details>
<summary>Explain StatefulSet</summary><br><b>

StatefulSet is the workload API object used to manage stateful applications. Manages the deployment and scaling of a set of Pods, and provides guarantees about the ordering and uniqueness of these Pods.[Learn more](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
</b></details>

### Storage

#### Volumes

<details>
<summary>What is a volume in regards to Kubernetes?</summary><br><b>

A directory accessible by the containers inside a certain Pod and containers. The mechanism responsible for creating the directory, managing it, ... mainly depends on the volume type.

</b></details>

<details>
<summary>What volume types are you familiar with?</summary><br><b>

* emptyDir: created when a Pod assigned to a node and ceases to exist when the Pod is no longer running on that node
* hostPath: mounts a path from the host itself. Usually not used due to security risks but has multiple use-cases where it's needed like access to some internal host paths (`/sys`, `/var/lib`, etc.)

</b></details>

<details>
<summary>Which problems, volumes in Kubernetes solve?</summary><br><b>

1. Sharing files between containers running in the same Pod
2. Storage in containers is ephemeral - it usually doesn't last for long. For example, when a container crashes, you lose all on-disk data. Certain volumes allows to manage such situation by persistent volumes

</b></details>

<details>
<summary>Explain ephemeral volume types vs. persistent volumes in regards to Pods</summary><br><b>

Ephemeral volume types have the lifetime of a pod as opposed to persistent volumes which exist beyond the lifetime of a Pod.

</b></details>

<details>
<summary>Provide at least one use-case for each of the following volume types:

* emptyDir
* hostPath
</summary><br><b>

* EmptyDir: You need a temporary data that you can afford to lose if the Pod is deleted. For example short-lived data required for one-time operations.
* hostPath: You need access to paths on the host itself (like data from `/sys` or data generated in `/var/lib`)
</b></details>

### Networking

<details>
<summary>True or False? By default there is no communication between two Pods in two different namespaces</summary><br><b>

False. By default two Pods in two different namespaces are able to communicate with each other.

Try it for yourself:

kubectl run test-prod -n prod --image ubuntu -- sleep 2000000000
kubectl run test-dev -n dev --image ubuntu -- sleep 2000000000

`k describe po test-prod -n prod` to get the IP of test-prod Pod.

Access dev Pod: `kubectl exec --stdin --tty test-dev -n dev -- /bin/bash`

And ping the IP of test-prod Pod you get earlier.You'll see that there is communication between the two pods, in two separate namespaces.

</b></details>

### Network Policies

<details>
<summary>Explain Network Policies</summary><br><b>

[kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/network-policies): "NetworkPolicies are an application-centric construct which allow you to specify how a pod is allowed to communicate with various network "entities"..."

In simpler words, Network Policies specify how pods are allowed/disallowed to communicate with each other and/or other network endpoints.

</b></details>

<details>
<summary>What are some use cases for using Network Policies?</summary><br><b>

  - Security:  You want to prevent from everyone to communicate with a certain pod for security reasons
  - Controlling network traffic: You would like to deny network flow between two specific nodes

</b></details>

<details>
<summary>True or False? If no network policies are applied to a pod, then no connections to or from it are allowed</summary><br><b>

False. By default pods are non-isolated.
</b></details>

<details>
<summary>In case of two pods, if there is an egress policy on the source denining traffic and ingress policy on the destination that allows traffic then, traffic will be allowed or denied?</summary><br><b>

Denied. Both source and destination policies has to allow traffic for it to be allowed.
</b></details>

<details>
<summary>Where Kubernetes cluster stores the cluster state?</summary><br><b>

etcd
</b></details>

### etcd

<details>
<summary>What is etcd?</summary><br><b>

etcd is an open source distributed key-value store used to hold and manage the critical information that distributed systems need to keep running.

[Read more here](https://www.redhat.com/en/topics/containers/what-is-etcd)

</b></details>

<details>
<summary>True or False? Etcd holds the current status of any kubernetes component</summary><br><b>

True
</b></details>

<details>
<summary>True or False? The API server is the only component which communicates directly with etcd</summary><br><b>

True
</b></details>

<details>
<summary>True or False? application data is not stored in etcd</summary><br><b>

True
</b></details>

<details>
<summary>Why etcd? Why not some SQL or NoSQL database?</summary><br><b>

When chosen as the data store etcd was (and still is of course):

* Highly Available - you can deploy multiple nodes
* Fully Replicated - any node in etcd cluster is "primary" node and has full access to the data
* Consistent - reads return latest data
* Secured - supports both TLS and SSL
* Speed - high performance data store (10k writes per sec!)
</b></details>

### Namespaces

<details>
<summary>What are namespaces?</summary><br><b>

Namespaces allow you split your cluster into virtual clusters where you can group your applications in a way that makes sense and is completely separated from the other groups (so you can for example create an app with the same name in two different namespaces)
</b></details>

<details>
<summary>Why to use namespaces? What is the problem with using one default namespace?</summary><br><b>

When using the default namespace alone, it becomes hard over time to get an overview of all the applications you manage in your cluster. Namespaces make it easier to organize the applications into groups that makes sense, like a namespace of all the monitoring applications and a namespace for all the security applications, etc.

Namespaces can also be useful for managing Blue/Green environments where each namespace can include a different version of an app and also share resources that are in other namespaces (namespaces like logging, monitoring, etc.).

Another use case for namespaces is one cluster, multiple teams. When multiple teams use the same cluster, they might end up stepping on each others toes. For example if they end up creating an app with the same name it means one of the teams overridden the app of the other team because there can't be too apps in Kubernetes with the same name (in the same namespace).
</b></details>

<details>
<summary>True or False? When a namespace is deleted all resources in that namespace are not deleted but moved to another default namespace</summary><br><b>

False. When a namespace is deleted, the resources in that namespace are deleted as well.
</b></details>

<details>
<summary>What special namespaces are there by default when creating a Kubernetes cluster?</summary><br><b>

* default
* kube-system
* kube-public
* kube-node-lease
</b></details>

<details>
<summary>What can you find in kube-system namespace?</summary><br><b>

* Master and Kubectl processes
* System processes
</b></details>

<details>
<summary>While namspaces do provide scope for resources, they are not isolating them</summary><br><b>

True. Try create two pods in two separate namspaces for example, and you'll see there is a connection between the two.
</b></details>

#### Namespaces - commands

<details>
<summary>How to list all namespaces?</code></summary><br><b>

`kubectl get namespaces` OR `kubectl get ns`

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

<details>
<summary>What kube-public contains?</summary><br><b>

* A configmap, which contains cluster information
* Publicly accessible data
</b></details>

<details>
<summary>How to get the name of the current namespace?</code></summary><br><b>

`kubectl config view | grep namespace`
</b></details>

<details>
<summary>What kube-node-lease contains?</summary><br><b>

It holds information on hearbeats of nodes. Each node gets an object which holds information about its availability.
</b></details>

<details>
<summary>True or False? With namespaces you can limit the resources consumed by the users/teams</summary><br><b>

True. With namespaces you can limit CPU, RAM and storage usage.
</b></details>

<details>
<summary>How to switch to another namespace? In other words how to change active namespace?</code></summary><br><b>

`kubectl config set-context --current --namespace=some-namespace` and validate with `kubectl config view --minify | grep namespace:`

OR

`kubens some-namespace`
</b></details>

#### Resources Quota

<details>
<summary>What is Resource Quota?</code></summary><br><b>
  
Resource quota provides constraints that limit aggregate resource consumption per namespace. It can limit the quantity of objects that can be created in a namespace by type, as well as the total amount of compute resources that may be consumed by resources in that namespace.
</b></details>

<details>
<summary>How to create a Resource Quota?</code></summary><br><b>

kubectl create quota some-quota --hard-cpu=2,pods=2
</b></details>

<details>
<summary>Which resources are accessible from different namespaces?</code></summary><br><b>

Services.
</b></details>

<details>
<summary>Which service and in which namespace the following file is referencing?

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: some-configmap
data:
  some_url: samurai.jack
```
</summary><br><b>

It's referencing the service "samurai" in the namespace called "jack".
</b></details>

<details>
<summary>Which components can't be created within a namespace?</code></summary><br><b>

Volume and Node.
</b></details>

<details>
<summary>How to list all the components that bound to a namespace?</code></summary><br><b>

`kubectl api-resources --namespaced=true`
</b></details>

<details>
<summary>How to create components in a namespace?</code></summary><br><b>

One way is by specifying --namespace like this: `kubectl apply -f my_component.yaml --namespace=some-namespace`
Another way is by specifying it in the YAML itself:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: some-configmap
  namespace: some-namespace
```

and you can verify with: `kubectl get configmap -n some-namespace`
</b></details>

<details>
<summary>How to execute the command "ls" in an existing pod?</code></summary><br><b>

kubectl exec some-pod -it -- ls
</b></details>

<details>
<summary>How to create a service that exposes a deployment?</code></summary><br><b>

kubectl expose deploy some-deployment --port=80 --target-port=8080
</b></details>

<details>
<summary>How to create a pod and a service with one command?</code></summary><br><b>

kubectl run nginx --image=nginx --restart=Never --port 80 --expose
</b></details>

<details>
<summary>Describe in detail what the following command does <code>kubectl create deployment kubernetes-httpd --image=httpd</code></summary><br><b>
</b></details>

<details>
<summary>Why to create kind deployment, if pods can be launched with replicaset?</summary><br><b>
</b></details>

<details>
<summary>How to get list of resources which are not bound to a specific namespace?</code></summary><br><b>

kubectl api-resources --namespaced=false
</b></details>

<details>
<summary>How to delete all pods whose status is not "Running"?</code></summary><br><b>

kubectl delete pods --field-selector=status.phase!='Running'
</b></details>

<details>
<summary>How to display the resources usages of pods?</summary><br><b>

kubectl top pod
</b></details>

<details>
<summary>Perhaps a general question but, you suspect one of the pods is having issues, you don't know what exactly. What do you do?</summary><br><b>

Start by inspecting the pods status. we can use the command `kubectl get pods` (--all-namespaces for pods in system namespace)<br>

If we see "Error" status, we can keep debugging by running the command `kubectl describe pod [name]`. In case we still don't see anything useful we can try stern for log tailing.<br>

In case we find out there was a temporary issue with the pod or the system, we can try restarting the pod with the following `kubectl scale deployment [name] --replicas=0`<br>

Setting the replicas to 0 will shut down the process. Now start it with `kubectl scale deployment [name] --replicas=1`
</b></details>

<details>
<summary>What happens what pods are using too much memory? (more than its limit)</summary><br><b>

They become candidates to for termination.
</b></details>

<details>
<summary>Describe how roll-back works</summary><br><b>
</b></details>

<details>
<summary>True or False? Memory is a compressible resource, meaning that when a container reach the memory limit, it will keep running</summary><br><b>

False. CPU is a compressible resource while memory is a non compressible resource - once a container reached the memory limit, it will be terminated.
</b></details>

### Operators

<details>
<summary>What is an Operator?</summary><br><b>

Explained [here](https://kubernetes.io/docs/concepts/extend-kubernetes/operator)

"Operators are software extensions to Kubernetes that make use of custom resources to manage applications and their components. Operators follow Kubernetes principles, notably the control loop."

In simpler words, you can think about an operator as a custom control loop in Kubernetes.
</b></details>

<details>
<summary>Why do we need Operators?</summary><br><b>

The process of managing stateful applications in Kubernetes isn't as straightforward as managing stateless applications where reaching the desired status and upgrades are both handled the same way for every replica. In stateful applications, upgrading each replica might require different handling due to the stateful nature of the app, each replica might be in a different status. As a result, we often need a human operator to manage stateful applications. Kubernetes Operator is suppose to assist with this.

This also help with automating a standard process on multiple Kubernetes clusters
</b></details>

<details>
<summary>What components the Operator consists of?</summary><br><b>

1. CRD (Custom Resource Definition) - You are fanmiliar with Kubernetes resources like Deployment, Pod, Service, etc. CRD is also a resource, but one that you or the developer the operator defines.
2. Controller - Custom control loop which runs against the CRD

</b></details>

<details>
<summary>Explain CRD</summary><br><b>

CRD is Custom Resource Definitions. It's custom Kubernetes component which extends K8s API.

TODO(abregman): add more info.

</b></details>

<details>
<summary>How Operator works?</summary><br><b>

It uses the control loop used by Kubernetes in general. It watches for changes in the application state. The difference is that is uses a custom control loop.

In addition, it also makes use of CRD's (Custom Resources Definitions) so basically it extends Kubernetes API.

</b></details>

<details>
<summary>True or False? Kubernetes Operator used for stateful applications</summary><br><b>

True
</b></details>

<details>
<summary>Explain what is the OLM (Operator Lifecycle Manager) and what is it used for</summary><br><b>

</b></details>

<details>
<summary>What is the Operator Framework?</summary><br><b>

open source toolkit used to manage k8s native applications, called operators, in an automated and efficient way.

</b></details>

<details>
<summary>What components the Operator Framework consists of?</summary><br><b>

1. Operator SDK - allows developers to build operators
2. Operator Lifecycle Manager - helps to install, update and generally manage the lifecycle of all operators
3. Operator Metering - Enables usage reporting for operators that provide specialized services
4. 
</b></details>

<details>
<summary>Describe in detail what is the Operator Lifecycle Manager</summary><br><b>

It's part of the Operator Framework, used for managing the lifecycle of operators. It basically extends Kubernetes so a user can use a declarative way to manage operators (installation, upgrade, ...).

</b></details>

<details>
<summary>What openshift-operator-lifecycle-manager namespace includes?</summary><br><b>

It includes:

  * catalog-operator - Resolving and installing ClusterServiceVersions the resource they specify.
  * olm-operator - Deploys applications defined by ClusterServiceVersion resource

</b></details>

<details>
<summary>What is kubconfig? What do you use it for?</summary><br><b>
  
A kubeconfig file is a file used to configure access to Kubernetes when used in conjunction with the kubectl commandline tool (or other clients).
Use kubeconfig files to organize information about clusters, users, namespaces, and authentication mechanisms.
</b></details>

<details>
<summary>Would you use Helm, Go or something else for creating an Operator?</summary><br><b>
  
Depends on the scope and maturity of the Operator. If it mainly covers installation and upgrades, Helm might be enough. If you want to go for Lifecycle management, insights and auto-pilot, this is where you'd probably use Go.
</b></details>

<details>
<summary>Are there any tools, projects you are using for building Operators?</summary><br><b>

This one is based more on a personal experience and taste...

* Operator Framework
* Kubebuilder
* Controller Runtime
...
</b></details>

### Secrets

<details>
<summary>Explain Kubernetes Secrets</summary><br><b>

Secrets let you store and manage sensitive information (passwords, ssh keys, etc.)

</b></details>

<details>
<summary>How to create a Secret from a key and value?</summary><br><b>

`kubectl create secret generic some-secret --from-literal=password='donttellmypassword'`

</b></details>

<details>
<summary>How to create a Secret from a file?</summary><br><b>

`kubectl create secret generic some-secret --from-file=/some/file.txt`
</b></details>

<details>
<summary>What <code>type: Opaque</code> in a secret file means? What other types are there?</summary><br><b>

Opaque is the default type used for key-value pairs.
</b></details>

<details>
<summary>True or False? storing data in a Secret component makes it automatically secured</summary><br><b>

False. Some known security mechanisms like "encryption" aren't enabled by default.
</b></details>

<details>
<summary>What is the problem with the following Secret file:

```
apiVersion: v1   
kind: Secret
metadata:
    name: some-secret
type: Opaque
data:
    password: mySecretPassword
```
</summary><br><b>

Password isn't encrypted.
You should run something like this: `echo -n 'mySecretPassword' | base64` and paste the result to the file instead of using plain-text.

</b></details>

<details>
<summary>What the following in a Deployment configuration file means? 

```
spec:
  containers:
    - name: USER_PASSWORD
      valueFrom:
        secretKeyRef:
          name: some-secret
          key: password
```
</summary><br><b>

USER_PASSWORD environment variable will store the value from password key in the secret called "some-secret"
In other words, you reference a value from a Kubernetes Secret.

</b></details>

<details>
<summary>How to commit secrets to Git and in general how to use encrypted secrets?</summary><br><b>

One possible process would be as follows:

1. You create a Kubernetes secret (but don't commit it)
2. You encrypt it using some 3rd party project (.e.g kubeseal)
3. You apply the seald/encrypted secret
4. You commit the the sealed secret to Git
5. You deploy an application that requires the secret and it can be automatically decrypted by using for example a Bitnami Sealed secrets controller
</b></details>

### Volumes

<details>
<summary>True or False? Kubernetes provides data persistence out of the box, so when you restart a pod, data is saved</summary><br><b>

False
</b></details>

<details>
<summary>Explain "Persistent Volumes". Why do we need it?</summary><br><b>

Persistent Volumes allow us to save data so basically they provide storage that doesn't depend on the pod lifecycle.
</b></details>

<details>
<summary>True or False? Persistent Volume must be available to all nodes because the pod can restart on any of them</summary><br><b>

True
</b></details>

<details>
<summary>What types of persistent volumes are there?</summary><br><b>

* NFS
* iSCSI
* CephFS
* ...
</b></details>

<details>
<summary>What is PersistentVolumeClaim?</summary><br><b>
</b></details>

<details>
<summary>Explain Volume Snapshots</summary><br><b>
  
Volume snapshots let you create a copy of your volume at a specific point in time.
</b></details>

<details>
<summary>True or False? Kubernetes manages data persistence</summary><br><b>

False
</b></details>

<details>
<summary>Explain Storage Classes</summary><br><b>
</b></details>

<details>
<summary>Explain "Dynamic Provisioning" and "Static Provisioning"</summary><br><b>
  
The main difference relies on the moment when you want to configure storage. For instance, if you need to pre-populate data in a volume, you choose static provisioning. Whereas, if you need to create volumes on demand, you go for dynamic provisioning.
</b></details>

<details>
<summary>Explain Access Modes</summary><br><b>
</b></details>

<details>
<summary>What is CSI Volume Cloning?</summary><br><b>
</b></details>

<details>
<summary>Explain "Ephemeral Volumes"</summary><br><b>
</b></details>

<details>
<summary>What types of ephemeral volumes Kubernetes supports?</summary><br><b>
</b></details>

<details>
<summary>What is Reclaim Policy?</summary><br><b>
</b></details>

<details>
<summary>What reclaim policies are there?</summary><br><b>

* Retain
* Recycle
* Delete
</b></details>

### Access Control

<details>
<summary>What is RBAC?</summary><br><b>
 
RBAC in Kubernetes is the mechanism that enables you to configure fine-grained and specific sets of permissions that define how a given user, or group of users, can interact with any Kubernetes object in cluster, or in a specific Namespace of cluster.
</b></details>

<details>
<summary>Explain the <code>Role</code> and <code>RoleBinding"</code> objects</summary><br><b>
</b></details>

<details>
<summary>What is the difference between <code>Role</code> and <code>ClusterRole</code> objects?</summary><br><b>
  
The difference between them is that a Role is used at a namespace level whereas a ClusterRole is for the entire cluster.
</b></details>

<details>
<summary>Explain what are "Service Accounts" and in which scenario would use create/use one</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account): "A service account provides an identity for processes that run in a Pod."

An example of when to use one:
You define a pipeline that needs to build and push an image. In order to have sufficient permissions to build an push an image, that pipeline would require a service account with sufficient permissions.
</b></details>

<details>
<summary>What happens you create a pod and you DON'T specify a service account?</summary><br><b>

The pod is automatically assigned with the default service account (in the namespace where the pod is running).
</b></details>

<details>
<summary>Explain how Service Accounts are different from User Accounts</summary><br><b>

  - User accounts are global while Service accounts unique per namespace
  - User accounts are meant for humans or client processes while Service accounts are for processes which run in pods
</b></details>

<details>
<summary>How to list Service Accounts?</summary><br><b>

`kubectl get serviceaccounts`
</b></details>

<details>
<summary>Explain "Security Context"</summary><br><b>

[kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/security-context): "A security context defines privilege and access control settings for a Pod or Container."
</b></details>

### Patterns



### CronJob

<details>
<summary>Explain what is CronJob and what is it used for</summary><br><b>
  
A CronJob creates Jobs on a repeating schedule. One CronJob object is like one line of a crontab (cron table) file. It runs a job periodically on a given schedule, written in Cron format.
</b></details>

<details>
<summary>What possible issue can arise from using the following spec and how to fix it?

```
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: some-cron-job
spec:
  schedule: '*/1 * * * *'
  startingDeadlineSeconds: 10
  concurrencyPolicy: Allow
```
</summary><br><b>

If the cron job fails, the next job will not replace the previous one due to the "concurrencyPolicy" value which is "Allow". It will keep spawning new jobs and so eventually the system will be filled with failed cron jobs.
To avoid such problem, the "concurrencyPolicy" value should be either "Replace" or "Forbid".
</b></details>

<details>
<summary>What issue might arise from using the following CronJob and how to fix it?

```
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: "some-cron-job"
spec:
  schedule: '*/1 * * * *'
jobTemplate:
  spec:
    template:
      spec:
      restartPolicy: Never
      concurrencyPolicy: Forbid
      successfulJobsHistoryLimit: 1
      failedJobsHistoryLimit: 1
```
</summary><br><b>

The following lines placed under the template:

```
concurrencyPolicy: Forbid
successfulJobsHistoryLimit: 1
failedJobsHistoryLimit: 1
```

As a result this configuration isn't part of the cron job spec hence the cron job has no limits which can cause issues like OOM and potentially lead to API server being down.<br>
To fix it, these lines should placed in the spec of the cron job, above or under the "schedule" directive in the above example.
</b></details>

###  Misc

<details>
<summary>Explain Imperative Management vs. Declarative Management</summary><br><b>

</b></details>

<details>
<summary>Explain what Kubernetes Service Discovery means</summary><br><b>
</b></details>

<details>
<summary>You have one Kubernetes cluster and multiple teams that would like to use it. You would like to limit the resources each team consumes in the cluster. Which Kubernetes concept would you use for that?</summary><br><b>

Namespaces will allow to limit resources and also make sure there are no collisions between teams when working in the cluster (like creating an app with the same name).
</b></details>

<details>
<summary>What Kube Proxy does?</summary><br><b>
  Kube Proxy is a network proxy that runs on each node in your cluster, implementing part of the Kubernetes Service concept
</b></details>

<details>
<summary>What "Resources Quotas" are used for and how?</summary><br><b>
</b></details>

<details>
<summary>Explain ConfigMap</summary><br><b>

Separate configuration from pods.
It's good for cases where you might need to change configuration at some point but you don't want to restart the application or rebuild the image so you create a ConfigMap and connect it to a pod but externally to the pod.

Overall it's good for:
* Sharing the same configuration between different pods
* Storing external to the pod configuration
</b></details>

<details>
<summary>How to use ConfigMaps?</summary><br><b>

1. Create it (from key&value, a file or an env file)
2. Attach it. Mount a configmap as a volume
</b></details>

<details>
<summary>True or False? Sensitive data, like credentials, should be stored in a ConfigMap</summary><br><b>

False. Use secret.
</b></details>

<details>
<summary>Explain "Horizontal Pod Autoscaler"</summary><br><b>

In Kubernetes, a HorizontalPodAutoscaler automatically updates a workload resource with the aim of automatically scaling the workload to match demand.
</b></details>

<details>
<summary>When you delete a pod, is it deleted instantly? (a moment after running the command)</summary><br><b>
</b></details>

<details>
<summary>What does being cloud-native mean?</summary><br><b>
  The term cloud native refers to the concept of building and running applications to take advantage of the distributed computing offered by the cloud delivery model.
</b></details>

<details>
<summary>Explain the pet and cattle approach of infrastructure with respect to kubernetes</summary><br><b>
</b></details>

<details>
<summary>Describe how you one proceeds to run a containerized web app in K8s, which should be reachable from a public URL.</summary><br><b>
</b></details>

<details>
<summary>How would you troubleshoot your cluster if some applications are not reachable any more?</summary><br><b>
</b></details>

<details>
<summary>Describe what CustomResourceDefinitions there are in the Kubernetes world? What they can be used for?</summary><br><b>
</b></details>

<details>
<summary> How does scheduling work in kubernetes?</summary><br><b>

The control plane component kube-scheduler asks the following questions,
1. What to schedule? It tries to understand the pod-definition specifications
2. Which node to schedule? It tries to determine the best node with available resources to spin a pod
3. Binds the Pod to a given node

View more [here](https://www.youtube.com/watch?v=rDCWxkvPlAw)
</b></details>

<details>
<summary> How are labels and selectors used?</summary><br><b>
</b></details>

<details>
<summary>What QoS classes are there?</summary><br><b>

* Guaranteed
* Burstable
* BestEffort
</b></details>

<details>
<summary>Explain Labels. What are they and why would one use them?</summary><br><b>
  
Kubernetes labels are key-value pairs that can connect identifying metadata with Kubernetes objects.
</b></details>

<details>
<summary>Explain Selectors</summary><br><b>
</b></details>

<details>
<summary>What is Kubeconfig?</summary><br><b>
</b></details>

### Gatekeeper

<details>
<summary>What is Gatekeeper?</summary><br><b>

[Gatekeeper docs](https://open-policy-agent.github.io/gatekeeper/website/docs): "Gatekeeper is a validating (mutating TBA) webhook that enforces CRD-based policies executed by Open Policy Agent"
</b></details>

<details>
<summary>Explain how Gatekeeper works</summary><br><b>

On every request sent to the Kubernetes cluster, Gatekeeper sends the policies and the resources to OPA (Open Policy Agent) to check if it violates any policy. If it does, Gatekeeper will return the policy error message back. If it isn't violates any policy, the request will reach the cluster.
</b></details>

### Policy Testing

<details>
<summary>What is Conftest?</summary><br><b>

Conftest allows you to write tests against structured files. You can think of it as tests library for Kubernetes resources.<br>
It is mostly used in testing environments such as CI pipelines or local hooks.
</b></details>

<details>
<summary>What is Datree? How is it different from Conftest?</summary><br><b>

Same as Conftest, it is used for policy testing and enforcement. The difference is that it comes with built-in policies.
</b></details>

### Helm

<details>
<summary>What is Helm?</summary><br><b>

Package manager for Kubernetes. Basically the ability to package YAML files and distribute them to other users and apply them in the cluster(s).

As a concept it's quite common and can be found in many platforms and services. Think for example on package managers in operating systems. If you use Fedora/RHEL that would be dnf. If you use Ubuntu then, apt. If you don't use Linux, then a different question should be asked and it's why? but that's another topic :)
</b></details>

<details>
<summary>Why do we need Helm? What would be the use case for using it?</summary><br><b>

Sometimes when you would like to deploy a certain application to your cluster, you need to create multiple YAML files/components like: Secret, Service, ConfigMap, etc. This can be tedious task. So it would make sense to ease the process by introducing something that will allow us to share these bundle of YAMLs every time we would like to add an application to our cluster. This something is called Helm.

A common scenario is having multiple Kubernetes clusters (prod, dev, staging). Instead of individually applying different YAMLs in each cluster, it makes more sense to create one Chart and install it in every cluster.

Another scenario is, you would like to share what you've created with the community. For people and companies to easily deploy your application in their cluster.
</b></details>

<details>
<summary>Explain "Helm Charts"</summary><br><b>

Helm Charts is a bundle of YAML files. A bundle that you can consume from repositories or create your own and publish it to the repositories.
</b></details>

<details>
<summary>It is said that Helm is also Templating Engine. What does it mean?</summary><br><b>

It is useful for scenarios where you have multiple applications and all are similar, so there are minor differences in their configuration files and most values are the same. With Helm you can define a common blueprint for all of them and the values that are not fixed and change can be placeholders. This is called a template file and it looks similar to the following

```
apiVersion: v1
kind: Pod
metadata:
  name: {[ .Values.name ]}
spec:
  containers:
  - name: {{ .Values.container.name }}
  image: {{ .Values.container.image }}
  port: {{ .Values.container.port }}
```

The values themselves will in separate file:

```
name: some-app
container:
  name: some-app-container
  image: some-app-image
  port: 1991
```
</b></details>

<details>
<summary>What are some use cases for using Helm template file?</summary><br><b>

* Deploy the same application across multiple different environments
* CI/CD
</b></details>

<details>
<summary>Explain the Helm Chart Directory Structure</summary><br><b>

someChart/     -> the name of the chart
  Chart.yaml   -> meta information on the chart
  values.yaml  -> values for template files
  charts/      -> chart dependencies
  templates/   -> templates files :)
</b></details>

<details>
<summary>How Helm supports release management?</summary><br><b>

Helm allows you to upgrade, remove and rollback to previous versions of charts. In version 2 of Helm it was with what is known as "Tiller". In version 3, it was removed due to security concerns.
</b></details>

#### Commands

<details>
<summary>How do you search for charts?</summary><br><b>

`helm search hub [some_keyword]`
</b></details>

<details>
<summary>Is it possible to override values in values.yaml file when installing a chart?</summary><br><b>
Yes. You can pass another values file:
`helm install --values=override-values.yaml [CHART_NAME]`

Or directly on the command line: `helm install --set some_key=some_value`
</b></details>

<details>
<summary>How do you list deployed releases?</summary><br><b>

`helm ls` or `helm list`
</b></details>

<details>
<summary>How to execute a rollback?</summary><br><b>

`helm rollback RELEASE_NAME REVISION_ID`
</b></details>

<details>
<summary>How to view revision history for a certain release?</summary><br><b>

`helm history RELEASE_NAME`
</b></details>

<details>
<summary>How to upgrade a release?</summary><br><b>

`helm upgrade RELEASE_NAME CHART_NAME`
</b></details>

### Security

<details>
<summary>What security best practices do you follow in regards to the Kubernetes cluster?</summary><br><b>

  * Secure inter-service communication (one way is to use Istio to provide mutual TLS)
  * Isolate different resources into separate namespaces based on some logical groups
  * Use supported container runtime (if you use Docker then drop it because it's deprecated. You might want to CRI-O as an engine and podman for CLI)
  * Test properly changes to the cluster (e.g. consider using Datree to prevent kubernetes misconfigurations)
  * Limit who can do what (by using for example OPA gatekeeper) in the cluster
  * Use NetworkPolicy to apply network security
  * Consider using tools (e.g. Falco) for monitoring threats
</b></details>

### Troubleshooting Scenarios

<details>
<summary>Running <code>kubectl get pods</code> you see Pods in "Pending" status. What would you do?</summary><br><b>

One possible path is to run `kubectl describe pod <pod name>` to get more details.<br>
You might see one of the following:
  * Cluster is full. In this case, extend the cluster.
  * ResourcesQuota limits are met. In this case you might want to modify them
  * Check if PersistentVolumeClaim mount is pending

If none of the above helped, run the command (`get pods`) with `-o wide` to see if the node is assigned to a node. If not, there might be an issue with scheduler.
</b></details>

<details>
<summary>Users unable to reach an application running on a Pod on Kubernetes. What might be the issue and how to check?</summary><br><b>

One possible path is to start with checking the Pod status.
1. Is the Pod pending? if yes, check for the reason with `kubectl describe pod <pod name>`
TODO: finish this...
</b></details>

### Istio

<details>
<summary>What is Istio? What is it used for?</summary><br><b>
  
Istio is an open source service mesh that helps organizations run distributed, microservices-based apps anywhere. Istio enables organizations to secure, connect, and monitor microservices, so they can modernize their enterprise apps more swiftly and securely.
</b></details>

### Controllers

<details>
<summary>What are controllers?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/architecture/controller): "In Kubernetes, controllers are control loops that watch the state of your cluster, then make or request changes where needed. Each controller tries to move the current cluster state closer to the desired state."
</b></details>

<details>
<summary>Name two controllers you are familiar with</summary><br><b>

1. Node Contorller: manages the nodes of a cluster. Among other things, the controller is responsible for monitoring nodes' health - if the node is suddenly unreachable it will evacuate all the pods running on it and will mark the node status accordingly.
2. Replication Controller - monitors the status of pod replicas based on what should be running. It makes sure the number of pods that should be running is actually running
</b></details>

<details>
<summary>What process is responsible for running and installing the different controllers?</summary><br><b>

Kube-Controller-Manager
</b></details>

<details>
<summary>What is the control loop? How it works?</summary><br><b>

Explained [here](https://www.youtube.com/watch?v=i9V4oCa5f9I)
</b></details>

<details>
<summary>What are all the phases/steps of a control loop?</summary><br><b>

- Observe - identify the cluster current state
- Diff - Identify whether a diff exists between current state and desired state
- Act - Bring current cluster state to the desired state (basically reach a state where there is no diff)
</b></details>

### Scheduler

<details>
<summary>True of False? The scheduler is responsible for both deciding where a Pod will run and actually running it</summary><br><b>

False. While the scheduler is responsible for choosing the node on which the Pod will run, Kubelet is the one that actually runs the Pod.
</b></details>

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

#### Node Affinity

<details>
<summary>Using node affinity, set a Pod to schedule on a node where the key is "region" and value is either "asia" or "emea"</summary><br><b>

`vi pod.yaml`

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedlingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: region
          operator: In
          values:
          - asia
          - emea
```
</b></details>

<details>
<summary>Using node affinity, set a Pod to never schedule on a node where the key is "region" and value is "neverland"</summary><br><b>

`vi pod.yaml`

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedlingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: region
          operator: NotIn
          values:
          - neverland
```
</b></details>

<details>
<summary>True of False? Using the node affinity type "requiredDuringSchedlingIgnoredDuringExecution" means the scheduler can't schedule unless the rule is met</summary><br><b>

True
</b></details>

<details>
<summary>True of False? Using the node affinity type "preferredDuringSchedlingIgnoredDuringExecution" means the scheduler can't schedule unless the rule is met</summary><br><b>

False. The scheduler tries to find a node that meets the requirements/rules and if it doesn't it will schedule the Pod anyway.
</b></details>

<details>
<summary>Can you deploy multiple schedulers?</summary><br><b>

Yes, it is possible. You can run another pod with a command similar to:

```
spec:
  containers:
  - command:
    - kube-scheduler
    - --address=127.0.0.1
    - --leader-elect=true
    - --scheduler-name=some-custom-scheduler
...
```
</b></details>

<details>
<summary>Assuming you have multiple schedulers, how to know which scheduler was used for a given Pod?</summary><br><b>

Running `kubectl get events` you can see which scheduler was used.
</b></details>

<details>
<summary>You want to run a new Pod and you would like it to be scheduled by a custom schduler. How to achieve it?</summary><br><b>

Add the following to the spec of the Pod:

```
spec:
  schedulerName: some-custom-scheduler
```
</b></details>

### Taints

<details>
<summary>Check if there are taints on node "master"</summary><br><b>

`k describe no master | grep -i taints`
</b></details>

<details>
<summary>Create a taint on one of the nodes in your cluster with key of "app" and value of "web" and effect of "NoSchedule". Verify it was applied</summary><br><b>

`k taint node minikube app=web:NoSchedule`

`k describe no minikube | grep -i taints`
</b></details>

<details>
<summary>You applied a taint with <code>k taint node minikube app=web:NoSchedule</code> on the only node in your cluster and then executed <code>kubectl run some-pod --image=redis</code>. What will happen?</summary><br><b>

The Pod will remain in "Pending" status due to the only node in the cluster having a taint of "app=web".
</b></details>

<details>
<summary>You applied a taint with <code>k taint node minikube app=web:NoSchedule</code> on the only node in your cluster and then executed <code>kubectl run some-pod --image=redis</code> but the Pod is in pending state. How to fix it?</summary><br><b>

`kubectl edit po some-pod` and add the following

```
  - effect: NoSchedule
    key: app
    operator: Equal
    value: web
```

Exit and save. The pod should be in Running state now.
</b></details>

<details>
<summary>Remove an existing taint from one of the nodes in your cluster</summary><br><b>

`k taint node minikube app=web:NoSchedule-`
</b></details>

<details>
<summary>What taint effects are there? Explain each one of them</summary><br><b>

`NoSchedule`: prevents from resources to be scheduled on a certain node
`PreferNoSchedule`: will prefer to shcedule resources on other nodes before resorting to scheduling the resource on the chosen node (on which the taint was applied)
`NoExecute`: Appling "NoSchedule" will not evict already running Pods (or other resources) from the node as opposed to "NoExecute" which will evict any already running resource from the Node
</b></details>

### Resource Limits

<details>
<summary>Explain why one would specify resource limits in regards to Pods</summary><br><b>

* You know how much RAM and/or CPU your app should be consuming and anything above that is not valid
* You would like to make sure that everyone can run their apps in the cluster and resources are not being solely used by one type of application
</b></details>

<details>
<summary>True or False? Resource limits applied on a Pod level meaning, if limits is 2gb RAM and there are two container in a Pod that it's 1gb RAM each</summary><br><b>

False. It's per container and not per Pod.
</b></details>

#### Resources Limits - Commands

<details>
<summary>Check if there are any limits on one of the pods in your cluster</summary><br><b>

`kubectl describe po <POD_NAME> | grep -i limits`
</b></details>

<details>
<summary>Run a pod called "yay" with the image "python" and resources request of 64Mi memory and 250m CPU</summary><br><b>

`kubectl run yay --image=python --dry-run=client -o yaml > pod.yaml`

`vi pod.yaml`

```
spec:
  containers:
  - image: python
    imagePullPolicy: Always
    name: yay
    resources:
      requests:
        cpu: 250m
        memory: 64Mi
```

`kubectl apply -f pod.yaml`
</b></details>

<details>
<summary>Run a pod called "yay2" with the image "python". Make sure it has resources request of 64Mi memory and 250m CPU and the limits are 128Mi memory and 500m CPU</summary><br><b>

`kubectl run yay2 --image=python --dry-run=client -o yaml > pod.yaml`

`vi pod.yaml`

```
spec:
  containers:
  - image: python
    imagePullPolicy: Always
    name: yay2
    resources:
      limits:
        cpu: 500m
        memory: 128Mi
      requests:
        cpu: 250m
        memory: 64Mi
```

`kubectl apply -f pod.yaml`
</b></details>

### Monitoring

<details>
<summary>What monitoring solutions are you familiar with in regards to Kubernetes?</summary><br><b>

There are many types of monitoring solutions for Kubernetes. Some open-source, some are in-memory, some of them cost money, ... here is a short list:

* metrics-server: in-memory open source monitoring
* datadog: $$$
* promethues: open source monitoring solution

</b></details>

<details>
<summary>Describe how the monitoring solution you are working with monitors Kubernetes and </summary><br><b>

This very much depends on what you chose to use. Let's address some of the solutions:

* metrics-server: an open source and free monitoring solution that uses the cAdvisor component of kubelet to retrieve information on the cluster and its resources and stores them in-memory.
Once installed, after some time you can run commands like `kubectl top node` and `kubectl top pod` to view performance metrics on nodes, pods and other resources.

TODO: add more monitoring solutions

</b></details>

### Kustomize

<details>
<summary>What is Kustomize?</summary><br><b>
</b></details>

<details>
<summary>Explain the need for Kustomize by describing actual use cases</summary><br><b>

* You have an helm chart of an application used by multiple teams in your organization and there is a requirement to add annotation to the app specifying the name of the of team owning the app
  * Without Kustomize you would need to copy the files (chart template in this case) and modify it to include the specific annotations we need
  * With Kustomize you don't need to copy the entire repo or files
* You are asked to apply a change/patch to some app without modifying the original files of the app
  * With Kustomize you can define kustomization.yml file that defines these customizations so you don't need to touch the original app files
</b></details>

<details>
<summary>Describe in high-level how Kustomize works</summary><br><b>

1. You add kustomization.yml file in the folder of the app you would like to customize.
   1. You define the customizations you would like to perform
2. You run `kustomize build APP_PATH` where your kustomization.yml also resides
</b></details>

### Deployment Strategies

<details>
<summary>What rollout/deployment strategies are you familiar with?</summary><br><b>

* Blue/Green Deployments: You deploy a new version of your app, while old version still running, and you start redirecting traffic to the new version of the app
* Canary Deployments: You deploy a new version of your app and start redirecting **portion** of your users/traffic to the new version. So you the migration to the new version is much more gradual
</b></details>

<details>
<summary>Explain Blue/Green deployments/rollouts in detail</summary><br><b>

Blue/Green deployment steps:

1. Traffic coming from users through a load balancer to the application which is currently version 1

Users -> Load Balancer -> App Version 1

2. A new application version 2 is deployed (while version 1 still running)

Users -> Load Balancer -> App Version 1
                          App Version 2

3. If version 2 runs properly, traffic switched to it instead of version 1

User -> Load Balancer     App version 1
                       -> App Version 2

4. Whether old version is removed or keep running but without users being redirected to it, is based on team or company decision

Pros:
  * We can rollback/switch quickly to previous version at any point
Cons:
  * In case of an issue with new version, ALL users are affected (instead of small portion/percentage)

</b></details>

<details>
<summary>Explain Canary deployments/rollouts in detail</summary><br><b>

Canary deployment steps:

1. Traffic coming from users through a load balancer to the application which is currently version 1

Users -> Load Balancer -> App Version 1

2. A new application version 2 is deployed (while version 1 still running) and part of the traffic is redirected to the new version

Users -> Load Balancer ->(95% of the traffic) App Version 1
                       ->(5% of the traffic) App Version 2

3. If the new version (2) runs well, more traffic is redirected to it

Users -> Load Balancer ->(70% of the traffic) App Version 1
                       ->(30% of the traffic) App Version 2

3. If everything runs well, at some point all traffic is redirected to the new version

Users -> Load Balancer -> App Version 2


Pros:
  * If there is any issue with the new deployed app version, only some portion of the users affected, instead of all of them
Cons:
  * Testing of new version is neccesrialy in the production environment (as the user traffic is exists only there)

</b></details>

<details>
<summary>What ways are you familiar with to implement deployment strategies (like canary, blue/green) in Kubernetes?</summary><br><b>

There are multiple ways. One of them is Argo Rollouts.
</b></details>

### Scenarios

<details>
<summary>An engineer form your organization told you he is interested only in seeing his team resources in Kubernetes. Instead, in reality, he sees resources of the whole organization, from multiple different teams. What Kubernetes concept can you use in order to deal with it?</summary><br><b>

Namespaces. See the following [namespaces question and answer](#namespaces-use-cases) for more information.
</b></details>

<details>
<summary>An engineer in your team runs a Pod but the status he sees is "CrashLoopBackOff". What does it means? How to identify the issue?</summary><br><b>

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
</b></details>

<details>
<summary>An engineer form your organization asked whether there is a way to prevent from Pods (with cretain label) to be scheduled on one of the nodes in the cluster. Your reply is:</summary><br><b>

Yes, using taints, we could run the following command and it will prevent from all resources with label "app=web" to be scheduled on node1: `kubectl taint node node1 app=web:NoSchedule`
</b></details>

<details>
<summary>You would like to limit the number of resources being used in your cluster. For example no more than 4 replicasets, 2 services, etc. How would you achieve that?</summary><br><b>

Using ResourceQuats
</b></details>

<!-- {% endraw %} -->