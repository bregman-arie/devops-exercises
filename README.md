# DevOps Interview Questions

:information_source: &nbsp;This repository contains questions on various DevOps and SRE related topics

:bar_chart: &nbsp;There are currently **611** questions

:books: &nbsp;To learn more about DevOps check the resources in [DevOpsBit.com](https://devopsbit.com)

:warning: &nbsp;The purpose of this repo is to help you test your knowledge and prepare for interviews. It doesn't represents a DevOps interview. Please read [Q&A](common-qa.md) for more details

:thought_balloon: &nbsp;If you wonder how to prepare to your DevOps Interview, we added a couple of suggestions [here](prepare_for_interview.md)

:pencil: &nbsp;You can add more questions & answers by submitting pull requests :) You can read more about it [here](CONTRIBUTING.md)

:cn: &nbsp;You can find a [中文](README-zh_CN.md) Chinese translation right [here](README-zh_CN.md)

****

<!-- ALL-TOPICS-LIST:START -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<center>
<table>
  <tr>
    <td align="center"><a href="#devops"><img src="images/devops.png" width="70px;" height="75px;" alt="DevOps" /><br /><b>DevOps</b></a><br /><sub><a href="#devops-beginner">Beginner :baby:</a></sub><br><sub><a href="#devops-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#jenkins"><img src="images/jenkins.png" width="80px;" height="85px;" alt="Jenkins"/><br /><b>Jenkins</b></a><br /><sub><a href="#jenkins-beginner">Beginner :baby:</a></sub><br><sub><a href="#jenkins-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#git"><img src="images/git.png" width="110px;" height="75px;" alt="Git"/><br /><b>Git</b></a><br /><sub><a href="#git-beginner">Beginner :baby:</a></sub><br><sub><a href="#git-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#ansible"><img src="images/ansible.png" width="65px;" height="75px;" alt="Ansible"/><br /><b>Ansible</b></a><br /><sub><a href="#ansible-beginner">Beginner :baby:</a></sub><br><sub><a href="#ansible-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#Network"><img src="images/network.png" width="80x;" height="75px;" alt="Network"/><br /><b>Network</b></a><br /><sub><a href="#network-beginner">Beginner :baby:</a></sub><br><sub><a href="#network-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#linux"><img src="images/linux.png" width="75x;" height="75px;" alt="Linux"/><br /><b>Linux</b></a><br /><sub><a href="#linux-beginner">Beginner :baby:</a></sub><br><sub><a href="#linux-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#terraform"><img src="images/terraform.png" width="75px;" height="75px;" alt="Terraform"/><br /><b>Terraform</b></a><br /><sub><a href="#terraform-beginner">Beginner :baby:</a></sub><br><sub><a href="#terraform-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#docker"><img src="images/docker.png" width="75px;" height="75px;" alt="Docker"/><br /><b>Docker</b></a><br /><sub><a href="#docker-beginner">Beginner :baby:</a></sub><br><sub><a href="#docker-advanced">Advanced :star:</a></sub></td>
  </tr>
  <tr>
    <td align="center"><a href="#coding"><img src="images/coding.png" width="75px;" height="75px;" alt="coding"/><br /><b>Coding</b></a><br /><sub><a href="#coding-beginner">Beginner :baby:</a></sub><br><sub><a href="#coding-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#python"><img src="images/python.png" width="80px;" height="75px;" alt="Python"/><br /><b>Python</b></a><br /><sub><a href="#python-beginner">Beginner :baby:</a></sub><br><sub><a href="#python-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#go"><b>Go</b></a><br /><sub><a href="#go-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#shell-scripting"><img src="images/bash.png" width="70px;" height="75px;" alt="Bash"/><br /><b>Shell Scripting</b></a><br /><sub><a href="#shell-scripting-beginner">Beginner :baby:</a></sub><br><sub><a href="#shell-scripting-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#kubernetes"><img src="images/kubernetes.png" width="75px;" height="75px;" alt="kubernetes"/><br /><b>Kubernetes</b></a><br /><sub><a href="#kubernetes-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#prometheus"><img src="images/prometheus.png" width="75px;" height="75px;" alt="Prometheus"/><br /><b>Prometheus</b></a><br /><sub><a href="#prometheus-beginner">Beginner :baby:</a></sub><br><sub><a href="#prometheus-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#mongo"><img src="images/mongo.png" width="75px;" height="75px;" alt="Mongo"/><br /><b>Mongo</b></a><br /><sub><a href="#mongo-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#sql"><img src="images/sql.png" width="75px;" height="75px;" alt="sql"/><br /><b>SQL</b></a><br /><sub><a href="#sql-beginner">Beginner :baby:</a></sub><br><sub><a href="#sql-advanced">Advanced :star:</a></sub></td>
  </tr>
  <tr>
    <td align="center"><a href="#cloud"><img src="images/cloud.png" width="110px;" height="75px;" alt="Cloud"/><br /><b>Cloud</b></a><br /><sub><a href="#cloud-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#aws"><b>AWS</b></a><br /><sub><a href="#aws-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#azure"><b>Azure</b></a><br /><sub><a href="#azure-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#gcp"><b>Google Cloud Platform</b></a><br /><sub><a href="#gcp-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#openstack"><img src="images/openstack.png" width="75px;" height="75px;" alt="openstack"/><br /><b>OpenStack</b></a><br /><sub><a href="#openstack-beginner">Beginner :baby:</a></sub><br><sub><a href="#openstack-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#security"><img src="images/security.png" width="75px;" height="75px;" alt="security"/><br /><b>Security</b></a><br /><sub><a href="#security-beginner">Beginner :baby:</a></sub><br><sub><a href="#security-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#puppet"><img src="images/puppet.png" width="75px;" height="75px;" alt="puppet"/><br /><b>Puppet</b></a><br /><sub><a href="#puppet-beginner">Beginner :baby:</a></sub><br><sub><a href="#puppet-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#openshift"><img src="images/openshift.png" width="75px;" height="75px;" alt="OpenShift"/><br /><b>OpenShift</b></a><br /><sub><a href="#openshift-beginner">Beginner :baby:</a></sub><br><sub></td>
  </tr>
  <tr>
    <td align="center"><a href="#monitoring"><img src="images/monitoring.png" width="75px;" height="75px;" alt="Monitoring"/><br /><b>Monitoring</b></a><br /><sub><a href="#monitoring-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#elastic"><img src="images/elastic.png" width="110px;" height="75px;" alt="Elastic"/><br /><b>Elastic</b></a><br /><sub><a href="#elastic-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#dns"><b>DNS</b></a><br /><sub><a href="#dns-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#virtualization"><b>Virtualization</b></a><br /><sub><a href="#virtualization-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#operating-system"><b>Operating System</b></a><br /><sub><a href="#operating-system-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#general"><img src="images/general.png" width="110px;" height="75px;" alt="General"/><br /><b>General</b></a></td>
    <td align="center"><a href="#scenarios"><img src="images/scenarios.png" width="110px;" height="75px;" alt="Scenarios"/><br /><b>Scenarios</b></a></td>
  </tr>
</table>
</center>
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-TOPICS-LIST:END -->

## DevOps

<a name="devops-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is DevOps?</summary><br><b>

There are many good answers to this question. I like Amazon's description of DevOps:

"DevOps is the combination of cultural philosophies, practices, and tools that increases an organization’s ability to deliver applications and services at high velocity: evolving and improving products at a faster pace than organizations using traditional software development and infrastructure management processes. This speed enables organizations to better serve their customers and compete more effectively in the market."

You can find more details here: https://aws.amazon.com/devops/what-is-devops
</b></details>

<details>
<summary>What are the benefits of DevOps? What it can help us to achieve?</summary><br><b>

You should mention some or all of the following:

  * Collaboration
  * Improved delivery
  * Security
  * Speed
  * Scale
  * Reliability

Detailed answer can be found here: https://aws.amazon.com/devops/what-is-devops 
</b></details>

<details>
<summary>What are the anti-patterns of DevOps?</summary><br><b>
</b></details>

<details>
<summary>What is Continuous Integration?</summary><br><b>

A development practice where developers integrate code into a shared repository frequently. It can range from a couple of changes every day or a week to a couple of changes in one hour in larger scales.

Each piece of code (change/patch) is verified, to make the change is safe to merge. Today, it's a common practice to test the change using an automated build that makes sure the code can integrated. It can be one build which runs several tests in different levels (unit, functional, etc.) or several separate builds that all or some has to pass in order for the change to be merged into the repository.
</b></details>

<details>
<summary>What is Continuous Deployment?</summary><br><b>
</b></details>

<details>
<summary>What is Continuous Delivery?</summary><br><b>
</b></details>

<details>
<summary>What CI/CD best practices are you familiar with? Or what do you consider as CI/CD best practice?</summary><br><b>
</b></details>

<details>
<summary>What systems and/or tools are you using for the following?:

  * CI/CD
  * Provisioning infrastructure
  * Configuration Management
  * Monitoring & alerting
  * Logging
  * Code review
  * Code coverage
  * Tests</summary><br><b>
  * CI/CD - Jenkins, Circle CI, Travis
  * Provisioning infrastructure - Terraform, CloudFormation
  * Configuration Management - Ansible, Puppet, Chef
  * Monitoring & alerting - Prometheus, Nagios
  * Logging - Logstash, Graylog, Fluentd
  * Code review - Gerrit, Review Board
  * Code coverage - Cobertura, Clover, JaCoCo
  * Tests - Robot, Serenity, Gauge
</b></details>

<details>
<summary>What are you taking into consideration when choosing a tool/technology?</summary><br><b>

In your answer you can mention one or more of the following:
  * mature vs. cutting edge
  * community size
  * architecture aspects - agent vs. agentless, master vs. masterless, etc.
</b></details>

<details>
<summary>Explain mutable vs. immutable infrastructure</summary><br><b>

In mutable infrastructure paradigm, changes are applied on top of the existing infrastructure and over time
the infrastructure builds up a history of changes. Ansible, Puppet and Chef are examples to tools which
follow mutable infrastructure paradigm.

In immutable infrastructure paradigm, every change is actually new infrastructure. So a change
to a server will result in a new server instead of updating it. Terraform is an example of technology
which follows the immutable infrastructure paradigm.
</b></details>

