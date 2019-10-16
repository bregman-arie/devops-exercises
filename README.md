# DevOps Interview Questions

<p align="center">"<i>DevOps is not a goal, but a never-ending process of continual improvement.</i>" - Jez Humble</p>

****

:information_source: &nbsp;This repository contains interview questions on various DevOps related topics

:bar_chart: &nbsp;There are currently **151** interview questions

:warning: &nbsp;Some answers might be only partial and shouldn't be used as they are in interviews

:pencil: &nbsp;You can add more questions & answers by submitting pull requests :)

****

<!-- ALL-TOPICS-LIST:START -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<center>
<table>
  <tr>
    <td align="center"><a href="#devops"><img src="images/devops.png" width="75px;" height="75px;" alt="DevOps" /><br /><b>DevOps</b></a><br /><sub><a href="#devops-beginner">Beginner :baby:</a></sub><br><sub><a href="#devops-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#jenkins"><img src="images/jenkins.png" width="75px;" height="85px;" alt="Jenkins"/><br /><b>Jenkins</b></a><br /><sub><a href="#jenkins-beginner">Beginner :baby:</a></sub><br><sub><a href="#jenkins-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#aws"><img src="images/aws.png" width="120px;" height="75px;" alt="AWS"/><br /><b>AWS</b></a><br /><sub><a href="#aws-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#Network"><img src="images/network.png" width="75x;" height="75px;" alt="Network"/><br /><b>Network</b></a><br /><sub><a href="#network-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#linux"><img src="images/linux.png" width="75x;" height="75px;" alt="Linux"/><br /><b>Linux</b></a><br /><sub><a href="#linux-beginner">Beginner :baby:</a></sub><br><sub><a href="#linux-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#ansible"><img src="images/ansible.png" width="75px;" height="75px;" alt="Ansible"/><br /><b>Ansible</b></a><br /><sub><a href="#ansible-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#terraform"><img src="images/terraform.png" width="75px;" height="75px;" alt="Terraform"/><br /><b>Terraform</b></a><br /><sub><a href="#terraform-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#docker"><img src="images/docker.png" width="75px;" height="75px;" alt="Docker"/><br /><b>Docker</b></a><br /><sub><a href="#docker-beginner">Beginner :baby:</a></sub><br><sub></td>
  </tr>
  <tr>
    <td align="center"><a href="#kubernetes"><img src="images/kubernetes.png" width="75px;" height="75px;" alt="kubernetes"/><br /><b>Kubernetes</b></a><br /><sub><a href="#kubernetes-beginner">Beginner :baby:</a></sub><br></td>
    <td align="center"><a href="#python"><img src="images/python.png" width="75px;" height="75px;" alt="Python"/><br /><b>Python</b></a><br /><sub><a href="#python-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#prometheus"><img src="images/prometheus.png" width="75px;" height="75px;" alt="Prometheus"/><br /><b>Prometheus</b></a><br /><sub><a href="#prometheus-beginner">Beginner :baby:</a></sub><br></td>
    <td align="center"><a href="#git"><img src="images/git.png" width="75px;" height="75px;" alt="Git"/><br /><b>Git</b></a><br /><sub><a href="#git-beginner">Beginner :baby:</a></sub><br><sub><a href="#git-advanced">Advanced :star:</a></sub></td>
    <td align="center"><a href="#go"><img src="images/go.png" width="75px;" height="75px;" alt="Go"/><br /><b>Go</b></a><br /><sub><a href="#go-beginner">Beginner :baby:</a></sub><br><sub></td>
    <td align="center"><a href="#mongo"><img src="images/mongo.png" width="75px;" height="75px;" alt="Mongo"/><br /><b>Mongo</b></a><br /><sub><a href="#mongo-beginner">Beginner :baby:</a></sub><br><sub></td>
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
<summary>What is Continuous Integration?</summary><br><b>

A development practice where developers integrate code into a shared repository frequently. It can range from a couple of changes every day or week to a couple of changes in one hour in larger scales.

