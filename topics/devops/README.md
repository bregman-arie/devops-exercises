# DevOps

## Questions

### General 

<details>
<summary>What is DevOps?</summary><br><b>

The definition of DevOps from selected companies:

**Amazon**:

"DevOps is the combination of cultural philosophies, practices, and tools that increases an organization’s ability to deliver applications and services at high velocity: evolving and improving products at a faster pace than organizations using traditional software development and infrastructure management processes. This speed enables organizations to better serve their customers and compete more effectively in the market."

**Microsoft**:

"DevOps is the union of people, process, and products to enable continuous delivery of value to our end users. The contraction of “Dev” and “Ops” refers to replacing siloed Development and Operations to create multidisciplinary teams that now work together with shared and efficient practices and tools. Essential DevOps practices include agile planning, continuous integration, continuous delivery, and monitoring of applications."

**Red Hat**:

"DevOps describes approaches to speeding up the processes by which an idea (like a new software feature, a request for enhancement, or a bug fix) goes from development to deployment in a production environment where it can provide value to the user. These approaches require that development teams and operations teams communicate frequently and approach their work with empathy for their teammates. Scalability and flexible provisioning are also necessary. With DevOps, those that need power the most, get it—through self service and automation. Developers, usually coding in a standard development environment, work closely with IT operations to speed software builds, tests, and releases—without sacrificing reliability."

**Google**:

"...The organizational and cultural movement that aims to increase software delivery velocity, improve service reliability, and build shared ownership among software stakeholders"
</b></details>

<details>
<summary>What are the benefits of DevOps? What can it help us to achieve?</summary><br><b>

  * Collaboration
  * Improved delivery
  * Security
  * Speed
  * Scale
  * Reliability
</b></details>

<details>
<summary>What are the anti-patterns of DevOps?</summary><br><b>

A couple of examples:

* One person is in charge of specific tasks. For example there is only one person who is allowed to merge the code of everyone else into the repository.
* Treating production differently from development environment. For example, not implementing security in development environment
* Not allowing someone to push to production on Friday ;)
</b></details>

<details>
<summary>How would you describe a successful DevOps engineer or a team?</summary><br><b>

The answer can focus on:

* Collaboration
* Communication
* Set up and improve workflows and processes (related to testing, delivery, ...)
* Dealing with issues

Things to think about:

* What DevOps teams or engineers should NOT focus on or do?
* Do DevOps teams or engineers have to be innovative or practice innovation as part of their role?
</b></details>

<details>
<summary>One of your team members suggests to set a goal of "deploying at least 20 times a day" in regards to CD. What is your take on that?</summary><br><b>

A couple of thoughts:

1. Why is it an important goal? Is it affecting the business somehow? One of the KPIs? In other words, does it matters?
2. This might introduce risks such as losing quality in favor of quantity
3. You might want to set a possibly better goal such as "be able to deploy whenever we need to deploy"
</b></details>

### Tooling

<details>
<summary>What do you take into consideration when choosing a tool/technology?</summary><br><b>

A few ideas to think about:

  * mature/stable vs. cutting edge
  * community size
  * architecture aspects - agent vs. agentless, master vs. masterless, etc.
  * learning curve
</b></details>

<details>
<summary>Can you describe which tool or platform you chose to use in some of the following areas and how?

  * CI/CD
  * Provisioning infrastructure
  * Configuration Management
  * Monitoring & alerting
  * Logging
  * Code review
  * Code coverage
  * Issue Tracking
  * Containers and Containers Orchestration
  * Tests</summary><br><b>

This is a more practical version of the previous question where you might be asked additional specific questions on the technology you chose

  * CI/CD - Jenkins, Circle CI, Travis, Drone, Argo CD, Zuul
  * Provisioning infrastructure - Terraform, CloudFormation
  * Configuration Management - Ansible, Puppet, Chef
  * Monitoring & alerting - Prometheus, Nagios
  * Logging - Logstash, Graylog, Fluentd
  * Code review - Gerrit, Review Board
  * Code coverage - Cobertura, Clover, JaCoCo
  * Issue tracking - Jira, Bugzilla
  * Containers and Containers Orchestration - Docker, Podman, Kubernetes, Nomad
  * Tests - Robot, Serenity, Gauge