<details>
<summary>What ways are you familiar with to deliver a software? What are the advantages and disadvantages of each method?</summary><br><b>

  * Archive - collect all your app files into one archive (e.g. tar) and deliver it to the user.
  * Package - depends on the OS, you can use your OS package format (e.g. in RHEL/Fefodra it's RPM) to deliver your software with a way to install, uninstall and update it using the standard packager commands
  * Images - Either VM or container images where your package is included with everything it needs in order to run successfully.
</b></details>

<details>
<summary>What is caching? How it works? Why is it important?</summary><br><b>
</b></details>

<details>
<summary>Explain stateless vs. stateful</summary><br><b>

Stateless applications don't store any data in the host which makes it ideal for horizontal scaling and microservices.
Stateful applications depend on the storage to save state and data, typically databases are stateful applications.
</b></details>

<details>
<summary>What is HTTP and how it works?</summary><br><b>
</b></details>

<details>
<summary>Describe the workflow of setting up some type of web server (Apache, IIS, Tomact, ...)</summary><br><b>
</b></details>

<details>
<summary>Explain "Open Source"</summary><br><b>
</b></details>

<details>
<summary>Describe me the architecture of service/app/project/... you designed and/or implemented</summary><br><b>
</b></details>

##### SRE

<details>
<summary>Compare SRE to DevOps</summary><br><b>
</b></details>

<details>
<summary>What SRE team is responsible for?</summary><br><b>

One can argue whether it's per company definition or a global one but at least according to a large companies, like Google for example, the SRE team is responsible for availability, latency, performance, efficiency, change management, monitoring, emergency response, and capacity planning of their services
</b></details>

<details>
<summary>What is an error budget?</summary><br><b>
</b></details>

<details>
<summary>What are MTTF (mean time to failure) and MTTR (mean time to repair)? What these metrics help us to evaluate?</summary><br><b>
</b></details>

<details>
<summary>What is a post-mortem meeting? Why is it important?</summary><br><b>
</b></details>

<details>
<summary>What is "infrastructure as code"? What implementation of IAC are you familiar with?</summary><br><b>
</b></details>


<a name="devops-advanced"></a>
#### :star: Advanced

<details>
<summary>Tell me how you perform plan capacity for your CI/CD resources (e.g. servers, storage, etc.)</summary><br><b>
</b></details>

<details>
<summary>How would you structure/implement CD for an application which depends on several other applications?</summary><br><b>
</b></details>

<details>
<summary>How do you measure your CI/CD quality? Are there any metrics you are using for measuring the quality?</summary><br><b>
</b></details>

<details>
<summary>What is a configuration drift? What problems is it causing?</summary><br><b>

Configuration drift happens when in an environment of servers with the exact same configuration and software, a certain server
or servers are being applied with updates or configuration which other servers don't get and over time these servers become
slightly different than all others.

This situation might lead to bugs which hard to identify and reproduce.
</b></details>

<details>
<summary>How to deal with a configuration drift?</summary><br><b>
</b></details>

<details>
<summary>Do you have experience with testing cross-projects changes? (aka cross-dependency)</summary><br><b>

Note: cross-dependency is when you have two or more changes to separate projects and you would like to test them in mutual build instead of testing each change separately.
</b></details>

<details>
<summary>Have you contributed to an open source project? Tell me about this experience</summary><br><b>
</b></details>

<details>
<summary>When you publish a project, you usually publish it with a license. What types of licenses are you familiar with and which one do you prefer to use?</summary><br><b>
</b></details>

## Jenkins

<a name="jenkins-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is Jenkins? What have you used it for?</summary><br><b>
</b></details>

<details>
<summary>What are the advantages of Jenkins over its competitors? Can you compare it to one of the following systems?

  * Travis
  * Bamboo
  * Teamcity
  * CircleCI</summary><br><b>
</b></details>

<details>
<summary>What are the limitations or disadvantages of Jenkins?</summary><br><b>
</b></details>

<details>
<summary>Explain the following:

  * Job
  * Build
  * Plugin
  * Slave
  * Executor</summary><br><b>
</b></details>

<details>
<summary>What plugins have you used in Jenkins?</summary><br><b>
</b></details>

<details>
<summary>Explain CI/CD and how you implemented it in Jenkins</summary><br><b>
</b></details>

<details>
<summary>What type of jobs are there? Which types have you used?</summary><br><b>
</b></details>

<details>
<summary>How did you report build results to users? What ways are you familiar with for reporting results?</summary><br><b>
</b></details>

<details>
<summary>You need to run unit tests every time a change submitted to a given project. Describe in details how your pipeline would look like and what will be executed in each stage</summary><br><b>
</b></details>

<details>
<summary>How to secure Jenkins?</summary><br><b>
</b></details>

<details>
<summary>Can you describe some of Jenkins best practices?</summary><br><b>
</b></details>

<details>
<summary>Describe how do you add new slaves to Jenkins</summary><br><b>

You can describe the UI way to add new slaves but better to explain how to do in a way that scales like a script or using dynamic source for slaves like one of the existing clouds.
</b></details>

<a name="jenkins-advanced"></a>
#### :star: Advanced

<details>
<summary>How to acquire multiple slaves for one specific build?</summary><br><b>
</b></details>

<details>
<summary>There are four teams in your organization. How to prioritize the builds of each team? So the jobs of team x will always run before team y for example</summary><br><b>
</b></details>

<details>
<summary>If you are managing a dozen of jobs, you can probably use the Jenkins UI. How do you manage the creation and deletion of hundreds of jobs every week/month?</summary><br><b>
</b></details>

<details>
<summary>What are some of Jenkins limitations?</summary><br><b>

  * Testing cross-dependencies (changes from multiple projects together)
  * Starting builds from any stage (although cloudbees implemented something called checkpoints)
</b></details>

<details>
<summary>How would you implement an option of a starting a build from a certain stage and not from the beginning?<summary><br><b>
</b></details>

##### Jenkins Dev

<details>
<summary>Do you have experience with developing a Jenkins plugin? Can you describe this experience?</summary><br><b>
</b></details>

<details>
<summary>Have you written Jenkins scripts? If yes, what for and how they work?</summary><br><b>
</b></details>

## Cloud 

<a name="cloud-beginner"></a>
#### :baby: Beginner

<details>
<summary>What are the advantages of cloud computing? Mention at least 3 advantages</summary><br><b>
</b></details>

<details>
<summary>What types of Cloud Computing are there?</summary><br><b>

IAAS
PAAS
SAAS
</b></details>

<details>
<summary>Explain each of the following Cloud Computing Deployments:

  * Public
  * Hybrid
  * Private</summary><br><b>
</b></details>


## AWS

<a name="aws-beginner"></a>
#### :baby: Beginner

##### Global Infrastructure

<details>
<summary>Explain the following

  * Availability zone
  * Region
  * Edge location</summary><br><b>
AWS regions are data centers hosted across different geographical locations worldwide, each region is completely independent of one another. 
Within each region,There are multiple isolated locations known as Availability Zones. Multiple availability zones insure high availability in case one of them goes down.

Edge locations are basically content delivery network which caches data and insures lower latency and faster delivery to the users in any location. They are located in major cities in the world.
</b></details>

<details>
<summary>What is IAM?</summary><br><b>
</b></details>

##### S3
 
<details>
<summary>Explain what is S3 and what is it used for</summary><br>
<b>
S3 stands for 3 S, Simple Storage Service.
S3 is a object storage service which is fast, scalable and durable. S3 enables customers to upload, download or store any file or object that is up to 5 TB in size. While having a maximum size of 5 GB per file (multipart upload if more than 5 GB in size).
</b>
</details>

<details>
<summary>What is a bucket?</summary><br><b>
An S3 bucket is a resource which is similar to folders in a file system and allows storing objects, which consist of data and its  meta data.
</b></details>

<details>
<summary>True or False? A bucket name must be globally unique</summary><br><b>
True
</b></details>

<details>
<summary>What objects in S3 consists of?
  * Another way to ask it: explain key, value, version id and meta data in context of objects</summary><br><b>
</b></details>

<details>
<summary>Explain data consistency</summary><br><b>
</b></details>

<details>
<summary>Can you host dynamic websites on S3?. What about static websites?</summary><br><b>
</b></details>

<details>
<summary>What security measures have you taken in context of S3?</summary><br><b>
</b></details>

<details>
<summary>What is a storage class? What storage classes are you familiar with?</summary><br><b>
</b></details>

##### EC2

<details>
<summary>What is EC2? What is it used for?</summary><br><b>
</b></details>

<details>
<summary>What EC2 pricing models are there?</summary><br><b>
</b></details>

<details>
<summary>How to increase RAM for a given EC2 instance?</summary><br><b>

Stop the instance, the type of the instance to match the desired RAM and start the instance.
</b></details>

<details>
<summary>What is an AMI?</summary><br><b>
</b></details>

<details>
<summary>How many storage options are there for EC2 Instances?</summary><br><b>
</b></details>

<details>
<summary>What happens when an EC2 instance is stopped or terminated?</summary><br><b>
</b></details>

<details>
<summary>What are Security Groups?</summary><br><b>
</b></details>

<details>
<summary>How to migrate an instance to another availability zone?</summary><br><b>
</b></details>

<details>
<summary>What are spot instances?</summary><br><b>
</b></details>

##### CloudFront

<details>
<summary>Explain what is CloudFront and what is it used for</summary><br><b>
</b></details>

<details>
<summary>Explain the following
  * Origin
  * Edge location
  * Distribution</summary><br><b>
</b></details>

<details>
<summary>What delivery methods available for the user with CDN?</summary><br><b>
</b></details>

<details>
<summary>True or False?. Objects are cached for the life of TTL</summary><br><b>
</b></details>

##### Load Balancers

<details>
<summary>What types of load balancers are supported in EC2 and what are they used for?</summary><br><b>

  * Application LB - layer 7 traffic
  * Network LB - ultra-high performances or static IP address
  * Classic LB - low costs, good for test or dev environments
</b></details>

##### Security 

<summary>What is the shared responsibility model? In other words, what AWS is responsible for and what the user is responsible for in regards to Security?</summary><br><b>
</b></details>

<summary>What is the AWS compliance program?</summary><br><b>
</b></details>

<summary>Explain what each of the following services is used for

  * AWS Inspector
  * AWS Artifact
  * AWS WAF
  * AWS Shield</summary><br><b>
</b></details>

<summary>What AWS VPN is usef for?</summary><br><b>
</b></details>

<summary>What is the difference between Site-to-Site VPN and Client VPN?</summary><br><b>
</b></details>

<summary>True or False? AWS Inspector can perform both network and host assessments</summary><br><b>

True
</b></details>

#### Databases

<details>
<summary>What is RDS?</summary><br><b>
</b></details>

<details>
<summary>What are some features or benefits of using RDS?</summary><br><b>

1. Multi AZ - great for Disaster Recovery
2. Read Replicas - for better performances
</b></details>

<details>
<summary>What is EBS?</summary><br><b>
</b></details>

<details>
<summary>What is VPC?</summary><br><b>
</b></details>

## Network

<a name="network-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is Ethernet?</summary><br><b>
</b></details>

<details>
<summary>What is a MAC address? What is it used for?</summary><br><b>
</b></details>

<details>
<summary>When is this MAC address used?: ff:ff:ff:ff:ff:ff</summary><br><b>
</b></details>

<details>
<summary>What is an IP address?</summary><br><b>
</b></details>

<details>
<summary>Explain subnet mask and given an example</summary><br><b>
</b></details>

<details>
<summary>What is a private IP address? What do we need it for?</summary><br><b>
</b></details>

<details>
<summary>Explain the OSI model. What layers there are? What each layer is responsible for?</summary><br><b>

Application: user end (HTTP is here)
Presentation: establishes context between application-layer entities (Encryption is here)
Session: establishes, manages and terminates the connections
Transport: transfers variable-length data sequences from a source to a destination host (TCP & UDP are here)
Network: transfers datagrams from one network to another (IP is here)
Data link: provides a link between two directly connected nodes (MAC is here)
Physical: the electrical and physical spec the data connection (Bits are here)
</b></details>

<details>
<summary>For each of the following determine to which OSI layer it belongs:

  * Error correction
  * Packets routing
  * Cables and electrical signals
  * MAC address
  * IP address
  * Sessions between applications
  * 3 way handshake</summary><br><b>
</b></details>

<details>
<summary>What delivery schemes are you familiar with?</summary><br><b>

Unitcast: One to one communication where there is one sender and one receiver.

Broadcast: Sending a message to everyone in the network. The address ff:ff:ff:ff:ff:ff is used for broadcasting.
           Two common protocols which use broadcast are ARP and DHCP.

Multicast: Sending a message to a group of subscribers. It can be one-to-many or many-to-many.
</b></details>

<details>
<summary>What is CSMA/CD? Is it used in modern ethernet networks?</summary><br><b>

CSMA/CD stands for Carrier Sense Multiple Access / Collision Detection.
Its primarily focus it to manage access to shared medium/bus where only one host can transmit at a given point of time.

CSMA/CD algorithm:

1. Before sending a frame, it checks whether another host already transmitting a frame.
2. If no one transmitting, it starts transmitting the frame.
3. If two hosts transmitted at the same time, we have a collision.
4. Both hosts stop sending the frame and they send to everyone a 'jam signal' notifying everyone that a collision occurred
5. They are waiting for a random time before sending again
6. Once each host waited for a random time, they try to send the frame again and so the
</b></details>

<details>
<summary>Describe the following network devices and the difference between them:

  * router
  * switch
  * hub</summary><br><b>
</b></details>

<details>
<summary>What is NAT?</summary><br><b>
</b></details>

<details>
<summary>What is a proxy? How it works? What do we need it for?</summary><br><b>
</b></details>

<details>
<summary>What is TCP? How it works? What is the 3 way handshake?</summary><br><b>
</b></details>

<details>
<summary>What is the difference between TCP and UDP?</summary><br><b>
	
TCP establishes a connection between the client and the server to guarantee the order of the packages, on the other hand, UDP does not establish a connection between client and server and doesn't handle package order. This makes UDP more lightweight than TCP and a perfect candidate for streaming services.
</b></details>

<details>
<summary>True or False? TCP is better than UDP</summary><br><b>
</b></details>

<details>
<summary>What TCP/IP protocols are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>Explain "default gateway"</summary><br><b>
</b></details>

<details>
<summary>What is ARP? How it works?</summary><br><b>
</b></details>

<details>
<summary>What is TTL?</summary><br><b>
</b></details>

<details>
<summary>What is DHCP? How it works?</summary><br><b>
</b></details>

<details>
<summary>What is SSL tunneling? How it works?</summary><br><b>
</b></details>

<details>
<summary>What is a socket? Where can you see the list of sockets in your system?</summary><br><b>
</b></details>

<details>
<summary>What is IPv6? Why should we consider using it if we have IPv4?</summary><br><b>
</b></details>

<details>
<summary>What is VLAN?</summary><br><b>
</b></details>

<details>
<summary>What is MTU?</summary><br><b>
</b></details>

<details>
<summary>True or False?. Ping is using UDP because it doesn't care about reliable connection</summary><br><b>
</b></details>

<details>
<summary>What is SDN?</summary><br><b>
</b></details>

<details>
<summary>What is ICMP? What is it used for?</summary><br><b>
</b></details>

<details>
<summary>What is NAT? How it works?</summary><br><b>
</b></details>

<details>
<summary>What is latency?</summary><br><b>
</b></details>

<details>
<summary>What is bandwidth?</summary><br><b>
</b></details>

<details>
<summary>Which factors affect network performances</summary><br><b>
</b></details>

<a name="network-advanced"></a>
#### :star: Advanced

<details>
<summary>Explain Spanning Tree Protocol (STP)</summary><br><b>
</b></details>

<details>
<summary>What is link aggregation? Why is it used?</summary><br><b>
</b></details>

<details>
<summary>What is Asymmetric Routing? How do deal with it?</summary><br><b>
</b></details>

<details>
<summary>What overlay (tunnel) protocols are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>What is GRE? How it works?</summary><br><b>
</b></details>

<details>
<summary>What is VXLAN? How it works?</summary><br><b>
</b></details>

<details>
<summary>What is SNAT?</summary><br><b>
</b></details>

<details>
<summary>Explain OSPF</summary><br><b>
</b></details>

<details>
<summary>Explain Spine & Leaf</summary><br><b>
</b></details>

<details>
<summary>What is Network Congestion? What can cause it?</summary><br><b>
</b></details>

<details>
<summary>What can you tell me about UDP packet format? What about TCP packet format? How is it different?</summary><br><b>
</b></details>

<details>
<summary>Using Hamming code, what would be the code word for the following data word 100111010001101?</summary><br><b>

00110011110100011101
</b></details>

## Linux

<a name="linux-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is your experience with Linux?</summary><br><b>

An open question. Answer based on your real experience.
</b></details>

<details>
<summary>Explain what each of the following commands does and give an example on how to use it:

  * ls
  * rm 
  * rmdir (can you achieve the same result by using <code>rm</code>?)
  * grep
  * wc
  * curl
  * touch
  * man
  * nslookup or dig
  * df</summary><br><b>
</b></details>

<details>
<summary>Running the command <code>df</code> you get "command not found". What could be wrong and how to fix it?</summary><br><b>
</b>
<p><b>
Most likely the default/generated $PATH was somehow modified or overridden thus not containing <code>/bin/</code> where df would normally go.
This issue could also happen if bash_profile or any configuration file of your interpreter was wrongly modified, causing erratics behaviours.
You would solve this by fixing your $PATH variable:

As to fix it there are serveral options:

1. Manually adding what you need to your $PATH <code>PATH="$PATH":/user/bin:/..etc</code> 
2. You have your weird env variables backed up.
3. You would look for your distro default $PATH variable, copy paste using method #1

Note: There are many ways of getting errors like this: if bash_profile or any configuration file of your interpreter was wrongly modified; causing erratics behaviours,
permissions issues, bad compiled software (if you compiled it by yourself)... there is no answer that will be true 100% of the time.</b>
</p>
</details>

<details>
<summary>How to make sure a service will start on a OS of your choice?</summary><br><b>
</b></details>

<details>
<summary>How do you schedule tasks periodically?</summary><br><b>

You can use the commands <code>cron</code> and <code>at</code>.
With cron, tasks are scheduled using the following format:

<code>*/30 * * * * bash myscript.sh</code> Executes the script every 30 minutes.

<minute> <hour> <day of month> <month> <day of week> <command to execute>

The tasks are stored in a cron file, you can write in it using <code>crontab -e</code>

Alternatively if you are using a distro with systemd it's recommended to use systemd timers.

</b></details>

<details>
<summary>Have you scheduled tasks in the past? What kind of tasks?</summary><br><b>

Normally you will schedule batch jobs.
</b></details>

##### Permissions

<details>
<summary>How to change the permissions of a file?</summary><br><b>

Using the `chmod` command.

</b></details>

<details>
<summary>What does the following permissions mean?:

  * 777
  * 644
  * 750</summary><br><b>

<pre>
777 - You give the owner, group and other: Execute (1), Write (2) and Read (4); 4+2+1 = 7.
644 - Owner has Read (4), Write (2), 4+2 = 6; Group and Other have Read (4).
750 - Owner has x+r+w, Group has Read (4) and Execute (1); 4+1 = 5. Other have no permissions.
</pre>
</b></details>

<details>
<summary>Explain what is setgid, setuid and sticky bit</summary><br><b>
</b></details>

<details>
<summary>You try to delete a file but it fails. Name at least three different reason as to why it could happen</summary><br><b>
</b></details>

<details>
<summary>What is systemd?</summary><br>
<b>
Systemd is a daemon (System 'd', d stands from daemon).

A daemon is a program that runs in the background without direct control of the user, although the user can at any time
talk to the daemon.

systemd has many features such as user processes control/tracking, snapshot support, inhibitor locks..


If we visualize the unix/linux system in layers, systemd would fall directly after the linux kernel.

Hardware -> Kernel -> <u>Daemons</u>, System Libraries, Server Display.


</b>
</details>

<details>
<summary>On a system which uses systemd, how would you display the logs?</summary><br><b>

<code>journalctl</code>
</b></details>

<details>
<summary>Describe how to make a certain process/app a service</summary><br><b>
</b></details>

##### Debugging

<details>
<summary>What are you using for troubleshooting and debugging <b>network</b> issues?</summary><br><b>

<code>dstat -t</code> is great for identifying network and disk issues.
<code>netstat -tnlaup</code> can be used to see which processes are running on which ports.
<code>lsof -i -P</code> can be used for the same purpose as netstat.
<code>ngrep -d any metafilter</code> for matching regex against payloads of packets.
<code>tcpdump</code> for capturing packets
<code>wireshark</code> same concept as tcpdump but with GUI (optional).
</b></details>

<details>
<summary>What are you using for troubleshooting and debugging <b>disk & file system</b> issues?</summary><br><b>

<code>dstat -t</code> is great for identifying network and disk issues.
<code>opensnoop</code> can be used to see which files are being opened on the system (in real time).
</b></details>

<details>
<summary>What are you using for troubleshooting and debugging <b>process</b> issues?</summary><br><b>

<code>strace</code> is great for understanding what your program does. It prints every system call your program executed.
</b></details>

<details>
<summary>What are you using for debugging CPU related issues?</summary><br><b>

<code>top</code> will show you how much CPU percentage each process consumes
<code>perf</code> is a great choice for sampling profiler and in general, figuring out what your CPU cycles are "wasted" on
<code>flamegraphs</code> is great for CPU consumption visualization (http://www.brendangregg.com/flamegraphs.html)
</b></details>

<details>
<summary>You get a call saying "my system is slow" - how would you deal with it?</summary><br><b>

1. Check with <code>top</code> if anything consumes your CPU or RAM.
2. Run <code>dstat -t</code> to check if it's related to disk or network.
3. Check I/O stats with <code>iostat</code>
</b></details>

<details>
<summary>How to debug binaries?</summary><br><b>
</b></details>

<details>
<summary>What is a Linux kernel module and how do you load a new module?</summary><br><b>
</b></details>

<details>
<summary>What is KVM?</summary><br><b>
</b></details>

<details>
<summary>What is SSH key? How is it used?</summary><br><b>
</b></details>

<details>
<summary>What is the difference between SSH and SSL?</summary><br><b>
</b></details>

<details>
<summary>What is SSH port forwarding?</summary><br><b>
</b></details>

<details>
<summary>Explain redirection</summary><br><b>
</b></details>

<details>
<summary>What are wildcards? Can you give an example of how to use them?</summary><br><b>
</b></details>

<details>
<summary>What do we grep for in each of the following commands?:

  * <code>grep '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' some_file</code>
  * <code>grep -E "error|failure" some_file</code>
  * <code>grep '[0-9]$' some_file</code>
</summary><br><b>

1. An IP address
2. The word "error" or "failure"
3. Lines which end with a number
</b></details>

<details>
<summary>Tell me everything you know about the Linux boot process</summary><br><b>

Another way to ask this: what happens from the moment you turned on the server until you get a prompt
</b></details>

<details>
<summary>What is an exit code? What exit codes are you familiar with?</summary><br><b>

An exit code (or return code) represents the code returned by a child process to its
parent process.

0 is an exit code which represents success while anything higher than 1 represents error.
Each number has different meaning, based on how the application was developed.

I consider this as a good blog post to read more about it: https://shapeshed.com/unix-exit-codes
</b></details>

##### Storage, Filesystem

<details>
<summary>What's an inode?</summary><br><b>

For each file (and directory) in Linux there is an inode, a data structure which stores meta data
related to the file like its size, owner, permissions, etc.
</b></details>

<details>
<summary>How to check which disks are currently mounted?</summary><br><b>
</b></details>

<details>
<summary>What is the difference between a soft link and hard link?</summary><br><b>

Hard link is the same file, using the same inode.
Soft link is a shortcut to another file, using a different inode.

Soft links can be created between different file systems while hard link can be created only within the same file system.
</b></details>

<details>
<summary>What happens when you delete the original file in case of soft link and hard link?</summary><br><b>
</b></details>

<details>
<summary>What is a swap partition? What is it used for?</summary><br><b>
</b></details>

<details>
<summary>You are trying to create a new file but you get "File system is full". You check with df for free space and you see you used only 20% of the space. What could be the problem?</summary><br><b>
</b></details>

<details>
<summary>How would you check what is the size of a certain directory?</summary><br><b>
</b></details>

<details>
<summary>What do you know about LVM?</summary><br><b>
</b></details>

<details>
<summary>Explain the following in regards to LVM:

  * PV
  * VG
  * LV</summary><br><b>
</b></details>

<details>
<summary>What is NFS? What is it used for?</summary><br><b>
</b></details>

<details>
<summary>What RAID is used for? Can you explain the differences between RAID 0, 1, 5 and 10?</summary><br><b>
</b></details>

<details>
<summary>What is lazy umount?</summary><br><b>
</b></details>

<details>
<summary>Fix the following commands:

  * sed "s/1/2/g' /tmp/myFile
  * find . -iname \*.yaml -exec sed -i "s/1/2/g" {} ;
  
  </summary><br><b>
</b>
<code>sed 's/1/2/g' /tmp/myFile</code><br>
<code> find . -iname "*.yaml" -exec sed -i "s/1/2/g" {} \; </code>
</details>

<details>
<summary>Explain what is stored in each of the following paths and if there is anything unique about it:</summary><br><b>

  * /tmp
  * /var/log
  * /bin
  * /proc
  * /usr/local
</b></details>

##### Processes

<details>
<summary>Can you explain what is a process?</summary><br><b>

A process is a running program. A program is one or more instructions and the program (or process) is executed by the operating system.
</b></details>

<details>
<summary>How to run a process in the background and why to do that in the first place?</summary><br><b>

You can achieve that by specifying & at end of the command.
As to why, since some commands/processes can take a lot of time to finish
execution or run forever
</b></details>

<details>
<summary>How can you find how much memory a specific process consumes?</summary><br><b>
</b></details>

<details>
<summary>What signal is used by default when you run 'kill <process id>'?</summary><br><b>
<pre>
The default signal is SIGTERM (15). This signal kills
process gracefully which means it allows it to save current
state configuration.
</pre>
</b></details>

<details>
<summary>What signals are you familiar with?</summary><br><b>

SIGTERM - default signal for terminating a process
SIGHUP - common usage is for reloading configuration
SIGKILL - a signal which cannot caught or ignored

To view all available signals run `kill -l`
</b></details>

<details>
<summary>What is a trap?</summary><br><b>
</b></details>

<details>
<summary>What happens when you press ctrl + c?</summary><br><b>
</b></details>

<details>
<summary>What are daemons?</summary><br><b>
</b></details>

<details>
<summary>What are the possible states of a process in Linux?</summary><br><b>
<pre>
Running (R)
Uninterruptible Sleep (D) - The process is waiting for I/O
Interruptible Sleep (S)
Stopped (T)
Dead (x)
Zombie (z)
</pre>
</b></details>

<details>
<summary>What is a zombie process?</summary><br><b>
</b></details>

<details>
<summary>How to get rid of zombie processes?</summary><br><b>

You can't kill a zombie process the regular way with `kill -9` for example as it's already dead.

One way to kill zombie process is by sending SIGCHLD to the parent process telling it to terminate its child processes. This might not work if the parent process wasn't programmed properly. The invocation is `kill -s SIGCHLD [parent_pid]`

You can also try closing/terminating the parent process. This will make the zombie process a child of init (1) which does periodic cleanups and will at some point clean up the zombie process.
</b></details>

<details>
<summary>What is the init process?</summary><br><b>
</b></details>

<details>
<summary>How to change the priority of a process? Why would you want to do that?</summary><br><b>
</b></details>

<details>
<summary>Can you explain how network process/connection is established and how it's terminated?><br></b>
</b></details>

<details>
<summary>What are system calls? What system calls are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>What <code>strace</code> does?</summary><br><b>
</b></details>

<details>
<summary>Find all the files which end with '.yml' and replace the number 1 in 2 in each file</summary><br><b>

ind /some_dir -iname \*.yml -print0 | xargs -0 -r sed -i "s/1/2/g"
</b></details>

<details>
<summary>How to check how much free memory a system has? How to check memory consumption by each process?</summary><br><b>

You can use the commands <code>top</code> and <code>free</code>
</b></details>

<details>
<summary>How would you split a 50 lines file into 2 files of 25 lines each?</summary><br><b>

You can use the <code>split</code> command this way: <code>split -l 25 some_file</code>
</b></details>

<details>
<summary>What is a file descriptor? What file descriptors are you familiar with?</summary><br><b>
Kerberos
File descriptor, also known as file handler, is a unique number which identifies an open file in the operating system.

In Linux (and Unix) the first three file descriptors are:
  * 0 - the default data stream for input
  * 1 - the default data stream for output
  * 2 - the default data stream for output related to errors

This is a great article on the topic: https://www.computerhope.com/jargon/f/file-descriptor.htm
</b></details>

<details>
<summary>What is NTP? What is it used for?</summary><br><b>
</b></details>

<details>
<summary>Explain Kernel OOM</summary><br><b>
</b></details>

##### Security

<details>
<summary>What is chroot? In what scenarios would you consider using it?</summary><br><b>
</b></details>

<details>
<summary>What is SELiunx?</summary><br><b>
</b></details>

<details>
<summary>What is Kerberos?</summary><br><b>
</b></details>

<details>
<summary>What is nftables?</summary><br><b>
</b></details>

<details>
<summary>What firewalld daemon is responsible for?</summary><br><b>
</b></details>

##### Network

<details>
<summary>What is a network namespace? What is it used for?</summary><br><b>
</b></details>

<details>
<summary>How can you turn your Linux server into a router?</summary><br><b>
</b></details>

<details>
<summary>What is a virtual IP? In what situation would you use it?</summary><br><b>
</b></details>

<details>
<summary>Which port is used in each of the following protocols?:

  * SSH
  * HTTP
  * DNS
  * HTTPS</summary><br><b>

  * SSH - 22
  * HTTP - 80
  * DNS - 53
  * HTTPS - 443
</b></details>

<details>
<summary>What is the routing table? How do you view it?</summary><br><b>
</b></details>

<details>
<summary>What are packet sniffers? Have you used one in the past? If yes, which packet sniffers have you used and for what purpose?</summary><br><b>
</b></details>

<details>
<summary>How to list active connections?</summary><br><b>
</b></details>

##### Linux DNS

<details>
<summary>What the file <code>/etc/resolv.conf</code> is used for? What does it include?</summary><br><b>
</b></details>

<details>
<summary>What commands are you using for performing DNS queries (or troubleshoot DNS related issues)?</summary><br><b>

You can specify one or more of the following:

 * <code>dig</code>
 * <code>nslookup</code>
</b></details>

##### Packaging

<details>
<summary>Do you have experience with packaging? Can you explain how it works?</summary><br><b>
</b></details>

<details>
<summary>RPM: explain the spec format(what it should and can include)</summary><br><b>
</b></details>

<details>
<summary>How do you list the content of a package without actually installing it?</summary><br><b>
</b></details>

##### Applications and Services

<details>
<summary>What is a load balancer?</summary><br><b> 
</b></details>

<details>
<summary>What load balancer algorithms are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>What is a proxy?</summary><br><b> 
</b></details>

<details>
<summary>What is a reverse proxy?</summary><br><b> 
</b></details>

<details>
<summary>What can you find in /etc/services</summary><br><b>
</b></details>

<details>
<summary>You run <code>ssh 127.0.0.1</code> but it fails with "connection refused". What could be the problem?</summary><br><b>

1. SSH server is not installed
2. SSH server is not running
</b></details>

<details>
<summary>How to print the shared libraries required by a certain program? What is it useful for?</summary><br><b>
</b></details>

##### Users

<details>
<summary>How do you create users? Where user information is stored?</summary><br><b>
</b></details>

<details>
<summary>Do you know how to create a new user without using adduser/useradd command?</summary><br><b>
</b></details>

<details>
<summary>How to add a new user to the system without providing him the ability to log-in into the system?</summary><br><b>

  * adduser user_name --shell=/bin/false --no-create-home
</b></details>

<details>
<summary>What can you do if you lost/forogt the root password?</summary><br><b>

Re-install the OS IS NOT the right answer :)
</b></details>

<details>
<summary>What is sudo? How do you set it up?</summary><br><b>
</b></details>

<a name="linux-advanced"></a>
#### :star: Advanced

<details>
<summary>What happens when you execute <code>ls</code>?. Provide a detailed answer</summary><br><b>
</b></details>

<details>
<summary>Can you describe how processes are being created?</summary><br><b>
</b></details>

<details>
<summary>What does the following block do?:

```
open("/my/file") = 5
read(5, "file content")
```
</summary><br><b>

These system calls are reading the file <code>/my/file</code> and 5 is the file descriptor number.
</b></details>

<details>
<summary>What is the difference between a process and a thread?</summary><br><b>
</b></details>

<details>
<summary>You found there is a server with high CPU load but you didn't find a process with high CPU. How is that possible?</summary><br><b>
</b></details>

##### Network

<details>
<summary>When you run <code>ip a</code> you see there is a device called 'lo'. What is it and why do we need it?</summary><br><b>
</b></details>

<details>
<summary>What <code>traceroute</code> command does? How it works?</summary><br><b>

Another common way to task this questions is "what part of the tcp header does traceroute modify?"
</b></details>

<details>
<summary>What is network bonding? What types are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>How to link two separate network namespaces so you can ping an interface on one namespace from the second one?</summary><br><b>
</b></details>

<details>
<summary>What are cgroups?</summary><br><b>
</b></details>

<details>
<summary>How to create a file of a certain size?</summary><br><b>

There are a couple of ways to do that:
  
  * dd if=/dev/urandom of=new_file.txt bs=2MB count=1
  * truncate -s 2M new_file.txt
  * fallocate -l 2097152 new_file.txt
</b></details>

<details>
<summary>What are the differences between the following system calls?: exec(), fork(), vfork() and clone()?</summary><br><b>
</b></details>

<details>
<summary>Explain Process Descriptor and Task Structure</summary><br><b>
</b></details>

<details>
<summary>What are the differences between threads and processes?</summary><br><b>
</b></details>

<details>
<summary>Explain Kernel Threads</summary><br><b>
</b></details>

<details>
<summary>What happens when socket system call is used?</summary><br><b>

This is a good article about the topic: https://ops.tips/blog/how-linux-creates-sockets
</b></details>

<details>
<summary>You executed a script and while still running, it got accidentally removed. Is it possible to restore the script while it's still running?</summary><br><b>
</b></details>

## Operating System

<a name="operating-system-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is an operating system?</summary><br><b>

There are many ways to answer that. For those who look for simplicity, the book "Operating Systems: Three Easy Pieces" offers nice version:

"responsible for making it easy to run programs (even allowing you to seemingly run many at the same time), allowing programs to share memory, enabling programs to interact with devices, and other fun stuff like that"
</b></details>

<details>
<summary>If you had to design an API for processes in an operating system, what would this API look like?</summary><br><b>

* Create - allow to create new processes 
* Delete - allow to remove/destroy processes
* State - allow to check the state of the process, whether it's running, stopped, waiting, etc.
* Stop - allow to stop a running process
</b></details>

<details>
<summary>How a process is created?</summary><br><b>

* The OS is reading program's code and any additional relevant data
* Program's bytes are loaded into the memory or more specifically, into the address space of the process.
* Memory is allocated for program's stack (aka run-time stack). The stack also initialized by the OS with data like argv, argc and parameters to main()
* Memory is allocated for program's heap which is required for data structures like linked lists and hash tables
* I/O initialization tasks like in Unix/Linux based systems where each process has 3 file descriptors (input, output and error)
* OS is running the program, strarting from main()

Note: The loading of the program's code into the memory done lazily which means the OS loads only partial relevant pieces required for the process to run and not the entire code.
</b></details>

<details>
<summary>True or False? The loading of the program into the memory is done eagerly (all at once)</summary><br><b>

False. It was true in the past but today's operating systems perform lazy loading which means only the relevant pieces required for the process to run are loaded first.
</b></details>

<details>
<summary>What are different states of a process?</summary><br><b>
</b></details>


## Virtualization

<a name="virtualization-beginner"></a>
#### :baby: Beginner

<details>
<summary>Explain what is Virtualization</summary><br><b>
</b></details>

<details>
<summary>What is "time sharing"?</summary><br><b>

Even when using a system with one physical CPU, it's possible to allow multiple users to work on it and run programs. This is possible with time sharing where computing resources are shared in a way it seems to the user the system has multiple CPUs but in fact it's simply one CPU shared by applying multiprogramming and multi-tasking.
</b></details>

<details>
<summary>What is "space sharing"?</summary><br><b>

Somewhat the opposite of time sharing. While in time sharing a resource is used for a while by one entity and then the same resource can be used by another resource, in space sharing the space is shared by multiple entities but in a way it's not being transfered between them.<br>
It's used by one entity until this entity decides to get rid of it. Take for example storage. In storage, a file is your until you decide to delete it.
</b></details>

## Ansible

<a name="ansible-beginner"></a>
#### :baby: Beginner

<details>
<summary>Describe each of the following components in Ansible, including the relationship between them:

  * Task
  * Module
  * Play
  * Playbook
  * Role</summary><br><b>

Task – a call to a specific Ansible module
Module – the actual unit of code executed by Ansible on your own host or a remote host. Modules are indexed by category (database, file, network, …) and also referred as task plugins.

Play – One or more tasks executed on a given host(s)

Playbook – One or more plays. Each play can be executed on the same or different hosts

Role – Ansible roles allows you to group resources based on certain functionality/service such that they can be easily reused. In a role, you have directories for variables, defaults, files, templates, handlers, tasks, and metadata. You can then use the role by simply specifying it in your playbook.
</b></details>

<details>
<summary>Which Ansible best practices are you familiar with?. Name at least three</summary><br><b>
</b></details>

<details>
<summary>What is an inventory file and how you define one?</summary><br><b>

An inventory file defines hosts and/or groups of hosts on which Ansible tasks executed upon.

An example of inventory file:

192.168.1.2
192.168.1.3
192.168.1.4

[web_servers]
190.40.2.20
190.40.2.21
190.40.2.22
</b></details>

<details>
<summary>What is a dynamic inventory file? When you would use one?</summary><br><br>

A dynamic inventory file tracks hosts from one or more sources like cloud providers and CMDB systems.

You should use one when using external sources and especially when the hosts in your environment are being automatically<br>
spun up and shut down, without you tracking every change in these sources.
</b></details>

<details>
<summary>You want to run Ansible playbook only on specific minor version of your OS, how would you achieve that?</summary><br><b>
</b></details>

<details>
<summary>Write a task to create the directory ‘/tmp/new_directory’</summary><br><b>

```
- name: Create a new directory
  file:
      path: "/tmp/new_directory"
      state: directory
```
</b></details>

<details>
<summary>What would be the result of the following play?</summary><br><b>

```
---
- name: Print information about my host
  hosts: localhost
  gather_facts: 'no'                                                                                                                                                                           
  tasks:
      - name: Print hostname
        debug:
            msg: "It's me, {{ ansible_hostname }}"
```

When given a written code, always inspect it thoroughly. If your answer is “this will fail” then you are right. We are using a fact (ansible_hostname), which is a gathered piece of information from the host we are running on. But in this case, we disabled facts gathering (gather_facts: no) so the variable would be undefined which will result in failure.
</b></details>

<details>
<summary>Write a playbook to install ‘zlib’ and ‘vim’ on all hosts if the file ‘/tmp/mario’ exists on the system.</summary><br><b>

```
---
- hosts: all
  vars:
      mario_file: /tmp/mario
      package_list:
          - 'zlib' 
          - 'vim'
  tasks:
      - name: Check for mario file
        stat:
            path: "{{ mario_file }}"
        register: mario_f

      - name: Install zlib and vim if mario file exists
        become: "yes"
        package:
            name: "{{ item }}"
            state: present
        with_items: "{{ package_list }}"
        when: mario_f.stat.exists
```
</b></details>

<details>
<summary>Write a playbook to deploy the file ‘/tmp/system_info’ on all hosts except for controllers group, with the following content</summary><br><b>

  ```
  I'm <HOSTNAME> and my operating system is <OS>
  ```

  Replace <HOSTNAME> and  <OS> with the actual data for the specific host you are running on

The playbook to deploy the system_info file

```
--- 
- name: Deploy /tmp/system_info file
  hosts: all:!controllers
  tasks: 
      - name: Deploy /tmp/system_info
        template:
            src: system_info.j2 
            dest: /tmp/system_info
```

The content of the system_info.j2 template

```
# {{ ansible_managed }}
I'm {{ ansible_hostname }} and my operating system is {{ ansible_distribution }
```
</b></details>

<details>
<summary>The variable 'whoami' defined in the following places:

  * role defaults -> whoami: mario
  * extra vars (variables you pass to Ansible CLI with -e) -> whoami: toad
  * host facts -> whoami: luigi
  * inventory variables (doesn’t matter which type) -> whoami: browser

According to variable precedence, which one will be used?</summary><br><b>

The right answer is ‘toad’.

Variable precedence is about how variables override each other when they set in different locations. If you didn’t experience it so far I’m sure at some point you will, which makes it a useful topic to be aware of.

In the context of our question, the order will be extra vars (always override any other variable) -> host facts -> inventory variables -> role defaults (the weakest).

A full list can be found at the link above. Also, note there is a significant difference between Ansible 1.x and 2.x.
</b></details>

<details>
<summary>For each of the following statements determine if it's true or false:

  * A module is a collection of tasks
  * It’s better to use shell or command instead of a specific module
  * Host facts override play variables
  * A role might include the following: vars, meta, and handlers
  * Dynamic inventory is generated by extracting information from external sources
  * It’s a best practice to use indention of 2 spaces instead of 4
  * ‘notify’ used to trigger handlers
  * This “hosts: all:!controllers” means ‘run only on controllers group hosts</summary><br><b>
</b></details>

<details>
<summary>What is ansible-pull?  How it’s different compared to ansible-playbook?</summary><br><b>
</b></details>


<a name="ansible-advanced"></a>
#### :star: Advanced

<details>
<summary>What are filters? Do you have experience with writing filters?</summary><br><b>
</b></details>

<details>
<summary>Write a filter to capitalize a string</summary><br><b>

<code>
def cap(self, string):
    return string.capitalize()
</code>
</b></details>

<details>
<summary>How do you test your Ansible based projects?</summary><br><b>
</b></details>

<details>
<summary>What are callback plugins? What can you achieve by using callback plugins?</summary><br><b>
</b></details>

<details>
<summary>File '/tmp/exercise' includes the following content

```
Goku = 9001
Vegeta = 5200
Trunks = 6000
Gotenks = 32
```

With one task, switch the content to:

```
Goku = 9001
Vegeta = 250
Trunks = 40
Gotenks = 32
```
</summary><br><b>

```
- name: Change saiyans levels
  lineinfile:
    dest: /tmp/exercise
    regexp: "{{ item.regexp }}"
    line: "{{ item.line }}"
  with_items:
    - { regexp: '^Vegeta', line: 'Vegeta = 250' }
    - { regexp: '^Trunks', line: 'Trunks = 40' }
    ...
```
</b></details>

## Terraform

<a name="terraform-beginner"></a>
#### :baby: Beginner

<details>
<summary>Can you explain what is Terraform? How it works?</summary><br><b>

Read [here](https://www.terraform.io/intro/index.html#what-is-terraform-)
</b></details>

<details>
<summary>What benefits infrastructure-as-code has?</summary><br><b>

- fully automated process of provisioning, modifying and deleting your infrastructure
- version control for your infrastructure which allows you to quickly rollback to previous versions
- validate infrastructure quality and stability with automated tests and code reviews
- makes infrastructure tasks less repetitive
</b></details>

<details>
<summary>Why Terraform and not other technologies? (e.g. Ansible, Puppet, CloufFormation)</summary><br><b>

A common *wrong* answer is to say that Ansible and Puppet are configuration management tools
and Terraform is a provisioning tool. While technically true, it doesn't mean Ansible and Puppet can't
be used for provisioning infrastructure. Also, it doesn't explain why Terraform should be used over
CloudFormation if at all.

The benefits of Terraform over the other tools:

  * It follows the immutable infrastructure approach which has benefits like avoiding a configuration drift over time
  * Ansible and Puppet are more procedural (you mention what to execute in each step) and Terraform is declarative since you describe the overall desired state and not per resource or task. You can give the example of going from 1 to 2 servers in each tool. In Terraform you specify 2, in Ansible and puppet you have to only provision 1 additional server so you need to explicitly make sure you provision only another one server.
</b></details>

<details>
<summary>Explain what is "Terraform configuration"</summary><br><b>
</b></details>

<details>
<summary>Explain each of the following:

  * Provider
  * Resource 
  * Provisioner 
</summary><br><b>
  * Provider is any cloud based technology - github, aws, postgresql etc - which one can make an API call to with its unique terraform provider binary to provision available services and components.<br>  
  * Resources are the services and components you provision on these platforms.<br>
  * Provisioner in terraform's lingo specifically refers to configuration tools like ansible or salt-stack which are used in combination with terraform to orchestrate a system.
</b></details>

<details>
<summary>What <code>terraform.tfstate</code> file is used for?</summary><br><b> 

It keeps track of the IDs of created resources so that Terraform knows what it is managing.
</b></details>

<details>
<summary>Explain what the following commands do:

  * <code>terraform init</code> 
  * <code>terraform plan</code>	
  * <code>terraform validate</code> 
  * <code>terraform apply</code> 
</summary><br><b>

<code>terraform init</code> scans your code to figure which providers are you using and download them.
<code>terraform plan</code> will let you see what terraform is about to do before actually doing it.
<code>terraform apply</code> will provision the resources specified in the .tf files.
</b></details>

<details>
<summary>How to write down a variable which changes by an external source or during <code>terraform apply</code>?</summary><br><b>

You use it this way: <code>variable “my_var” {}</code>
</b></details>

<details>
<summary>Give an example of several Terraform best practices</summary><br><b>
</b></details>

<details>
<summary>Explain how implicit and explicit dependencies work in Terraform</summary><br><b>
</b></details>

<details>
<summary>What is <code>local-exec</code> and <code>remote-exec</code> in the context of provisioners?</summary><br><b>
</b></details>

<details>
<summary>What is a "tainted resource"?</summary><br><b>

It's a resource which was successfully created but failed during provisioning. Terraform will fail and mark this resource as "tainted".
</b></details>

<details>
<summary>What <code>terraform taint</code> does?</summary><br><b>
</b></details>

<details>
<summary>What types of variables are supported in Terraform?</summary><br><b>

String
Integer
Map
List
</b></details>

<details>
<summary>What is a data source? In what scenarios for example would need to use it?</summary><br><b>
</b></details>

<details>
<summary>What are output variables and what <code>terraform output</code> does?</summary><br><b>
</b></details>

<details>
<summary>Explain Modules</summary>
</b></details>

<details>
<summary>What is the Terraform Registry?</summary><br><b>
</b></details>

<details>
<summary>Explain <code>remote-exec</code> and <code>local-exec</code></summary><br><b>
</b></details>


<a name="terraform-advanced"></a>
#### :star: Advanced

<details>
<summary>Explain "Remote State". When would you use it and how?</summary><br><b>
  Terraform generates a `terraform.tfstate` json file that describes components/service provisioned on the specified provider. Remote  
  State stores this file in a remote storage media to enable collaboration amongst team.
</b></details>

<details>
<summary>Explain "State Locking"</summary><br><b>
  State locking is a mechanism that blocks an operations against a specific state file from multiple callers so as to avoid conflicting   operations from different team members. Once the first caller's operation's lock is released the other team member may go ahead to   
  carryout his own operation. Nevertheless Terraform will first check the state file to see if the desired resource already exist and 
  if not it goes ahead to create it.
</b></details>

<details>
<summary>What is the "Random" provider? What is it used for</summary><br><b>
 The random provider aids in generating numeric or alphabetic characters to use as a prefix or suffix for a desired named identifier.
</b></details>

## Docker

<a name="docker-beginner"></a>

#### :baby: beginner

<details>
<summary>What is Docker? What are you using it for?</summary><br><b>
</b></details>

<details>
<summary>How containers are different from VMs?</summary><br><b>

The primary difference between containers and VMs is that containers allow you to virtualize
multiple workloads on the operating system while in the case of VMs the hardware is being virtualized to
run multiple machines each with its own OS.
</b></details>

<details>
<summary>In which scenarios would you use containers and in which you would prefer to use VMs?</summary><br><b>

You should choose VMs when:
  * you need run an application which requires all the resources and functionalities of an OS
  * you need full isolation and security

You should choose containers when:
  * you need a lightweight solution that quickly starts
  * Running multiple versions or instances of a single application
</b></details>

<details>
<summary>Explain Docker architecture</summary><br><b>
</b></details>

<details>
<summary>Describe in detail what happens when you run `docker run hello-world`?</summary><br><b>

Docker CLI passes your request to Docker daemon.
Docker daemon downloads the image from Docker Hub
Docker daemon creates a new container by using the image it downloaded
Docker daemon redirects output from container to Docker CLI which redirects it to the standard output
</b></details>

<details>
<summary>How do you run a container?</summary><br><b>
</b></details>

<details>
<summary>What best practices are you familiar related to working with containers?</summary><br><b>
</b></details>

<details>
<summary>What `docker commit` does?. When will you use it?</summary><br><b>
</b></details>

<details>
<summary>How would you transfer data from one container into another?</summary><br><b>
</b></details>

<details>
<summary>What happens to data of the container when a container exists?</summary><br><b>
</b></details>

<details>
<summary>Explain what each of the following commands do:

  * docker run
  * docker rm
  * docker ps
  * docker build
  * docker commit</summary><br><b>
</b></details>

<details>
<summary>How do you remove old, non running, containers?</summary><br><b>
</b></details>

##### Dockerfile

<details>
<summary>What is Dockerfile</summary><br><b>
</b></details>

<details>
<summary>What is the difference between ADD and COPY in Dockerfile?</summary><br><b>
</b></details>

<details>
<summary>What is the difference between CMD and RUN in Dockerfile?</summary><br><b>
</b></details>

<details>
<summary>Explain what is Docker compose and what is it used for</summary><br><b>
</b></details>

<details>
<summary>What are the differences between Docker compose, Docker swarm and Kubernetes?</summary><br><b>
</b></details>

<details>
<summary>Explain Docker interlock</summary><br><b>
</b></details>

<details>
<summary>What is the difference between Docker Hub and Docker cloud?</summary><br><b>

Docker Hub is a native Docker registry service which allows you to run pull
and push commands to install and deploy Docker images from the Docker Hub.

Docker Cloud is built on top of the Docker Hub so Docker Cloud provides
you with more options/features compared to Docker Hub. One example is
Swarm management which means you can create new swarms in Docker Cloud.
</b></details>

<details>
<summary>Where Docker images are stored?</summary><br><b>
</b></details>

<details>
<summary>Explain image layers</summary><br><b>
</b></details>

<a name="docker-advanced"></a>
#### :star: Advanced

<details>
<summary>How do you manage persistent storage in Docker?</summary><br><b>
</b></details>

<details>
<summary>How can you connect from the inside of your container to the localhost of your host, where the container runs?</summary><br><b>
</b></details>

<details>
<summary>How do you copy files from Docker container to the host and vice versa?</summary><br><b>
</b></details>

## Kubernetes

<a name="kubernetes-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is Kubernetes?</summary><br><b>
</b></details>

<details>
<summary>Why Docker isn't enough? Why do we need Kubernetes?</summary><br><b>

Kubernetes is especially good for scenarios when you no longer running small number of containers. When you have to scale from 3 containers for eaxmple to hundreds or thousands of containers.
</b></details>

<details>
<summary>Describe the architecture of Kubernetes</summary><br><b>
</b></details>

<details>
<summary>What is a worker?</summary><br><b>
</b></details>

<details>
<summary>Explain what is a Pod</summary><br><b>
</b></details>

<details>
<summary>True or False? A pod can manage multiple containers</summary><br><b>
</b></details>

<details>
<summary>How do you monitor your Kubernetes?</summary><br><b>
</b></details>

<details>
<summary>What is kubectl? How do you use it?</summary><br><b>
</b></details>

<details>
<summary>What is kubconfig? What do you use it for?</summary><br><b>
</b></details>

## Coding

<a name="coding-beginner"></a>
#### :baby: Beginner

<details>
<summary>What programming language do you prefer to use for DevOps related tasks? Why specifically this one?</summary><br><b>
</b></details>

<details>
<summary>What is Object Oriented Programming? Why is it important?</summary><br><b>
</b></details>

<details>
<summary>Explain recursion</summary<br><b>
</b></details>

<details>
<summary>Explain what are design patterns and describe three of them in detail</summary><br><b>
</b></details>

<details>
<summary>Explain big O notation</summary><br><b>
</b></details>

##### Common algorithms

<details>
<summary>Binary search:
  * How it works?
  * Can you implement it? (in any language you prefer)
  * What is the average performance of the algorithm you wrote?</summary><br><b>

It's a search algorithm used with sorted arrays/lists to find a target value by dividing the array each iteration and comparing the middle value to the target value. If the middle value is smaller than target value, then the target value is searched in the right part of the divided array, else in the left side. This continues until the value is found (or the array divided max times) 

[python implementation](coding/python/binary_search.py)

The average performance of the above algorithm is O(log n). Best performance can be O(1) and worst O(log n).
</b></details>

##### Code Review

<details>
<summary>What are your code-review best practices?</summary><br><b>
</b></details>

<details>
<summary>Do you agree/disagree with each of the following statements and why?:

  * The commit message is not important. When reviewing a change/patch one should focus on the actual change</summary><br><b>
  * You shouldn't test your code before submitting it. This is what CI/CD exists for.
</b></details>

##### Strings

<details>
<summary>In any language you want, write a function to determine if a given string is a palindrome</summary><br><b>
</b></details>

<details>
<summary>In any language you want, write a function to determine if two strings are Anagrams </summary><br><b>
</b></details>

##### Time Complexity

<details>
<summary>Describe what would be the time complexity of the operations <code>access</code>, <code>search</code> <code>insert</code> and <code>remove</code> for the following data structures:</summary><br><b>

  * Stack
  * Queue
  * Linked List
  * Binary Search Tree
</b></details>

<details>
<summary>What is the complexity for the best, worst and average cases of each of the following algorithms?:

  * Quick sort
  * Merge sort
  * Bucket Sort
  * Radix Sort</summary><br><b>
</b></details>

##### Data Structures & Types

<details>
<summary>Implement Stack in any language you would like</summary><br><b>
</b></details>

<details>
<summary>Implement Hash table in any language you would like</summary><br><b>
</b></details>

<a name="coding-advanced"></a>
#### :star: Advanced

<details>
<summary>Name 3 design patterns. Do you know how to implement (= provide an example) these design pattern in any language you'll choose?</summary><br><b>
</b></details>

<details>
<summary>Given an array/list of integers, find 3 integers which are adding up to 0 (in any language you would like)</summary><br><b>

```
def find_triplets_sum_to_zero(li):
    li = sorted(li)
    for i, val in enumerate(li):
        low, up = 0, len(li)-1
        while low < i < up:
            tmp = var + li[low] + li[up]
            if tmp > 0:
                up -= 1
            elif tmp < 0:
                low += 1
            else:
                yield li[low], val, li[up]
                low += 1
                up -= 1
```
</b></details>

## Python

<a name="python-beginner"></a>
#### :baby: Beginner

<details>
<summary>What are some characteristics of the Python programming language?</summary><br><b>

```
1. It is a high level general purpose programming language created in 1991 by Guido Van Rosum.
2. The language is interpreted, being the CPython (Written in C) the most used/maintained implementation.
3. It is strongly typed. The typing discipline is duck typing and gradual.
4. Python focuses on readability and makes use of whitespaces/identation instead of brackets { }
5. The python package manager is called PIP "pip installs packages", having more than 200.000 available packages.
6. Python comes with pip installed and a big standard library that offers the programmer many precooked solutions.
7. In python **Everything** is an object.

There are many other characteristics but these are the main ones that every python programmer should know.

```
</b></details>

<details>
<summary>What data types supported in Python and which of them are mutable? How can you show that a certain data type is mutable?</summary><br><b>

The mutable data types are:

    List
    Dictionary
    Set
    
The immutable data types are:

    Numbers (int, float, ...)
    String
    Bool
    Tuple
    Frozenset

You can usually use the function hash() to check an object mutability, if it is hashable it is immutable, although this does not always work as intended as user defined objects might be mutable and hashable
</b></details>

<details>
<summary>What is PEP8? Give an example of 3 style guidelines</summary><br><b>

PEP8 is a list of coding conventions and style guidelines for Python

5 style guidelines:

    1. Limit all lines to a maximum of 79 characters.
    2. Surround top-level function and class definitions with two blank lines.
    3. Use commas when making a tuple of one element
    4. Use spaces (and not tabs) for indentation
    5. Use 4 spaces per indentation level
</b></details>

<details>
<summary>Explain inheritance and how to use it in Python</summary><br><b>

```
By definition inheritance is the mechanism where an object acts as a base of another object, retaining all its
properties.

So if Class B inherits from Class A, every characteristics from class A will be also available in class B.
Class A would be the 'Base class' and B class would be the 'derived class'.

This comes handy when you have several classes that share the same functionalities.

The basic syntax is:

class Base: pass

class Derived(Base): pass

A more forged example:

class Animal:
    def __init__(self):
        print("and I'm alive!")

    def eat(self, food):
        print("ñom ñom ñom", food)

class Human(Animal):
    def __init__(self, name):
        print('My name is ', name)
        super().__init__()

    def write_poem(self):
        print('Foo bar bar foo foo bar!')

class Dog(Animal):
    def __init__(self, name):
        print('My name is', name)
        super().__init__()

    def bark(self):
        print('woof woof')


michael = Human('Michael')
michael.eat('Spam')
michael.write_poem()

bruno = Dog('Bruno')
bruno.eat('bone')
bruno.bark()

>>> My name is  Michael
>>> and I'm alive!
>>> ñom ñom ñom Spam
>>> Foo bar bar foo foo bar!
>>> My name is Bruno
>>> and I'm alive!
>>> ñom ñom ñom bone
>>> woof woof

Calling super() calls the Base method, thus, calling super().__init__() we called the Animal __init__.

There is a more advanced python feature called MetaClasses that aid the programmer to directly control class creation.

```

</b></details>

<details>
<summary> What is an error? What is an exception? What types of exceptions are you familiar with?</summary><br><b>

```

#  Note that you generally don't need to know the compiling process but knowing where everything comes from
#  and giving complete answers shows that you truly know what you are talking about.

Generally, every compiling process have a two steps.
    - Analysis
    - Code Generation.
    
    Analysis can be broken into:
        1. Lexical analysis   (Tokenizes source code)
        2. Syntactic analysis (Check whether the tokens are legal or not, tldr, if syntax is correct)
           
               for i in 'foo'
                          ^
             SyntaxError: invalid syntax
        
        We missed ':'
        
        
        3. Semantic analysis  (Contextual analysis, legal syntax can still trigger errors, did you try to divide by 0,
          hash a mutable object or use an undeclared function?)
          
                 1/0
                ZeroDivisionError: division by zero
        
    These three analysis steps are the responsible for error handlings.
    
    The second step would be responsible for errors, mostly syntax errors, the most common error.
    The third step would be responsible for Exceptions.
    
    As we have seen, Exceptions are semantic errors, there are many builtin Exceptions:
        
        ImportError
        ValueError
        KeyError
        FileNotFoundError
        IndentationError
        IndexError
        ...
    
    You can also have user defined Exceptions that have to inherit from the `Exception` class, directly or indirectly.

    Basic example:
        
    class DividedBy2Error(Exception):
        def __init__(self, message):
            self.message = message
    
    
    def division(dividend,divisor):
        if divisor == 2:
            raise DividedBy2Error('I dont want you to divide by 2!')
        return dividend / divisor
    
    division(100, 2)
    
    >>> __main__.DividedBy2Error: I dont want you to divide by 2!

```


</b></details>

<details>
<summary>Explain Exception Handling and how to use it in Python</summary><br><b>
</b></details>

<details>
<summary>What <code>//</code> is used for?</summary><br><b>
</b></details>

<details>
<summary>Write a program which will revert a string (e.g. pizza -> azzip)</summary><br><b>

```
Shortest way is str[::-1] but not the most efficient.

"Classic" way:

foo = ''

for char in 'pizza':
    foo = char + foo

>> 'azzip'   

```
</b></details>

<details>
<summary>How to extract the unique characters from a string? for example given the input "itssssssameeeemarioooooo" the output will be "mrtisaoe"</summary><br><b>

```
x = "itssssssameeeemarioooooo"
y = ''.join(set(x))
```
</b></details>

<details>
<summary>Write a function to return the sum of one or more numbers. The user will decide how many numbers to use</summary><br><b>

First you ask the user for the amount of numbers that will be use. Use a while loop that runs until amount_of_numbers becomes 0 through subtracting amount_of_numbers by one each loop. In the while loop you want ask the user for a number which will be added a variable each time the loop runs.

```
def return_sum():
	amount_of_numbers = int(input("How many numbers? "))
	total_sum = 0
	while amount_of_numbers != 0:
		num = int(input("Input a number. "))
		total_sum += num
		amount_of_numbers -= 1
	return total_sum

```
</b></details>

<details>
<summary>How to merge two sorted lists into one sorted list?</summary><br><b>
</b></details>

<details>
<summary>How to merge two dictionaries?</summary><br><b>
</b></details>

<details>
<summary>How do you swap values between two variables?</summary><br><b>

```
x, y = y, x
```

</b></details>

<details>
<summary>How to check if all the elements in a given lists are unique? so [1, 2, 3] is unique but [1, 1, 2, 3] is not unique because 1 exists twice</summary><br><b>
</b>

There are many ways of solving this problem:<br>
<code># Note: :list and -> bool are just python typings, they are not needed for the correct execution of the algorithm. </code>

Taking advantage of sets and len:

```
def is_unique(l:list) -> bool:
    return len(set(l)) == len(l)
```

This one is can be seen used in other programming languages.

```
def is_unique2(l:list) -> bool:
    seen = []

    for i in l:
        if i in seen:
            return False
        seen.append(i)
    return True
```

Here we just count and make sure every element is just repeated once.

```
def is_unique3(l:list) -> bool:
    for i in l:
        if l.count(i) > 1:
            return False
    return True
```

This one might look more convulated but hey, one liners.

```
def is_unique4(l:list) -> bool:
    return all(map(lambda x: l.count(x) < 2, l))
```

</details>

<details>
<summary>What _ is used for in Python?</summary><br><b>

1. Translation lookup in i18n
2. Hold the result of the last executed expression or statement in the interactive interpreter.
3. As a general purpose "throwaway" variable name. For example: x, y, _ = get_data() (x and y are used but since we don't care about third variable, we "threw it away").
</b></details>

<details>
<summary>How to check how much time it took to execute a certain script or block of code?</summary><br><b>
</b></details>

<details>
<summary>Find all the permutations of a given string</summary><br><b>
</b></details>

##### Common Algorithms Implementation

<details>
<summary>Can you implement "binary search" in Python?</summary><br><b>

[Solution](coding/python/binary_search.py)
</b></details>

##### Files

<details>
<summary>How to write to a file?</summary><br><b>

```
with open('file.txt', 'w') as file:
    file.write("My insightful comment")
```
</b></details>

<details>
<summary>How to reverse a file?</summary><br><b>
</b></details>

<details>
<summary>Sum all the integers in a given file</summary><br><b>
</b></details>

#### Regex

<details>
<summary>How do you perform regular expressions related operations in Python? (match patterns, substitute strings, etc.)</summary><br><b>

Using the re module
</b></details>

<details>
<summary>How to substitute the string "green" with "blue"?</summary><br><b>
</b></details>

<details>
<summary>How to find all the IP addresses in a variable? How to find them in a file?</summary><br><b>
</b></details>

<details>
<summary>Sort a list of lists by the second item of each nested list</summary><br><b>

```
li = [[1, 4], [2, 1], [3, 9], [4, 2], [4, 5]]

sorted(x, key=lambda l: l[1])
```
</b></details>

<details>
<summary>Can you write a function which will print all the file in a given directory? including sub-directories</summary><br><b>
</b></details>

<details>
<summary>You have the following list: <code>[{'name': 'Mario', 'food': ['mushrooms', 'goombas']}, {'name': 'Luigi', 'food': ['mushrooms', 'turtles']}]</code>
  Extract all type of foods. Final output should be: {'mushrooms', 'goombas', 'turtles'}</summary><br><b>

```
brothers_menu =  \
[{'name': 'Mario', 'food': ['mushrooms', 'goombas']}, {'name': 'Luigi', 'food': ['mushrooms', 'turtles']}]

# "Classic" Way
def get_food(brothers_menu) -> set:
    temp = []

    for brother in brothers_menu:
        for food in brother['food']:
            temp.append(food)

    return set(temp)

# One liner way (Using list comprehension)
set([food for bro in x for food in bro['food']])
```

</b></details>

<details>
<summary>What is List Comprehension? Is it better than a typical loop? Why? Can you demonstrate how to use it?</summary><br><b>
</b></details>

<details>
<summary>How to reverse a string?</summary><br><b>

Shortest way is: <code>my_string[::-1]</code> but it doesn't mean it's the most efficient one. <br>
Cassic way is:
```
def reverse_string(string):
    temp = ""
    for char in string:
        temp =  char + temp
    return temp
```
</b></details>

<details>
<summary>How to sort a dictionary by values?</summary><br><b>
</b></details>

<details>
<summary>How to sort a dictionary by keys?</summary><br><b>
</b></details>

<details>
<summary>Explain data serialization and how do you perform it with Python</summary><br><b>
</b></details>

<details>
<summary>How do you handle argument parsing in Python?</summary><br><b>
</b></details>

<details>
<summary>Explain what is GIL</summary><br><b>
</b></details>

<details>
<summary>What is an iterator?</summary><br><b>
</b></details>

<details>
<summary>What is a generator? Why using generators?</summary><br><b>
</b></details>

<details>
<summary>Explain the following types of methods and how to use them:

  * Static method
  * Class method
  * instance method</summary><br><b>
</b></details>

<details>
<summary>How to reverse a list?</summary><br><b>
</b></details>

<details>
<summary>How to combine list of strings into one string with spaces between the strings</summary><br><b>
</b></details>

<details>
<summary>Explain the following:
  * zip()
  * map()
  * filter()</summary><br><b>
</b></details>

<details>
<summary>How do you debug Python code?</summary><br><b>
</b></details>

<details>
<summary>What empty <code>return</code> returns?</summary><br><b>
</b>

Short answer is: It returns a None object.

We could go a bit deeper and explain the difference between 

```
def a ():
    return
    
>>> None
```

And

```
def a ():
    pass
    
>>> None
```
Or we could be asked this as a following question, since they both give the same result.

We could use the dis module to see what's going on:

```
  2           0 LOAD_CONST               0 (<code object a at 0x0000029C4D3C2DB0, file "<dis>", line 2>)
              2 LOAD_CONST               1 ('a')
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (a)

  5           8 LOAD_CONST               2 (<code object b at 0x0000029C4D3C2ED0, file "<dis>", line 5>)
             10 LOAD_CONST               3 ('b')
             12 MAKE_FUNCTION            0
             14 STORE_NAME               1 (b)
             16 LOAD_CONST               4 (None)
             18 RETURN_VALUE

Disassembly of <code object a at 0x0000029C4D3C2DB0, file "<dis>", line 2>:
  3           0 LOAD_CONST               0 (None)
              2 RETURN_VALUE

Disassembly of <code object b at 0x0000029C4D3C2ED0, file "<dis>", line 5>:
  6           0 LOAD_CONST               0 (None)
              2 RETURN_VALUE
```

An empty <code> return</code> is exactly the same as <code>return None</code> and functions without any explicit return
will always return None regardless of the operations, therefore 


```
def sum(a, b):
    global c
    c = a + b
    
>>> None
```

</details>

##### Data Structures & Types

<details>
<summary>Implement Stack in Python</summary><br><b>
</b></details>

<details>
<summary>Implement Hash table in Python</summary><br><b>
</b></details>

##### Tests

<details>
<summary>What is your experience with writing tests in Python?</summary><br><b>
</b></details>

<details>
<summary>Explain mocks</summary><br><b>
</b></details>

<a name="python-advanced"></a>
#### :star: Advanced

<details>
<summary>Explain what is a decorator</summary><br><b>
</b>
<b>In python, everything is an object, even functions themselves. Therefore you could pass functions as arguments
for another function eg;

```
def wee(word):
    return word

def oh(f):
    return f + "Ohh"
    
>>> oh(wee("Wee"))
<<< Wee Ohh
```

This allows us to control the before execution of any given function and if we added another function as wrapper,
(a function receiving another function that receives a function as parameter) we could also control the after execution.

Sometimes we want to control the before-after execution of many functions and it would get tedious to write

<code> f = function(function_1())</code>
<code> f = function(function_1(function_2(*args)))</code>

every time, that's what decorators do, they introduce syntax to write all of this on the go, using the keyword '@'.
</b>
</details>

<details>
<summary>Can you show how to write and use decorators?</summary><br><b>

<code>
These two decorators (ntimes and timer) are usually used to display decorators functionalities, you can find them in lots of
tutorials/reviews. I first saw these examples two years ago in pyData 2017. https://www.youtube.com/watch?v=7lmCu8wz8ro&t=3731s</code>

```
Simple decorator:

def deco(f):
    print(f"Hi I am the {f.__name__}() function!")
    return f

@deco
def hello_world():
    return "Hi, I'm in!"

a = hello_world()
print(a)

>>> Hi I am the hello_world() function!
    Hi, I'm in!
```

This is the simplest decorator version, it basically saves us from writting <code>a = deco(hello_world())</code>.
But at this point we can only control the before execution, let's take on the after:

```
def deco(f):
    def wrapper(*args, **kwargs):
        print("Rick Sanchez!")
        func = f(*args, **kwargs)
        print("I'm in!")
        return func
    return wrapper

@deco
def f(word):
    print(word)

a = f("************")
>>> Rick Sanchez!
    ************
    I'm in!
```

deco receives a function -> f
wrapper receives the arguments -> *args, **kwargs

wrapper returns the function plus the arguments -> f(*args, **kwargs)
deco returns wrapper.

As you can see we conveniently do things before and after the execution of a given function.

For example, we could write a decorator that calculates the execution time of a function.

```
import time
def deco(f):
    def wrapper(*args, **kwargs):
        before = time.time()
        func = f(*args, **kwargs)
        after = time.time()
        print(after-before)
        return func
    return wrapper

@deco
def f():
    time.sleep(2)
    print("************")

a = f()
>>> 2.0008859634399414
```

Or create a decorator that executes a function n times.

```
def n_times(n):
    def wrapper(f):
        def inner(*args, **kwargs):
            for _ in range(n):
                func = f(*args, **kwargs)
            return func
        return inner
    return wrapper

@n_times(4)
def f():
    print("************")

a = f()

>>>************
   ************
   ************
   ************
```

</b></details>
<details>
<summary>Write a script which will determine if a given host is accessible on a given port</summary><br><b>
</b></details>

<details>
<summary>Are you familiar with Dataclasses? Can you explain what are they used for?</summary><br><b>
</b></details>

<details>
<summary>You wrote a class to represent a car. How would you compare two cars instances if two cars are equal if they have the same model and color?</summary><br><b>
</b></details>

<details>
<summary>Explain Context Manager</summary><br><b>
</b></details>

<details>
<summary>Explain the Buffer Protocol</summary><br><b>
</b></details>

<details>
<summary>Explain Descriptors</summary><br><b>
</b></details>

<details>
<summary>Do you have experience with web scraping? Can you describe what have you used and for what?</summary><br><b>
</b></details>

<details>
<summary>Can you implement Linked List in Python?<br><b>
</b></details>

<details>
<summary>Can you implement Linux's <code>tail</code> command in Python? Bonus: implement <code>head</code> as well</summary><br><b>
</b></details>

<details>
<summary>You have created a web page where a user can upload a document. But the function which reads the uploaded files, runs for a long time, based on the document size and user has to wait for the read operation to complete before he/she can continue using the web site. How can you overcome this?</summary><br><b>
</b></details>

## Monitoring

<a name="monitoring-beginner"></a>
#### :baby: Beginner

<details>
<summary>Explain monitoring. What is it? What its goal?</summary><br><b>
</b></details>

<details>
<summary>What is wrong with the old approach of watching for a specific value and trigger an email/phone alert while value is exceeded?</summary><br><b>

This approach require from a human to always check why the value exceeded and how to handle it while today, it is more effective to notify people only when they need to take an actual action.
If the issue doesn't require any human intervention, then the problem can be fixed by some processes running in the relevant environment.
</b></details>

<details>
<summary>What types of monitoring outputs are you familiar with and/or used in the past?</summary><br><b>

Alerts
Tickets
Logging
</b></details>

<details>
<summary>What is the different between infrastructure monitoring and application monitoring? (methods, tools, ...)</summary><br><b>
</b></details>

## Prometheus

<a name="prometheus-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is Prometheus? What are some of Prometheus's main features?</summary><br><b>
</b></details>

<details>
<summary>Describe Prometheus architecture and components</summary><br><b>
</b></details>

<details>
<summary>Can you compare Prometheus to other solutions like InfluxDB for example?</summary><br><b>
</b></details>

<details>
<summary>What is an Alert?</summary><br><b>
</b></details>

<details>
<summary>Describe the following Prometheus components:

  * Prometheus server
  * Push Gateway
  * Alert Manager</summary><br><b>

Prometheus server responsible for scraping the storing the data<br>
Push gateway is used for short-lived jobs<br>
Alert manager is responsible for alerts ;)
</b></details>

<details>
<summary>What is an Instance? What is a Job?</summary><br><b>
</b></details>

<details>
<summary>What core metrics types Prometheus supports?</summary><br><b>
</b></details>

<details>
<summary>What is an exporter? What is it used for?</summary><br><b>
</b></details>

<details>
<summary>Which Prometheus best practices are you familiar with?. Name at least three</summary><br><b>
</b></details>

<details>
<summary>How to get total requests in a given period of time?</summary><br><b>
</b></details>

<a name="prometheus-advanced"></a>
#### :star: Advanced

<details>
<summary>How do you join two metrics?</summary><br><b>
</b></details>

<details>
<summary>How to write a query that returns the value of a label?</summary><br><b>
</b></details>

<details>
<summary>How do you convert cpu_user_seconds to cpu usage in percentage?</summary><br><b>
</b></details>

## Git

<a name="git-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is the difference between <code>git pull</code> and <code>git fetch</code>?</summary><br><b>

Shortly, git pull = git fetch + git merge

When you run git pull, it gets all the changes from the remote or central
repository and attaches it to your corresponding branch in your local repository.

git fetch gets all the changes from the remote repository, stores the changes in
a separate branch in your local repository
</b></details>

<details>
<summary>Explain the following: <code>git directory</code>, <code>working directory</code> and <code>staging area</code></summary><br><b>

The Git directory is where Git stores the meta data and object database for your project. This is the most important part of Git, and it is what is copied when you clone a repository from another computer.

The working directory is a single checkout of one version of the project. These files are pulled out of the compressed database in the Git directory and placed on disk for you to use or modify.

The staging area is a simple file, generally contained in your Git directory, that stores information about what will go into your next commit. It’s sometimes referred to as the index, but it’s becoming standard to refer to it as the staging area.

This answer taken from [git-scm.com](https://git-scm.com/book/en/v1/Getting-Started-Git-Basics#_the_three_states)
</b></details>

<details>
<summary>How to resolve git merge conflicts?</summary><br><b>

<p>
First, you open the files which are in conflict and identify what are the conflicts.
Next, based on what is accepted in your company or team, you either discuss with your
colleagues on the conflicts or resolve them by yourself
After resolving the conflicts, you add the files with `git add <file_name>`
Finally, you run `git rebase --continue`
</p>
</b></details>

<details>
<summary>What is the difference between <code>git reset</code> and <code>git revert</code>?</summary><br><b>

<p>

`git revert` creates a new commit which undoes the changes from last commit.

`git reset` depends on the usage, can modify the index or change the commit which the branch head
is currently pointing at.
</p>
</b></details>

<details>
<summary>You would like to move forth commit to the top. How would you achieve that?</summary><br><b>

Using <code>git rebase></code> command
</b></details>

<details>
<summary>In what situations are you using <code>git rebase</code>?</summary><br><b>
</b></details>

<details>
<summary>What merge strategies are you familiar with?</summary><br><b>

Mentioning two or three should be enough and it's probably good to mention that 'recursive' is the default one.

recursive
resolve
ours
theirs

This page explains it the best: https://git-scm.com/docs/merge-strategies
</b></details>

<details>
<summary>How can you see which changes have done before committing them?</summary><br><b>

<code>git diff</code>
</b></details>

<details>
<summary>How do you revert a specific file to previous commit?</summary><br><b>

```
git checkout HEAD~1 -- /path/of/the/file
```
</b></details>

<details>
<summary>What is the <code>.git</code> directory? What can you find there?</summary><br><b>
</b></details>

<details>
<summary>What are some Git anti-patterns? Things that you shouldn't do</summary><br><b>

  * Not waiting to long between commits
  * Not removing the .git directory :)
</b></details>

<a name="git-advanced"></a>
#### :star: Advanced

<details>
<summary>Explain Git octopus merge</summary><br><b>

Probably good to mention that it's:

  * It's good for cases of merging more than one branch (and also the default of such use cases)
  * It's primarily meant for bundling topic branches together 

This is a great article about Octopus merge: http://www.freblogg.com/2016/12/git-octopus-merge.html
</b></details>

## Go

<a name="go-beginner"></a>
#### :baby: Beginner

<details>
<summary>What are some characteristics of the Go programming language?</summary><br><b>

  * Strong and static typing - the type of the variables can't be changed over time and they have to be defined at compile time
  * Simplicity 
  * Fast compile times
  * Built-in concurrency
  * Garbage collected
  * Platform independent
  * Compile to standalone binary - anything you need to run your app will be compiled into one binary. Very useful for version management in run-time. 

Go also has good community.
</b></details>

<details>
<summary>What is the difference between <code>var x int = 2</code> and <code>x := 2</code>?</summary><br><b>

The result is the same, a variable with the value 2.

With <code>var x int = 2</code> we are setting the variable type to integer while with <code>x := 2</code> we are letting Go figure out by itself the type.
</b></details>

<details>
<summary>True or False? In Go we can redeclare variables and once declared we must use it.</summary>

False. We can't redeclare variables but yes, we must used declared variables.
</b></details>

<details>
<summary>What libraries of Go have you used?</summary><br><b>

This should be answered based on your usage but some examples are:

  * fmt - formatted I/O
</b></details>

<details>
<summary>What is the problem with the following block of code? How to fix it?

```
func main() {
    var x float32 = 13.5
    var y int
    y = x
}
```
</summary><br><b>
</b></details>

<details>
<summary>The following block of code tries to convert the integer 101 to a string but instead we get "e". Why is that? How to fix it?

```
package main

import "fmt"

func main() {
    var x int = 101
    var y string
    y = string(x)
    fmt.Println(y)
}
```
</summary><br><b>

It looks what unicode value is set at 101 and uses it for converting the integer to a string.
If you want to get "101" you should use the package "strconv" and replace <code>y = string(x)</code> with <code>y = strconv.Itoa(x)</code>
</b></details>

<details>
<summary>What is wrong with the following code?:

```
package main

func main() {
    var x = 2
    var y = 3
    const someConst = x + y
}
```
</summary><br><b>
</b></details>

<details>
<summary>What will be the output of the following block of code?:

```
package main

import "fmt"

const (
	x = iota
	y = iota
)
const z = iota

func main() {
	fmt.Printf("%v\n", x)
	fmt.Printf("%v\n", y)
	fmt.Printf("%v\n", z)
}
```
</summary><br><b>
</b></details>

<details>
<summary>What _ is used for in Go?</summary><br><b>
</b></details>

<details>
<summary>What will be the output of the following block of code?:

```
package main

import "fmt"

const (
	_ = iota + 3
	x
)

func main() {
	fmt.Printf("%v\n", x)
}
```
</summary><br><b>
</b></details>

## Mongo

<a name="mongo-beginner"></a>
#### :baby: Beginner

<details>
<summary>What are the advantages of MongoDB? Or in other words, why choosing MongoDB and not other implementation of NoSQL?</summary><br><b>
</b></details>

<details>
<summary>What is the difference between SQL and NoSQL?</summary><br><b>

The main difference is that SQL databases are structured (data is stored in the form of
tables with rows and columns - like an excel spreadsheet table) while NoSQL is 
unstructured, and the data storage can vary depending on how the NoSQL DB is set up, such
as key-value pair, document-oriented, etc.
</b></details>

<details>
<summary>In what scenarios would you prefer to use NoSQL/Mongo over SQL?</summary><br><b>

  * Heterogeneous data which changes often
  * Data consistency and integrity is not top priority
  * Best if the database needs to scale rapidly
</b></details>

<details>
<summary>What is a document? What is a collection?</summary><br><b>
</b></details>

<details>
<summary>What is an aggregator?</summary><br><b>
</b></details>

<details>
<summary>What is better?. Embedded documents or referenced?</summary><br><b>
</b></details>

##### Queries

<details>
<summary>Explain this query: <code>db.books.find({"name": /abc/})</code></summary><br><b>
</b></details>

<details>
<summary>Explain this query: <code>db.books.find().sort({x:1})</code></summary><br><b>
</b></details>

## OpenShift

<a name="openshift-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is OpenShift? Did you use it? If yes, how?</summary><br><b>
</b></details>

<details>
<summary>Can you explain the difference between OpenShift and Kubernetes?</summary><br><b>
</b></details>

<details>
<summary>Define Pods and explain what are stateful pods</summary><br><b>
</b></details>

<details>
<summary>What types of build strategies are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>Explain what are labels and what they are used for</summary><br><b>
</b></details>

<details>
<summary>Explain what are annotations and how they are different from labels</summary><br><b>
</b></details>

<details>
<summary>Explain what is Downward API</summary><br><b>
</b></details>

## Shell Scripting

<a name="shell-scripting-beginner"></a>
#### :baby: Beginner

<details>
<summary>Tell me about your experience with shell scripting</summary><br><b>
</b></details>

<details>
<summary>What this line in scripts mean?: <code>#!/bin/bash</code></summary><br><b>
</b></details>

<details>
<summary>What do you tend to include in every script you write?</summary><br><b>

Few example:

  * Comments on how to run it and/or what it does
  * Adding "set -e" since I want the script to exit if a certain command failed 

You can have an entirely different answer. It's based only on your experience.
</b></details>

<details>
<summary>True or False?: when a certain command/line fails, the script, by default, will exit and will no keep running</summary><br><b>

Depends on the language and settings used.
When a script written in Bash fails to run a certain command it will keep running and will execute all other commands mentioned after the command which failed.
Most of the time we would actually want the opposite to happen. In order to make Bash exist when a specific command fails, use 'set -e' in your script.
</b></details>

<details>
<summary>Today we have tools and technologies like Ansible. Why would someone still use shell scripting?</summary><br><b>

  * Speed
  * The module we need doesn't exist
  * We are delivering the scripts to customers who don't have access to the public network and don't necessarily have Ansible installed on their systems.
</b></details>

<details>
<summary>Explain what would be the result of each command:

  * <code>echo $0</code>
  * <code>echo $?</code>
  * <code>echo $$</code>
  * <code>echo $@</code>
  * <code>echo $#</code></summary><br><b>
</b></details>

<details>
<summary>How do you debug shell scripts?</summary><br><b>

Answer depends on the language you are using for writing your scripts. If Bash is used for example then:

  * Adding -x to the script I'm running in Bash
  * Old good way of adding echo statements

If Python, then using pdb is very useful.
</b></details>

<details>
<summary>How do you get input from the user in shell scripts?</summary><br><b>

Using the keyword <code>read</code> so for example <code>read x</code> will wait for user input and will store it in the variable x.
</b></details>

<details>
<summary>Explain conditionals and how do you use them</summary><br><b>
</b></details>

<details>
<summary>What is a loop? What types of loops are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>Explain <code>continue</code> and <code>break</code>. When do you use them if at all?</summary><br><b>
</b></details>

<details>
<summary>How to store the output of a command in a variable?</summary><br><b>
</b></details>

<details>
<summary>How do you check variable length?</summary><br><b>
</b></details>

<details>
<summary>What is the difference between single and double quotes?</summary><br><b>
</b></details>

<details>
<summary>Write a script which will list the differences between two directories</summary><br><b>
</b></details>

<a name="shell-scripting-advanced"></a>
#### Advanced

<details>
<summary>Explain the following code:

<code>:(){ :|:& };:</code>

</summary><br><b>
</b></details>

<details>
<summary>Can you give an example to some Bash best practices?</summary><br><b>
</b></details>

<details>
<summary>What is the ternary operator? How do you use it in bash?</summary><br><b>

A short way of using if/else. An example:

[[ $a = 1 ]] && b="yes, equal" || b="nope"
</b></details>

<details>
<summary>What does the following code do and when would you use it?
	
<code>diff <(ls /tmp) <(ls /var/tmp)</code>

</summary><br>
It is called 'process substitution'. It provides a way to pass the output of a command to another command when using a pipe <code>|</code> is not possible. It can be used when a command does not support <code>STDIN</code> or you need the output of multiple commands. 
https://superuser.com/a/1060002/167769
</details>


## SQL

<a name="sql-beginner"></a>
#### :baby: Beginner

<details>
<summary>What does SQL stand for?</summary><br><b>

Structured Query Language

</b></details>

<details>
<summary>How is SQL Different from NoSQL</summary><br><b>

The main difference is that SQL databases are structured (data is stored in the form of
tables with rows and columns - like an excel spreadsheet table) while NoSQL is 
unstructured, and the data storage can vary depending on how the NoSQL DB is set up, such
as key-value pair, document-oriented, etc.
</b></details>

<details>
<summary>What does it mean when a database is ACID compliant?</summary><br>

ACID stands for Atomicity, Consistency, Isolation, Durability. In order to be ACID compliant, the database much meet each of the four criteria

**Atomicity** - When a change occurs to the database, it should either succeed or fail as a whole. 

For example, if you were to update a table, the update should completely execute. If it only partially executes, the 
update is considered failed as a whole, and will not go through - the DB will revert back to it's original
state before the update occurred. It should also be mentioned that Atomicity ensures that each 
transaction is completed as it's own stand alone "unit" - if any part fails, the whole statement fails.

**Consistency** - any change made to the database should bring it from one valid state into the next.

For example, if you make a change to the DB, it shouldn't corrupt it. Consistency is upheld by checks and constraints that
are pre-defined in the DB. For example, if you tried to change a value from a string to an int when the column
should be of datatype string, a consistent DB would not allow this transaction to go through, and the action would
not be executed

**Isolation** - this ensures that a database will never be seen "mid-update" - as multiple transactions are running at
the same time, it should still leave the DB in the same state as if the transactions were being run sequentially.

For example, let's say that 20 other people were making changes to the database at the same time. At the
time you executed your query, 15 of the 20 changes had gone through, but 5 were still in progress. You should
only see the 15 changes that had completed - you wouldn't see the database mid-update as the change goes through.

**Durability** - Once a change is committed, it will remain committed regardless of what happens
(power failure, system crash, etc.). This means that all completed transactions 
must be recorded in non-volatile memory. 

Note that SQL is by nature ACID compliant. Certain NoSQL DB's can be ACID compliant depending on 
how they operate, but as a general rule of thumb, NoSQL DB's are not considered ACID compliant
</details>

<details>
<summary>When is it best to use SQL? NoSQL?</summary><br><b>

SQL - Best used when data integrity is crucial. SQL is typically implemented with many
businesses and areas within the finance field due to it's ACID compliance.

NoSQL - Great if you need to scale things quickly. NoSQL was designed with web applications 
in mind, so it works great if you need to quickly spread the same information around to 
multiple servers

Additionally, since NoSQL does not adhere to the strict table with columns and rows structure
that Relational Databases require, you can store different data types together.
</b></details>

<details>
<summary>What is a Cartesian Product?</summary><br>

A Cartesian product is when all rows from the first table are joined to all rows in the second
table. This can be done implicitly by not defining a key to join, or explicitly by 
calling a CROSS JOIN on two tables, such as below:

Select * from customers **CROSS JOIN** orders;

Note that a Cartesian product can also be a bad thing - when performing a join
on two tables in which both do not have unique keys, this could cause the returned information
to be incorrect. 
</details>

##### SQL Specific Questions

For these questions, we will be using the Customers and Orders tables shown below:

**Customers**

Customer_ID | Customer_Name | Items_in_cart | Cash_spent_to_Date
------------ | ------------- | ------------- | -------------
100204 | John Smith | 0 | 20.00
100205 | Jane Smith | 3 | 40.00
100206 | Bobby Frank | 1 | 100.20

**ORDERS**

Customer_ID | Order_ID | Item | Price | Date_sold
------------ | ------------- | ------------- | ------------- | -------------
100206 | A123 | Rubber Ducky | 2.20 | 2019-09-18
100206 | A123 | Bubble Bath | 8.00 | 2019-09-18
100206 | Q987 | 80-Pack TP | 90.00 | 2019-09-20
100205 | Z001 | Cat Food - Tuna Fish | 10.00 | 2019-08-05
100205 | Z001 | Cat Food - Chicken | 10.00 | 2019-08-05
100205 | Z001 | Cat Food - Beef | 10.00 | 2019-08-05
100205 | Z001 | Cat Food - Kitty quesadilla | 10.00 | 2019-08-05
100204 | X202 | Coffee | 20.00 | 2019-04-29

<details>
<summary>How would I select all fields from this table?</summary><br><b>

Select * <br>
From Customers;
</b></details>

<details>
<summary>How many items are in John's cart?</summary><br><b>

Select Items_in_cart <br>
From Customers <br>
Where Customer_Name = "John Smith";
</b></details>

<details>
<summary>What is the sum of all the cash spent across all customers?</summary><br><b>

Select SUM(Cash_spent_to_Date) as SUM_CASH <br>
From Customers;
</b></details>

<details>
<summary>How many people have items in their cart?</summary><br><b>

Select count(1) as Number_of_People_w_items <br>
From Customers <br>
where Items_in_cart > 0;
</b></details>

<details>
<summary>How would you join the customer table to the order table?</summary><br><b>

You would join them on the unique key. In this case, the unique key is Customer_ID in
both the Customers table and Orders table
</b></details>

<details>
<summary>How would you show which customer ordered which items?</summary><br><b>

Select c.Customer_Name, o.Item <br>
From Customers c <br>
Left Join Orders o <br>
  On c.Customer_ID = o.Customer_ID;

</b></details>

<a name="sql-advanced"></a>
#### Advanced

<details>
<summary>Using a with statement, how would you show who ordered cat food, and the total amount of money spent?</summary><br><b>

with cat_food as ( <br>
Select Customer_ID, SUM(Price) as TOTAL_PRICE <br>
From Orders <br>
Where Item like "%Cat Food%" <br>
Group by Customer_ID <br>
) <br>
Select Customer_name, TOTAL_PRICE <br>
From Customers c <br>
Inner JOIN cat_food f <br>
  ON c.Customer_ID = f.Customer_ID <br>
where c.Customer_ID in (Select Customer_ID from cat_food);

Although this was a simple statement, the "with" clause really shines when 
a complex query needs to be run on a table before joining to another. With statements are nice, 
because you create a pseudo temp when running your query, instead of creating a whole new table.

The Sum of all the purchases of cat food weren't readily available, so we used a with statement to create
the pseudo table to retrieve the sum of the prices spent by each customer, then join the table normally.
</b></details>

## Azure

<a name="azure-beginner"></a>
#### :baby: Beginner

<details>
<summary>Explain Azure's architecture</summary><br><b>
</b></details>

<details>
<summary>Explain availability sets and availability zones</summary><br><b>
</b></details>

<details>
<summary>What is the Azure Resource Manager? Can you describe the format for ARM templates?</summary><br><b>
</b></details>

<details>
<summary>Explain Azure managed disks</summary><br><b>
</b></details>

## GCP

<a name="gcp-beginner"></a>
#### :baby: Beginner

<details>
<summary>Explain GCP's architecture</summary><br><b>
</b></details>

<details>
<summary>What are the main components and services of GCP?</summary><br><b>
</b></details>

<details>
<summary>What GCP management tools are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>Tell me what do you know about GCP networking</summary><br><b>
</b></details>

## OpenStack

<a name="openstack-beginner"></a>
#### :baby: Beginner

<details>
<summary>Tell me about your experience with OpenStack. What do you think are the advantages and disadvantages of OpenStack?</summary><br><b>
</b></details>

<details>
<summary>What components/projects of OpenStack are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>Can you tell me what each of the following components/projects is responsible for?:

  * Nova
  * Neutron
  * Cinder
  * Glance
  * Keystone</summary><br><b>
</b></details>

<details>
<summmary>Describe in detail how you bring up an instance with an IP you can reach from outside the cloud</summary><br><b>
</b></details>

<details>
<summary>You get a call from a customer saying: "I can ping my instance but can't connect (ssh) it". What might be the problem?</summary><br><b>
</b></details>

<details>
<summary>What types of networks OpenStack supports?</summary><br><b>
</b></details>

<details>
<summary>How do you debug OpenStack storage issues? (tools, logs, ...)</summary><br><b>
</b></details>

<details>
<summary>How do you debug OpenStack compute issues? (tools, logs, ...)</summary><br><b>
</b></details>

<details>
<summary>Are you familiar with TripleO? What benefits it has?</summary><br><b>
</b></details>

##### Networking

<details>
<summary>What is a provider network?</summary><br><b>
</b></details>

<details>
<summary>What components and services exist for L2 and L3?</summary><br><b>
</b></details>

<details>
<summary>What is the ML2 plug-in? Explain its architecture</summary><br><b>
</b></details>

<details>
<summary>What is the L2 agent? How it works and what is it responsible for?</summary><br><b>
</b></details>

<details>
<summary>What is the L3 agent? How it works and what is it responsible for?</summary><br><b>
</b></details>

<details>
<summary>Explain what the Metadata agent is responsible for</summary><br><b>
</b></details>

<details>
<summary>What networking entities Neutron supports?</summary><br><b>
</b></details>

<details>
<summary>How do you debug OpenStack networking issues? (tools, logs, ...)</summary><br><b>
</b></details>

<a name="openstack-advanced"></a>
#### :baby: Advanced

##### Networking

<details>
<summary>Explain BGP dynamic routing</summary>
</b></details>

<details>
<summary>What is the role of network namespaces in OpenStack?</summary>
</b></details>


## Security

<a name="security-beginner"></a>
#### :baby: Beginner

<details>
<summary>Can you describe the DevSecOps core principals?</summary><br><b>
</b></details>

<details>
<summary>What DevOps security best practices are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>What security techniques are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>How do you manage passwords in different tools and platforms?</summary><br><b>
</b></details>

<details>
<summary>Explain the following:

  * Vulnerability
  * Exploits
  * Risk
  * Threat</summary><br><b>
</b></details>

<details>
<summary>What is XSS?</summary><br><b>
</b></details>

<details>
<summary>What is an SQL injection? How to manage it?</summary><br><b>
</b></details>

<details>
<summary>What is Certification Authority?</summary><br><b>
</b></details>

<details>
<summary>How do you identify and manage vulnerabilities?</summary><br><b>
</b></details>

<details>
<summary>Explain "Privilege Restriction"</summary><br><b>
</b></details>

<details>
<summary>How HTTPS is different from HTTP?</summary><br><b>
</b></details>

<details>
<summary>What types of firewalls are there?</summary><br><b>
</b></details>

<details>
<summary>What is DDoS attack? How do you deal with it?</summary><br><b>
</b></details>

<details>
<summary>What is the difference between asynchronous and synchronous encryption?</summary><br><b>
</b></details>

<details>
<summary>Explain Man-in-the-middle attack</summary><br><b>
</b></details>

<details>
<summary>Explain CVE and CVSS</summary><br><b>
</b></details>

<details>
<summary>What is ARP Poisoning?</summary><br><b>
</b></details>

<details>
<summary>Describe how do you secure public repositories</summary>
</b></details>

<details>
<summary>How do cookies work?</summary><br><b>
</b></details>

<details>
<summary>What is DNS Spoofing? How to prevent it?</summary><br><b>
</b></details>

<details>
<summary>Explain OAuth</summary><br><b>
<a name="puppet-advanced"></a>
</b></details>

<details>
<summary>Explain "Format String Vulnerability"</summary><br><b>
</b></details>

<details>
<summary>Explain "Buffer Overflow"</summary><br><b>
</b></details>

<details>
<summary>Explain DMZ</summary><br><b>
</b></details>

<details>
<summary>Explain TLS</summary><br><b>
</b></details>

<details>
<summary>What is CSRF? How to handle CSRF?</summary><br><b>
</b></details>

<details>
<summary>Explain HTTP Header Injection vulnerability</summary><br><b>
</b></details>

<details>
<summary>What security sources are you using to keep updated on latest news?</summary><br><b>
</b></details>

<details>
<summary>What TCP and UDP vulnerabilities are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>Do using VLANs contribute to network security?</summary><br><b>
</b></details>

<details>
<summary>What are some examples of security architecture requirements?</summary><br><b>
</b></details>

##### Containers

<details>
<summary>What security measures are you taking when dealing with containers?</summary><br><b>
</b></details>

<details>
<summary>Explain what is Docker Bench</summary><br><b>
</b></details>

<a name="security-advanced"></a>
#### :baby: Advanced

<details>
<summary>Explain MAC flooding attack</summary><br><b>
</b></details>

<details>
<summary>What is "Diffie-Hellman key exchange" and how does it work?</summary><br><b>
</b></details>

<details>
<summary>Explain "Forward Secrecy"</summary><br><b>
</b></details>

## Puppet

<a name="puppet-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is Puppet? How it works?</summary><br><b>
</b></details>

<details>
<summary>Explain Puppet architecture</summary><br><b>
</b></details>

<details>
<summary>Can you compare Puppet to other configuration management tools? Why did you chose to use Puppet?</summary><br><b>
</b></details>

<details>
<summary>Explain the following:

  * Module
  * Manifest
  * Node</summary><br><b>
</b></details>

<details>
<summary>Explain Facter</summary><br><b>
</b></details>

<details>
<summary>What is MCollective?</summary><br><b>
</b></details>

<a name="puppet-advanced"></a>
#### :baby: Advanced

<details>
<summary>Do you have experience with writing modules? Which module have you created and for what?</summary><br><b>
</b></details>

<details>
<summary>Explain what is Hiera</summary><br><b>
</b></details>

## Elastic

<a name="elastic-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is the Elastic Stack?</summary><br><b>

The Elastic Stack consists of:

  * Elasticsearch
  * Elastic Hadoop
  * Kibana
  * Logstash
  * Beats
  * APM Server

The most used projects are the Elasticserach, Logstash and Kibana. Also known as the ELK stack.
</b></details>

<details>
<summary>Describe what happens from the moment the app logged some information until it's displayed to the user in the dashboard when the Elastic stack is used</summary><br><b>  

1. The data logged by the application is sent to Elasticsearch
2. Elasticsearch stores the document it got and the document is indexed for quick future access
3. Logstash processes the data
4. The user creates visualizations which uses the index in elasticsearch and more specifically the data there (this is done in Kibana).
5. The user creates a dashboard which composed out of the visualization created earlier
</b></details>

##### Elasticsearch

<details>
<summary>Explain what is Elasticsearch</summary><br><b>

From the official [docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/documents-indices.html):

"Elasticsearch is a distributed document store. Instead of storing information as rows of columnar data, Elasticsearch stores complex data structures that have been serialized as JSON documents"
</b></details>

<details>
<summary>What is an Index?</summary><br><b>

Index in Elastic is in most cases compared to a whole database from the SQL/NoSQL world.<br>
You can choose to have one index to hold all the data of your app or have multiple indices where each index holds different type of your app (e.g. index for each service your app is running).

The official docs also offer a great explanation (in general, it's really good documentation, as every project should have):

"An index can be thought of as an optimized collection of documents and each document is a collection of fields, which are the key-value pairs that contain your data"
</b></details>

<details>
<summary>What is an Inverted Index?</summary><br><b>

From the official docs:

"An inverted index lists every unique word that appears in any document and identifies all of the documents each word occurs in."
</b></details>

<details>
<summary>What is a Document?</summary><br><b>

Continuing with the comparison to SQL/NoSQL a Document in Elastic is a row in table in the case of SQL or a document in a collection in the case of NoSQL.
As in NoSQL a Document is a JSON object which holds data on a unit in your app. What is this unit depends on the your app. If your app related to book then each document describes a book. If you are app is about shirts then each document is a shirt.
</b></details>

<details>
<summary>True or False? Elasticsearch indexes all data in every field and each indexed field has the same data structure for unified and quick query ability</summary><br><b>

False.

From the official docs:

"Each indexed field has a dedicated, optimized data structure. For example, text fields are stored in inverted indices, and numeric and geo fields are stored in BKD trees."
</b></details>

<details>
<summary>What reserved fields a document has?</summary><br><b>

  * _index
  * _id
  * _type
</b></details>

<details>
<summary>Explain Mapping</summary><br><b>
</b></details>

<details>
<summary>What are the advantages of defining your own mapping? (or: when would you use your own mapping?)</summary><br><b>

* You can optimize fields for partial matching
* You can define custom formats of known fields (e.g. date)
* You can perform language-specific analysis
</b></details>

<details>
<summary>Explain Shards</summary><br><b>
</b></details>

<details>
<summary>Explain Replicas</summary><br><b>
</b></details>

##### Query DSL

<details>
<summary>Explain Elasticsearch query syntax (Booleans, Fields, Ranges)</summary><br><b>
</b></details>

<details>
<summary>Explain what is Relevance Score</summary><br><b>
</b></details>

<details>
<summary>Explain Query Context and Filter Context</summary><br><b>

From the official docs:

"In the query context, a query clause answers the question “How well does this document match this query clause?” Besides deciding whether or not the document matches, the query clause also calculates a relevance score in the _score meta-field."

"In a filter context, a query clause answers the question “Does this document match this query clause?” The answer is a simple Yes or No — no scores are calculated. Filter context is mostly used for filtering structured data"
</b></details>

##### Logstash

<details>
<summary>What are Logstash plugins? What plugins types are there?</summary><br><b>

  * Input Plugins - how to collect data from different sources
  * Filter Plugins - processing data
  * Output Plugins - push data to different outputs/services/platforms
</b></details>

<details>
<summary>What are Logstash Codecs?</summary><br><b>
</b></details>

##### Kibana

<details>
<summary>What is Kibana?</summary><br><b>

From the official docs:

"Kibana is an open source analytics and visualization platform designed to work with Elasticsearch. You use Kibana to search, view, and interact with data stored in Elasticsearch indices. You can easily perform advanced data analysis and visualize your data in a variety of charts, tables, and maps."
</b></details>

<details>
<summary>What visualization types are supported/included in Kibana?</summary><br><b>
</b></details>

<details>
<summary>What visualization type would you use for statistical outliers</summary><br><b>
</b></details>

<details>
<summary>Describe in detail how do you create a dashboard in Kibana</summary><br><b>
</b></details>

##### Beats

<details>
<summary>What is Filebeat?</summary><br><b>
</b></details>

<a name="elastic-advanced"></a>
#### :star: Advnaced

<details>
<summary>Describe how would an architecture of production environment with large amounts of data would be different from a small-scale environment</summary><br><b>

There are several possible answers for this question. One of them is as follows:

A small-scale architecture of elastic will consist of the elastic stack as it is. This means we will have beats, logstash, elastcsearch and kibana.<br>
A production environment with large amounts of data can include some kind of buffering component (e.g. Reddis or RabbitMQ) and also security component such as Nginx.
</b></details>

## DNS

<a name="dns-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is DNS? What is it used for?</summary><br><b>

DNS (Domain Name Systems) is a protocol used for converting domain names into IP addresses.<br>
As you know computer networking is done with IP addresses (layer 3 of the OSI model) but for as humans it's hard to remember IP addresses, it's much easier to remember names. This why we need something such as DNS to convert any domain name we type into an IP address. You can think on DNS as a huge phonebook or database where each corresponding name has an IP.
</b></details>

<details>
<summary>How DNS works?</summary><br><b>

In general the process is as follows:

  * The user types an address in the web browser (some_site.com)
  * The operating system gets a request from the browser to translate the address the user entered
  * A query created to check a local entry of the address exists in the system. In case it doesn't, the request is forwarded to the DNS resolver
  * The Resolver is a server, usually configured by your ISP when you connect to the internet, that responsible for resolving your query by contacting other DNS servers
  * The Resolver contacts the root nameserver (aka as .)
  * The root nameserver responds with the address of the relevant Top Level Domain DNS server (if your address ends with org then the org TLD)
  * The Resolver then contacts the TLD DNS and TLD DNS responds with the IP address that matches the address the user typed in the browser
  * The Resolver passes this information to the browser
  * The user is happy :D
</b></details>

<details>
<summary>What types of DNS records are there?</summary><br><b>

  * A
  * PTR
  * MX
  * AAAA
</b></details>

<details>
<summary>What is a A record?</summary><br><b>
</b></details>

<details>
<summary>What is a AAAA record?</summary><br><b>
</b></details>

<details>
<summary>What is a PTR record?</summary><br><b>

While an A record points a domain name to an IP address, a PTR record does the opposite and resolves the IP address to a domain name.
</b></details>

<details>
<summary>What is a MX record?</summary><br><b>
</b></details>

<details>
<summary>Is DNS using TCP or UDP?</summary><br><b>
</b></details>

<details>
<summary>What is Round Robin DNS?</summary><br><b>
</b></details>

<details>
<summary>What is DNS Record TTL? Why do we need it?</summary><br><b>
</b></details>

<details>
<summary>What is a zone? What types of zones are there?</summary><br><b>
</b></details>

## General

Although the following questions are not DevOps related, they are still quite common so it's better to prepare for them as well.

<details>
<summary>Tell us little bit about yourself</summary><br><b>
</b></details>

<details>
<summary>Tell me about your last big project/task you worked on</summary><br><b>
</b></details>

<details>
<summary>What was most challenging part in the project you worked on?</summary><br><b>
</b></details>

<details>
<summary>Why do you want to work here?</summary><br><b>
</b></details>

<details>
<summary>How did you hear about us?</summary><br><b>

Tell them how did you hear about them :D
</b></details>

<details>
<summary>How would you describe a good leadership? What makes a good boss for you?</summary><br><b>
</b></details>

<details>
<summary>Tell me about a time where you didn't agree on an implementation</summary><br><b>
</b></details>

<details>
<summary>How do you deal with a situation where key stakeholders are not around and a big decision needs to be made? </summary><br><b>
</b></details>

<details>
<summary>Give an example of a time you were able to change the view of a team about a particular tool/project/technology</summary><br><b>
</b></details>

<details>
<summary>Have you ever caused a service outage? (or broke a working project, tool, ...?)</summary><br><b>
</b></details>

<details>
<summary>Rank the following in order 1 to 5, where 1 is most important: salaray, benefits, career, team/people, work life balance</summary><br><b>

Don't put salary in bottom or top.
</b></details>

<details>
<summary>You have three important tasks scheduled for today. One is for your boss, second for a colleague who is also a friend, third is for a customer. All tasks are equally important. What do you do first?</summary><br><b>
</b></details>

<details>
<summary>You have a colleague you don‘t get along with. Tell us some strategies how you create a good work relationship with them anyway.</summary><br><b>
</b></details>

<details>
<summary>What do you love about your work?</summary><br><b>
</b></details>

<details>
<summary>Why should we hire you for the role?</summary><br><b>
</b></details>

## Questions you CAN ask

A list of questions you as a candidate can ask the interviewer during or after the interview.
These are only a suggestion. Use them carefully :)

<details>
<summary>What do you like about working here?</summary><br><b>
</b></details>

<details>
<summary>How does the company promote personal growth?</summary><br><b>
</b></details>

<details>
<summary>What is the current level of technical debt you are dealing with?</summary><br><b>

Be careful when asking this question - all companies, regardless of size, have some level of tech debt. 
Phrase the question in the light that all companies have the deal with this, but you want to see the current
pain points they are dealing with <br>

This is a great way to figure how managers deal with unplanned work, and how good they are at 
setting expectations with projects.
</b></details>

<details>
<summary>What was your favorite project you've worked on?</summary><br><b>

This can give you insights in some of the cool projects a company is working on, and if 
you would enjoy working on projects like these. This is also a good way to see if
the managers are allowing employees to learn and grow with projects outside of the
normal work you'd do.
</b></details>

<details>
<summary>If you could change one thing about your day to day, what would it be?</summary><br><b>

Similar to the tech debt question, this helps you identify any pain points with the company.
Additionally, it can be a great way to show how you'd be an asset to the team.<br>

For Example, if they mention they have problem X, and you've solved that in the past,
you can show how you'd be able to mitigate that problem.
</b></details>

<details>
<summary>Let's say that we agree and you hire me to this position, after X months, what do you expect that I have achieved?</summary><br><b>
</b></details>

## Scenarios

Scenarios are questions which don't have verbal answer and require you one of the following:

  * Set up environments
  * Write scripts
  * Design and/or develop infrastructure projects

These questions usually given as an home task to the candidate and they can combine several topics together.
Below you can find several scenario questions:

* [Writing a Dockerfile and running a container](scenarios/write_dockerfile_run_container.md)
* [Elasticsearch & Kibana on AWS](scenarios/elk_kibana_aws.md)
* [Ansible, Minikube and Docker](scenarios/ansible_minikube_docker.md)
* [Cloud Slack bot](scenarios/cloud_slack_bot.md)
* [Jenkins: writing scripts](scenarios/jenkins_scripts.md)
* [Jenkins: writing pipelines](scenarios/jenkins_pipelines.md)
* [CI for open source project](scenarios/ci_for_open_source_project.md)

## Credits

Thanks to all of our amazing [contributors](https://github.com/bregman-arie/devops-interview-questions/graphs/contributors) who make it easy for everyone to learn and prepare to their interviews.

Logos credits can be found [here](credits.md)

## License

[![License: CC BY-NC-ND 3.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%203.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/3.0/)