Each piece of code (change/patch) is verified, to make the change is safe to merge. Today, it's a common practice to test the change using an automated build that makes sure the code can integrated. It can be one build which runs several tests in different levels (unit, functional, etc.) or several separate builds that all or some has to pass in order for the change to be merged into the repository.
</b></details>

<details>
<summary>What is Continuous Deployment?</summary><br><b>
</b></details>

<details>
<summary>What is Continuous Delivery?</summary><br><b>
</b></details>

<details>
<summary>What DevOps helps us to achieve?</summary><br><b>
</b></details>

<details>
<summary>What do you consider as best practices for CI/CD?</summary><br><b>
</b></details>

<details>
<summary>What are the anti-patterns of DevOps?</summary><br><b>
</b></details>

<details>
<summary>Which DevOps tools you consider as top tools? Which tools have you worked with?</summary><br><b>
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

You may use one or all of the following:
  * mature vs. cutting edge
  * community size
  * architecture aspects - agent vs. agentless, master vs. masterless, etc.
</b></details>

<details>
<summary>What is the difference between SQL and NoSQL?</summary><br><b>
</b></details>

<details>
<summary>What the difference between VPN and VPS?</summary><br><b>
</b></details>

<details>
<summary>What is the difference between SSH and SSL?</summary><br><b>
</b></details>

<details>
<summary>What scripting language are you familiar with? why specifically this one?</summary><br><b>
</b></details>

<details>
<summary>Describe some of the scripts you have written. What are they used for? how long did it take you to write them?</summary><br><b>
</b></details>

<details>
<summary>How long do you think it would take you to learn another language?</summary><br><b>
</b></details>

<details>
<summary>Explain mutable vs. immutable infrastructure</summary><br><b>

In mutable infrastructure paradigm, changes applied on top of the existing infrastructure and over time
the infrastructure builds up a history of changes. Ansible, Puppet and Chef are examples to tools which
follow mutable infrastructure paradigm.

In immutable infrastructure paradigm, every change is actually new infrastructure. So a change
to a server will result in a new server instead of updating it. Terraform is an example of technology
which follows the mutable infrastructure paradigm.
</b></details>