</b></details>

<details>
<summary>A team member of yours, suggests to replace the current CI/CD platform used by the organization with a new one. How would you reply?</summary><br><b>

Things to think about:

* What we gain from doing so? Are there new features in the new platform? Does the new platform deals with some of the limitations presented in the current platform?
* What this suggestion is based on? In other words, did he/she tried out the new platform? Was there extensive technical research?
* What does the switch from one platform to another will require from the organization? For example, training users who use the platform? How much time the team has to invest in such move?
</b></details>

### Version Control

<details>
<summary>What is Version Control?</summary><br><b>
	
* Version control is the system of tracking and managing changes to software code.
* It helps software teams to manage changes to source code over time.
* Version control also helps developers move faster and allows software teams to preserve efficiency and agility as the team scales to include more developers.
</b></details>

<details>
<summary>What is a commit?</summary><br><b>
	
* In Git, a commit is a snapshot of your repo at a specific point in time.
* The git commit command will save all staged changes, along with a brief description from the user, in a “commit” to the local repository.
</b></details>

<details>
<summary>What is a merge?</summary><br><b>

* Merging is Git's way of putting a forked history back together again. The git merge command lets you take the independent lines of development created by git branch and integrate them into a single branch.
</b></details>

<details>
<summary>What is a merge conflict?</summary><br><b>

* A merge conflict is an event that occurs when Git is unable to automatically resolve differences in code between two commits. When all the changes in the code occur on different lines or in different files, Git will successfully merge commits without your help.
</b></details>

<details>
<summary>What best practices are you familiar with regarding version control?</summary><br><b>
	
* Use a descriptive commit message
* Make each commit a logical unit
* Incorporate others' changes frequently
* Share your changes frequently
* Coordinate with your co-workers
* Don't commit generated files
</b></details>

<details>
<summary>Would you prefer a "configuration->deployment" model or "deployment->configuration"? Why?</summary><br><b>

Both have advantages and disadvantages.
With "configuration->deployment" model for example, where you build one image to be used by multiple deployments, there is less chance of deployments being different from one another, so it has a clear advantage of a consistent environment.
</b></details>

<details>
<summary>Explain mutable vs. immutable infrastructure</summary><br><b>

In mutable infrastructure paradigm, changes are applied on top of the existing infrastructure and over time
the infrastructure builds up a history of changes. Ansible, Puppet and Chef are examples of tools which
follow mutable infrastructure paradigm.

In immutable infrastructure paradigm, every change is actually a new infrastructure. So a change
to a server will result in a new server instead of updating it. Terraform is an example of technology
which follows the immutable infrastructure paradigm.
</b></details>

### Software Distribution

<details>
<summary>Explain "Software Distribution"</summary><br><b>

