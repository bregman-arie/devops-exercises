# Terraform 

- [Terraform](#terraform)
  - [Exercises](#exercises)
    - [Terraform 101](#terraform-101)
    - [AWS](#aws)
  - [Questions](#questions)
    - [Terraform 101](#terraform-101-1)
    - [Terraform Hands-On Basics](#terraform-hands-on-basics)
    - [Dependencies](#dependencies)
    - [Providers](#providers)
    - [Variables](#variables)
      - [Input Variables](#input-variables)
      - [Output Variables](#output-variables)
      - [Locals](#locals)
      - [Variables Hands-On](#variables-hands-on)
    - [Data Sources](#data-sources)
    - [Lifecycle](#lifecycle)
    - [Provisioners](#provisioners)
    - [State](#state)
      - [Terraform Backend](#terraform-backend)
      - [Workspaces](#workspaces)
      - [State Hands-On](#state-hands-on)
    - [Terraform Structures and Syntax](#terraform-structures-and-syntax)
      - [Lists](#lists)
      - [Loops](#loops)
      - [Maps](#maps)
      - [Conditionals](#conditionals)
      - [Misc](#misc)
    - [Modules](#modules)
      - [Modules Hands-On](#modules-hands-on)
    - [Import](#import)
    - [Version Control](#version-control)
    - [AWS](#aws-1)
    - [Validations](#validations)
    - [Secrets](#secrets)
    - [Production](#production)

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

A DSL called "HCL" (Hashicorp Configuration Language). A declarative language for defining infrastructure.

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
<summary>Explain the following block of Terraform code

```
resource "aws_instance" "some-instance" {
  ami           = "ami-201720221991yay"
  instance_type = "t2.micro
}
```
</summary><br><b>

It's a resource of type "aws_instance" used to provision an instance. The name of the resource (NOT INSTANCE) is "some-instance".

The instance itself will be provisioned with type "t2.micro" and using an image of the AMI "ami-201720221991yay".
</b></details>

<details>
<summary>What do you do next after writing the following in main.tf file?

```
resource "aws_instance" "some-instance" {
  ami           = "ami-201720221991yay"
  instance_type = "t2.micro
}
```
</summary><br><b>

Run `terraform init`. This will scan the code in the directory to figure out which providers are used (in this case AWS provider) and will download them.
</b></details>

<details>
<summary>You've executed <code>terraform init</code> and now you would like to move forward to creating the resources but you have concerns and would like to make be 100% sure on what you are going to execute. What should you be doing?</summary><br><b>

Execute `terraform plan`. That will provide a detailed information on what Terraform will do once you apply the changes.
</b></details>

<details>
<summary>You've downloaded the providers, seen the what Terraform will do (with terraform plan) and you are ready to actually apply the changes. What should you do next?</summary><br><b>

Run `terraform apply`. That will apply the changes described in your .tf files.
</b></details>

<details>
<summary>Explain the meaning of the following strings that seen at the beginning of each line When you run <code>terraform apply</code>

* '+'
* '-'
* '-/+'
</summary><br><b>

* '+' - The resource or attribute is going to be added
* '-' - the resource or attribute is going to be removed
* '-/+' - the resource or attribute is going to be replaced
</b></details>

<details>
<summary>How to cleanup Terraform resources? Why the user shold be careful doing so?</summary><br><b>

`terraform destroy` will cleanup all the resources tracked by Terraform.

A user should be careful with this command because there is no way to revert it. Sure, you can always run again "apply" but that can take time, generates completely new resources, etc.
</b></details>

### Dependencies 

<details>
<summary>Sometimes you need to reference some resources in the same or separate .tf file. Why and how it's done?</summary><br><b>

Why: because resources are sometimes connected or need to be connected. For example, you create an AWS instance with "aws_instance" resource but, at the same time you would like also to allow some traffic to it (because by default traffic is not allowed). For that you'll create a "aws_security_group" resource and then, in your aws_instance resource, you'll reference it.

How:

Using the syntax <PROVIDER TYPE>.<NAME>.<ATTRIBUTE>

In your AWS instance it would like that:

```
resource "aws_instance" "some-instance" {
  
  ami           = "some-ami"
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.instance.id]

}
```
</b></details>

<details>
<summary>Does it matter in which order Terraform creates resources?</summary><br><b>

Yes, when there is a dependency between different Terraform resources, you want the resources to be created in the right order and this is exactly what Terraform does.

To make it ever more clear, if you have a resource X that references the ID of resource Y, it doesn't makes sense to create first resource X because it won't have any ID to get from a resource that wasn't created yet. 
</b></details>

<details>
<summary>Is there a way to print/see the dependencies between the different resources?</summary><br><b>

Yes, with `terraform graph`

The output is in DOT - A graph description language.
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
<summary>How to install a provider? </summary><br><b>

You write a provider block like the following one and run `terraform init`

```
provider "aws" {
  region = "us-west-1"
}
```

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

<details>
<summary>Where providers are downloaded to? (when for example you run <code>terraform init</code>)</summary><br><b>

`.terraform` directory.
</b></details>

<details>
<summary>Describe in high level what happens behind the scenes when you run terraform init on on the following Terraform configuration

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}
```
</summary><br><b>

1. Terraform checks if there is an aws provider in this address: `registry.terraform.io/hashicorp/aws`
2. Installs latest version of aws provider (assuming the URL exists and valid)
</b></details>

<details>
<summary>True or False? You can install providers only from hashicorp</summary><br><b>

False. You can specify any provider from any URL, not only those from hashicorp.
</b></details>

### Variables

#### Input Variables

<details>
<summary>What input variables are good for in Terraform?</summary><br><b>

Variables allow you define piece of data in one location instead of repeating the hardcoded value of it in multiple different locations. Then when you need to modify the variable's value, you do it in one location instead of changing each one of the hardcoded values.
</b></details>

<details>
<summary>What type of input variables are supported in Terraform?</summary><br><b>

```
string
number
bool
list(<TYPE>)
set(<TYPE>)
map(<TYPE>)
object({<ATTR_NAME> = <TYPE>, ... })
tuple([<TYPE>, ...])
```
</b></details>

<details>
<summary>What's the default input variable type in Terraform?</summary><br><b>

`any`
</b></details>

<details>
<summary>What ways are there to pass values for input variables?</summary><br><b>

* Using `-var` option in the CLI
* Using a file by using the `-var-file` option in the CLI
* Environment variable that starts with `TF_VAR_<VAR_NAME>`

If no value given, user will be prompted to provide one.
</b></details>

<details>
<summary>How to reference a variable?</summary><br><b>

Using the syntax `var.<VAR_NAME>`
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
<summary>Whenever you run terraform apply, it prompts to enter a value for a given variable. How to avoid being prompted?</summary><br><b>

While removing the variable is theoretically a correct answer, it will probably fail the execution.

You can use something like the `-var` option to provide the value and avoid being prompted to insert a value. Another option is to run `export TF_VAR_<VAR_NAME>=<VALUE>`.

</b></details>

#### Output Variables

<details>
<summary>What are output variables? Why do we need them?</summary><br><b>

Output variable allow you to display/print certain piece of data as part of Terraform execution.

The most common use case for it is probably to print the IP address of an instance. Imagine you provision an instance and you would like to know what the IP address to connect to it. Instead of looking for it for the console/OS, you can use the output variable and print that piece of information to the screen

</b></details>

<details>
<summary>Explain the "sensitive" parameter of output variable</summary><br><b>

When set to "true", Terraform will avoid logging output variable's data. The use case for it is sensitive data such as password or private keys.

</b></details>

<details>
<summary>Explain the "depends" parameter of output variable</summary><br><b>

It is used to set explicitly dependency between the output variable and any other resource. Use case: some piece of information is available only once another resource is ready.

</b></details>

#### Locals

<details>
<summary>What are locals?</summary><br><b>

Similarly to variables they serve as placeholders for data and values. Differently from variables, users can't override them by passing different values.

</b></details>

<details>
<summary>What's the use case for using locals?</summary><br><b>

You have multiple hardcoded values that repeat themselves in different sections, but at the same time you don't want to expose them as in, allow users to override values.

</b></details>

#### Variables Hands-On

<details>
<summary>Demonstrate input variable definition with type, description and default parameters</summary><br><b>

```
variable "app_id" {
  type = string
  description = "The id of application"
  default = "some_value"
}
```

Unrelated note: variables are usually defined in their own file (vars.tf for example).

</b></details>

<details>
<summary>How to define an input variable which is an object with attributes "model" (string), "color" (string), year (number)?</summary><br><b>

```
variable "car_model" {
  description = "Car model object"
  type        = object({
    model   = string
    color   = string
    year    = number
  })
}
```

Note: you can also define a default for it.

</b></details>

<details>
<summary>How to reference variables?</summary><br><b>

Variable are referenced with `var.VARIABLE_NAME` syntax. Let's have a look at an example:

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
<summary>How to reference variable from inside of string literal? (bonus question: how that type of expression is called?)</summary><br><b>

Using the syntax: `"${var.VAR_NAME}"`. It's called "interpolation".

Very common to see it used in user_data attribute related to instances.

```
user_data = <<-EOF
            This is some fabulos string
            It demonstrates how to use interpolation
            Yes, it's truly ${var.awesome_or_meh}
            EOF
```

</b></details>

<details>
<summary>How can list all outputs without applying Terraform changes?</summary><br><b>

`terraform output` will list all outputs without applying any changes
</b></details>

<details>
<summary>Can you see the output of specific variable without applying terrafom changes?</summary><br><b>

Yes, with `terraform output <OUTPUT_VAR>`.

Very useful for scripts :)
</b></details>

<details>
<summary>Demonstrate how to define locals</summary><br><b>

```
locals {
  x = 2
  y = "o"
  z = 2.2
}
```
</b></details>

<details>
<summary>Demonstrate how to use a local</summary><br><b>

if we defined something like this

```
locals {
  x = 2
}
```

then to use it, you have to use something like this: `local.x`
</b></details>

### Data Sources

<details>
<summary>Explain data sources in Terraform</summary><br><b>

* Data sources used to get data from providers or in general from external resources to Terraform (e.g. public clouds like AWS, GCP, Azure).
* Data sources used for reading. They are not modifying or creating anything
* Many providers expose multiple data sources

</b></details>

<details>
<summary>Demonstrate how to use data sources</summary><br><b>

```
data "aws_vpc" "default {
  default = true
}
```

</b></details>

<details>
<summary>How to get data out of a data source?</summary><br><b>

The general syntax is `data.<PROVIDER_AND_TYPE>.<NAME>.<ATTRBIUTE>`

So if you defined the following data source

```
data "aws_vpc" "default {
  default = true
}
```

You can retrieve the ID attribute this way: `data.aws_vpc.default.id` 
</b></details>

<details>
<summary>Is there such a thing as combining data sources? What would be the use case?</summary><br><b>

Yes, you can define a data source while using another data source as a filter for example.

Let's say we want to get AWS subnets but only from our default VPC:

```
data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}
```

</b></details>

### Lifecycle

<details>
<summary>When you update a resource, how it works?</summary><br><b>

By default the current resource is deleted, a new one is created and any references pointing the old resource are updated to point the new resource

</b></details>

<details>
<summary>Is it possible to modify the default lifecycle? How? Why?</summary><br><b>

Yes, it's possible. There are different lifecycles one can choose from. For example "create_before_destroy" which inverts the order and first creates the new resource, updates all the references from old resource to the new resource and then removes the old resource.

How to use it:

```
lifecycle {
  create_before_destroy = true
}
```

Why to use it in the first place: you might have resources that have dependency where they dependency itself is immutable (= you can't modify it hence you have to create a new one), in such case the default lifecycle won't work because you won't be able to remove the resource that has the dependency as it still references an old resource. AWS ASG + launch configurations is a good example of such use case.

</b></details>

<details>
<summary>You've deployed a virtual machine with Terraform and you would like to pass data to it (or execute some commands). Which concept of Terraform would you use?</summary><br><b>

[Provisioners](https://www.terraform.io/docs/language/resources/provisioners)

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


### State

<details>
<summary>What's Terraform State?</summary><br><b>

[terraform.io](https://www.terraform.io/language/state): "Terraform must store state about your managed infrastructure and configuration. This state is used by Terraform to map real world resources to your configuration, keep track of metadata, and to improve performance for large infrastructures."

In other words, it's a mechanism in Terraform to track resources you've created or cleaned up. This is how terraform knows what to update/create/delete when you run `terraform apply` and also other commands like `terraform destroy`.

</b></details>

<details>
<summary>Where Terraform state is stored?</summary><br><b>

There is more than one answer to this question. It's very much depends on whether you share it with others or it's only local in your Terraform directory, but taking a beginner's case, when you run terraform in a directory, the state will be stored in that directory in `terraform.tfstate` file.

</b></details>

<details>
<summary>Can you name three different things included in the state file?</summary><br><b>

* The representation of resources - JSON format of the resources, their attributes, IDs, ... everything that required to identify the resource and also anything that was included in the .tf files on these resources
* Terraform version
* Outputs
</b></details>

<details>
<summary>Why does it matter where you store the tfstate file? In your answer make sure to address the following:

* Public vs. Private
* Git repository vs. Other locations
</summary><br><b>

- tfstate contains credentials in plain text. You don't want to put it in publicly shared location
- tfstate shouldn't be modified concurrently so putting it in a shared location available for everyone with "write" permissions might lead to issues. (Terraform remote state doesn't has this problem).
- tfstate is an important file. As such, it might be better to put it in a location that has regular backups and good security.
  
As such, tfstate shouldn't be stored in git repositories. secured storage such as secured buckets, is a better option.

</b></details>

<details>
<summary>True or False? it's common to edit terraform state file directly by hand and even recommended for many different use cases</summary><br><b>

False. You should avoid as much possible to edit Terraform state files directly by hand.
</b></details>

<details>
<summary>Why storing state file locally on your computer may be problematic?</summary><br><b>

In general, storing state file on your computer isn't a problem. It starts to be a problem when you are part of a team that uses Terraform and then you would like to make sure it's shared. In addition to being shared, you want to be able to handle the fact that different teams members can edit the file and can do it at the same time, so locking is quite an important aspect as well.
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

To avoid that, Terraform can apply state locking if the backend supports that. For example, AWS s3 supports state locking and consistency via DynamoDB. Often, if the backend supports it, Terraform will make use of state locking automatically so nothing is required from the user to activate it.
</b></details>

<details>
<summary>Describe how you manage state file(s) when you have multiple environments (e.g. development, staging and production)</summary><br><b>

Probably no right or wrong answer here, but it seems, based on different source, that the overall preferred way is to have a dedicated state file per environment.
</b></details>

<details>
<summary>Why storing the state in versioned control repo is not a good idea?</summary><br><b>

* Sensitive data: some resources may specify sensitive data (like passwords and tokens) and everything in a state file is stored in plain text
* Prone to errors: when working with Git repos, you mayo often find yourself switch branches, checkout specific commits, perform rebases, ... all these operations may end up in you eventually performing `terraform apply` on non-latest version of your Terraform code
</b></details>

#### Terraform Backend

<details>
<summary>What's a Terraform backend? What is the default backend?</summary><br><b>

Terraform backend determines how the Terraform state is stored and loaded. By default the state is local, but it's possible to set a remote backend
</b></details>

<details>
<summary>Describe how to set a remote backend of any type you choose</summary><br><b>

Let's say we chose use Amazon s3 as a remote Terraform backend where we can store Terraform's state.

1. Write Terraform code for creating an s3 bucket
   1. It would be a good idea to add lifecycle of "prevent_destroy" to it so it's not accidentally deleted
2. Enable versioning (add a resource of "aws_s3_bucket_versioning")
3. Encrypt the bucket ("aws_s3_bucket_server_side_encryption_configuration")
4. Block public access
5. Handle locking. One way is to add DB for it
6. Add the point you'll want to run init and apply commands to avoid an issue where you at the same time create the resources for remote backend and also switch to a remote backend
7. Once resources were created, add Terraform backend code 

```
terraform {
  backend "s3" {
    bucket ...
  }
}
```
7. Run `teraform init` as it will configure the backend

</b></details>

<details>
<summary>How <code>terraform apply</code> workflow is different when a remote backend is used?</summary><br><b>

It starts with acquiring a state lock so others can't modify the state at the same time.

</b></details>

<details>
<summary>What would be te process of switching back from remote backend to local?</summary><br><b>

1. You remove the backend code and perform `terraform init` to switch back to `local` backend
2. You remove the resources that are the remote backend itself

</b></details>

<details>
<summary>True or False? it's NOT possible to use variable in a backend configuration</summary><br><b>

That's true and quite a limitation as it means you'll have to go to the resources of the remote backend and copy some values to the backend configuration.

One way to deal with it is using partial configurations in a completely separate file from the backend itself and then load them with `terraform init -backend-config=some_backend_partial_conf.hcl`

</b></details>

<details>
<summary>Is there a way to obtain information from a remote backend/state usign Terraform?</summary><br><b>

Yes, using the concept of data sources. There is a data source for a remote state called "terraform_remote_state".

You can use it the following syntax `data.terraform_remote_state.<NAME>.outputs.<ATTRIBUTE>`

</b></details>

#### Workspaces

<details>
<summary>Explain what is a Terraform workspace</summary><br><b>

[developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/state/workspaces): "The persistent data stored in the backend belongs to a workspace. The backend initially has only one workspace containing one Terraform state associated with that configuration. Some backends support multiple named workspaces, allowing multiple states to be associated with a single configuration."

</b></details>

<details>
<summary>True or False? Each workspace has its own state file</summary><br><b>

True

</b></details>

<details>
<summary>Why workspaces might not be the best solution for managing states for different environemnts? like staging and production</summary><br><b>

One reason is that all the workspaces are stored in one location (as in one backend) and usually you don't want to use the same access control and authentication for both staging and production for obvious reasons. Also working in workspaces is quite prone to human errors as you might accidently think you are in one workspace, while you are working a completely different one.
</b></details>


#### State Hands-On

<details>
<summary>Which command will produce a state file?</summary><br><b>

`terraform apply`

</b></details>

<details>
<summary>How to inspect current state?</summary><br><b>

`terraform show`

</b></details>

<details>
<summary>How to list resources created with Terraform?</summary><br><b>

`terraform state list`

</b></details>

<details>
<summary>How do you rename an existing resource?</summary><br><b>

`terraform state mv`

</b></details>

<details>
<summary>How to create a new workspace?</summary><br><b>

`terraform workspace new <WORKSPACE_NAME>`

</b></details>

<details>
<summary>How to identify which workspace are you using?</summary><br><b>

`terraform workspace show`

</b></details>

### Terraform Structures and Syntax

#### Lists

<details>
<summary>How to define an input variable which is a list of numbers?</summary><br><b>

```
variable "list_of_nums" {
  type = list(number)
  description = "An example of list of numbers"
  default = [2, 0, 1, 7]
}
```

</b></details>

<details>
<summary>How to create a number of resources based on the length of a list?</summary><br><b>

```
resource "some_resource" "some_name" {
  count = length(var.some_list)
}
```

</b></details>

<details>
<summary>You have a list variable called "users". How to access the second item in that list and attribute called "name"?</summary><br><b>

`users[1].name`

</b></details>

<details>
<summary>You have a list variable called "users". How to access attribute "name" of all items?</summary><br><b>

`users[*].name`

</b></details>

#### Loops

<details>
<summary>What loops are useful for in Terraform?</summary><br><b>

The most common use case is when you need to create multiple resources with only a slight difference (like different name). Instead of defining multiple separate resources, you can define it once and create multiple instances of it using loops.

</b></details>

<details>
<summary>Demonstrate how to define a simple Terraform loop</summary><br><b>

```
resource "aws_instance" "server" {
  count = 15
}
```

The above configuration will create 15 aws instances.

</b></details>

<details>
<summary>How to create multiple AWS instances but each with a different name?</summary><br><b>

```
resource "aws_instance" "server" {
  count = 6

  tags = {
    Name = "instance-${count.index}"
  }
}
```

The above configuration will create 6 instances, each with a different name.

</b></details>

<details>
<summary>You have the following variable defined in Terraform

```
variable "users" {
  type    = list(string)
  default = ["mario", "luigi", "peach"]
}
```

How to use it to create users on one of the public clouds (or any other platform, infra)?
</summary><br><b>

```
resource "aws_iam_user" "user" {
  count = length(var.users)

  name = var.users[count.index]
}
```

</b></details>

<details>
<summary>Is there any limitation to "count" meta-argument?</summary><br><b>

* `count` isn't supported within an inline block
* It's quite limited when it comes to lists.You'll notice that modifying items in lists or even operations like removal sometimes interpreted in a way you didn't expect. For example, removing an item from a list, may shift other items to a new position and since each position represents a resource with count, that may lead to a result where wrong resources are being modified and removed. There are ways to do deal it, but still using count with lists is not always straightforward
</b></details>

<details>
<summary>What's a for_each loop? How is it different from "count"?</summary><br><b>

* for_each can applied only on collections like maps or sets (as opposed to count that can be applied on lists)
* for_each helps to deal with the limitation of `count` which isn't optimal for use cases of modifying lists
* for_each supports inline blocks as opposed to `count`
</b></details>

<details>
<summary>Demonstrate how to use the for_each loop</summary><br><b>

```
resource “google_compute_instance” “instances” {
  
  for_each = var.names_map
  name = each.value
}
```
</b></details>

<details>
<summary>The following resource tries to use for_each loop on a list of string but it fails, why?

```
resource “google_compute_instance” “instances” {
  
  for_each = var.names
  name = each.value
}
```
</summary><br><b>

for_each can applied only on collections like maps or sets so the list should be converted to a set like this: `for_each = toset(var.names)`

</b></details>

<details>
<summary>How to use for_each loop for inline blocks?</summary><br><b>


```
resouce "some_instance" "instance" {

dynamic "tag" {
  for_each = var.tags

  content {
    key   = tag.key
    value = tag.value
    }
  }
}
```

</b></details>

<details>
<summary>There is a list variable called "users". You would like to define an output variable with a value of all users in uppercase. How to achieve that?</summary><br><b>

```
output "users" {
  value = [for name in var.user_names : upper(name)]
}
```

</b></details>

<details>
<summary>What's the result of the following code?

```
resource "random_integer" "num" {
  min = 20
  max = 17
}

resource "aws_instance" "instances" {
  count = random_integer.num.results
}
```

</summary><br><b>

The above code will fail as it's not possible to reference resource outputs with count, because Terraform has to compute count before any resources are created (or modified).

</b></details>

<details>
<summary>There is a variable called "values" with the following value: ["mario", "luigi", "peach"]. How to create an output variable with the string value of the items in the list: "mario, luigi, peach," ?</summary><br><b>

```
output "users" {
  value = "%{ for name in var.values }${name}, %{ endfor }"
}
```

</b></details>

<details>
<summary>There is a list variable called "users". You would like to define an output variable with a value of all users in uppercase but only if the name is longer than 3 characters. How to achieve that?</summary><br><b>

```
output "users" {
  value = [for name in var.user_names : upper(name) if length(name) > 3]
}
```

</b></details>

#### Maps

<details>
<summary>There is a map called "instances"

* How to extract only the values of that map?
* How to extract only the attribute "name" from each value?
</summary><br><b>

* Using the values built-in function: `values(instances)`
* `values(instances)[*].name`

</b></details>

<details>
<summary>You have a map variable, called "users", with the keys "name" and "age". Define an output list variable with the following "my name is {name} and my age is {age}"</summary><br><b>

```
output "name_and_age" {
  value = [for name, age in var.users : "my name is ${name} and my age is ${age}"]
}
```

</b></details>

<details>
<summary>You have a map variable, called "users", with the keys "name" (string) and "age" (float). Define an output map variable with the key being name in uppercase and value being age in the closest whole number </summary><br><b>

```
output "name_and_age" {
  value = {for name, age in var.users : upper(name) => floor(age) 
}
```

</b></details>

#### Conditionals

<details>
<summary>How to use conditional expressions in Terraform?</summary><br><b>

`some_condition ? "value_if_true" : "value_if_false"`

</b></details>

<details>
<summary>Explain the following condition: <code>var.x ? 1 : 0</code></summary><br><b>

If `x` evaluated to true, the result is 1, otherwise (if false) the result is 0.

</b></details>

<details>
<summary>Explain the following condition: <code>var.x != "" ? var.x : "yay"</code></summary><br><b>

If `x` is an empty string the result is "yay", otherwise it's the value of `x` variable

</b></details>

<details>
<summary>Can conditionals be used with meta-arguments?</code></summary><br><b>

Yes, for example the "count" meta-argument:

```
resource "aws_instance" "server" {
  count = var.amount ? 1 : 0
  ...
}
```

</b></details>

<details>
<summary>Is it possible to combine conditionals and loop?</code></summary><br><b>

Yes, for example:

```
dynamic "tag" {
  for_each = {
    for key, value in var.tags:
    key => value
    if key != ""
  }
}
```

</b></details>

#### Misc

<details>
<summary>What are meta-arguments in Terraform?</summary><br><b>

Arguments that affect the lifecycle of a resources (its creation, modification, ...) and supported by Terraform regardless to the type of resource in which they are used.

Some examples:

* count: how many resources to create out of one definition of a resource
* lifecycle: how to treat resource creation or removal

</b></details>

<details>
<summary>What meta-arguments are you familiar with?</summary><br><b>

* count: how many resources to create out of one definition of a resource
* lifecycle: how to treat resource creation or removal
* depends_on: create a dependency between resources
</b></details>

<details>
<summary>What <code>templatefile</code> function does?</summary><br><b>

Renders a template file and returns the result as string.

</b></details>

<details>
<summary>You are trying to use templatefile as part of a module and you use a relative path to load a file but sometimes it fails, especially when others try to reuse the module. How can you deal with that?</summary><br><b>

Switch relative paths with what is known as path references. These are fixes paths like module root path, module expression file path, etc.

</b></details>

<details>
<summary>How do you test terraform syntax?</summary><br><b>

A valid answer could be "I write Terraform configuration and try to execute it" but this makes testing cumbersome and quite complex in general.

There is `terraform console` command which allows you to easily execute terraform functions and experiment with general syntax.

</b></details>

<details>
<summary>True or False? Terraform console should be used carefully as it may modify your resources</summary><br><b>

False. terraform console is ready-only.

</b></details>

<details>
<summary>You need to render a template and get it as string. Which function would you use?</summary><br><b>

`templatefile` function.

</b></details>

<details>
<summary>Explain what <code>depends_on</code> used for and given an example</summary><br><b>

`depends_on` used to create a dependency between resources in Terraform. For example, there is an application you would like to deploy in a cluster. If the cluster isn't ready (and also managed by Terraform of course) then you can't deploy the app. In this case, you will define "depends_on" in the app configuration and its value will be the cluster resource.

</b></details>

### Modules

<details>
<summary>Explain Modules</summary>

[Terraform.io](https://www.terraform.io/language/modules/develop): "A module is a container for multiple resources that are used together. Modules can be used to create lightweight abstractions, so that you can describe your infrastructure in terms of its architecture, rather than directly in terms of physical objects."

In addition, modules are great for creating reusable Terraform code that can be shared and used not only between different repositories but even within the same repo, between different environments (like staging and production).

</b></details>

<details>
<summary>What makes a Terraform code module? In other words, what a module is from practical perspective?</summary>

Basically any file or files in a directory is a module in Terraform. There is no special syntax to use in order to define a module.

</b></details>

<details>
<summary>How do you test a Terraform module?</summary><br><b>

There are multiple answers, but the most common answer would likely to be using the tool <code>terratest</code>, and to test that a module can be initialized, can create resources, and can destroy those resources cleanly.

</b></details>

<details>
<summary>When creating a module, do you prefer to use inline blocks, separate resources or both? why?</summary>

No right or wrong here.

Personally, I prefer to use only separate resources in modules as it makes modules more flexible. So if a resource includes inline blocks, that may limit you at some point.

</b></details>

<details>
<summary>True or False? Module source can be only local path</summary>

False. It can be a Git URL, HTTP URL, ... for example:

```
module "some_module" {

  source = "github.com/foo/modules/bar?ref=v0.1"
}
```

</b></details>

<details>
<summary>Where can you obtain Terraform modules?</summary><br><b>

Terraform modules can be found at the [Terrafrom registry](https://registry.terraform.io/browse/modules)

</b></details>

<details>
<summary>You noticed there are relative paths in some of your modules and you would like to change that. What can you do and why is that a problem in the first place?</summary><br><b>

Relative paths usually work fine in your own environment as you are familiar with the layout and paths used, but when sharing a module and making it reusable, you may bump into issues as it runs on different environments where the relative paths may no longer be relevant.

A better approach would be to use `path reference` like one of the following:

* `path.module`: the path of the module where the expression is used
* `path.cwd`: the path of the current working directory
* `path.root`: the path of the root module

</b></details>

#### Modules Hands-On

<details>
<summary>How to use a module?</summary><br><b>

The general syntax is:

```
module "<MODULE_NAME>" {
  source = "<MODULE_SOURCE>"

  ...
}
```

The critical part is the source which you use to tell Terraform where the module can be found.
</b></details>

<details>
<summary>Demonstrate using a module called "amazing_modle" in the path "../modules/amazing-module"</summary><br><b>

```
module "amazing_module" {
  source = "../modules/amazing-module"
}
```
</b></details>

<details>
<summary>What should be done every time you modify the source parameter of a module?</summary><br><b>

`terraform init` should be executed as it takes care of downloading and installing the module from the new path.
</b></details>

<details>
<summary>How to access module output variables?</summary><br><b>

the general syntax is `module.<MODULE_NAME>.<OUTPUT_VAR_NAME>`

</b></details>

<details>
<summary>You would like to load and render a file from module directory. How to do that?</summary><br><b>

script = templatesfile("${path.module}/user-data.sh", {
  ...
})
</b></details>

<details>
<summary>There is a module to create a compute instance. How would you use the module to create three separate instances?</summary><br><b>

starting with Terraform 0.13, the `count` meta-argument can be used with modules. So you could use something like this:

```
module "instances" {
  source = "/some/module/path"

  count = 3
}
```

You can also use it in outputs vars: `value = module.instances[*]`

</b></details>

### Import

<details>
<summary>Explain Terraform's import functionality</summary><br><b>

`terraform import` is a CLI command used for importing an existing infrastructure into Terraform's state.

It's does NOT create the definitions/configuration for creating such infrastructure.

</b></details>

<details>
<summary>State two use cases where you would use <code>terraform import</code></summary><br><b>

1. You have existing resources in one of the providers and they are not managed by Terraform (as in not included in the state)
2. You lost your tfstate file and need to rebuild it

</b></details>

### Version Control

<details>
<summary>You have a Git repository with Terraform files but no .gitignore. What would you add to a .gitignore file in Terraform repository?</summary><br><b>

```
.terraform
*.tfstate
*.tfstate.backup
```

You don't want to store state file nor any downloaded providers in .terraform directory. It also doesn't makes sense to share/store the state backup files.

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

<details>
<summary>You manage ASG with Terraform which means you also have "aws_launch_configuration" resources. The problem is that launch configurations are immutable and sometimes you need to change them. This creates a problem where Terraform isn't able to delete ASG because they reference old launch configuration. How to do deal with it?</summary><br><b>

Add the following to "aws_launch_configuration" resource

```
lifecycle {
  create_before_destroy = true
}
```

This will change the order of how Terraform works. First it will create the new resource (launch configuration). then it will update other resources to reference the new launch configuration and finally, it will remove old resources

</b></details>

<details>
<summary>How to manage multiple regions in AWS provider configuration?</summary><br><b>

```
provider "aws" {
  region = "us-west-1"
  alias = "west_region"
}

provider "aws" {
  region = "us-east-1"
  alias = "east_region"
}

data "aws_region" "west_region" {
  provider = aws.west_region
}

data "aws_region" "east_region" {
  provider = aws.east_region
}
```

To use it:

```
resource "aws_instance" "west_region_instance" {
  provider = aws.west_region
  instance_type = "t2.micro"
  ...
}
```

</b></details>

<details>
<summary>Assuming you have multiple regions configured and you would like to use a module in one of them. How to achieve that?</summary><br><b>

```
module "some_module" {
  source = "..."

  providers = {
    aws = aws.some_region
  }

  ...
}
```

</b></details>

<details>
<summary>How to manage multiple AWS accounts?</summary><br><b>

One way is to define multiple different provider blocks, each with its own "assume_role"

```
provider "aws" {
  region = "us-west-1"
  alias = "some-region"

  assume_role {
    role_arn = "arn:aws:iam::<SOME_ACCOUNT_ID>:role/<SOME_ROLE_NAME>"
  }
}
```

</b></details>

### Validations

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

### Secrets

<details>
<summary>What's the issue with the following provider configuration?

```
provider "aws" {
  region = "us-west-1"

  access_key = "blipblopblap"
  secret_key = "bipbopbipbop"
}
```
</summary><br><b>

It's not secure! you should never store credentials in plain text this way. 

</b></details>

<details>
<summary>What can you do to NOT store provider credentials in Terraform configuration files in plain text?</summary><br><b>

1. Use environment variables
2. Use password CLIs (like 1Password which is generic but there also specific provider options like aws-vault)

</b></details>

<details>
<summary>How can you manage secrets/credentials in CI/CD?</summary><br><b>

That very much depends on the CI/CD system/platform you are using.

- GitHub Actions: Use Open ID Connect (OIDC) to establish connection with your provider. You then can specify in your GitHub Actions workflow the following:

```
- uses: aws-actions/configure-aws-credentials@v1
with:
 role-to-assume: arn:aws:iam::someIamRole
 aws-region: ...
```


- Jenkins: If Jenkins runs on the provider, you can use the provider access entities (like roles, policies, ...) to grant the instance, on which Jenkins is running, access control
- CircleCI: you can use `CircleCI Context` and then specify it in your CircleCI config file

```
context:
- some-context
```

</b></details>

<details>
<summary>What are the pros and cons of using environment variables for managing secrets in Terraform configurations?</summary><br><b>

Pros:
 * You avoid using secrets directly in configurations in plain text
 * free (no need to pay for secret management platforms/solutions)
 * Straightforward to use

Cons:
  * Configurations might not be usable without the environment variables which may make impact the user experience as the user has to know what environment variables he should pass for everything to work properly
  * Mostly managed outside of Terraform mechanisms which makes it hard to enforce, track, ... anything that is related to secrets when it depends on the user to pass environment variables

</b></details>

<details>
<summary>True or False? If you pass secrets with environment variables, they are not visible in your state file</summary><br><b>

False. State files include sensitive data as it is. Which means it's very important that wherever you store your state file, it's encrypted and accessible only to those who should be able to access it.

</b></details>

<details>
<summary>True or False? If you pass secrets from a centralized secrets store (like Hashicorp Vault) they are not visible in plan files (terraform plan)</summary><br><b>

False. It doesn't matter where your secrets store (file, environment variables, centralized secrets store), they will be visible in both state file and plan output.

</b></details>

### Production

This section is about how Terraform is actually used in real-life scenarios and organizations.

<details>
<summary>What structure layout do you use for your projects?</summary><br><b>

There is no right or wrong answer, just what you personally adopted or your team, and being able to explain why.

One common approach is to have a separate directory for each environment.

```
terraform_project/
  staging/
  production/
```

Each environment has its own backend (as you don't want to use the same authentication and access controls for all environments)

Going further, under each environment you'll separate between comoponents, applications and services


```
terraform_project/
  staging/
    applications/
      some-app-service-1/
      some-app-service-2/
    databases/
      mongo/
      postgres/
    networking/
```
</b></details>

<details>
<summary>What files do you have you have in your Terraform projects?</summary><br><b>

Again, no right or wrong answer. Just your personal experience.

main.tf
providers.tf
outputs.tf
variables.tf
dependencies.tf

Each one of these files can be divided to smaller parts if needed (no reason to maintain VERY long files)

</b></details>

<details>
<summary>An engineer in your team complains about having to copy-paste quite a lot of code between different folders and files of Terraform. What would you do?</summary><br><b>

Suggest to use Terraform modules.

</b></details>

<details>
<summary>When working with nested layout of many directories, it can make it cumbresome to run terraform commands in many different folders. How to deal with it?</summary><br><b>

There are multiple ways to deal with it:
1. Write scripts that perform some commands recurisvely with different conditions
2. Use tools like Terragrunt where you commands like "run-all" that can run in parallel on multiple different paths

</b></details>

<details>
<summary>One of the engineers in your team complains the inline shell scripts are quite big and maintaining them in Terraform files seems like a bad idea. What would you do?</summary><br><b>

A good solution for not including shell scripts inline (as in inside terraform configuration files) is to keep them in a separate file and then use the terraform `templatefile` function to render and get them as a string

</b></details>

<details>
<summary>You noticed a lot of your Terraform code/configuration is duplicated, between repositories and also within the same repository between different directories. What one way you may adopt that will help handling with that?</summary><br><b>

Using Terraform modules can help greatly with duplicated code and so different environments for example (staging and production) can reuse the same code by using the same modules.

</b></details>

<details>
<summary>You noticed your Terraform code includes quite a lot of hardcoded values (like ports, subnets, ...) and they are duplicated in many locations. How'd you deal with it?</summary><br><b>

Using variables might not be a good solution because some things shouldn't be exposed and accidentally overridden. In such case you might want to use the concept of `locals`

</b></details>

<details>
<summary>Every time there is a change in tags standards (for example your team decided to change one of the tags' name) you find yourself changing tags in multiple files and you find the process quite tedious. What can be done about it?</summary><br><b>

Instead of defining tags at resource level, consider using `default_tags` as part of the provider configuration.

</b></details>

<details>
<summary>You would like to change the name of a resource but afraid to cause downtime. What can be done?</summary><br><b>

If it's a matter of changing a resource name, you could make use of `terraform state mv <ORIGINAL_RESOURCE_NAME> <NEW_RESOURCE_NAME>`

</b></details>

<details>
<summary>You try to deploy a cluster and an app on that cluster, but the app resource was created before the cluster. How to manage such situation?</summary><br><b>

Use the meta-argument `depends_on` in the app resource definition. This way the app will depend on the cluster resource and order will be maintained in creation of the resources.

</b></details>