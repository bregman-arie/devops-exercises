## Cloud

<details>
<summary>What is Cloud Computing? What is a Cloud Provider?</summary><br><b>

Cloud computing refers to the delivery of on-demand computing services 
over the internet on a pay-as-you-go basis.

In simple words, Cloud computing is a service that lets you use any computing
service such as a server, storage, networking, databases, and intelligence, 
right through your browser without owning anything. You can do anything you 
can think of unless it doesn’t require you to stay close to your hardware.

Cloud service providers are companies that establish public clouds, manage private clouds, or offer on-demand cloud computing components (also known as cloud computing services) like Infrastructure-as-a-Service (IaaS), Platform-as-a-Service (PaaS), and Software-as-a-Service(SaaS). Cloud services can reduce business process costs when compared to on-premise IT.
</b></details>

<details>
<summary>What are the advantages of cloud computing? Mention at least 3 advantages</summary><br><b>

* Pay as you go: you are paying only for what you are using. No upfront payments and payment stops when resources are no longer used.
* Scalable: resources are scaled down or up based on demand
* High availability: resources and applications provide seamless experience, even when some services are down
* Disaster recovery 
</b></details>

<details>
<summary>True or False? Cloud computing is a consumption-based model (users only pay for for resources they use)</summary><br><b>

True
</b></details>

<details>
<summary>What types of Cloud Computing services are there?</summary><br><b>

IAAS - Infrastructure as a Service
PAAS - Platform as a Service
SAAS - Software as a Service
</b></details>

<details>
<summary>Explain each of the following and give an example:

  * IAAS
  * PAAS
  * SAAS</summary><br><b>
  * IAAS - Users have control over complete Operating System and don't need to worry about the physical resources, which is managed by Cloud Service Provider.
  * PAAS - CLoud Service Provider takes care of Operating System, Middlewares and users only need to focus on our Data and Application.
  * SAAS - A cloud based method to provide software to users, software logics running on cloud, can be run on-premises or managed by Cloud Service Provider.
</b></details>

<details>
<summary>What types of clouds (or cloud deployments) are there?</summary><br><b>

  * Public - Cloud services sharing computing resources among multiple customers
  * Private - Cloud services having computing resources limited to specific customer or organization, managed by third party or organizations itself
  * Hybrid - Combination of public and private clouds
</b></details>

<details>
<summary>What are the differences between Cloud Providers and On-Premise solution?</summary><br><b>

In cloud providers, someone else owns and manages the hardware, hire the relevant infrastructure teams and pays for real-estate (for both hardware and people). You can focus on your business.

In On-Premise solution, it's quite the opposite. You need to take care of hardware, infrastructure teams and pay for everything which can be quite expensive. On the other hand it's tailored to your needs.
</b></details>

<details>
<summary>What is Serverless Computing?</summary><br><b>

The main idea behind serverless computing is that you don't need to manage the creation and configuration of server. All you need to focus on is splitting your app into multiple functions which will be triggered by some actions.

It's important to note that:

* Serverless Computing is still using servers. So saying there are no servers in serverless computing is completely wrong
* Serverless Computing allows you to have a different paying model. You basically pay only when your functions are running and not when the VM or containers are running as in other payment models
</b></details>

<details>
<summary>Can we replace any type of computing on servers with serverless?</summary><br><b>
</b></details>

<details>
<summary>Is there a difference between managed service to SaaS or is it the same thing?</summary><br><b>
</b></details>

<details>
<summary>What is auto scaling?</summary><br><b>

AWS definition: "AWS Auto Scaling monitors your applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost"

Read more about auto scaling [here](https://aws.amazon.com/autoscaling)
</b></details>

<details>
<summary>True or False? Auto Scaling is about adding resources (such as instances) and not about removing resource</summary><br><b>

False. Auto scaling adjusts capacity and this can mean removing some resources based on usage and performances.
</b></details>

#### Cloud - Security

<details>
<summary>How to secure instances in the cloud?</summary><br><b>

  * Instance should have minimal permissions needed. You don't want an instance-level incident to become an account-level incident
  * Instances should be accessed through load balancers or bastion hosts. In other words, they should be off the internet (in a private subnet behind a NAT). 
  * Using latest OS images with your instances (or at least apply latest patches)
</b></details>
