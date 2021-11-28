## Terraform

<details>
<summary>Explain what Terraform is and how does it works</summary><br><b>

[Terraform.io](https://www.terraform.io/intro/index.html#what-is-terraform-): "Terraform is an infrastructure as code (IaC) tool that allows you to build, change, and version infrastructure safely and efficiently."<br>
</b></details>

<details>
<summary>Why one would prefer using Terraform and not other technologies? (e.g. Ansible, Puppet, CloudFormation)</summary><br><b>

A common *wrong* answer is to say that Ansible and Puppet are configuration management tools
and Terraform is a provisioning tool. While technically true, it doesn't mean Ansible and Puppet can't
be used for provisioning infrastructure. Also, it doesn't explain why Terraform should be used over
CloudFormation if at all.

The benefits of Terraform over the other tools:

  * It follows the immutable infrastructure approach which has benefits like avoiding a configuration drift over time
  * Ansible and Puppet are more procedural (you mention what to execute in each step) and Terraform is declarative since you describe the overall desired state and not per resource or task. You can give the example of going from 1 to 2 servers in each tool. In Terraform you specify 2, in Ansible and puppet you have to only provision 1 additional server so you need to explicitly make sure you provision only another one server.
</b></details>

<details>
<summary>How do you structure your Terraform projects?</summary><br><b>

terraform_directory
   providers.tf -> List providers (source, version, etc.)
   variables.tf -> any variable used in other files such as main.tf
   main.tf -> Lists the resources
</b></details>

<details>
<summary>True or False? Terraform follows the mutable infrastructure paradigm</summary><br><b>

False. Terraform follows immutable infrastructure paradigm.
</b></details>

<details>
<summary>True or False? Terraform uses declarative style to describe the expected end state</summary><br><b>
True
</b></details>

<details>
<summary>What is HCL?</summary><br><b>
HCL stands for Hashicorp Configuration Language. It is the language Hashicorp made to use as the configuration language for a number of its tools, including terraform.
</b></details>

<details>
<summary>Explain what is "Terraform configuration"</summary><br><b>

A configuration is a root module along with a tree of child modules that are called as dependencies from the root module.
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
<code>terraform validate</code> checks if configuration is syntactically valid and internally consistent within a directory.
<code>terraform apply</code> will provision the resources specified in the .tf files.
</b></details>

#### Terraform - Resources

<details>
<summary>What is a "resource"?</summary><br><b>

HashiCorp: "Terraform uses resource blocks to manage infrastructure, such as virtual networks, compute instances, or higher-level components such as DNS records. Resource blocks represent one or more infrastructure objects in your Terraform configuration."
</b></details>

<details>
<summary>Explain each part of the following line: `resource "aws_instance" "web_server" {...}`</summary><br><b>

  - resource: keyword for defining a resource
  - "aws_instance": the type of the resource
  - "web_server": the name of the resource
</b></details>

<details>
<summary>What is the ID of the following resource: `resource "aws_instance" "web_server" {...}`</summary><br><b>

`aws_instance.web_server`
</b></details>

<details>
<summary>True or False? Resource ID must be unique within a workspace</summary><br><b>

True
</b></details>

<details>
<summary>Explain each of the following in regards to resources

  * Arguments
  * Attributes
  * Meta-arguments</summary><br><b>
  
  - Arguments: resource specific configurations
  - Attributes: values exposed by the resource in a form of `resource_type.resource_name.attribute_name`. They are set by the provider or API usually.
  - Meta-arguments: Functions of Terraform to change resource's behavior
</b></details>

#### Terraform - Providers

<details>
<summary>Explain what is a "provider"</summary><br><b>

[terraform.io](https://www.terraform.io/docs/language/providers/index.html): "Terraform relies on plugins called "providers" to interact with cloud providers, SaaS providers, and other APIs...Each provider adds a set of resource types and/or data sources that Terraform can manage. Every resource type is implemented by a provider; without providers, Terraform can't manage any kind of infrastructure."
</b></details>

<details>
<summary>What is the name of the provider in this case: `resource "libvirt_domain" "instance" {...}`</summary><br><b>

libvirt
</b></details>

#### Terraform - Variables

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

#### Terraform - State

<details>
<summary>What <code>terraform.tfstate</code> file is used for?</summary><br><b>

It keeps track of the IDs of created resources so that Terraform knows what it's managing.
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

#### Terraform - Provisioners

<details>
<summary>What are "Provisioners"? What they are used for?</summary><br><b>

Provisioners used to execute actions on local or remote machine. It's extremely useful in case you provisioned an instance and you want to make a couple of changes in the machine you've created without manually ssh into it after Terraform finished to run and manually run them.
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
<summary>Explain Modules</summary>

A Terraform module is a set of Terraform configuration files in a single directory. Modules are small, reusable Terraform configurations that let you manage a group of related resources as if they were a single resource. Even a simple configuration consisting of a single directory with one or more .tf files is a module. When you run Terraform commands directly from such a directory, it is considered the root module. So in this sense, every Terraform configuration is part of a module.
</b></details>

<details>
<summary>What is the Terraform Registry?</summary><br><b>

The Terraform Registry provides a centralized location for official and community-managed providers and modules.
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
<summary>What is the "Random" provider? What is it used for</summary><br><b>
 The random provider aids in generating numeric or alphabetic characters to use as a prefix or suffix for a desired named identifier.
</b></details>

<details>
<summary>How do you test a terraform module?</summary><br><b>
  Many examples are acceptable, but the most common answer would likely to be using the tool <code>terratest</code>, and to test that a module can be initialized, can create resources, and can destroy those resources cleanly.
</b></details>

<details>
<summary>Aside from <code>.tfvars</code> files or CLI arguments, how can you inject dependencies from other modules?</summary><br><b>
  The built-in terraform way would be to use <code>remote-state</code> to lookup the outputs from other modules.
  It is also common in the community to use a tool called <code>terragrunt</code> to explicitly inject variables between modules.
</b></details>

<details>
<summary>What is Terraform import?</summary><br><b>

Terraform import is used to import existing infrastructure. It allows you to bring resources created by some other means (eg. manually launched cloud resources) and bring it under Terraform management. 
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

