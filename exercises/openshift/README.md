## OpenShift

### OpenShift Exercises

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Projects 101 | Projects | [Exercise](projects_101.md) | [Solution](solutions/projects_101.md)
| My First Application | Applications | [Exercise](my_first_app.md) | [Solution](solutions/my_first_app.md)

### OpenShift Self Assessment

* [OpenShift 101](#Openshift-101)
* [OpenShift Architecture](#Openshift-architecture)
* [OpenShift Hands-On Basics](#Openshift-hands-on-basics)
* [OpenShift Projects](#Openshift-projects)

<a name="openshift-101"></a>
### OpenShift 101

<details>
<summary>What is OpenShift?</summary><br><b>

OpenShift is a container orchestration platform based on Kubernetes.<br>
It can be used for deploying applications while having minimal management overhead.
</b></details>

<details>
<summary>How OpenShift is related to Kubernetes?</summary><br><b>

OpenShift is build on top of Kubernetes while defining its own custom resources in addition to the built-in resources.
</b></details>

<details>
<summary>True or False? OpenShift is a IaaS (infrastructure as a service) solution</summary><br><b>

False. OpenShift is a PaaS (platform as a service) solution.
</b></details>

<details>
<summary>True or False? OpenShift CLI supports everything kubectl supports, along with additional functionality</summary><br><b>

True
</b></details>

<details>
<summary>What are some of OpenShift added features on top of Kubernetes?</summary><br><b>

- UI: OpenShift provides unified UI out-of-the-box
- Routes: Simple procedure for exposing services
- Developer Workflow Support: built-in CI/CD (openshift pipelines), built-in container registry and tooling for building artifacts from source to container images
</b></details>

<details>
<summary>True or False? To run containers on OpenShift, you have to own root privileges</summary><br><b>

False. OpenShift supports rootless containers by default.
</b></details>

<a name="openshift-architecture"></a>
## OpenShift - Architecture

<details>
<summary>What types of nodes OpenShift has?</summary><br><b>

- Workers: Where the end-user applications are running
- Masters: Responsible for managing the cluster
</b></details>

<details>
<summary>Which component responsible for determining pod placement?</summary><br><b>

The Scheduler.
</b></details>

<details>
<summary>What else the scheduler responsible for except pod placement?</summary><br><b>

Application high availability by spreading pod replicas between worker nodes
</b></details>

<a name="openshift-hands-on-basics"></a>
## OpenShift - Hands-On Basics

<details>
<summary>OpenShift supports many resources. How to get a list of all these resources?</summary><br><b>

`oc api-resources`
</b></details>

<details>
<summary>Explain OpenShift CLIs like <code>oc</code> and <code>odo</code></summary><br><b>

oc is used for creating applications, but also for administrating OpenShift cluster<br>
odo is used solely for managing applications on OpenShift (mainly from developers' perspective) and has nothing to do with administrating the cluster
</b></details>

<a name="openshift-projects"></a>
## OpenShift - Projects

<details>
<summary>What is a project in OpenShift?</summary><br><b>

A project in OpenShift is a Kubernetes namespace with annotations.<br>
In simpler words, think about it as an isolated environment for users to manage and organize their resources (like Pods, Deployments, Service, etc.).
</b></details>

<details>
<summary>How to list all projects? What the "STATUS" column means in projects list output?</summary><br><b>

`oc get projects` will list all projects. The "STATUS" column can be used to see which projects are currently active.
</b></details>

<details>
<summary>You have a new team member and you would like to assign to him the "admin" role on your project in OpenShift. How to achieve that?</summary><br><b>

`oc adm policy add-role-to-user <role> <user> -n <project>`
</b></details>

#### OpenShift - Applications

<details>
<summary>How to create a MySQL application using an image from Docker Hub?</summary><br><b>

`oc new-app mysql`
</b></details>

#### OpenShift - Images

<details>
<summary>What is an image stream?</summary><br><b>
</b></details>

<details>
<summary>What would be the best way to run and manage multiple OpenShift environments?</summary><br><b>

Federation
</b></details>

#### OpenShift - Federation

<details>
<summary>What is OpenShift Federation?</summary><br><b>

Management and deployment of services and workloads accross multiple independent clusters from a single API
</b></details>

<details>
<summary>Explain the following in regards to Federation:

  * Multi Cluster
  * Federated Cluster
  * Host Cluster
  * Member Cluster
</summary><br><b>

  * Multi Cluster - Multiple clusters deployed independently, not being aware of each other
  * Federated Cluster - Multiple clusters managed by the OpenShift Federation Control Plane
  * Host Cluster - The cluster that runs the Federation Control Plane
  * Member Cluster - Cluster that is part of the Federated Cluster and connected to Federation Control Plane
</b></details>

## OpenShift - Storage

<details>
<summary>What is a storage device? What storage devices are there?</summary><br><b>

* Hard Disks
* SSD
* USB
* Magnetic Tape
</b></details>

<details>
<summary>What is Random Seek Time?</summary><br><b>

The time it takes for a disk to reach the place where the data is located and read a single block/sector.

Bones question: What is the random seek time in SSD and Magnetic Disk?
Answer: Magnetic is about 10ms and SSD is somewhere between 0.08 and 0.16ms
</b></details>

#### OpenShift - Pods

<details>
<summary>What happens when a pod fails or exit due to container crash</summary><br><b>

Master node automatically restarts the pod unless it fails too often.
</b></details>

<details>
<summary>What happens when a pod fails too often?</summary><br><b>

It's marked as bad by the master node and temporarly not restarted anymore.
</b></details>

<details>
<summary>How to find out on which node a certain pod is running?</summary><br><b>

`oc get po -o wide`
</b></details>

#### OpenShift - Services

<details>
<summary>Explain Services and their benefits</summary><br><b>

  - Services in OpenShift define access policy to one or more set of pods.<br>
  - They are connecting applications together by enabling communication between them
  - They provide permanent internal IP addresses and hostnames for applications
  - They are able to provide basic internal load balancing
</b></details>

#### OpenShift - Labels

<details>
<summary>Explain labels. What are they? When do you use them?</summary><br><b>

  - Labels are used to group or select API objects
  - They are simple key-value pairs and can be included in metadata of some objects
  - A common use case: group pods, services, deployments, ... all related to a certain application
</b></details>

#### OpenShift - Service Accounts

<details>
<summary>How to list Service Accounts?</summary><br><b>

`oc get serviceaccounts`
</b></details>

#### OpenShift - Networking

<details>
<summary>What is a Route?</summary><br><b>

A route is exposing a service by giving it hostname which is externally reachable
</b></details>

<details>
<summary>What Route is consists of?</summary><br><b>

  - name
  - service selector
  - (optional) security configuration
</b></details>

<details>
<summary>True or False? Router container can run only on the Master node</summary><br><b>

False. It can run on any node.
</b></details>

<details>
<summary>Given an example of how a router is used</summary><br><b>

1. Client is using an address of application running on OpenShift
2. DNS resolves to host running the router
3. Router checks whether route exists
4. Router proxies the request to the internal pod 
</b></details>

#### OpenShift - Security

<details>
<summary>What are "Security Context Constraints"?</summary><br><b>

From [OpenShift Docs](https://docs.openshift.com/container-platform/4.7/authentication/managing-security-context-constraints.html): "Similar to the way that RBAC resources control user access, administrators can use security context constraints (SCCs) to control permissions for pods".
</b></details>

<details>
<summary>How to add the ability for the user `user1` to view the project `wonderland` assuming you are authorized to do so</summary><br><b>

oc adm policy add-role-to-user view user1 -n wonderland
</b></details>

<details>
<summary>How to check what is the current context?</summary><br><b>

`oc whoami --show-context`
</b></details>

#### OpenShift - Serverless

<details>
<summary>What is OpenShift Serverless?</summary><br><b>

  - In general 'serverless' is a cloud computing model where scaling and provisioning is taken care for application developers, so they can focus on the development aspect rather infrastructure related tasks
  - OpenShift Serverless allows you to dynamically scale your applications and provides the ability to build event-driven applications, whether the sources are on Kubernetes, the cloud or on-premise solutions
  - OpenShift Serverless is based on the Knative project.
</b></details>

<details>
<summary>What are some of the event sources you can use with OpenShift Serverless?</summary><br><b>

  * Kafka
  * Kubernetes APIs
  * AWS Kinesis
  * AWS SQS
  * JIRA
  * Slack

More are supported and provided with OpenShift.
</b></details>

<details>
<summary>Explain serverless functions</summary><br><b>
</b></details>

<details>
<summary>What is the difference between Serverless Containers and Serverless functions?</summary><br><b>
</b></details>

#### OpenShift - Misc

<details>
<summary>What is Replication Controller?</summary><br><b>

Replication Controller responsible for ensuring the specified number of pods is running at all times.<br>
If more pods are running than needed -> it deletes some of them<br>
If not enough pods are running -> it creates more
</b></details>