Read [this](https://venam.nixers.net/blog/unix/2020/03/29/distro-pkgs.html) fantastic article on the topic.

From the article: "Thus, software distribution is about the mechanism and the community that takes the burden and decisions to build an assemblage of coherent software that can be shipped."
</b></details>

<details>
<summary>Why are there multiple software distributions? What differences they can have?</summary><br><b>

Different distributions can focus on different things like: focus on different environments (server vs. mobile vs. desktop), support specific hardware, specialize in different domains (security, multimedia, ...), etc. Basically, different aspects of the software and what it supports, get different priority in each distribution.
</b></details>

<details>
<summary>What is a Software Repository?</summary><br><b>

Wikipedia: "A software repository, or “repo” for short, is a storage location for software packages. Often a table of contents is stored, as well as metadata."

Read more [here](https://en.wikipedia.org/wiki/Software_repository)
</b></details>

<details>
<summary>What ways are there to distribute software? What are the advantages and disadvantages of each method?</summary><br><b>

  * Source - Maintain build script within version control system so that user can build your app after cloning repository. Advantage: User can quickly checkout different versions of application. Disadvantage: requires build tools installed on users machine.
  * Archive - collect all your app files into one archive (e.g. tar) and deliver it to the user. Advantage: User gets everything he needs in one file. Disadvantage: Requires repeating the same procedure when updating, not good if there are a lot of dependencies.
  * Package - depends on the OS, you can use your OS package format (e.g. in RHEL/Fefodra it's RPM) to deliver your software with a way to install, uninstall and update it using the standard packager commands. Advantages: Package manager takes care of support for installation, uninstallation, updating and dependency management. Disadvantage: Requires managing package repository.
  * Images - Either VM or container images where your package is included with everything it needs in order to run successfully. Advantage: everything is preinstalled, it has high degree of environment isolation. Disadvantage: Requires knowledge of building and optimizing images.
</b></details>

<details>
<summary>Are you familiar with "The Cathedral and the Bazaar models"? Explain each of the models</summary><br><b>

* Cathedral - source code released when software is released
* Bazaar - source code is always available publicly (e.g. Linux Kernel)
</b></details>

<details>
<summary>What is caching? How does it work? Why is it important?</summary><br><b>

Caching is fast access to frequently used resources which are computationally expensive or IO intensive and do not change often. There can be several layers of cache that can start from CPU caches to distributed cache systems. Common ones are in memory caching and distributed caching. <br/> Caches are typically data structures that contains some data, such as a hashtable or dictionary. However, any data structure can provide caching capabilities, like set, sorted set, sorted dictionary etc. While, caching is used in many applications, they can create subtle bugs if not implemented correctly or used correctly. For example,cache invalidation, expiration or updating is usually quite challenging and hard.
</b></details>

<details>
<summary>Explain stateless vs. stateful</summary><br><b>

Stateless applications don't store any data in the host which makes it ideal for horizontal scaling and microservices.
Stateful applications depend on the storage to save state and data, typically databases are stateful applications.
</b></details>

<details>
<summary>What is Reliability? How does it fit DevOps?</summary><br><b>

Reliability, when used in DevOps context, is the ability of a system to recover from infrastructure failure or disruption. Part of it is also being able to scale based on your organization or team demands.
</b></details>

<details>
<summary>What does "Availability" mean? What means are there to track Availability of a service?</summary><br><b>
</b></details>

<details>
<summary>Why isn't 100% availability a target? Why do most companies or teams set it to be 99%.X?</summary><br><b>
</b></details>

<details>
<summary>Describe the workflow of setting up some type of web server (Apache, IIS, Tomcat, ...)</summary><br><b>
</b></details>

<details>
<summary>How does a web server work?</summary><br><b>
<a href="https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server" title="Click here to redirect to MDN official page" style="background-color:#FFFFFF;color:#000000;text-decoration:none">According to MDN Web Docs -</a>
	
We can understand web servers using two view points, which is:
	
	(i) Hardware (ii) Software

(i)   A web server is nothing but a remote computer which stores website's component files(HTML,CSS and Javascript files) and web server's software.A web server connects to
      the Internet and supports physical data interchange with other devices connected to the web.
	
(ii)  On the software side, a web server includes several parts that control how web users access hosted files. At a minimum, this is an HTTP server. An HTTP server is software       that understands URLs (web addresses) and HTTP (the protocol your browser uses to view webpages). An HTTP server can be accessed through the domain names of the websites         it stores, and it delivers the content of these hosted websites to the end user's device.
	
## How communication between web server and web browsers established:
	
 Whenever a browser needs a file that is hosted on a web server, the browser requests the page from the web server and the web server responds with that page.
This communcation between web browser and web server happens in the following ways:

(1) User enters the domain name in the browser,and the browser then search for the IP address of the entered name. It can be done in 2 ways- 
	
    -By searching in its cache. 
    -By requesting one or more DNS (Domain Name System) Servers.

(2) After knowing the IP Address, the browser requests the file via HTTP and the request reaches the correct (hardware) web server.

(3) The (software) HTTP server accepts the request, finds the requested document, and sends it back to the browser, also through HTTP. (If the server doesn't find the requested document, it returns a 404 response instead.)

(4) The Browser finally gets the webpages and displays it, or displays the error message.

</b></details>

<details>
<summary>Explain "Open Source"</summary><br><b>
</b></details>

<details>
<summary>Describe the architecture of service/app/project/... you designed and/or implemented</summary><br><b>
</b></details>

<details>
<summary>What types of tests are you familiar with?</summary><br><b>

Styling, unit, functional, API, integration, smoke, scenario, ...

You should be able to explain those that you mention.
</b></details>

<details>
<summary>You need to install periodically a package (unless it's already exists) on different operating systems (Ubuntu, RHEL, ...). How would you do it?</summary><br><b>

There are multiple ways to answer this question (there is no right and wrong here):

* Simple cron job
* Pipeline with configuration management technology (such Puppet, Ansible, Chef, etc.)
...
</b></details>

<details>
<summary>What is Chaos Engineering?</summary><br><b>

Wikipedia: "Chaos engineering is the discipline of experimenting on a software system in production in order to build confidence in the system's capability to withstand turbulent and unexpected conditions"

Read about Chaos Engineering [here](https://en.wikipedia.org/wiki/Chaos_engineering)
</b></details>

<details>
<summary>What is "infrastructure as code"? What implementation of IAC are you familiar with?</summary><br><b>

IAC (infrastructure as code) is a declarative approach of defining infrastructure or architecture of a system. Some implementations are ARM templates for Azure and Terraform that can work across multiple cloud providers.
</b></details>

<details>
<summary>What benefits does infrastructure-as-code have?</summary><br><b>

- fully automated process of provisioning, modifying and deleting your infrastructure
- version control for your infrastructure which allows you to quickly rollback to previous versions
- validate infrastructure quality and stability with automated tests and code reviews
- makes infrastructure tasks less repetitive
</b></details>

<details>
<summary>How do you manage build artifacts?</summary><br><b>

Build artifacts are usually stored in a repository. They can be used in release pipelines for deployment purposes. Usually there is retention period on the build artifacts.
</b></details>

<details>
<summary>What Continuous Integration solution are you using/prefer and why?</summary><br><b>
</b></details>

<details>
<summary>What deployment strategies are you familiar with or have used?</summary><br><b>

	There are several deployment strategies:
	* Rolling
	* Blue green deployment
	* Canary releases
	* Recreate strategy

</b></details>

<details>
<summary>You joined a team where everyone developing one project and the practice is to run tests locally on their workstation and push it to the repository if the tests passed. What is the problem with the process as it is now and how to improve it?</summary><br><b>
</b></details>

<details>
<summary>Explain test-driven development (TDD)</summary><br><b>
</b></details>

<details>
<summary>Explain agile software development</summary><br><b>
</b></details>

<details>
<summary>What do you think about the following sentence?: "Implementing or practicing DevOps leads to more secure software"</summary><br><b>
</b></details>

<details>
<summary>Do you know what is a "post-mortem meeting"? What is your opinion on that?</summary><br><b>
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
	Configuration drift can be avoided with desired state configuration (DSC) implementation. Desired state configuration can be a declarative file that defined how a system should be. There are tools to enforce desired state such a terraform or azure dsc. There are incremental or complete strategies.
</b></details>

<details>
<summary>Explain Declarative and Procedural styles. The technologies you are familiar with (or using) are using procedural or declarative style?</summary><br><b>

Declarative - You write code that specifies the desired end state<br>
Procedural - You describe the steps to get to the desired end state

Declarative Tools - Terraform, Puppet, CloudFormation, Ansible<br>
Procedural Tools - Chef

To better emphasize the difference, consider creating two virtual instances/servers.
In declarative style, you would specify two servers and the tool will figure out how to reach that state.
In procedural style, you need to specify the steps to reach the end state of two instances/servers - for example, create a loop and in each iteration of the loop create one instance (running the loop twice of course).
</b></details>

<details>
<summary>Do you have experience with testing cross-projects changes? (aka cross-dependency)</summary><br><b>

Note: cross-dependency is when you have two or more changes to separate projects and you would like to test them in mutual build instead of testing each change separately.
</b></details>

<details>
<summary>Have you contributed to an open source project? Tell me about this experience</summary><br><b>
</b></details>

<details>
<summary>What is Distributed Tracing?</summary><br><b>
</b></details>

### GitOps

<details>
<summary>What is GitOps?</summary><br><b>

GitLab: "GitOps is an operational framework that takes DevOps best practices used for application development such as version control, collaboration, compliance, and CI/CD tooling, and applies them to infrastructure automation".

Read more [here](https://about.gitlab.com/topics/gitops)
</b></details>

<details>
<summary>What are some of the advantages of applying GitOps?</summary><br><b>

* It introduces limited/granular access to infrastructure
* It makes it easier to trace who makes changes to infrastructure

</b></details>

<details>
<summary>When a repository refereed to as "GitOps Repository" what does it means?</summary><br><b>

A repository that doesn't holds the application source code, but the configuration, infra, ... files that required to test and deploy the application.
</b></details>

<details>
<summary>What are some practical implementations or practices of GitOp?</summary><br><b>

* Store Infra files in a version control repository (like Git)
* Apply review/approval process for changes
</b></details>

<details>
<summary>Two engineers in your team argue on where to put the configuration and infra related files of a certain application. One of them suggests to put it in the same repo as the application repository and the other one suggests to put to put it in its own separate repository. What's your take on that?</summary><br><b>

One might say we need more details as to what these configuration and infra files look like exactly and how complex the application and its CI/CD pipeline(s), but in general, most of the time you will want to put configuration and infra related files in their own separate repository and not in the repository of the application for multiple reasons:

* Every change submitted to the configuration, shouldn't trigger the CI/CD of the application, it should be testing out and applying the modified configuration, not the application itself
* When you mix application code with conifguration and infra related files
</b></details>

#### SRE

<details>
<summary>What are the differences between SRE and DevOps?</summary><br><b>

Google: "One could view DevOps as a generalization of several core SRE principles to a wider range of organizations, management structures, and personnel."

Read more about it [here](https://sre.google/sre-book/introduction)
</b></details>

<details>
<summary>What SRE team is responsible for?</summary><br><b>

Google: "the SRE team is responsible for availability, latency, performance, efficiency, change management, monitoring, emergency response, and capacity planning of their services"

Read more about it [here](https://sre.google/sre-book/introduction)
</b></details>

<details>
<summary>What is an error budget?</summary><br><b>

Atlassian: "An error budget is the maximum amount of time that a technical system can fail without contractual consequences."

Read more about it [here](https://www.atlassian.com/incident-management/kpis/error-budget)
</b></details>

<details>
<summary>What do you think about the following statement: "100% is the only right availability target for a system"</summary><br><b>

Wrong. No system can guarantee 100% availability as no system is safe from experiencing zero downtime.
Many systems and services will fall somewhere between 99% and 100% uptime (or at least this is how most systems and services should be).
</b></details>

<details>
<summary>What are MTTF (mean time to failure) and MTTR (mean time to repair)? What these metrics help us to evaluate?</summary><br><b>

	* MTTF (mean time to failure) other known as uptime, can be defined as how long the system runs before if fails.
	* MTTR (mean time to recover) on the other hand, is the amount of time it takes to repair a broken system.
	* MTBF (mean time between failures) is the amount of time between failures of the system.
</b></details>

<details>
<summary>What is the role of monitoring in SRE?</summary><br><b>

Google: "Monitoring is one of the primary means by which service owners keep track of a system’s health and availability"

Read more about it [here](https://sre.google/sre-book/introduction)
</b></details>

<details>
<summary>What are the two main SRE KPIs</summary><br><b>

Service Level Indicators (SLI) and Service Level Objectives (SLO).
</b></details>

<details>
<summary>What is Toil?</summary><br><b>

Google: Toil is the kind of work tied to running a production service that tends to be manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows

Read more about it [here](https://sre.google/sre-book/eliminating-toil/) 
</b></details>


<details>
<summary>What is a postmortem ? </summary><br><b>

The postmortem is a process that should take place folowing an incident. It’s purpose is to identify the root cause of an incident and the actions that should be taken to avoid this kind of incidents from hapenning again. </b></details>


<details>
<summary>What is the core value often put forward when talking about postmortem?</summary><br><b>

Blamelessness. 
Postmortems need to be blameless and this value should be remided at the begining of every postmortem. This is the best way to ensure that people are playing the game to find the root cause and not trying to hide their possible faults.</b></details>

