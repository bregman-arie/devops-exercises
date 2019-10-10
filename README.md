# DevOps Interview Questions

<p align="center">"<i>DevOps is not a goal, but a never-ending process of continual improvement.</i>" - Jez Humble</p>

****

:information_source: &nbsp;This repository contains interview questions on various DevOps related topics

:bar_chart: &nbsp;There are currently **112** interview questions

:warning: &nbsp;Some answers might be only partial and shouldn't be used as they are in interviews

:pencil: &nbsp;You can add more questions & answers by submitting pull requests :)

****

## Table of Contents

  1. [DevOps](#devops)
  1. [Jenkins](#jenkins)
  1. [AWS](#aws)
  1. [Network](#network)
  1. [Linux](#linux)
  1. [Ansible](#ansible)
  1. [Terraform](#terraform)
  1. [Containers](#containers)
  1. [Docker](#docker)
  1. [Kubernetes](#kubernetes)
  1. [Python](#python)
  1. [Prometheus](#prometheus)
  1. [Git](#git)
  1. [Scenarios](#scenarios)


## DevOps

#### :baby: Beginner

<details>
<summary><b>What is Continuous Integration?</b></summary><br>
</details>

<details>
<summary><b>What is Continuous Deployment?</b></summary><br>
</details>

<details>
<summary><b>What is Continuous Delivery?</b></summary><br>
</details>

<details>
<summary><b>What DevOps helps us to achieve?</b></summary><br>
</details>

<details>
<summary><b>What do you consider as best practices for CI/CD?</b></summary><br>
</details>

<details>
<summary><b>What are the anti-patterns of DevOps?</b></summary><br>
</details>

<details>
<summary><b>Which DevOps tools you consider as top tools? Which tools have you worked with?</b></summary><br>
</details>

<details>
<summary><b>What systems and/or tools are you using for the following?:

  * CI/CD
  * Provisioning infrastructure
  * Configuration Management
  * Monitoring & alerting
  * Logging
  * Code review
  * Code coverage
  * Tests</b></summary><br>
</details>

<details>
<summary><b>What is the difference between SQL and NoSQL?</b></summary><br>
</details>

<details>
<summary><b>What the difference between VPN and VPS?</b></summary><br>
</details>

<details>
<summary><b>What is the difference between SSH and SSL?</b></summary><br>
</details>

<details>
<summary><b>What scripting language are you familiar with? why specifically this one?</b></summary><br>
</details>

<details>
<summary><b>Describe some of the scripts you have written. What are they used for? how long did it take you to write them?</b></summary><br>
</details>

<details>
<summary><b>How long do you think it would take you to learn another language?</b></summary><br>
</details>

#### :star: Advanced

<details>
<summary><b>Tell me how you perform plan capacity for your CI/CD resources (e.g. servers, storage, etc.)</b></summary><br>
</details>

<details>
<summary><b>How would you structure/implement CD for an application which depends on several other applications?</b></summary><br>
</details>

<details>
<summary><b>How do you manage dependencies?</b></summary><br>
</details>

<details>
<summary><b>Explain what are design patterns. Which design patterns are you familar with?</b></summary><br>
</details>

<details>
<summary><b>How do you measure your CI/CD quality? Are there any metrics you are using?</b></summary><br>
</details>

<details>
<summary><b>What is a configuration drift? What problems is it causing?</b></summary><br>

Configuration drift happens when in an environment of servers with the exact same configuration and software, a certain server
or servers are being applied with updates or configuration which other servers don't get and over time these servers become
slightly different than all others.

This situation might lead to bugs which hard to identify and reproduce.
</details>

<details>
<summary><b>How to deal with configuration drift?</b></summary><br>
</details>

<details>
<summary><b>In what scenarios would you prefer to use SQL?</b></summary><br>
</details>

<details>
<summary><b>In what scenarios would you prefer to use NoSQL?</b></summary><br>
</details>


## Jenkins

#### :baby: Beginner

<details>
<summary><b>Explain what is Jenkins and what is it used for</b></summary><br>
</details>

<details>
<summary><b>Explain each of the following in the context of nodes:
  * Master
  * Slave
  * Executor
  * Agent
  * Label</b></summary><br>
</details>

<details>
<summary><b>Explain each of the following in context of jobs:
  * Job
  * Build
  * Test
  * Artifacts</b></summary><br>
</details>

<details>
<summary><b>Explain the architecture of Jenkins</b></summary><br>
</details>

<details>
<summary><b>What are the different ways to trigger a build?</b></summary><br>
</details>

<details>
<summary><b>How do you start a build automatically upon a change in a certain repository?</b></summary><br>
</details>

<details>
<summary><b>What is a plugin?</b></summary><br>
</details>

<details>
<summary><b>What plugins are you using in Jenkins? Which do you consider to most useful?</b></summary><br>
</details>

<details>
<summary><b>Installation questions</b></summary><br>
  * How to install Jenkins?
  * How to install a plugin?
  * How to install an agent?
</details>

<details>
<summary><b>Explain CI/CD and how you implemented in Jenkins</b></summary><br>
</details>


<details>
<summary><b>What type of jobs there are? what is the advantage of each type?</b></summary><br>
</details>

<details>
<summary><b>What ways are you familiar with to notify users on build results?</b></summary><br>
</details>

<details>
<summary><b>How to secure Jenkins?</b></summary><br>
</details>

#### :star: Advanced

<details>
<summary><b>Write a script to remove all the jobs which include the string "REMOVE_ME"</b></summary><br>
</details>


## AWS

#### Global Infrastructure

<details>
<summary><b>Explain the following
  - Availability zone
  - Region
  - Edge location</b></summary><br>
</details>

#### :baby: S3 - Beginner
 
<details>
<summary><b>Explain what is S3 and what is it used for</b></summary><br>
</details>

<details>
<summary><b>What is a bucket?</b></summary><br>
</details>

<details>
<summary><b>True or False? a bucket name must be globally unique</b></summary><br>
</details>

<details>
<summary><b>What objects in S3 consists of?
  * Another way to ask it: explain key, value, version id and metadata in context of objects</b></summary><br>
</details>

<details>
<summary><b>Explain data consistency</b></summary><br>
</details>

<details>
<summary><b>Can you host dynamic websites on s3? what about static websites?</b></summary><br>
</details>

<details>
<summary><b>What security measures have you taken in context of S3?</b></summary><br>
</details>

#### CloudFront

<details>
<summary><b>Explain what is CloudFront and what is it used for</b></summary><br>
</details>

<details>
<summary><b>Explain the following
  * Origin
  * Edge location
  * Distribution</b></summary><br>
</details>

<details>
<summary><b>What delivery methods available for the user with CDN?</b></summary><br>
</details>

<details>
<summary><b>True or False? object are cached for the life of TTL</b></summary><br>
</details>


#### :baby: EC2 - Beginner

<details>
<summary><b>What type of instances have you created?</b></summary><br>
</details>

<details>
<summary><b>How to increase RAM for a given EC2 instance?</b></summary><br>
</details>


## Network

Network questions can be found [here](https://github.com/bregman-arie/computer-networking/blob/master/interview_questions/README.md)


## Linux

#### :baby: Beginner

<details>
<summary><b>Explain what each of the following commands does and given an example on how to use it
  * ls
  * rm 
  * rmdir (can you achieve the same result by using `rm`?)
  * grep
  * wc
  * df</b></summary><br>
</details>

<details>
<summary><b>How to make sure a service will start on a OS of your choice?</b></summary><br>
</details>

<details>
<summary><b>How do you schedule tasks periodically?</b></summary><br>
</details>

<details>
<summary><b>How to change the permissions of a file?</b></summary><br>
</details>

<details>
<summary><b>What does the following permissions mean?:
  * 777
  * 644
  * 750</b></summary><br>
</details>

<details>
<summary><b>How to add a new user to the system without providing him the ability to log-in into the system?</b></summary><br>
</details>

<details>
<summary><b>What commands are you using for troubleshooting issues? specifically:
  * Disk issues
  * Memory, CPU issues
  * Networking issues</b></summary><br>
</details>

<details>
<summary><b>What is the difference between Linux and Unix?</b></summary><br>
</details>

<details>
<summary><b>What is a Linux kernel module and how do you load a new module?</b></summary><br>
</details>

<details>
<summary><b>What is KVM?</b></summary><br>
</details>

<details>
<summary><b>Explain what would be the result of each command:

echo $0
echo $?
echo $$
echo $@
echo $#</b></summary><br>
</details>

<details>
<summary><b>How to grep two strings?</b></summary><br>
</details>

<details>
<summary><b>What is the different between a soft link and hard link?</b></summary><br>

hard link is the same file, using the same inode.
soft link is a shortcut to another file, using a different inode.

soft links can be created between different file systems while
hard link can be created only within the same file system.
</details>

<details>
<summary><b>How to run a process in the background and why to do that in the first place?</b></summary><br>

You can achieve that by specifying & at end of the command.
As to Why? since some commands/processes can take a lot of time to finish
execution or run forever
</details>

<details>
<summary><b>What signal is used when you run 'kill <process id>'?</b></summary><br>

The default signal is SIGTERM (15). This signal kills
process gracefully which means it allows it to save current
state configuration.
</details>

<details>
<summary><b>What signals are you familiar with?</b></summary><br>

SIGTERM - default signal for terminating a process
SIGHUP - common usage is for reloading configuration
SIGKILL - a signal which cannot caught or ignored

To view all available signals run `kill -l`
</details>

<details>
<summary><b>In what state a process in Linux can be?</b></summary><br>

Ready
Running
Blocked
Terminated
Zombie
</details>


## Ansible

<details>
<summary><b>Describe each of the following components in Ansible, including the relationship between them:

  * Task
  * Module
  * Play
  * Playbook
  * Role</b></summary><br>

Task – a call to a specific Ansible module
Module – the actual unit of code executed by Ansible on your own host or a remote host. Modules are indexed by category (database, file, network, …) and also referred as task plugins.

Play – One or more tasks executed on a given host(s)

Playbook – One or more plays. Each play can be executed on the same or different hosts

Role – Ansible roles allows you to group resources based on certain functionality/service such that they can be easily reused. In a role, you have directories for variables, defaults, files, templates, handlers, tasks, and metadata. You can then use the role by simply specifying it in your playbook.
</details>

<details>
<summary><b>You want to run Ansible playbook only on specific minor version of your OS, how would you achieve that?</b></summary><br>
</details>

<details>
<summary><b>Write a task to create the directory ‘/tmp/new_directory’</b></summary><br>

```
- name: Create a new directory
  file:
      path: "/tmp/new_directory"
      state: directory
```
</details>

<details>
<summary><b>What would be the result of the following play?</b></summary><br>

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
</details>

<details>
<summary><b>Write a playbook to install ‘zlib’ and ‘vim’ on all hosts if the file ‘/tmp/mario’ exists on the system.</b></summary><br>

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
</details>

<details>
<summary><b>Write a playbook to deploy the file ‘/tmp/system_info’ on all hosts except for controllers group, with the following content</b></summary><br>

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
</details>

## Terraform

#### :baby: Beginner

<details>
<summary><b>Can you explain what is Terraform? How it works?</b></summary><br>
</details>

<details>
<summary><b>What benefits infrastructure-as-code has?</b></summary><br>

- fully automated process of provisoning, modifying and deleting your infrastructure
- version control for your infrastructure which allows you to quickly rollback to previous versions
- valide infrastructure quoality and stability with automated tests and code reviews
- makes infrastructure tasks less reptitive
</details>

<details>
<summary><b>Why Terraform and not other technologies? (e.g. Ansible, Puppet, CloufFormation)</b></summary><br>
</details>


## Containers

<details>
<summary><b>How containers different from VMs?</b></summary><br>
</details>

<details>
<summary><b>In which scenarios would you use containers and in which you would prefer to use VMs?</b></summary><br>
</details>

## Docker

<details>
<summary><b>What happens when you run `docker run hello-world`?</b></summary><br>

Docker CLI passes your request to Docker daemon.
Docker daemon downloads the image from Docker Hub
Docker daemon creates a new container by using the image it downloaded
Docker daemon redirects output from container to Docker CLI which redirects it to the standard output
</details>

<details>
<summary><b>How do you run a container?</b></summary><br>
</details>

<details>
<summary><b>What do you see when you run `docker ps`?</b></summary><br>
</details>

<details>
<summary><b>What `docker commit` does? when will you use it?</b></summary><br>
</details>

<details>
<summary><b>How would you transfer data from one container into another?</b></summary><br>
</details>

<details>
<summary><b>What is the difference between ADD and COPY in Dockerfile?</b></summary><br>
</details>

<details>
<summary><b>What is the difference between CMD and RUN in Dockerfile?</b></summary><br>
</details>

<details>
<summary><b>Explain what is Docker compose and what is it used for</b></summary><br>
</details>

<details>
<summary><b>What are the differences between Docker compose, Docker swarm and Kuberenets?</b></summary><br>
</details>

<details>
<summary><b>Explain Docker interlock</b></summary><br>
</details>

<details>
<summary><b>What is the difference between Docker Hub and Docker cloud?</b></summary><br>

Docker Hub is a native Docker registry service which allows you to run pull
and push commands to install and deploy Docker images from the Docker Hub.

Docker Cloud is built on top of the Docker Hub so Docker Cloud provides
you with more options/features compared to Docker Hub. One example is
Swarm management which means you can create new swarms in Docker Cloud.
</details>

## Kubernetes

<details>
<summary><b>What is Kubernetes?</b></summary><br>
</details>

<details>
<summary><b>Why Docker isn't enough? Why do we need Kubernetes?</b></summary><br>
</details>

<details>
<summary><b>Describe the architecture of Kuberenets</b></summary><br>
</details>

<details>
<summary><b>How do you monitor your Kuberenets?</b></summary><br>
</details>

<details>
<summary><b>What is kubectl? How do you use it?</b></summary><br>
</details>

<details>
<summary><b>What is kubconfig? What do you use it for?</b></summary><br>
</details>

<details>
<summary><b>How do you create users?</b></summary><br>
</details>


## Python

#### :baby: Beginner

<details>
<summary><b>What data type supported in Python and which of them are mutable?
  What function can you use to show that a certain data type is mutable?</b></summary><br>

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
</details>

<details>
<summary><b>What is PEP8? Give an example of 5 style guidelines</b></summary><br>

PEP8 is a list of coding conventions and style guidelines for Python

5 style guidelines:

    1. Limit all lines to a maximum of 79 characters.
    2. Surround top-level function and class definitions with two blank lines.
    3. Use commas when making a tuple of one element
    4. Use spaces (and not tabs) for indentation
    5. Use 4 spaces per indentation level
</details>

<details>
<summary><b>Write a program which will revert a string (e.g. pizza -> azzip)</b></summary><br>

```
Shortest way is str[::-1]

"Classic" way:
```
</details>

<details>
<summary><b>What _ is used for in Python?</b></summary><br>

1. Translation lookup in i18n
2. Hold the result of the last executed expression or statement
3. As a general purpose "throwaway" variable name. For example: x, y, _ = get_data() (x and y are used but since we don't care about third variable, we "threw it away").
</details>

<details>
<summary><b>Sort a list of lists by the second item of each nested list</b></summary><br>

```
li = [[1, 4], [2, 1], [3, 9], [4, 2], [4, 5]]

sorted(x, key=lambda l: l[1])
```
</details>

<details>
<summary><b>You have the following lists: [{'name': 'Mario', 'food': ['mushrooms', 'goombas']}, {'name': 'Luigi', 'food': ['mushrooms', 'turtles']}]
  Extract all type of foods. Final output should be: {'mushrooms', 'goombas', 'turtles'}</b></summary><br>

```
set([food for bro in x for food in bro['food']])
```
</details>

## Prometheus

<details>
<summary><b>Describe the following Prometheus components:
  - Prometheus server
  - Push Gateway
  - Alert Manager</b></summary><br>

Prometheus server responsible for scraping the storing the data
Push gateway is used for short-lived jobs
Alert manager is responsible for alerts ;)
</details>

<details>
<summary><b>What is an exporter? What is it used for?</b></summary><br>
</details>

## Git

#### :baby: Beginner

<details>
<summary><b>What is the difference between `git pull` and `git fetch`?</b></summary><br>

Shortly, git pull = git fetch + git merge

When you run git pull, it gets all the changes from the remote or central
repository and attaches it to your corresponding branch in your local reposistory.

git fetch gets all the changes from the remote repository, stores the changes in
a separate branch in your local repository
</details>

<details>
<summary><b>Explain the following: <code>git directory`</code>, <code>`working directory`</code> and <code>staging area</code></b></summary><br>

The Git directory is where Git stores the metadata and object database for your project. This is the most important part of Git, and it is what is copied when you clone a repository from another computer.

The working directory is a single checkout of one version of the project. These files are pulled out of the compressed database in the Git directory and placed on disk for you to use or modify.

The staging area is a simple file, generally contained in your Git directory, that stores information about what will go into your next commit. It’s sometimes referred to as the index, but it’s becoming standard to refer to it as the staging area.

This answer taken from [git-scm.com](https://git-scm.com/book/en/v1/Getting-Started-Git-Basics#_the_three_states)
</details>

<details>
<summary><b>How to resolve git merge conflicts?</b></summary><br>

<p>
First, you open the files which are in conflict and identify what are the conflicts.
Next, based on what is accepted in your company or team, you either discuss with your
colleagues on the conflicts or resolve them by yourself
After resolving the conflicts, you add the files with `git add <file_name>`
Finally, you run `git rebase --continue`
</p>
</details>

<details>
<summary><b>What is the difference between `git reset` and `git revert`?</b></summary><br>

<p>
`git revert` creates a new commit which undoes the changes from last commit.

`git reset` depends on the usage, can modify the index or change the commit which the branch head
is currently pointing at.
</p>
</details>

<details>
<summary><b>In what situations are you using `git rebase`?</b></summary><br>
</details>
<details>
<summary><b>What branching strategies are you familiar with</b></summary><br>?
</details>

#### :star: Advanced

<details>
<summary><b>Explain Git octopus merge</b></summary><br>
</details>

## Scenarios

Scenarios are questions which combine several subjects together. Some scenarios will
require from you to design, plan and implement environments with different constraints
and considerations.

* [Elasticsearch & Kibana on AWS](scenarios/elk_kibana_aws.md)
* [Ansible, Minikube and Docker](scenarios/ansible_minikube_docker.md)
