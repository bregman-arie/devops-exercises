# Azure

- [Azure](#azure)
  - [Questions](#questions)
    - [Azure 101](#azure-101)
    - [Azure Resource Manager](#azure-resource-manager)
    - [Compute](#compute)
    - [Network](#network)
    - [Storage](#storage)
    - [Security](#security)

## Questions

### Azure 101

<details>
<summary>What is Azure Portal?</summary><br><b>

[Microsoft Docs](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/what-is-microsoft-azure): "The Azure portal is a web-based, unified console that provides an alternative to command-line tools. With the Azure portal, you can manage your Azure subscription by using a graphical user interface."
</b></details>

<details>
<summary>What is Azure Marketplace?</summary><br><b>

[Microsoft Docs](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/what-is-microsoft-azure): "Azure marketplace helps connect users with Microsoft partners, independent software vendors, and startups that are offering their solutions and services, which are optimized to run on Azure."
</b></details>

<details>
<summary>Explain availability sets and availability zones</summary><br><b>

An availability set is a logical grouping of VMs that allows Azure to understand how your application is built to provide redundancy and availability. It is recommended that two or more VMs are created within an availability set to provide for a highly available application and to meet the 99.95% Azure SLA.
</b></details>

<details>
<summary>What is Azure Policy?</summary><br><b>


[Microsoft Learn](https://learn.microsoft.com/en-us/azure/governance/policy/overview): "Azure Policy helps to enforce organizational standards and to assess compliance at-scale. Through its compliance dashboard, it provides an aggregated view to evaluate the overall state of the environment, with the ability to drill down to the per-resource, per-policy granularity. It also helps to bring your resources to compliance through bulk remediation for existing resources and automatic remediation for new resources."
</b></details>

<details>
<summary>Explain Azure managed disks</summary><br><b>
</b></details>

### Azure Resource Manager

<details>
<summary>Explain what's Azure Resource Manager</summary><br><b>

From [Azure docs](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview): "Azure Resource Manager is the deployment and management service for Azure. It provides a management layer that enables you to create, update, and delete resources in your Azure account. You use management features, like access control, locks, and tags, to secure and organize your resources after deployment."
</b></details>

<details>

<summary>What are the ARM template's sections ?</summary><br><b>

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview): The template has the following sections:

Parameters - Provide values during deployment that allow the same template to be used with different environments.

Variables - Define values that are reused in your templates. They can be constructed from parameter values.

User-defined functions - Create customized functions that simplify your template.

Resources - Specify the resources to deploy.

Outputs - Return values from the deployed resources.
</b></details>

<details>

<summary>What's an Azure Resource Group?</summary><br><b>

From [Azure docs](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal): "A resource group is a container that holds related resources for an Azure solution. The resource group can include all the resources for the solution, or only those resources that you want to manage as a group."
</b></details>

### Compute

<details>
<summary>What Azure compute services are you familiar with?</summary><br><b>

  * Azure Virtual Machines
  * Azure Batch
  * Azure Service Fabric
  * Azure Container Instances
  * Azure Virtual Machine Scale Sets
</b></details>

<details>

<summary>What "Azure Virtual Machines" service is used for?</summary><br><b>

Azure VMs support Windows and Linux OS. They can be used for hosting web servers, applications, backups, Databases, they can also be used as jump server or azure self-hosted agent for building and deploying apps.
</b></details>

<details>
<summary>What "Azure Virtual Machine Scale Sets" service is used for?</summary><br><b>

Scaling Linux or Windows virtual machines; it lets you create and manage a group of load balanced VMs. The number of VM instances can automatically increase or decrease in response to demand or a defined schedule.
</b></details>

<details>
<summary>What "Azure Functions" service is used for?</summary><br><b>

Azure Functions is the serverless compute service of Azure.
</b></details>

<details>
<summary>What "Durable Azure Function" are?</summary>
<br>

[Microsoft Learn](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/what-is-microsoft-azure): Durable Functions is an extension of Azure Functions that lets you write stateful functions in a serverless compute environment.
</details>

<details>
<summary>What "Azure Container Instances" service is used for?</summary><br><b>

Running containerized applications (without the need to provision virtual machines).
</b></details>

<details>
<summary>What "Azure Batch" service is used for?</summary><br><b>

Running parallel and high-performance computing applications
</b></details>

<details>
<summary>What "Azure Service Fabric" service is used for?</summary><br><b>
</b></details>

<details>
<summary>What "Azure Kubernetes" service is used for?</summary><br><b>
</b></details>

### Network

<details>
<summary>What Azure network services are you familiar with?</summary><br><b>
</b></details>
<details>
<summary>Explain VNet peering</summary><br><b>

VNet peering enables connecting virtual networks. This means that you can route traffic between resources of the connected VNets privately through IPv4 addresses. Connecting VNets within the same region is known as regional VNet Peering, however connecting VNets across Azure regions is known as global VNet Peering.

</b></details>

<details>
<summary>What's an Azure region?</summary><br><b>

An Azure region is a set of datacenters deployed within an interval-defined and connected through a dedicated regional low-latency network.
</b></details>

<details>
<summary>What is the N-tier architecture?</summary><br><b>
</b></details>

### Storage

<details>
<summary>What Azure storage services are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>What storage options Azure supports?</summary><br><b>
</b></details>

### Security

<details>
<summary>What is the Azure Security Center? What are some of its features?</summary><br><b>

It's a monitoring service that provides threat protection across all of the services in Azure.
More specifically, it:

* Provides security recommendations based on your usage
* Monitors security settings and continuously all the services
* Analyzes and identifies potential inbound attacks
* Detects and blocks malware using machine learning
</b></details>

<details>
<summary>What is Azure Active Directory?</summary><br><b>

Azure AD is a cloud-based identity service. You can use it as a standalone service or integrate it with existing Active Directory service you already running.
</b></details>

<details>
<summary>What is Azure Advanced Threat Protection?</summary><br><b>
</b></details>

<details>
<summary>What components are part of Azure ATP?</summary><br><b>
</b></details>

<details>
<summary>Where logs are stored in Azure Monitor?</summary><br><b>
</b></details>

<details>
<summary>Explain Azure Site Recovery</summary><br><b>
</b></details>

<details>
<summary>Explain what the advisor does</summary><br><b>
</b></details>

<details>

<summary>Which protocols are available for configuring health probe</summary><br><b>
</b></details>

<details>
<summary>Explain Azure Active</summary><br><b>
</b></details>

<details>
<summary>What is a subscription? What types of subscriptions are there?</summary><br><b>
</b></details>

<details>
<summary>Explain what is a blob storage service</summary><br><b>
</b></details>