<details>
<summary>What ways are you familiar with to deliver a software?</summary><br><b>

  * Archive - collect all your app files into one archive (e.g. tar) and deliver it to the user.
  * Package - depends on the OS, you can use your OS package format (e.g. in RHEL/Fefodra it's RPM) to deliver your software with a way to install, uninstall and update it using the standard packager commands
  * Images - Either VM or container images where your package is included with everything it needs in order to run successfully.
</b></details>

<details>
<summary>What is caching? How it works? Why is it important?</summary><br><b>
</b></details>

<details>
<summary>Explain stateless vs. stateful</summary><br><b>
</b></details>

<details>
<summary>What is HTTP and how it works?</summary><br><b>
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
<summary>How do you manage dependencies?</summary><br><b>
</b></details>

<details>
<summary>Explain what are design patterns. Which design patterns are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>How do you measure your CI/CD quality? Are there any metrics you are using?</summary><br><b>
</b></details>

<details>
<summary>What is a configuration drift? What problems is it causing?</summary><br><b>

Configuration drift happens when in an environment of servers with the exact same configuration and software, a certain server
or servers are being applied with updates or configuration which other servers don't get and over time these servers become
slightly different than all others.

This situation might lead to bugs which hard to identify and reproduce.
</b></details>

<details>
<summary>How to deal with configuration drift?</summary><br><b>
</b></details>

<details>
<summary>In what scenarios would you prefer to use SQL?</summary><br><b>

  * Homogeneous data, no changes anticipated
  * ACID compliance is important to you

</b></details>

<details>
<summary>In what scenarios would you prefer to use NoSQL over SQL?</summary><br><b>

  * Heterogeneous data which changes often
  * Data consistency and integrity is not top priority
</b></details>


## Jenkins

<a name="jenkins-beginner"></a>
#### :baby: Beginner
<details>
<summary>What is a plugin?</summary><br><b>
</b></details>

<details>
<summary>What plugins are you using in Jenkins? Which do you consider to most useful?</summary><br><b>
</b></details>

<details>
<summary>Installation questions</summary><br><b>
  * How to install Jenkins?
  * How to install a plugin?
  * How to install an agent?
</b></details>

<details>
<summary>Explain CI/CD and how you implemented in Jenkins</summary><br><b>
</b></details>


<details>
<summary>What type of jobs there are? what is the advantage of each type?</summary><br><b>
</b></details>

<details>
<summary>What ways are you familiar with to notify users on build results?</summary><br><b>
</b></details>

<details>
<summary>How to secure Jenkins?</summary><br><b>
</b></details>

<a name="jenkins-advanced"></a>
#### :star: Advanced

<details>
<summary>Write a script to remove all the jobs which include the string "REMOVE_ME"</summary><br><b>
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
</b></details>

##### S3
 
<details>
<summary>Explain what is S3 and what is it used for</summary><br><b>
</b></details>

<details>
<summary>What is a bucket?</summary><br><b>
</b></details>

<details>
<summary>True or False? a bucket name must be globally unique</summary><br><b>
True
</b></details>

<details>
<summary>What objects in S3 consists of?
  * Another way to ask it: explain key, value, version id and metadata in context of objects</summary><br><b>
</b></details>

<details>
<summary>Explain data consistency</summary><br><b>
</b></details>

<details>
<summary>Can you host dynamic websites on s3? what about static websites?</summary><br><b>
</b></details>

<details>
<summary>What security measures have you taken in context of S3?</summary><br><b>
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
<summary>True or False? objects are cached for the life of TTL</summary><br><b>
</b></details>


##### EC2

<details>
<summary>What type of instances have you created?</summary><br><b>
</b></details>

<details>
<summary>How to increase RAM for a given EC2 instance?</summary><br><b>

Stop the instance, the type of the instance to match the desired RAM and start the instance.
</b></details>


## Network

<a name="network-beginner"></a>
#### :baby: Beginner

<details>
<summary>Explain the OSI model. What layers there are? What each layer reponsible for?</summary><br><b>

Application: user end (HTTP is here)
Presentation: establishes context between application-layer entities (Encryption is here)
Session: establishes, manages and terminates the connections
Transport: transfers variable-length data sequences from a source to a destination host (TCP & UDP are here)
Network: transfers datagrams from one network to another (IP is here)
Data link: provides a link between two directly connected nodes (MAC is here)
Physical: the electrical and physical spec the data connection (Bits are here)
</b></details>

<details>
<summary>What delivery schemes are you familiar with?</summary><br><b>

Unitcast: One to one communication where there is one sender and one reciever.

Broadcast: Sending a message to everone in the network. The address ff:ff:ff:ff:ff:ff is used for broadcasting.
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
4. Both hosts stop sending the frame and they send to everyone a 'jam signal' notifying everyone that a collision occured
5. They are waiting for a random time before sending again
6. Once each host waited for a raondom time, they try to send the frame again and so the
</b></details>

<details>
<summary>Describe the following network devices and the difference between them: router, switch and hub</summary><br><b>
</b></details>

<details>
<summary>What is NAT?</summary><br><b>
</b></details>

<details>
<summary>What is the difference between TCP and UDP?</summary><br><b>
</b></details>

<details>
<summary>What is ARP? How it works?</summary><br><b>
</b></details>

<details>
<summary>What is DHCP? How it works?</summary><br><b>
</b></details>

<details>
<summary>What is SSL tunneling? How it works?</summary><br><b>
</b></details>

<details>
<summary>What is a socket?</summary><br><b>
</b></details>

<details>
<summary>What is IPv6? Why should we consider using it if we have IPv4?</summary><br><b>
</b></details>

<details>
<summary>What is MTU?</summary><br><b>
</b></details>

<details>
<summary>What is SDN?</summary><br><b>
</b></details>

<details>
<summary>What is ICMP?</summary><br><b>
</b></details>

## Linux

<a name="linux-beginner"></a>
#### :baby: Beginner

<details>
<summary>Explain what each of the following commands does and given an example on how to use it
  * ls
  * rm 
  * rmdir (can you achieve the same result by using <code>rm</code>?)
  * grep
  * wc
  * df</summary><br><b>
</b></details>

<details>
<summary>How to make sure a service will start on a OS of your choice?</summary><br><b>
</b></details>

<details>
<summary>How do you schedule tasks periodically?</summary><br><b>

You can use the commands <code>cron</code> and <code>at</code>.
With cron, tasks are scheduled using the following format:

<minute> <hour> <day of month> <month> <day of week> <command to execute>

The tasks are stored in a cron file.
</b></details>

<details>
<summary>How to change the permissions of a file?</summary><br><b>
</b></details>

<details>
<summary>What does the following permissions mean?:
  * 777
  * 644
  * 750</summary><br><b>
</b></details>

<details>
<summary>How to add a new user to the system without providing him the ability to log-in into the system?</summary><br><b>
</b></details>

<details>
<summary>What commands are you using for troubleshooting issues? specifically:
  * Disk issues
  * Memory, CPU issues
  * Networking issues</summary><br><b>
</b></details>

<details>
<summary>What is the difference between Linux and Unix?</summary><br><b>
</b></details>

<details>
<summary>What is a Linux kernel module and how do you load a new module?</summary><br><b>
</b></details>

<details>
<summary>What is KVM?</summary><br><b>
</b></details>

<details>
<summary>What is an exit code? What exit codes are you familiar with?</summary><br><b>

An exit code (or return code) represents the code returned by a child process to its
parent process.

0 is an exit code which represents success while anything higher than 1 represents error.
Each number has different meaning, based on how the application was developed.

I consider this as a good blog post to read more about it: https://shapeshed.com/unix-exit-codes
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
<summary>How to grep two strings?</summary><br><b>
</b></details>

<details>
<summary>What is the different between a soft link and hard link?</summary><br><b>

hard link is the same file, using the same inode.
soft link is a shortcut to another file, using a different inode.

soft links can be created between different file systems while
hard link can be created only within the same file system.
</b></details>

<details>
<summary>How to run a process in the background and why to do that in the first place?</summary><br><b>

You can achieve that by specifying & at end of the command.
As to Why? since some commands/processes can take a lot of time to finish
execution or run forever
</b></details>

<details>
<summary>What signal is used when you run 'kill <process id>'?</summary><br><b>

The default signal is SIGTERM (15). This signal kills
process gracefully which means it allows it to save current
state configuration.
</b></details>

<details>
<summary>What signals are you familiar with?</summary><br><b>

SIGTERM - default signal for terminating a process
SIGHUP - common usage is for reloading configuration
SIGKILL - a signal which cannot caught or ignored

To view all available signals run `kill -l`
</b></details>

<details>
<summary>In what state a process in Linux can be?</summary><br><b>

Ready
Running
Blocked
Terminated
Zombie
</b></details>

<details>
<summary>Find all files which end with '.yml' and replace the number 1 in 2 in each file</summary><br><b>

find /some_dir -iname \*.yml -exec sed -i "s/1/2/g" {} \;
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

File descriptor, also known as file handler, is a unique number which identifies an open file in the operating system.

In Linux (and Unix) the first three file descriptors are:
  * 0 - the default data stream for input
  * 1 - the default data stream for output
  * 2 - the default data stream for output related to errors

This is a great article on the topic: https://www.computerhope.com/jargon/f/file-descriptor.htm
</b></details>

<details>
<summary>What's an inode?</summary><br><b>

For each file (and directory) in Linux there is an inode, a data structure which stores metadata
related to the file like its size, owner, permissions, etc.
</b></details>

<details>
<summary>How to list ports which being currently used?</summary><br><b>
</b></details>

<details>
<summary>DNS: What is A record?</summary><br><b>
</b></details>

<details>
<summary>DNS: What is MX record?</summary><br><b>
</b></details>

<details>
<summary>DNS: is it using TCP or UDP?</summary><br><b>
</b></details>

<a name="linux-advanced"></a>
#### :star: Advanced

<details>
<summary>How to delete the last word from each line in a file?</summary><br><b>

sed "s/\s*\w\+\s*$//" file
</b></details>

<details>
<summary>How to create a file of a certain size?</summary><br><b>

There are a couple of ways to do that:
  
  * dd if=/dev/urandom of=new_file.txt bs=2MB count=1
  * truncate -s 2M new_file.txt
  * fallocate -l 2097152 new_file.txt
</b></details>


## Ansible

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

  replace <HOSTNAME> and  <OS> with the actual data for the specific host you are running on

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

## Terraform


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
be used for provisioning infrastructure. Also, it doesn't explains why Terraform should be used over
CloudFormation if at all.

The benefits of Terraform over the other tools:
  * it follows the immutable infrastructure approach which has benefits like avoiding a configuration drift over time
  * Ansible and Puppet are more procedural (you mention what to execute in each step) and Terraform is declartive since you describe the overall desired state and not per resource or task. You can give the example of going from 1 to 2 servers in each tool. In terrform you specify 2, in Ansible and puppet you have to only provision 1 additional server
</b></details>

<details>
<summary>Explain what the following commands do:

  * <code>terraform init</code>
  * <code>terraform plan</code>
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


## Docker

<a name="docker-beginner"></a>

#### :baby: beginner

<details>
<summary>How containers are different from VMs?</summary><br><b>

The primary difference between containers and VMs is that containers allow you to virtualize
multiple workloads on the operating system while in the case of VMs the hardware is being virtualized to
run multiple machines each with its own OS.
</b></details>

<details>
<summary>In which scenarios would you use containers and in which you would prefer to use VMs?</summary><br><b>

You should choose VMs when:
  * you need run an application which requires all the resources and functionalilies of an OS
  * you need full isolation and security

You should choose containers when:
  * you need a lightweight solution that quickly starts
  * Running multiple versions or instances of a single application
</b></details>

<details>
<summary>What happens when you run `docker run hello-world`?</summary><br><b>

Docker CLI passes your request to Docker daemon.
Docker daemon downloads the image from Docker Hub
Docker daemon creates a new container by using the image it downloaded
Docker daemon redirects output from container to Docker CLI which redirects it to the standard output
</b></details>

<details>
<summary>How do you run a container?</summary><br><b>
</b></details>

<details>
<summary>What do you see when you run `docker ps`?</summary><br><b>
</b></details>

<details>
<summary>What `docker commit` does? when will you use it?</summary><br><b>
</b></details>

<details>
<summary>How would you transfer data from one container into another?</summary><br><b>
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
<summary>What are the differences between Docker compose, Docker swarm and Kuberenets?</summary><br><b>
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

## Kubernetes

<details>
<summary>What is Kubernetes?</summary><br><b>
</b></details>

<details>
<summary>Why Docker isn't enough? Why do we need Kubernetes?</summary><br><b>
</b></details>

<details>
<summary>Describe the architecture of Kuberenets</summary><br><b>
</b></details>

<details>
<summary>How do you monitor your Kuberenets?</summary><br><b>
</b></details>

<details>
<summary>What is kubectl? How do you use it?</summary><br><b>
</b></details>

<details>
<summary>What is kubconfig? What do you use it for?</summary><br><b>
</b></details>

<details>
<summary>How do you create users?</summary><br><b>
</b></details>


## Python

<a name="python-beginner"></a>
#### :baby: Beginner

<details>
<summary>What data type supported in Python and which of them are mutable?
  What function can you use to show that a certain data type is mutable?</summary><br><b>

The mutable data types are:

    List
    Dictionary
    Set
    
The immutable data types are:

    Numbers (int, float, ...)
    String
    Bool
    Tuple

The id function can be used to check if a given variable is mutable or not.
</b></details>

<details>
<summary>What is PEP8? Give an example of 5 style guidelines</summary><br><b>

PEP8 is a list of coding conventions and style guidelines for Python

5 style guidelines:

    1. Limit all lines to a maximum of 79 characters.
    2. Surround top-level function and class definitions with two blank lines.
    3. Use commas when making a tuple of one element
    4. Use spaces (and not tabs) for indentation
    5. Use 4 spaces per indentation level
</b></details>

<details>
<summary>Write a program which will revert a string (e.g. pizza -> azzip)</summary><br><b>

```
Shortest way is str[::-1]

"Classic" way:
```
</b></details>

<details>
<summary>What _ is used for in Python?</summary><br><b>

1. Translation lookup in i18n
2. Hold the result of the last executed expression or statement
3. As a general purpose "throwaway" variable name. For example: x, y, _ = get_data() (x and y are used but since we don't care about third variable, we "threw it away").
</b></details>

<details>
<summary>Sort a list of lists by the second item of each nested list</summary><br><b>

```
li = [[1, 4], [2, 1], [3, 9], [4, 2], [4, 5]]

sorted(x, key=lambda l: l[1])
```
</b></details>

<details>
<summary>You have the following list: <code>[{'name': 'Mario', 'food': ['mushrooms', 'goombas']}, {'name': 'Luigi', 'food': ['mushrooms', 'turtles']}]</code>
  Extract all type of foods. Final output should be: {'mushrooms', 'goombas', 'turtles'}</summary><br><b>

```
set([food for bro in x for food in bro['food']])
```
</b></details>

## Prometheus

<details>
<summary>Describe the following Prometheus components:
  - Prometheus server
  - Push Gateway
  - Alert Manager</summary><br><b>

Prometheus server responsible for scraping the storing the data<br>
Push gateway is used for short-lived jobs<br>
Alert manager is responsible for alerts ;)
</b></details>

<details>
<summary>What is an exporter? What is it used for?</summary><br><b>
</b></details>

## Git

<a name="git-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is the difference between <code>git pull</code> and <code>git fetch</code>?</summary><br><b>

Shortly, git pull = git fetch + git merge

When you run git pull, it gets all the changes from the remote or central
repository and attaches it to your corresponding branch in your local reposistory.

git fetch gets all the changes from the remote repository, stores the changes in
a separate branch in your local repository
</b></details>

<details>
<summary>Explain the following: <code>git directory</code>, <code>working directory</code> and <code>staging area</code></summary><br><b>

The Git directory is where Git stores the metadata and object database for your project. This is the most important part of Git, and it is what is copied when you clone a repository from another computer.

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

details>
<summary>You would like to move forth commit to the top. How would you achieve that?</summary><br><b>

Using <code>git rebase></code> command
</b></summary>

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

The result is the same, a variable with the variable 2.

with <code>var x int = 2</code> we are setting the variable type to integer while with <code>x := 2</code> we are letting Go figure out by itself the type.
</b></details>

<details>
<summary>What libraries of Go have you used?</summary><br><b>

This should be answered based on your usage but some examples are:

  * fmt - formatted I/O
</b></details>

<details>
<summary>Write an "hello world" program?</summary><br><b>

```
package main

import "fmt"

func main() {
        fmt.Println("Hello World")
}
```
</b></details>

## Mongo

<a name="mongo-beginner"></a>
#### :baby: Beginner

<details>
<summary>What is a document? What is a collection?</summary><br><b>
</b></details>

<details>
<summary>What is an aggregator?</summary><br><b>
</b></details>


## Scenarios

Scenarios are questions which combine several subjects together. Some scenarios will
require from you to design, plan and implement environments with different constraints
and considerations.

* [Elasticsearch & Kibana on AWS](scenarios/elk_kibana_aws.md)
* [Ansible, Minikube and Docker](scenarios/ansible_minikube_docker.md)
* [Cloud Slack bot](scenarios/cloud_slack_bot.md)
