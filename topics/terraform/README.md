# Terraform 

- [Terraform](#terraform)
  - [Exercises](#exercises)
    - [Terraform 101](#terraform-101)
    - [AWS](#aws)
  - [Questions](#questions)
    - [Terraform 101](#terraform-101-1)
    - [Terraform Hands-On Basics](#terraform-hands-on-basics)
    - [Providers](#providers)
    - [Provisioners](#provisioners)
    - [Modules](#modules)
    - [Variables](#variables)
    - [State](#state)
    - [Import](#import)
    - [AWS](#aws-1)

## Exercises

<a name="exercises-terraform-101"></a>
### Terraform 101

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Local Provider  | Basics | [Exercise](exercises/terraform_local_provider/exercise.md) | [Solution](exercises/terraform_local_provider/solution.md) | |

### AWS

 The following exercises require account in AWS and might cost you $$$

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Launch EC2 instance | EC2 | [Exercise](exercises/launch_ec2_instance/exercise.md) | [Solution](exercises/launch_ec2_instance/solution.md) | |
| Rename S3 bucket | S3 | [Exercise](exercises/s3_bucket_rename/exercise.md) | [Solution](exercises/s3_bucket_rename/solution.md) | |

## Questions

### Terraform 101

<details>
<summary>What is Terraform?</summary><br><b>

[Terraform](https://www.terraform.io/intro): "HashiCorp Terraform is an infrastructure as code tool that lets you define both cloud and on-prem resources in human-readable configuration files that you can version, reuse, and share. You can then use a consistent workflow to provision and manage all of your infrastructure throughout its lifecycle. Terraform can manage low-level components like compute, storage, and networking resources, as well as high-level components like DNS entries and SaaS features."
</b></details>


<details>
<summary>What are the advantages in using Terraform or IaC in general?</summary><br><b>

- Full automation: In the past, resource creation, modification and removal were handled manually or by using a set of tooling. With Terraform or other IaC technologies, you manage the full lifecycle in an automated fashion.<br>
- Modular and Reusable: Code that you write for certain purposes can be used and assembled in different ways. You can write code to create resources on a public cloud and it can be shared with other teams who can also use it in their account on the same (or different) cloud><br>
- Improved testing: Concepts like CI can be easily applied on IaC based projects and code snippets. This allow you to test and verify operations beforehand
- 
</b></details>

<details>
<summary>What are some of Terraform features?</summary><br><b>

- Declarative: Terraform uses the declarative approach (rather than the procedural one) in order to define end-status of the resources
- No agents: as opposed to other technologies (e.g. Puppet) where you use a model of agent and server, with Terraform you use the different APIs (of clouds, services, etc.) to perform the operations
- Community: Terraform has strong community who constantly publishes modules and fixes when needed. This ensures there is good modules maintenance and users can get support quite quickly at any point
- 
</b></details>

<details>
<summary>What language does Terraform uses?</summary><br><b>

A DSL called "HCL" (Hashiciorp Configuration Language). A declarative language for defining infrastructure.

</b></details>

<details>
<summary>What's a typical Terraform workflow?</summary><br><b>

1. Write Terraform definitions: `.tf` files written in HCL that described the desired infrastructure state (and run `terraform init` at the very beginning)
2. Review: With command such as `terraform plan` you can get a glance at what Terraform will perform with the written definitions
3. Apply definitions: With the command `terraform apply` Terraform will apply the given definitions, by adding, modifying or removing the resources

This is a manual process. Most of the time this is automated so user submits a PR/MR to propose terraform changes, there is a process to test these changes and once merged they are applied (`terraform apply`).

</b></details>

<details>
<summary>What are some use cases for using Terraform?</summary><br><b>

- Infra provisioning and management: You need to automated or code your infra so you are able to test it easily, apply it and make any changes necessary.
- Multi-cloud environment: You manage infrastructure on different clouds, but looking for a consistent way to do it across the clouds
- Consistent environments: You manage environments such as test, production, staging, ... and looking for a way to have them consistent so any modification in one of them, applies to other environments as well

</b></details>

<details>
<summary>What's the difference between Terraform and technologies such as Ansible, Puppet, Chef, etc.</summary><br><b>

Terraform is considered to be an IaC technology. It's used for provisioning resources, for managing infrastructure on different platforms.

Ansible, Puppet and Chef are Configuration Management technologies. They are used once there is an instance running and you would like to apply some configuration on it like installing an application, applying security policy, etc.

To be clear, CM tools can be used to provision resources so in the end goal of having infrastructure, both Terraform and something like Ansible, can achieve the same result. The difference is in the how. Ansible doesn't saves the state of resources, it doesn't know how many instances there are in your environment as opposed to Terraform. At the same time while Terraform can perform configuration management tasks, it has less modules support for that specific goal and it doesn't track the task execution state as Ansible. The differences are there and it's most of the time recommended to mix the technologies, so Terraform used for managing infrastructure and CM technologies used for configuration on top of that infrastructure.

</b></details>

### Terraform Hands-On Basics

<details>
<summary>How to reference other parts of your Terraform code?</summary><br><b>

Using the syntax <PROVIDER TYPE>.<NAME>.<ATTRIBUTE>
</b></details>

### Providers

<details>
<summary>Explain what is a "provider"</summary><br><b>

[terraform.io](https://www.terraform.io/docs/language/providers/index.html): "Terraform relies on plugins called "providers" to interact with cloud providers, SaaS providers, and other APIs...Each provider adds a set of resource types and/or data sources that Terraform can manage. Every resource type is implemented by a provider; without providers, Terraform can't manage any kind of infrastructure."
</b></details>

<details>
<summary>Where can you find publicly available providers?</summary><br><b>

In the [Terraform Registry](https://registry.terraform.io/browse/providers) 
</b></details>

<details>
<summary>What are the names of the providers in this case?

```
terraform {
    required_providers {
      aws = {
        source  = "hashicorp/aws"
      }
      azurerm = {
        source  = "hashicorp/azurerm"
        version = "~> 3.0.2"
      }
    }
  }
```
</summary><br><b>

azurerm and aws
</b></details>

<details>
<summary>True or False? Applying the following Terraform configuration will fail since no source or version specific for 'aws' provider

```
terraform {
    required_providers {
      aws = {}
    }
  }
```
</summary><br><b>

False. It will look for "aws" provider in the public Terraform registry and will take the latest version.
</b></details>

<details>
<summary>Write a configuration of a Terraform provider (any type you would like)</summary><br><b>

AWS is one of the most popular providers in Terraform. Here is an example of how to configure it to use one specific region and specifying a specific version of the provider

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-west-2"
}
```
</b></details>

<details>
<summary>Where Terraform installs providers from by default? </summary><br><b>

By default Terraform providers are installed from Terraform Registry
</b></details>

<details>
<summary>What is the Terraform Registry?</summary><br><b>

The Terraform Registry provides a centralized location for official and community-managed providers and modules.
</b></details>

### Provisioners

<details>
<summary>What are "Provisioners"? What they are used for?</summary><br><b>

Provisioners can be described as plugin to use with Terraform, usually focusing on the aspect of service configuration and make it operational.

Few example of provisioners:

* Run configuration management on a provisioned instance using technology like Ansible, Chef or Puppet.
* Copying files
* Executing remote scripts
</b></details>

<details>
<summary>Why is it often recommended to use provisioners as last resort?</summary><br><b>

Since a provisioner can run a variety of actions, it's not always feasible to plan and understand what will happen when running a certain provisioner. For this reason, it's usually recommended to use Terraform built-in option, whenever's possible.
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
<code>terraform taint resource.id</code> manually marks the resource as tainted in the state file. So when you run <code>terraform apply</code> the next time, the resource will be destroyed and recreated.
</b></details>

<details>
<summary>What is a data source? In what scenarios for example would need to use it?</summary><br><b>
Data sources lookup or compute values that can be used elsewhere in terraform configuration.

There are quite a few cases you might need to use them:
* you want to reference resources not managed through terraform
* you want to reference resources managed by a different terraform module
* you want to cleanly compute a value with typechecking, such as with <code>aws_iam_policy_document</code>
</b></details>

<details>
<summary>What are output variables and what <code>terraform output</code> does?</summary><br><b>
Output variables are named values that are sourced from the attributes of a module. They are stored in terraform state, and can be used by other modules through <code>remote_state</code>
</b></details>

<details>
<summary>Explain <code>remote-exec</code> and <code>local-exec</code></summary><br><b>
</b></details>


<details>
<summary>Explain "Remote State". When would you use it and how?</summary><br><b>
  Terraform generates a `terraform.tfstate` json file that describes components/service provisioned on the specified provider. Remote
  State stores this file in a remote storage media to enable collaboration amongst team.
</b></details>

<details>
<summary>Explain "State Locking"</summary><br><b>
  State locking is a mechanism that blocks an operations against a specific state file from multiple callers so as to avoid conflicting operations from different team members. Once the first caller's operation's lock is released the other team member may go ahead to
  carryout his own operation. Nevertheless Terraform will first check the state file to see if the desired resource already exist and
  if not it goes ahead to create it.
</b></details>

<details>
<summary>Aside from <code>.tfvars</code> files or CLI arguments, how can you inject dependencies from other modules?</summary><br><b>
  The built-in terraform way would be to use <code>remote-state</code> to lookup the outputs from other modules.
  It is also common in the community to use a tool called <code>terragrunt</code> to explicitly inject variables between modules.
</b></details>

<details>
<summary>How do you import existing resource using Terraform import?</summary><br><b>

1. Identify which resource you want to import.
2. Write terraform code matching configuration of that resource.
3. Run terraform command <code>terraform import RESOURCE ID</code><br>

eg. Let's say you want to import an aws instance. Then you'll perform following:
1. Identify that aws instance in console
2. Refer to it's configuration and write Terraform code which will look something like:
```
resource "aws_instance" "tf_aws_instance" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    Name = "import-me"
  }
}
```
3. Run terraform command <code>terraform import aws_instance.tf_aws_instance i-12345678</code>
</b></details>

### Modules

<details>
<summary>Explain Modules</summary>

[Terraform.io](https://www.terraform.io/language/modules/develop): "A module is a container for multiple resources that are used together. Modules can be used to create lightweight abstractions, so that you can describe your infrastructure in terms of its architecture, rather than directly in terms of physical objects."
</b></details>

<details>
<summary>How do you test a terraform module?</summary><br><b>

There are multiple answers, but the most common answer would likely to be using the tool <code>terratest</code>, and to test that a module can be initialized, can create resources, and can destroy those resources cleanly.
</b></details>

<details>
<summary>Where can you obtain Terraform modules?</summary><br><b>

Terraform modules can be found at the [Terrafrom registry](https://registry.terraform.io/browse/modules)
</b></details>

<details>
<summary>There's a discussion in your team whether to store modules in one centralized location/repository or have them in each of the projects/repositories where they are used. What's your take on that?</summary><br><b>

You might have a different opinion but my personal take on that, is to keep modules in one centralized repository as any maintenance or updates to the module you need to perform, are done in one place instead of multiple times in different repositories.
</b></details>

### Variables

<details>
<summary>What types of variables are supported in Terraform?</summary><br><b>

string
number
bool
list(<TYPE>)
set(<TYPE>)
map(<TYPE>)
object({<ATTR_NAME> = <TYPE>, ... })
tuple([<TYPE>, ...])
</b></details>

<details>
<summary>What are Input Variables in Terraform? Why one should use them?</summary><br><b>

Input variables serve as parameters to the module in Terraform. They allow you for example to define once the value of a variable and use that variable in different places in the module so next time you would want to change the value, you will change it in one place instead of changing the value in different places in the module.
</b></details>

<details>
<summary>How to define variables?</summary><br><b>

```
variable "app_id" {
  type = string
  description = "The id of application"
  default = "some_value"
}
```

Usually they are defined in their own file (vars.tf for example).
</b></details>

<details>
<summary>How variables are used in modules?</summary><br><b>

They are referenced with `var.VARIABLE_NAME`

vars.tf:

```
variable "memory" {
  type = string
  default "8192"
}

variable "cpu" {
  type = string
  default = "4"
}
```

main.tf:

```
resource "libvirt_domain" "vm1" {
   name = "vm1"
   memory = var.memory
   cpu = var.cpu
}
```
</b></details>

<details>
<summary>How would you enforce users that use your variables to provide values with certain constraints? For example, a number greater than 1</summary><br><b>

Using `validation` block

```
variable "some_var" {
  type = number
  
  validation {
    condition = var.some_var > 1
    error_message = "you have to specify a number greater than 1"
  }

}
```
</b></details>

<details>
<summary>What is the effect of setting variable as "sensitive"?</summary><br><b>

It doesn't show its value when you run `terraform apply` or `terraform plan` but eventually it's still recorded in the state file.
</b></details>

<details>
<summary>True or False? If an expression's result depends on a sensitive variable, it will be treated as sensitive as well</summary><br><b>

True
</b></details>

<details>
<summary>The same variable is defined in the following places:

  - The file `terraform.tfvars`
  - Environment variable
  - Using `-var` or `-var-file`
  
According to variable precedence, which source will be used first?</summary><br><b>

The order is:

  - Environment variable
  - The file `terraform.tfvars`
  - Using `-var` or `-var-file`
</b></details>

<details>
<summary>What other way is there to define lots of variables in more "simplified" way?</summary><br><b>

Using `.tfvars` file which contains variable consists of simple variable names assignments this way:

```
x = 2
y = "mario"
z = "luigi"
```
</b></details>

### State

<details>
<summary>What's Terraform State?</summary><br><b>

[Terraform.io](https://www.terraform.io/language/state): "Terraform must store state about your managed infrastructure and configuration. This state is used by Terraform to map real world resources to your configuration, keep track of metadata, and to improve performance for large infrastructures."
</b></details>

<details>
<summary>What <code>terraform.tfstate</code> file is used for?</summary><br><b>

It keeps track of the IDs of created resources so that Terraform knows what it's managing.
</b></details>

<details>
<summary>How to inspect current state?</summary><br><b>

terraform show
</b></details>

<details>
<summary>How to list resources created with Terraform?</summary><br><b>

terraform state list
</b></details>

<details>
<summary>How do you rename an existing resource?</summary><br><b>

terraform state mv
</b></details>

<details>
<summary>Why does it matter where you store the tfstate file? Where would you store it?</summary><br><b>

  - tfstate contains credentials in plain text. You don't want to put it in publicly shared location
  - tfstate shouldn't be modified concurrently so putting it in a shared location available for everyone with "write" permissions might lead to issues. (Terraform remote state doesn't has this problem).
  - tfstate is in important file. As such, it might be better to put it in a location that has regular backups.

As such, tfstate shouldn't be stored in git repositories. secured storage such as secured buckets, is a better option.
</b></details>

<details>
<summary>Which command is responsible for creating state file?</summary><br><b>

  - terraform apply file.terraform
  - Above command will create tfstate file in the working folder.
</b></details>

<details>
<summary>By default where does the state get stored?</summary><br><b>

  - The state is stored by default in a local file named terraform.tfstate.
</b></details>

<details>
<summary>What is Terraform import?</summary><br><b>

Terraform import is used to import existing infrastructure. It allows you to bring resources created by some other means (eg. manually launched cloud resources) and bring it under Terraform management. 
</b></details>

<details>
<summary>Can we store tfstate file at remote location? If yes, then in which condition you will do this?</summary><br><b>

  - Yes, It can also be stored remotely, which works better in a team environment. Given condition that remote location is not publicly accessible since tfstate file contain sensitive information as well. Access to this remote location must be only shared with team members.
</b></details>

<details>
<summary>Mention some best practices related to tfstate</summary><br><b>

  - Don't edit it manually. tfstate was designed to be manipulated by terraform and not by users directly.
  - Store it in secured location (since it can include credentials and sensitive data in general)
  - Backup it regularly so you can roll-back easily when needed 
  - Store it in remote shared storage. This is especially needed when working in a team and the state can be updated by any of the team members
  - Enabled versioning if the storage where you store the state file, supports it. Versioning is great for backups and roll-backs in case of an issue.
</b></details>

<details>
<summary>How and why concurrent edits of the state file should be avoided?</summary><br><b>

If there are two users or processes concurrently editing the state file it can result in invalid state file that doesn't actually represents the state of resources.<br>

To avoid that, Terraform can apply state locking if the backend supports that. For example, AWS s3 supports state locking and consistency via DynamoDB. Often, if the backend support it, Terraform will make use of state locking automatically so nothing is required from the user to activate it.
</b></details>

<details>
<summary>Describe how you manage state file(s) when you have multiple environments (e.g. development, staging and production)</summary><br><b>

There is no right or wrong here, but it seems that the overall preferred way is to have a dedicated state file per environment.
</b></details>

<details>
<summary>How to write down a variable which changes by an external source or during <code>terraform apply</code>?</summary><br><b>

You use it this way: <code>variable “my_var” {}</code>
</b></details>

<details>
<summary>You've deployed a virtual machine with Terraform and you would like to pass data to it (or execute some commands). Which concept of Terraform would you use?</summary><br><b>

[Provisioners](https://www.terraform.io/docs/language/resources/provisioners)
</b></details>

### Import

<details>
<summary>Explain Terraform's import functionality</summary><br><b>

`terraform import` is a CLI command used for importing an existing infrastructure into Terraform's state.

It's does NOT create the definitions/configuration for creating such infrastructure
</b></details>

<details>
<summary>State two use cases where you would use <code>terraform import</code></summary><br><b>

1. You have existing resources in the cloud and they are not managed by Terraform (as in not included in the state)
2. You lost your tfstate file and need to rebuild it
</b></details>

### AWS

<details>
<summary>What happens if you update user_data in the following case apply the changes?

```
resource "aws_instance" "example" {
 ami = "..."
 instance_type = "t2.micro"

user_data = <<-EOF
            #!/bin/bash
            echo "Hello, World" > index.xhtml
            EOF
```
</summary><br><b>

Nothing, because user_data is executed on boot so if an instance is already running, it won't change anything.

To make it effective you'll have to use `user_data_replace_on_change = true`.
</b></details>