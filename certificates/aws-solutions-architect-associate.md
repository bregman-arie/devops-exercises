## AWS - Solutions Architect Associate 

Last update: 2021

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

#### AWS - IAM

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
<summary>True or False? When creating an AWS account, root account is created by default. This is the recommended account to use and share in your organization</summary><br><b>

False. Instead of using the root account, you should be creating users and use them.
</b></details>

<details>
<summary>True or False? Groups in AWS IAM, can contain only users and not other groups</summary><br><b>

True
</b></details>

<details>
<summary>True or False? Users in AWS IAM, can belong only to a single group</summary><br><b>

False. Users can belong to multiple groups.
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


#### AWS Networking

<details>
<summary>What is VPC?</summary><br><b>

"A logically isolated section of the AWS cloud where you can launch AWS resources in a virtual network that you define"
Read more about it [here](https://aws.amazon.com/vpc).
</b></details>

<details>
<summary>True or False? VPC spans multiple regions</summary><br><b>

False
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
<summary>True or False? NACL allow or deny traffic on the subnet level</summary><br><b>

True
</b></details>

<details>
<summary>True or False? Multiple Internet Gateways can be attached to one VPC</summary><br><b>

False. Only one internet gateway can be attached to a single VPC.
</b></details>

<details>
<summary>True or False? Route Tables used to allow or deny traffic from the internet to AWS instances</summary><br><b>

False.
</b></details>

<details>
<summary>Explain Security Groups and Network ACLs</summary><br><b>

* NACL - security layer on the subnet level.
* Security Group - security layer on the instance level.

Read more about it [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) and [here](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
</b></details>

<details>
<summary>What is AWS Direct Connect?</summary><br><b>

Allows you to connect your corporate network to AWS network.
</b></details>

#### AWS Compute

<details>
<summary>What is EC2?</summary><br><b>

"a web service that provides secure, resizable compute capacity in the cloud".
Read more [here](https://aws.amazon.com/ec2)
</b></details>

<details>
<summary>True or False? EC2 is a regional service</summary><br><b>

True. As opposed to IAM for example, which is a global service, EC2 is a regional service.
</b></details>

<details>
<summary>What is AMI?</summary><br><b>

Amazon Machine Images is "An Amazon Machine Image (AMI) provides the information required to launch an instance".
Read more [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
</b></details>

<details>
<summary>What are the different source for AMIs?</summary><br><b>

* Personal AMIs - AMIs you create
* AWS Marketplace for AMIs - Paid AMIs usually with bundled with licensed software
* Community AMIs - Free
</b></details>

<details>
<summary>What is instance type?</summary><br><b>

"the instance type that you specify determines the hardware of the host computer used for your instance"
Read more about instance types [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
</b></details>

<details>
<summary>True or False? The following are instance types available for a user in AWS:

  * Compute optimizied
  * Network optimizied
  * Web optimized</summary><br><b>

False. From the above list only compute optimized is available.
</b></details>

<details>
<summary>What is EBS?</summary><br><b>

"provides block level storage volumes for use with EC2 instances. EBS volumes behave like raw, unformatted block devices."
More on EBS [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)
</b></details>

<details>
<summary>What EC2 pricing models are there?</summary><br><b>

On Demand - pay a fixed rate by the hour/second with no commitment. You can provision and terminate it at any given time.
Reserved - you get capacity reservation, basically purchase an instance for a fixed time of period. The longer, the cheaper.
Spot - Enables you to bid whatever price you want for instances or pay the spot price.
Dedicated Hosts - physical EC2 server dedicated for your use.
</b></details>

<details>
<summary>What are Security Groups?</summary><br><b>

"A security group acts as a virtual firewall that controls the traffic for one or more instances"
More on this subject [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)
</b></details>

<details>
<summary>What can you attach to an EC2 instance in order to store data?</summary><br><b>

EBS
</b></details>

<details>
<summary>What EC2 RI types are there?</summary><br><b>

Standard RI - most significant discount + suited for steady-state usage
Convertible RI - discount + change attribute of RI + suited for steady-state usage
Scheduled RI - launch within time windows you reserve

Learn more about EC2 RI [here](https://aws.amazon.com/ec2/pricing/reserved-instances)
</b></details>

#### AWS Containers

<details>
<summary>What is Amazon ECS?</summary><br><b>

Amazon definition: "Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service. Customers such as Duolingo, Samsung, GE, and Cook Pad use ECS to run their most sensitive and mission critical applications because of its security, reliability, and scalability."

Learn more [here](https://aws.amazon.com/ecs)
</b></details>

<details>
<summary>What is Amazon ECR?</summary><br><b>

Amazon definition: "Amazon Elastic Container Registry (ECR) is a fully-managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images."

Learn more [here](https://aws.amazon.com/ecr)
</b></details>

<details>
<summary>What is AWS Fargate?</summary><br><b>

Amazon definition: "AWS Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS)."

Learn more [here](https://aws.amazon.com/fargate)
</b></details>

#### AWS Storage
 
<details>
<summary>Explain what is AWS S3?</summary><br><b>

S3 stands for 3 S, Simple Storage Service.
S3 is a object storage service which is fast, scalable and durable. S3 enables customers to upload, download or store any file or object that is up to 5 TB in size.

More on S3 [here](https://aws.amazon.com/s3) 
</b></details>

<details>
<summary>What is a bucket?</summary><br><b>

An S3 bucket is a resource which is similar to folders in a file system and allows storing objects, which consist of data.
</b></details>

<details>
<summary>True or False? A bucket name must be globally unique</summary><br><b>

True
</b></details>

<details>
<summary>Explain folders and objects in regards to buckets</summary><br><b>

* Folder - any sub folder in an s3 bucket
* Object - The files which are stored in a bucket
</b></details>

<details>
<summary>Explain the following:

  * Object Lifecycles
  * Object Sharing
  * Object Versioning</summary><br><b>

  * Object Lifecycles - Transfer objects between storage classes based on defined rules of time periods
  * Object Sharing - Share objects via a URL link
  * Object Versioning - Manage multiple versions of an object
</b></details>

<details>
<summary>Explain Object Durability and Object Availability</summary><br><b>

Object Durability: The percent over a one-year time period that a file will not be lost
Object Availability: The percent over a one-year time period that a file will be accessible
</b></details>

<details>
<summary>What is a storage class? What storage classes are there?</summary><br><b>

Each object has a storage class assigned to, affecting its availability and durability. This also has effect on costs.
Storage classes offered today:
  * Standard:
    * Used for general, all-purpose storage (mostly storage that needs to be accessed frequently)
    * The most expensive storage class 
    * 11x9% durability
    * 2x9% availability
    * Default storage class

  * Standard-IA (Infrequent Access)
    * Long lived, infrequently accessed data but must be available the moment it's being accessed
    * 11x9% durability
    * 99.90% availability

  * One Zone-IA (Infrequent Access):
    * Long-lived, infrequently accessed, non-critical data
    * Less expensive than Standard and Standard-IA storage classes
    * 2x9% durability
    * 99.50% availability
    
  * Intelligent-Tiering:
    * Long-lived data with changing or unknown access patterns. Basically, In this class the data automatically moves to the class most suitable for you based on usage patterns
    * Price depends on the used class
    * 11x9% durability
    * 99.90% availability

  * Glacier: Archive data with retrieval time ranging from minutes to hours
  * Glacier Deep Archive: Archive data that rarely, if ever, needs to be accessed with retrieval times in hours
  * Both Glacier and Glacier Deep Archive are:
    * The most cheap storage classes
    * have 9x9% durability 

More on storage classes [here](https://aws.amazon.com/s3/storage-classes)

</b></details>

<details>
<summary>A customer would like to move data which is rarely accessed from standard storage class to the most cheapest class there is. Which storage class should be used?

  * One Zone-IA
  * Glacier Deep Archive
  * Intelligent-Tiering</summary><br><b>

Glacier Deep Archive
</b></details>

<details>
<summary>What Glacier retrieval options are available for the user?</summary><br><b>

Expedited, Standard and Bulk
</b></details>

<details>
<summary>True or False? Each AWS account can store up to 500 PetaByte of data. Any additional storage will cost double</summary><br><b>

False. Unlimited capacity.
</b></details>

<details>
<summary>Explain what is Storage Gateway</summary><br><b>

"AWS Storage Gateway is a hybrid cloud storage service that gives you on-premises access to virtually unlimited cloud storage".
More on Storage Gateway [here](https://aws.amazon.com/storagegateway)
</b></details>

<details>
<summary>Explain the following Storage Gateway deployments types

  * File Gateway
  * Volume Gateway
  * Tape Gateway</summary><br><b>

Explained in detail [here](https://aws.amazon.com/storagegateway/faqs)
</b></details>

<details>
<summary>What is the difference between stored volumes and cached volumes?</summary><br><b>

Stored Volumes - Data is located at customer's data center and periodically backed up to AWS
Cached Volumes - Data is stored in AWS cloud and cached at customer's data center for quick access
</b></details>

<details>
<summary>What is "Amazon S3 Transfer Acceleration"?</summary><br><b>

AWS definition: "Amazon S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket"

Learn more [here](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html)
</b></details>

<details>
<summary>What is Amazon EFS?</summary><br><b>

Amazon definition: "Amazon Elastic File System (Amazon EFS) provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources."

Learn more [here](https://aws.amazon.com/efs)
</b></details>

<details>
<summary>What is AWS Snowmobile?</summary><br><b>

"AWS Snowmobile is an Exabyte-scale data transfer service used to move extremely large amounts of data to AWS."

Learn more [here](https://aws.amazon.com/snowmobile)
</b></details>

##### AWS ELB

<details>
<summary>What is ELB (Elastic Load Balancing)?</summary><br><b>

AWS definition: "Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions."

More on ELB [here](https://aws.amazon.com/elasticloadbalancing)
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

<details>
<summary>What types of load balancers are supported in EC2 and what are they used for?</summary><br><b>

  * Application LB - layer 7 traffic
  * Network LB - ultra-high performances or static IP address
  * Classic LB - low costs, good for test or dev environments
</b></details>

#### AWS DNS

<details>
<summary>What is Route 53?</summary><br><b>

"Amazon Route 53 is a highly available and scalable cloud Domain Name System (DNS) web service"
Some of Route 53 features:
  * Register domain
  * DNS service - domain name translations
  * Health checks - verify your app is available

More on Route 53 [here](https://aws.amazon.com/route53)
</b></details>

#### AWS CloudFront

<details>
<summary>Explain what is CloudFront</summary><br><b>

AWS definition: "Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment."

More on CloudFront [here](https://aws.amazon.com/cloudfront)
</b></details>

<details>
<summary>Explain the following

  * Origin
  * Edge location
  * Distribution</summary><br><b>
</b></details>

#### AWS Monitoring & Logging

<details>
<summary>What is AWS CloudWatch?</summary><br><b>

AWS definition: "Amazon CloudWatch is a monitoring and observability service..."

More on CloudWatch [here](https://aws.amazon.com/cloudwatch)
</b></details>

<details>
<summary>What is AWS CloudTrail?</summary><br><b>

AWS definition: "AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account."

Read more on CloudTrail [here](https://aws.amazon.com/cloudtrail)
</b></details>

<details>
<summary>What is Simply Notification Service?</summary><br><b>

AWS definition: "a highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications."

Read more about it [here](https://aws.amazon.com/sns)
</b></details>

<details>
<summary>Explain the following in regards to SNS:

  * Topics
  * Subscribers
  * Publishers</summary><br><b>

  * Topics - used for grouping multiple endpoints
  * Subscribers - the endpoints where topics send messages to 
  * Publishers - the provider of the message (event, person, ...)
</b></details>

#### AWS Security 

<details>
<summary>What is the shared responsibility model? What AWS is responsible for and what the user is responsible for based on the shared responsibility model?</summary><br><b>

The shared responsibility model defines what the customer is responsible for and what AWS is responsible for.

More on the shared responsibility model [here](https://aws.amazon.com/compliance/shared-responsibility-model)
</b></details>

<details>
<summary>True or False? Based on the shared responsibility model, Amazon is responsible for physical CPUs and security groups on instances</summary><br><b>

False. It is responsible for Hardware in its sites but not for security groups which created and managed by the users.
</b></details>

<details>
<summary>Explain "Shared Controls" in regards to the shared responsibility model</summary><br><b>

AWS definition: "apply to both the infrastructure layer and customer layers, but in completely separate contexts or perspectives. In a shared control, AWS provides the requirements for the infrastructure and the customer must provide their own control implementation within their use of AWS services"

Learn more about it [here](https://aws.amazon.com/compliance/shared-responsibility-model)
</b></details>

<details>
<summary>What is the AWS compliance program?</summary><br><b>
</b></details>

<details>
<summary>What is AWS Artifact?</summary><br><b>

AWS definition: "AWS Artifact is your go-to, central resource for compliance-related information that matters to you. It provides on-demand access to AWS’ security and compliance reports and select online agreements."

Read more about it [here](https://aws.amazon.com/artifact)
</b></details>

<details>
<summary>What is AWS Inspector?</summary><br><b>

AWS definition: "Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. Amazon Inspector automatically assesses applications for exposure, vulnerabilities, and deviations from best practices.""

Learn more [here](https://aws.amazon.com/inspector)
</b></details>

<details>
<summary>What is AWS Guarduty?</summary><br><b>
</b></details>

<details>
<summary>What is AWS Shield?</summary><br><b>

AWS definition: "AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS."
</b></details>

<details>
<summary>What is AWS WAF? Give an example of how it can used and describe what resources or services you can use it with</summary><br><b>
</b></details>

<details>
<summary>What AWS VPN is used for?</summary><br><b>
</b></details>

<details>
<summary>What is the difference between Site-to-Site VPN and Client VPN?</summary><br><b>
</b></details>

<details>
<summary>What is AWS CloudHSM?</summary><br><b>

Amazon definition: "AWS CloudHSM is a cloud-based hardware security module (HSM) that enables you to easily generate and use your own encryption keys on the AWS Cloud."

Learn more [here](https://aws.amazon.com/cloudhsm)
</b></details>

<details>
<summary>True or False? AWS Inspector can perform both network and host assessments</summary><br><b>

True
</b></details>

<details>
<summary>What is AWS Acceptable Use Policy?</summary><br><b>

It describes prohibited uses of the web services offered by AWS.
More on AWS Acceptable Use Policy [here](https://aws.amazon.com/aup)
</b></details>

<details>
<summary>What is AWS Key Management Service (KMS)?</summary><br><b>

AWS definition: "KMS makes it easy for you to create and manage cryptographic keys and control their use across a wide range of AWS services and in your applications."
More on KMS [here](https://aws.amazon.com/kms)
</b></details>

<details>
<summary>True or False? A user is not allowed to perform penetration testing on any of the AWS services</summary><br><b>

False. On some services, like EC2, CloudFront and RDS, penetration testing is allowed.
</b></details>

<details>
<summary>True or False? DDoS attack is an example of allowed penetration testing activity</summary><br><b>

False.
</b></details>

<details>
<summary>True or False? AWS Access Key is a type of MFA device used for AWS resources protection</summary><br><b>

False. Security key is an example of an MFA device.
</b></details>

<details>
<summary>What is Amazon Cognito?</summary><br><b>

Amazon definition: "Amazon Cognito handles user authentication and authorization for your web and mobile apps."

Learn more [here](https://docs.aws.amazon.com/cognito/index.html)
</b></details>

<details>
<summary>What is AWS ACM?</summary><br><b>

Amazon definition: "AWS Certificate Manager is a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources."

Learn more [here](https://aws.amazon.com/certificate-manager)
</b></details>

#### AWS Databases

<details>
<summary>What is AWS RDS?</summary><br><b>
</b></details>

<details>
<summary>What is AWS DynamoDB?</summary><br><b>
</b></details>

<details>
<summary>Explain "Point-in-Time Recovery" feature in DynamoDB</summary><br><b>

Amazon definition: "You can create on-demand backups of your Amazon DynamoDB tables, or you can enable continuous backups using point-in-time recovery. For more information about on-demand backups, see On-Demand Backup and Restore for DynamoDB."

Learn more [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html)
</b></details>

<details>
<summary>Explain "Global Tables" in DynamoDB</summary><br><b>

Amazon definition: "A global table is a collection of one or more replica tables, all owned by a single AWS account."

Learn more [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html)
</b></details>

<details>
<summary>What is DynamoDB Accelerator?</summary><br><b>

Amazon definition: "Amazon DynamoDB Accelerator (DAX) is a fully managed, highly available, in-memory cache for DynamoDB that delivers up to a 10x performance improvement – from milliseconds to microseconds..."

Learn more [here](https://aws.amazon.com/dynamodb/dax)
</b></details>

<details>
<summary>What is AWS Redshift and how is it different than RDS?</summary><br><b>

cloud data warehouse
</b></details>

<details>
<summary>What is AWS ElastiCache? For what cases is it used?</summary><br><b>

Amazon Elasticache is a fully managed Redis or Memcached in-memory data store.                                                                       
It's great for use cases like two-tier web applications where the most frequently accesses data is stored in ElastiCache so response time is optimal.
</b></details>

<details>
<summary>What is Amazon Aurora</summary><br><b>

A MySQL & Postgresql based relational database. Also, the default database proposed for the user when using RDS for creating a database.
Great for use cases like two-tier web applications that has a MySQL or Postgresql database layer and you need automated backups for your application.
</b></details>

<details>
<summary>What is Amazon DocumentDB?</summary><br><b>

Amazon definition: "Amazon DocumentDB (with MongoDB compatibility) is a fast, scalable, highly available, and fully managed document database service that supports MongoDB workloads. As a document database, Amazon DocumentDB makes it easy to store, query, and index JSON data."

Learn more [here](https://aws.amazon.com/documentdb)
</b></details>

<details>
<summary>What "AWS Database Migration Service" is used for?</summary><br><b>
</b></details>

<details>
<summary>What type of storage is used by Amazon RDS?</summary><br><b>

EBS
</b></details>

<details>
<summary>Explain Amazon RDS Read Replicas</summary><br><b>

AWS definition: "Amazon RDS Read Replicas provide enhanced performance and durability for RDS database (DB) instances. They make it easy to elastically scale out beyond the capacity constraints of a single DB instance for read-heavy database workloads."
Read more about [here](https://aws.amazon.com/rds/features/read-replicas)
</b></details>

#### AWS Serverless Compute

<details>
<summary>Explain what is AWS Lambda</summary><br><b>

AWS definition: "AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume."

Read more on it [here](https://aws.amazon.com/lambda)
</b></details>

<details>
<summary>True or False? In AWS Lambda, you are charged as long as a function exists, regardless of whether it's running or not</summary><br><b>

False. Charges are being made when the code is executed.
</b></details>

<details>
<summary>Which of the following set of languages Lambda supports?

  * R, Swift, Rust, Kotlin
  * Python, Ruby, Go 
  * Python, Ruby, PHP</summary><br><b>

  * Python, Ruby, Go 
</b></details>

#### Identify the service or tool

<details>
<summary>What would you use for automating code/software deployments?</summary><br><b>

AWS CodeDeploy
</b></details>

<details>
<summary>What would you use for easily creating similar AWS environments/resources for different customers?</summary><br><b>

CloudFormation
</b></details>

<details>
<summary>Which service would you use for building a website or web application?</summary><br><b>

Lightsail
</b></details>

<details>
<summary>Which tool would you use for choosing between Reserved instances or On-Demand instances?</summary><br><b>

Cost Explorer
</b></details>

<details>
<summary>What would you use to check how many unassociated Elastic IP address you have?</summary><br><b>

Trusted Advisor
</b></details>

<details>
<summary>What service allows you to transfer large amounts (Petabytes) of data in and out of the AWS cloud?</summary><br><b>

AWS Snowball
</b></details>

<details>
<summary>What provides a virtual network dedicated to your AWS account?</summary><br><b>

VPC
</b></details>

<details>
<summary>What you would use for having automated backups for an application that has MySQL database layer?</summary><br><b>

Amazon Aurora
</b></details>

<details>
<summary>What would you use to migrate on-premise database to AWS?</summary><br><b>

AWS Database Migration Service (DMS)
</b></details>

<details>
<summary>What would you use to check why certain EC2 instances were terminated?</summary><br><b>

AWS CloudTrail
</b></details>

<details>
<summary>What would you use for SQL database?</summary><br><b>

AWS RDS
</b></details>

<details>
<summary>What would you use for NoSQL database?</summary><br><b>

AWS DynamoDB
</b></details>

<details>
<summary>What would you use for running SQL queries interactively on S3?</summary><br><b>

AWS Athena
</b></details>

<details>
<summary>What would you use for adding image and video analysis to your application?</summary><br><b>

AWS Rekognition
</b></details>

<details>
<summary>Which service would you use for debugging and improving performances issues with your applications?</summary><br><b>

AWS X-Ray
</b></details>

<details>
<summary>Which service is used for sending notifications?</summary><br><b>

SNS
</b></details>

<details>
<summary>Which service would you use for monitoring malicious activity and unauthorized behavior in regards to AWS accounts and workloads?</summary><br><b>

Amazon GuardDuty
</b></details>

<details>
<summary>Which service would you use for centrally manage billing, control access, compliance, and security across multiple AWS accounts?</summary><br><b>

AWS Organizations
</b></details>

<details>
<summary>Which service would you use for web application protection?</summary><br><b>

AWS WAF
</b></details>

<details>
<summary>You would like to monitor some of your resources in the different services. Which service would you use for that?</summary><br><b>

CloudWatch
</b></details>

<details>
<summary>Which service would you use for performing security assessment?</summary><br><b>

AWS Inspector
</b></details>

<details>
<summary>Which service would you use for creating DNS record?</summary><br><b>

Route 53
</b></details>

<details>
<summary>What would you use if you need a fully managed document database?</summary><br><b>

Amazon DocumentDB
</b></details>

<details>
<summary>Which service would you use to add access control (or sign-up, sign-in forms) to your web/mobile apps?</summary><br><b>

AWS Cognito
</b></details>

<details>
<summary>Which service would you use if you need messaging queue?</summary><br><b>

Simple Queue Service (SQS)
</b></details>

<details>
<summary>Which service would you use if you need managed DDOS protection?</summary><br><b>

AWS Shield
</b></details>

<details>
<summary>Which service would you use if you need store frequently used data for low latency access?</summary><br><b>

ElastiCache
</b></details>

<details>
<summary>What would you use to transfer files over long distances between a client and an S3 bucket?</summary><br><b>

Amazon S3 Transfer Acceleration
</b></details>

#### AWS Billing & Support

<details>
<summary>What is AWS Organizations?</summary><br><b>

AWS definition: "AWS Organizations helps you centrally govern your environment as you grow and scale your workloads on AWS."
More on Organizations [here](https://aws.amazon.com/organizations)
</b></details>

<details>
<summary>Explain AWS pricing model</summary><br><b>

It mainly works on "pay-as-you-go" meaning you pay only for what are using and when you are using it.
In s3 you pay for 1. How much data you are storing 2. Making requests (PUT, POST, ...)
In EC2 it's based on the purchasing option (on-demand, spot, ...), instance type, AMI type and the region used.

More on AWS pricing model [here](https://aws.amazon.com/pricing)
</b></details>

<details>
<summary>How one should estimate AWS costs when for example comparing to on-premise solutions?</summary><br><b>

* TCO calculator
* AWS simple calculator
* Cost Explorer
</b></details>

<details>
<summary>What basic support in AWS includes?</summary><br><b>

* 24x7 customer service
* Trusted Advisor
* AWS personal Health Dashoard
</b></details>

<details>
<summary>How are EC2 instances billed?</summary><br><b>
</b></details>

<details>
<summary>What AWS Pricing Calculator is used for?</summary><br><b>
</b></details>

<details>
<summary>What is Amazon Connect?</summary><br><b>

Amazon definition: "Amazon Connect is an easy to use omnichannel cloud contact center that helps companies provide superior customer service at a lower cost."

Learn more [here](https://aws.amazon.com/connect)
</b></details>

<details>
<summary>What are "APN Consulting Partners"?</summary><br><b>

Amazon definition: "APN Consulting Partners are professional services firms that help customers of all types and sizes design, architect, build, migrate, and manage their workloads and applications on AWS, accelerating their journey to the cloud."

Learn more [here](https://aws.amazon.com/partners/consulting)
</b></details>

<details>
<summary>Which of the following are AWS accounts types (and are sorted by order)?

  * Basic, Developer, Business, Enterprise
  * Newbie, Intermediate, Pro, Enterprise
  * Developer, Basic, Business, Enterprise
  * Beginner, Pro, Intermediate Enterprise</summary><br><b>

  * Basic, Developer, Business, Enterprise
</b></details>

<details>
<summary>True or False? Region is a factor when it comes to EC2 costs/pricing</summary><br><b>

True. You pay differently based on the chosen region.
</b></details>

<details>
<summary>What is "AWS Infrastructure Event Management"?</summary><br><b>

AWS Definition: "AWS Infrastructure Event Management is a structured program available to Enterprise Support customers (and Business Support customers for an additional fee) that helps you plan for large-scale events such as product or application launches, infrastructure migrations, and marketing events."
</b></details>

#### AWS Automation

<details>
<summary>What is AWS CodeDeploy?</summary><br><b>

Amazon definition: "AWS CodeDeploy is a fully managed deployment service that automates software deployments to a variety of compute services such as Amazon EC2, AWS Fargate, AWS Lambda, and your on-premises servers."

Learn more [here](https://aws.amazon.com/codedeploy)
</b></details>

<details>
<summary>Explain what is CloudFormation</summary><br><b>
</b></details>

#### AWS Misc

<details>
<summary>What is AWS Lightsail?</summary><br><b>

AWS definition: "Lightsail is an easy-to-use cloud platform that offers you everything needed to build an application or website, plus a cost-effective, monthly plan."
</b></details>

<details>
<summary>What is AWS Rekognition?</summary><br><b>

AWS definition: "Amazon Rekognition makes it easy to add image and video analysis to your applications using proven, highly scalable, deep learning technology that requires no machine learning expertise to use."

Learn more [here](https://aws.amazon.com/rekognition)
</b></details>

<details>
<summary>What AWS Resource Groups used for?</summary><br><b>

Amazon definition: "You can use resource groups to organize your AWS resources. Resource groups make it easier to manage and automate tasks on large numbers of resources at one time. "

Learn more [here](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html)
</b></details>

<details>
<summary>What is AWS Global Accelerator?</summary><br><b>

Amazon definition: "AWS Global Accelerator is a service that improves the availability and performance of your applications with local or global users..."

Learn more [here](https://aws.amazon.com/global-accelerator)
</b></details>

<details>
<summary>What is AWS Config?</summary><br><b>

Amazon definition: "AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources."

Learn more [here](https://aws.amazon.com/config)
</b></details>

<details>
<summary>What is AWS X-Ray?</summary><br><b>

AWS definition: "AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture."
Learn more [here](https://aws.amazon.com/xray)
</b></details>

<details>
<summary>What is AWS OpsWorks?</summary><br><b>

Amazon definition: "AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet."

Learn more about it [here](https://aws.amazon.com/opsworks)
</b></details>

<details>
<summary>What is AWS Service Catalog?</summary><br><b>

Amazon definition: "AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS."

Learn more [here](https://aws.amazon.com/servicecatalog)
</b></details>

<details>
<summary>What is AWS CAF?</summary><br><b>

Amazon definition: "AWS Professional Services created the AWS Cloud Adoption Framework (AWS CAF) to help organizations design and travel an accelerated path to successful cloud adoption. "

Learn more [here](https://aws.amazon.com/professional-services/CAF)
</b></details>

<details>
<summary>What is AWS Cloud9?</summary><br><b>

AWS definition: "AWS Cloud9 is a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser"
</b></details>

<details>
<summary>What is AWS Application Discovery Service?</summary><br><b>

Amazon definition: "AWS Application Discovery Service helps enterprise customers plan migration projects by gathering information about their on-premises data centers."

Learn more [here](https://aws.amazon.com/application-discovery)
</b></details>

<details>
<summary>What is the Trusted Advisor?</summary><br><b>
</b></details>

<details>
<summary>What is the AWS well-architected framework and what pillars it's based on?</summary><br><b>

AWS definition: "The Well-Architected Framework has been developed to help cloud architects build secure, high-performing, resilient, and efficient infrastructure for their applications. Based on five pillars — operational excellence, security, reliability, performance efficiency, and cost optimization"

Learn more [here](https://aws.amazon.com/architecture/well-architected)
</b></details>

<details>
<summary>What AWS services are serverless (or have the option to be serverless)?</summary><br><b>

AWS Lambda
AWS Athena
</b></details>

<details>
<summary>What is AWS EMR?</summary><br><b>

AWS definition: "big data platform for processing vast amounts of data using open source tools such as Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi, and Presto."

Learn more [here](https://aws.amazon.com/emr)
</b></details>

<details>
<summary>What is AWS Athena?</summary><br><b>

"Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL."

Learn more about AWS Athena [here](https://aws.amazon.com/athena)
</b></details>

<details>
<summary>What is Amazon Cloud Directory?</summary><br><b>

Amazon definition: "Amazon Cloud Directory is a highly available multi-tenant directory-based store in AWS. These directories scale automatically to hundreds of millions of objects as needed for applications."

Learn more [here](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/what_is_cloud_directory.html)
</b></details>

<details>
<summary>What is AWS Elastic Beanstalk?</summary><br><b>

AWS definition: "AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services...You can simply upload your code and Elastic Beanstalk automatically handles the deployment"

Learn more about it [here](https://aws.amazon.com/elasticbeanstalk)
</b></details>

<details>
<summary>What is AWS SWF?</summary><br><b>

Amazon definition: "Amazon SWF helps developers build, run, and scale background jobs that have parallel or sequential steps. You can think of Amazon SWF as a fully-managed state tracker and task coordinator in the Cloud."

Learn more on Amazon Simple Workflow Service [here](https://aws.amazon.com/swf)
</b></details>

<details>
<summary>What is Simple Queue Service (SQS)?</summary><br><b>

AWS definition: "Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications".

Learn more about it [here](https://aws.amazon.com/sqs)
</b></details>

#### AWS Disaster Recovery

<details>
<summary>In regards to disaster recovery, what is RTO and RPO?</summary><br><b>

RTO - The maximum acceptable length of time that your application can be offline.

RPO - The maximum acceptable length of time during which data might be lost from your application due to an incident.
</b></details>

<details>
<summary>What types of disaster recovery techniques AWS supports?</summary><br><b>

* The Cold Method - Periodically backups and sending the backups off-site<br>
* Pilot Light - Data is mirrored to an environment which is always running
* Warm Standby - Running scaled down version of production environment
* Multi-site - Duplicated environment that is always running
</b></details>

<details>
<summary>Which disaster recovery option has the highest downtime and which has the lowest?</summary><br><b>

Lowest - Multi-site
Highest - The cold method
</b></details>

### Final Note

Good luck! You can do it :)
