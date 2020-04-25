## AWS - Cloud Practitioner

A summary of what you need to know for the exam can be found [here](https://codingshell.com/aws-cloud-practitioner)

#### Cloud 101

<details>
<summary>What types of Cloud Computing services are there?</summary><br><b>

IAAS
PAAS
SAAS
</b></details>

<details>
<summary>Explain each of the following and give an example:

  * IAAS
  * PAAS
  * SAAS</summary><br><b>
</b></details>

<details>
<summary>What types of clouds (or cloud deployments) are there?</summary><br><b>

  * Public
  * Hybrid
  * Private
</b></details>

<details>
<summary>Explain each of the following Cloud Computing Deployments:

  * Public
  * Hybrid
  * Private</summary><br><b>
</b></details>

#### AWS Global Infrastructure

<details>
<summary>Explain the following

  * Availability zone
  * Region
  * Edge location</summary><br><b>
AWS regions are data centers hosted across different geographical locations worldwide, each region is completely independent of one another.<br>

Within each region, there are multiple isolated locations known as Availability Zones. Multiple availability zones ensure high availability in case one of them goes down.<br>

Edge locations are basically content delivery network which caches data and insures lower latency and faster delivery to the users in any location. They are located in major cities in the world.
</b></details>

#### AWS Networking

<details>
<summary>What is AWS Direct Connect?</summary><br><b>

Allows you to connect your corporate network to AWS network.
</b></details>

<details>
<summary>What is Route 53?</summary><br><b>

"Amazon Route 53 is a highly available and scalable cloud Domain Name System (DNS) web service"

More on Route 53 [here](https://aws.amazon.com/route53)
</b></details>

<details>
<summary>What is VPC?</summary><br><b>

"A logically isolated section of the AWS cloud where you can launch AWS resources in a virtual network that you define"
Read more about it [here](https://aws.amazon.com/vpc).
</b></details>

<details>
<summary>True or False? Subnets belong to the same VPC, can be in different availability zones</summary><br><b>

True. Just to clarify, a subnet must reside entirely in one AZ.
</b></details>

<details>
<summary>What is an Internet Gateway?</summary><br><b>

"component that allows communication between instances in your VPC and the internet" (AWS docs).
Read more about it [here](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
</b></details>

<details>
<summary>Multiple Internet Gateways can be attached to one VPC</summary><br><b>

False. Only one internet gateway can be attached to a single VPC.
</b></details>

<details>
<summary>Explain Security Groups and Network ACLs</summary><br><b>

* NACL - security layer on the subnet level.
* Security Group - security layer on the instance level.

Read more about it [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) and [here](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
</b></details>

#### AWS EC2

<details>
<summary>What is EC2?</summary><br><b>
</b></details>

#### AWS Storage
 
<details>
<summary>Explain what is AWS S3?</summary><br><b>

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

#### AWS IAM

<details>
<summary>What is IAM? What are some of its features?</summary><br><b>

Full explanation is [here](https://aws.amazon.com/iam)
In short: it's used for managing users, groups, access policies & roles
</b></details>

<details>
<summary>True or False? IAM configuration is defined globally and not per region</summary><br><b>

True
</b></details>

<details>
<summary>Given an example of IAM best practices?</summary><br><b>

* Set up MFA
* Delete root account access keys
* Create IAM users instead of using root for daily management
</b></details>

<details>
<summary>What are Roles?</summary><br><b>

A way for allowing a service of AWS to use another service of AWS. You assign roles to AWS resources.
For example, you can make use of a role which allows EC2 service to acesses s3 buckets (read and write).
</b></details>

<details>
<summary>What are Policies?</summary><br><b>

Policies documents used to give permissions as to what a user, group or role are able to do. Their format is JSON.
</b></details>

<details>
<summary>A user is unable to access an s3 bucket. What might be the problem?</summary><br><b>

There can be several reasons for that. One of them is lack of policy. To solve that, the admin has to attach the user with a policy what allows him to access the s3 bucket.
</b></details>

<details>
<summary>What should you use to:

  * Grant access between two services/resources?
  * Grant user access to resources/services?</summary><br><b>

  * Role
  * Policy
</b></details>

<details>
<summary>What permissions does a new user have?</summary><br><b>

Only a login access.
</b></details>

### Final Note

Good luck! You can do it :)
