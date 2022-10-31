# Google Cloud Platform

- [Google Cloud Platform](#google-cloud-platform)
  - [Exercises](#exercises)
    - [Account Setup](#account-setup)
    - [Compute Engine](#compute-engine)
  - [Questions](#questions)
    - [Global Infrastructure](#global-infrastructure)
      - [gcloud](#gcloud)
    - [Resource Hierarchy](#resource-hierarchy)
    - [IAM and Roles](#iam-and-roles)
    - [Labels and Tags](#labels-and-tags)
      - [gcloud](#gcloud-1)
    - [Compute Engine](#compute-engine-1)
      - [gcloud](#gcloud-2)
    - [Other](#other)
    - [Google Kubernetes Engine (GKE)](#google-kubernetes-engine-gke)
    - [Anthos](#anthos)
  
## Exercises

### Account Setup

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Create a project | Organization | [Exercise](exercises/create_project/exercise.md) | [Solution](exercises/create_project/solution.md) | |
| Assign roles | IAM | [Exercise](exercises/assign_roles/exercise.md) | [Solution](exercises/assign_roles/solution.md) | |


### Compute Engine

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Create an instance | Compute, Labels | [Exercise](exercises/instance_101/exercise.md) | [Solution](exercises/instance_101/solution.md) | |


## Questions

### Global Infrastructure

<details>
<summary>Explain each of the following

  * Zone
  * Region
</summary><br><b>

GCP regions are data centers hosted across different geographical locations worldwide.<br>

Within each region, there are multiple isolated locations known as Zones. Each zone is one or more data-centers with redundant network and connectivity and power supply. Multiple zones ensure high availability in case one of them goes down

</b></details>

<details>
<summary>True or False? Each GCP region is designed to be completely isolated from the other GCP regions </summary><br><b>

True.
</b></details>

<details>
<summary>What considerations to take when choosing an GCP region for running a new application?</summary><br><b>

* Services Availability: not all service (and all their features) are available in every region
* Reduced latency: deploy application in a region that is close to customers
* Compliance: some countries have more strict rules and requirements such as making sure the data stays within the borders of the country or the region. In that case, only specific region can be used for running the application
* Pricing: the pricing might not be consistent across regions so, the price for the same service in different regions might be different.
</b></details>

<details>
<summary>True or False? All GCP services are available in all regions zones</summary><br><b>

False. You can see [here](https://cloud.google.com/about/locations) which products/services available in each region.
</b></details>

#### gcloud

<details>
<summary>How to list all regions?</summary><br><b>

`gcloud compute regions list`
</b></details>

### Resource Hierarchy

<details>
<summary>Explain resources hierarchy in GCP</summary><br><b>

Organization
  Folder
    Project
      Resoruces

* Organizations - Company
* Folder - usually for departments, teams, products, etc.
* Project - can be different projects or same project but different environments (dev, staging, production)
* Resources - actual GCP services (Compute, App engine, Storage, etc.)

</b></details>

<details>
<summary>True or False? In a project, you can have one or more organizations</summary><br><b>

False. It's quite the opposite. First there is an organization and under organization you can have one or more folder with one or more projects.
</b></details>

<details>
<summary>True or False? A resource has to be associated with at least one project</summary><br><b>

True. You can't have resources associate with no projects.
</b></details>

<details>
<summary>True or False? Project name has to be globally unique</summary><br><b>

True.
</b></details>

### IAM and Roles

<details>
<summary>Explain roles and permissions</summary><br><b>

Role is an encapsulation of set of permissions. For example an "owner" role has more than 3000 assigned permissions to the different components and services of GCP.
</b></details>

<details>
<summary>True or False? Permissive parent policy will always overrule restrictive child policy</summary><br><b>

True
</b></details>

### Labels and Tags

<details>
<summary>What are labels?</summary><br><b>

You can think about labels in GCP as sticky notes that you attach to different GCP resources. That makes it easier for example, to search for specific resources (like applying the label called "web-app" and search for all the resources that are related somehow to "web-app")
</b></details>

<details>
<summary>Can you provide some examples to labels usage in GCP?</summary><br><b>

* Location (cost center)
* Project (or environment, folder, etc.)
* Service type
* Service owner
* Application type
* Application owner
</b></details>

<details>
<summary>What are network tags and how are they different from labels? </summary><br><b>

As the name suggests, network tags can be applied only to network resources.
While labels don't affect the resources on which they are applied, network tags do affect resources (e.g. firewall access and networking routes)
</b></details>

#### gcloud

<details>
<summary>List the labels of an instance called "instance-1"</summary><br><b>

`gcloud compute instances describe instance-1 --format "yaml(labels)"`
</b></details>

<details>
<summary>Update a label to "app=db" for the instance called "instance-1"</summary><br><b>

`gcloud compute instances update instance-1 --update-labels app=db`
</b></details>

<details>
<summary>Remove the label "env" from an instance called "instance-1"</summary><br><b>

`gcloud compute instances update instance-1 --remove-labels env`
</b></details>

### Compute Engine

#### gcloud

<details>
<summary>Create an instance with the following properties:

* name: instance-1
* machine type: e2-micro
* labels: app=web, env=dev
</summary><br><b>

`gcloud compute instances create instance-1 --labels app=web,env=dev --machine-type=e2-micro`
</b></details>

### Other

<details>
<summary>Tell me what do you know about GCP networking</summary><br><b>

Virtual Private Cloud(VPC) network is a virtual version of physical network, implemented in Google's internal Network. VPC is a gloabal resource in GCP.
Subnetworks(subnets) are regional resources, ie., subnets can be created withinin regions.

VPC are created in 2 modes,

1. Auto mode VPC - One subnet in each region is created automatically by GCP while creating VPC

2. Custom mode VPC - No subnets are automatically created. This type of network provides complete control over the subnets creation to the users. 
</b></details>

<details>
<summary>Explain Cloud Functions</summary><br><b>

Google Cloud Functions is a serverless execution environment for building and connecting cloud services. With Cloud Functions you write simple, single-purpose functions that are attached to events emitted from your cloud infrastructure and services. Your function is triggered when an event being watched is fired.

</b></details>

<details>
<summary>What is Cloud Datastore?</summary><br><b>

Cloud Datastore is a schemaless NoSQL datastore in Google's cloud. Applications can use Datastore to query your data with SQL-like queries that support filtering and sorting. Datastore replicates data across multiple datacenters, which provides a high level of read/write availability.

</b></details>

<details>
<summary>What network tags are used for?</summary><br><b>

Network tags allow you to apply firewall rules and routes to a specific instance or set of instances: You make a firewall rule applicable to specific instances by using target tags and source tags.

</b></details>

<details>
<summary>What are flow logs? Where are they enabled?</summary><br><b>

VPC Flow Logs records a sample of network flows sent from and received by VM instances, including instances used as Google Kubernetes Engine nodes. These logs can be used for network monitoring, forensics, real-time security analysis, and expense optimization.

Enable Flow Logs

1. Open VPC Network in GCP Console

2. Click the name of the subnet 

3. Click EDIT button

4. Set Flow Logs to On

5. Click Save



</b></details>

<details>
<summary>How do you list buckets?</summary><br><b>
    Two ways to do that:
	 
   $ gsutil ls
	 
   $ gcloud alpha storage ls
	
</b></details>
 
<details>
<summary>What Compute metadata key allows you to run code at startup?</summary><br><b>

startap-script
</b></details>

<details>
<summary>What the following commands does? `gcloud deployment-manager deployments create`</summary><br><b>

Deployment Manager creates a new deployment. 

</b></details>

<details>
<summary>What is Cloud Code?</summary><br><b>
It is a set of tools to help developers write, run and debug GCP kubernetes based applications. It provides built-in support for rapid iteration, debugging and running applications in development and production K8s environments.
</b></details>

### Google Kubernetes Engine (GKE)

<details>
<summary>What is GKE</summary><br><b>

* It is the managed kubernetes service on GCP for deploying, managing and scaling containerised applications using Google infrastructure.
</b></details>

### Anthos

<details>
<summary>What is Anthos</summary><br><b>
It is a managed application platform for organisations like enterprises that require quick modernisation and certain levels
of consistency for their legacy applications in a hybrid or multicloud world. From this explanation the core ideas can be drawn from these statements;

* Managed -> the customer does not need to worry about the underlying software intergrations, they just enable the API.
* application platform -> It consists of open source tools like K8s, Knative, Istio and Tekton
* Enterprises -> these are usually organisations with complex needs
* Consistency -> to have the same policies declaratively initiated to be run anywhere securely e.g on-prem, GCP or other-clouds (AWS or Azure)

fun fact: Anthos is flower in greek, they grow in the ground (earth) but need rain from the clouds to flourish.
</b></details>

<details>
<summary>List the technical components that make up Anthos</summary><br><b>

* Infrastructure management - Google Kubernetes Engine (GKE)
* Cluster management - GKE, Ingress for Anthos
* Service management - Anthos Service Mesh
* Policy enforcement - Anthos Config Management, Anthos Enterprise Data Protection, Policy Controller
* Application deployment - CI/CD tools like Cloud Build, GitLab
* Application development - Cloud Code
</b></details>

<details>
<summary>What is the primary computing environment for Anthos to easily manage workload deployment?</summary><br><b>

* Google Kubernetes Engine (GKE)
</b></details>

<details>
<summary>How does Anthos handle the control plane and node components for GKE?</summary><br><b>

On GCP the kubernetes api-server is the only control plane component exposed to customers whilst compute engine manages
instances in the project.
</b></details>

<details>
<summary>Which load balancing options are available?</summary><br><b>

* Networking load balancing for L4 and HTTP(S) Load Balancing for L7 which are both managed services that do not require
  additional configuration.
* Ingress for Anthos which allows the ability to deploy a load balancer that serves an application across multiple clusters
  on GKE
</b></details>

<details>
<summary>Can you deploy Anthos on AWS?</summary><br><b>

* Yes, Anthos on AWS is now GA. For more read [here](https://cloud.google.com/anthos/gke/docs/aws)
</b></details>

<details>
<summary>List and explain the enterprise security capabilities provided by Anthos</summary><br><b>

* Control plane security - GCP manages and maintains the K8s control plane out of the box. The user can secure the api-server by using master authorized networks and private clusters. These allow the user to disable access on the public IP address by assigning a private IP address to the master.
* Node security - By default workloads are provisioned on Compute engine instances that use Google's Container Optimised OS. This operating system implements a locked-down firewall, limited user accounts with root disabled and a read-only filesystem. There is a further option to enable GKE Sandbox for stronger isolation in multi-tenant deployment scenarios.
* Network security - Within a created cluster VPC, Anthos GKE leverages a powerful software-defined network that enables simple Pod-to-Pod communications. Network policies allow locking down ingress and egress connections in a given namespace. Filtering can also be implemented to incoming load-balanced traffic for services that require external access, by supplying whitelisted CIDR IP ranges.
* Workload security - Running workloads run with limited privileges, default Docker AppArmor security policies are applied to all Kubernetes Pods. Workload identity for Anthos GKE aligns with the open source kubernetes service accounts with GCP service account permissions.
* Audit logging - Adminstrators are given a way to retain, query, process and alert on events of the deployed environments.
</b></details>

<details>
<summary>How can workloads deployed on Anthos GKE on-prem clusters securely connect to Google Cloud services?</summary><br><b>

* Google Cloud Virtual Private Network (Cloud VPN) - this is for secure networking
* Google Cloud Key Management Service (Cloud KMS) - for key management
</b></details>

<details>
<summary>What is Island Mode configuration with regards to networking in Anthos GKE deployed on-prem?</summary><br><b>

* This is when pods can directly talk to each other within a cluster, but cannot be reached from outside the cluster thus forming an "island" within the network that is not connected to the external network.
</b></details>

<details>
<summary>Explain Anthos Config Management</summary><br><b>

It is a core component of the Anthos stack which provides platform, service and security operators with a single, unified approach to multi-cluster management that spans both on-premises and cloud environments. It closely follows K8s best practices, favoring declarative approaches over imperative operations, and actively monitors cluster state and applies the desired state as defined in Git. It includes three key components as follows:

1. An importer that reads from a central Git repository
2. A component that synchronises stored configuration data into K8s objects
3. A component that monitors drift between desired and actual cluster configurations with a capability of reconciliation when need rises.
</b></details>

<details>
<summary>How does Anthos Config Management help?</summary><br><b>

It follows common modern software development practices which makes cluster configuration, management and policy changes auditable, revertable, and versionable easily enforcing IT governance and unifying resource management in an organisation.
</b></details>

<details>
<summary>What is Anthos Service Mesh?</summary><br><b>

* It is a suite of tools that assist in monitoring and managing deployed services on Anthos of all shapes and sizes whether running in cloud, hybrid or multi-cloud environments. It leverages the APIs and core components from Istio, a highly configurable and open-source service mesh platform.
</b></details>

<details>
<summary>Describe the two main components of Anthos Service Mesh</summary><br><b>

1. Data plane - it consists of a set of distributed proxies that mediate all inbound and outbound network traffic between individual services which are configured using a centralised control plane and an open API
2. Control plane - is a fully managed offering outside of Anthos GKE clusters to simplify management overhead and ensure highest possible availability.
</b></details>

<details>
<summary>What are the components of the managed control plane of Anthos Service Mesh?</summary><br><b>

1. Traffic Director - it is GCP's fully managed service mesh traffic control plane, responsible for translating Istio API objects into configuration information for the distributed proxies, as well as directing service mesh ingress and egress traffic
2. Managed CA - is a centralised certificate authority responsible for providing SSL certificates to each of the distributed proxies, authentication information and distributing secrets
3. Operations tooling - formerly stackdriver, provides a managed ingestion point for observability and telemetry, specifically monitoring, tracing and logging data generated by each of the proxies. This powers the observability dashboard for operators to visually inspect their services and service dependencies assisting in the implementation of SRE best practices for monitoring SLIs and establishing SLOs.
</b></details>

<details>
<summary>How does Anthos Service Mesh help?</summary><br><b>
Tool and technology integration that makes up Anthos service mesh delivers signficant operational benefits to Anthos environments, with minimal additional overhead such as follows:

* Uniform observability - the data plane reports service to service communication back to the control plane generating a service dependency graph. Traffic inspection by the proxy inserts headers to facilitate distributed tracing, capturing and reporting service logs together with service-level metrics (i.e latency, errors, availability).
* Operational agility - fine-grained controls for managing the flow of inter-mesh (north-south) and intra-mesh (east-west) traffic are provided.
* Policy-driven security - policies can be enforced consistently across diverse protocols and runtimes as service communications are secured by default.
</b></details>

<details>
<summary>List possible use cases of traffic controls that can be implemented within Anthos Service Mesh</summary><br><b>

* Traffic splitting across differing service versions for canary or A/B testing
* Circuit breaking to prevent cascading failures
* Fault injection to help build resilient and fault-tolerant deployments
* HTTP header-based traffic steering between individual services or versions
</b></details>

<details>
<summary>What is Cloud Run for Anthos?</summary><br><b>

It is part of the Anthos stack that brings a serverless container experience to Anthos, offering a high-level platform experience on top of K8s clusters. It is built with Knative, an open-source operator for K8s that brings serverless application serving and eventing capabilities.
</b></details>

<details>
<summary>How does Cloud Run for Anthos simplify operations?</summary><br><b>

Platform teams in organisations that wish to offer developers additional tools to test, deploy and run applications can use Knative to enhance this experience on Anthos as Cloud Run. Below are some of the benefits;

* Easy migration from K8s deployments - Without Cloud Run, platform engineers have to configure deployment, service, and HorizontalPodAutoscalers(HPA) objects to a loadbalancer and autoscaling. If application is already serving traffic it becomes hard to change configurations or roll back efficiently. Using Cloud Run all this is managed thus the Knative service manifest describes the application to be autoscaled and loadbalanced
* Autoscaling - a sudden traffic spike may cause application containers in K8s to crash due to overload thus an efficient automated autoscaling is executed to serve the high volume of traffic
* Networking - it has built-in load balancing capabilities and policies for traffic splitting between multiple versions of an application.
* Releases and rollouts - supports the notion of the Knatibe API's revisions which describe new versions or different configurations of your application and canary deployments by splitting traffic.
* Monitoring - observing and recording metrics such as latency, error rate and requests per second.
</b></details>

<details>
<summary>List and explain three high-level out of the box autoscaling primitives offered by Cloud Run for Anthos that do not exist in K8s natively</summary><br><b>

* Rapid, request-based autoscaling - default autoscalers monitor request metrics which allows Cloud Run for Anthos to handle spiky traffic patterns smoothly
* Concurrency controls - limits such as max in-flight requests per container are enforced to ensure the container does not become overloaded and crash. More containers are added to handle the spiky traffic, buffering the requests.
* Scale to zero - if an application is inactive for a while Cloud Run scales it down to zero to reduce its footprint. Alternatively one can turn off scale-to-zero to prevent cold starts.
</b></details>

<details>
<summary>List some Cloud Run for Anthos use cases</summary><br><b>

As it does not support stateful applications or sticky sessions, it is suitable for running stateless applications such as:

* Machine learning model predictions e.g Tensorflow serving containers
* API gateways, API middleware, web front ends and Microservices
* Event handlers, ETL
</b></details>