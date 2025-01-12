## CI/CD

### CI/CD Exercises

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Set up a CI pipeline | CI | [Exercise](ci_for_open_source_project.md) | | |
| Deploy to Kubernetes | Deployment | [Exercise](deploy_to_kubernetes.md) | [Solution](solutions/deploy_to_kubernetes/README.md) | |
| Jenkins - Remove Jobs | Jenkins Scripts | [Exercise](remove_jobs.md) | [Solution](solutions/remove_jobs_solution.groovy) | |
| Jenkins - Remove Builds | Jenkins Scripts | [Exercise](remove_builds.md) | [Solution](solutions/remove_builds_solution.groovy) | |

### CI/CD Self Assessment

<details>
<summary>What is Continuous Integration?</summary><br><b>

A development practice where developers integrate code into a shared repository frequently. It can range from a couple of changes every day or a week to a couple of changes in one hour in larger scales.

Each piece of code (change/patch) is verified to make sure that the change is safe to merge. Today, it's a common practice to test the change using an automated build that makes sure the code can be integrated. It can be one build which runs several tests in different levels (unit, functional, etc.) or several separate builds that all or some has to pass in order for the change to be merged into the repository.
</b></details>

<details>
<summary>What is Continuous Deployment?</summary><br><b>

A development strategy used by developers to release software automatically into production where any code commit must pass through an automated testing phase. Only when this is successful is the release considered production worthy. This eliminates any human interaction and should be implemented only after production-ready pipelines have been set with real-time monitoring and reporting of deployed assets. If any issues are detected in production it should be easy to rollback to previous working state.

For more info please read [here](https://www.atlassian.com/continuous-delivery/continuous-deployment)
</b></details>

<details>
<summary>Can you describe an example of a CI (and/or CD) process starting the moment a developer submitted a change/PR to a repository?</summary><br><b>

There are many answers for such a question, as CI processes vary, depending on the technologies used and the type of the project to where the change was submitted.
Such processes can include one or more of the following stages:

* Compile 
* Build
* Install
* Configure
* Update
* Test

An example of one possible answer:

A developer submitted a pull request to a project. The PR (pull request) triggered two jobs (or one combined job). One job for running lint test on the change and the second job for building a package which includes the submitted change, and running multiple api/scenario tests using that package. Once all tests passed and the change was approved by a maintainer/core, it's merged/pushed to the repository. If some of the tests failed, the change will not be allowed to merged/pushed to the repository.

A complete different answer or CI process, can describe how a developer pushes code to a repository, a workflow then triggered to build a container image and push it to the registry. Once in the registry, the k8s cluster is applied with the new changes.
</b></details>

<details>
<summary>What is Continuous Delivery?</summary><br><b>

A development strategy used to frequently deliver code to QA and Ops for testing. This entails having a staging area that has production like features where changes can only be accepted for production after a manual review. Because of this human entanglement there is usually a time lag between release and review making it slower and error prone as compared to continuous deployment.

For more info please read [here](https://www.atlassian.com/continuous-delivery/continuous-deployment)
</b></details>

<details>
<summary>What is difference between Continuous Delivery and Continuous Deployment?</summary><br><b>

Both encapsulate the same process of deploying the changes which were compiled and/or tested in the CI pipelines.<br>
The difference between the two is that Continuous Delivery isn't fully automated process as opposed to Continuous Deployment where every change that is tested in the process is eventually deployed to production. In continuous delivery someone is either approving the deployment process or the deployment process is based on constraints and conditions (like time constraint of deploying every week/month/...)
</b></details>

<details>
<summary>What CI/CD best practices are you familiar with? Or what do you consider as CI/CD best practice?</summary><br><b>

* Commit and test often.
* Testing/Staging environment should be a clone of production environment.
* Clean up your environments (e.g. your CI/CD pipelines may create a lot of resources. They should also take care of cleaning up everything they create)
* The CI/CD pipelines should provide the same results when executed locally or remotely
* Treat CI/CD as another application in your organization. Not as a glue code.
* On demand environments instead of pre-allocated resources for CI/CD purposes
* Stages/Steps/Tasks of pipelines should be shared between applications or microservices (don't re-invent common tasks like "cloning a project")
</b></details>

<details>
<summary>You are given a pipeline and a pool with 3 workers: virtual machine, baremetal and a container. How will you decide on which one of them to run the pipeline?</summary><br><b>

The decision on which type of worker (virtual machine, bare-metal, or container) to use for running a pipeline would depend on several factors, including the nature of the pipeline, the requirements of the software being built, the available resources, and the specific goals and constraints of the development and deployment process. Here are some considerations that can help in making the decision:

1. Pipeline requirements
2. Resource availability
3. Scalability and flexibility
4. Deployment and isolation requirements
5. Security considerations
6. Development and operational workflows
7. Cost considerations

Based on these considerations, the appropriate choice of worker (virtual machine, bare-metal, or container) for running the pipeline would be determined by weighing the pros and cons of each option and aligning with the specific requirements, resources, and goals of the development and deployment process. It may also be useful to consult with relevant stakeholders, such as developers, operations, and infrastructure teams, to gather input and make an informed decision.
</b></details>

<details>
<summary>Where do you store CI/CD pipelines? Why?</summary><br><b>

There are multiple approaches as to where to store the CI/CD pipeline definitions:

1. App Repository - store them in the same repository of the application they are building or testing (perhaps the most popular one)
2. Central Repository - store all organization's/project's CI/CD pipelines in one separate repository (perhaps the best approach when multiple teams test the same set of projects and they end up having many pipelines)
3. CI repo for every app repo - you separate CI related code from app code but you don't put everything in one place (perhaps the worst option due to the maintenance)
4. The platform where the CI/CD pipelines are being executed (e.g. Kubernetes Cluster in case of Tekton/OpenShift Pipelines).
</b></details>

<details>
<summary>How do you perform plan capacity for your CI/CD resources? (e.g. servers, storage, etc.)</summary><br><b>

Capacity planning for CI/CD resources involves estimating the resources required to support the CI/CD pipeline and ensuring that the infrastructure has enough capacity to meet the demands of the pipeline. Here are some steps to perform capacity planning for CI/CD resources:

1. Analyze workload
2. Monitor current usage
3. Identify resource bottlenecks
4. Forecast future demand
5. Plan for growth
6. Consider scalability and elasticity
7. Evaluate cost and budget
8. Continuously monitor and adjust

By following these steps, you can effectively plan the capacity for your CI/CD resources, ensuring that your pipeline has sufficient resources to operate efficiently and meet the demands of your development process.
</b></details>

<details>
<summary>How would you structure/implement CD for an application which depends on several other applications?</summary><br><b>

Implementing Continuous Deployment (CD) for an application that depends on several other applications requires careful planning and coordination to ensure smooth and efficient deployment of changes across the entire ecosystem. Here are some general steps to structure/implement CD for an application with dependencies:

1. Define the deployment pipeline
2. Automate the deployment process
3. Version control and dependency management
4. Continuous integration and testing
5. Rolling deployments
6. Monitor and manage dependencies
7. Testing across the ecosystem
8. Rollback and recovery strategies
9. Security and compliance
10. Documentation and communication

Implementing CD for an application with dependencies requires careful planning, coordination, and automation to ensure efficient and reliable deployments. By following best practices such as automation, version control, testing, monitoring, rollback strategies, and effective communication, you can ensure a smooth and successful CD process for your application ecosystem.
</b></details>

<details>
<summary>How do you measure your CI/CD quality? Are there any metrics or KPIs you are using for measuring the quality?</summary><br><b>

Measuring the quality of CI/CD processes is crucial to identify areas for improvement, ensure efficient and reliable software delivery, and achieve continuous improvement. Here are some commonly used metrics and KPIs (Key Performance Indicators) to measure CI/CD quality:

1. Build Success Rate: This metric measures the percentage of successful builds compared to the total number of builds. A high build success rate indicates that the majority of builds are successful and the CI/CD pipeline is stable.
2. Build and Deployment Time: This metric measures the time it takes to build and deploy changes from code commit to production. Faster build and deployment times indicate shorter feedback loops and faster time to market.
3. Deployment Frequency: This metric measures the frequency of deployments to production within a given time period. Higher deployment frequency indicates faster release cycles and more frequent updates to production.
4. Mean Time to Detect (MTTD): This metric measures the average time it takes to detect issues or defects in the CI/CD pipeline or production environment. Lower MTTD indicates faster detection and resolution of issues, leading to higher quality and more reliable deployments.
5. Mean Time to Recover (MTTR): This metric measures the average time it takes to recover from issues or incidents in the CI/CD pipeline or production environment. Lower MTTR indicates faster recovery and reduced downtime, leading to higher availability and reliability.
6. Feedback Loop Time: This metric measures the time it takes to receive feedback on code changes, including code reviews, test results, and other feedback mechanisms. Faster feedback loop times enable quicker iterations and faster improvements in the CI/CD process.
7. Customer Satisfaction: This metric measures the satisfaction of end-users or customers with the quality and reliability of the deployed software. Higher customer satisfaction indicates that the CI/CD process is delivering high-quality software that meets customer expectations.

These are just some examples of metrics and KPIs that can be used to measure the quality of CI/CD processes. It's important to choose metrics that align with the goals and objectives of your organization and regularly track and analyze them to continuously improve the CI/CD process and ensure high-quality software delivery.
</b></details>

#### CI/CD - Jenkins

<details>
<summary>What is Jenkins? What have you used it for?</summary><br><b>

Jenkins is an open source automation tool written in Java with plugins built for Continuous Integration purpose. Jenkins is used to build and test your software projects continuously making it easier for developers to integrate changes to the project, and making it easier for users to obtain a fresh build. It also allows you to continuously deliver your software by integrating with a large number of testing and deployment technologies.

Jenkins integrates development life-cycle processes of all kinds, including build, document, test, package, stage, deploy, static analysis and much more.

</b></details>

<details>
<summary>What are the advantages of Jenkins over its competitors? Can you compare it to one of the following systems?

  * Travis
  * Bamboo
  * Teamcity
  * CircleCI</summary><br><b>

  Jenkins has several advantages over its competitors, including Travis, Bamboo, TeamCity, and CircleCI. Here are some of the key advantages:

1. Open-source and free
2. Customizable and flexible
3. Wide range of integrations and Plugins
4. Active and supportive community

When comparing Jenkins to its competitors, there are some key differences in terms of features and capabilities. For example:

- Travis: Travis is a cloud-based CI/CD platform that is known for its ease of use and fast setup. However, it has fewer customization options and integrations compared to Jenkins.
- Bamboo: Bamboo is a CI/CD tool from Atlassian, the makers of JIRA and Confluence. It provides a range of features for building, testing, and deploying software, but it can be more expensive and complex to set up compared to Jenkins.
- TeamCity: TeamCity is a CI/CD tool from JetBrains, the makers of IntelliJ IDEA. It provides a range of features for building, testing, and deploying software, but it can be more complex and resource-intensive compared to Jenkins.
- CircleCI: CircleCI is a cloud-based CI/CD platform that is known for its fast build times and easy integration with GitHub. However, it can be more expensive compared to Jenkins, especially for larger projects.
</b></details>

<details>
<summary>What are the limitations or disadvantages of Jenkins?</summary><br><b>

This might be considered to be an opinionated answer:

* Old fashioned dashboards with not many options to customize it
* Containers readiness (this has improved with Jenkins X)
* By itself, it doesn't have many features. On the other hand, there many plugins created by the community to expand its abilities
* Managing Jenkins and its pipelines as a code can be one hell of a nightmare
</b></details>

<details>
<summary>Explain the following:

- Job
- Build
- Plugin
- Node or Worker
- Executor</summary><br><b>
- Job is an automation definition = what and where to execute once the user clicks on "build" 
- Build is a running instance of a job. You can have one or more builds at any given point of time (unless limited by configuration)
- A worker is the machine/instance on which the build is running. When a build starts, it "acquires" a worker out of a pool to run on it.
- An executor is variable of the worker, defining how many builds can run on that worker in parallel. An executor value of 3 means, that 3 builds can run at any point on that executor (not necessarily of the same job. Any builds)
</b></details>

<details>
<summary>What plugins have you used in Jenkins?</summary><br><b>

Jenkins has a vast library of plugins, and the most commonly used plugins depend on the specific needs and requirements of each organization. However, here are some of the most popular and widely used plugins in Jenkins:

    Pipeline: This plugin allows users to create and manage complex, multi-stage pipelines using a simple and easy-to-use scripting language. It provides a powerful and flexible way to automate the entire software delivery process, from code commit to deployment.

    Git: This plugin provides integration with Git, one of the most popular version control systems used today. It allows users to pull code from Git repositories, trigger builds based on code changes, and push code changes back to Git.

    Docker: This plugin provides integration with Docker, a popular platform for building, shipping, and running distributed applications. It allows users to build and run Docker containers as part of their build process, enabling easy and repeatable deployment of applications.

    JUnit: This plugin provides integration with JUnit, a popular unit testing framework for Java applications. It allows users to run JUnit tests as part of their build process and generates reports and statistics on test results.

    Cobertura: This plugin provides code coverage reporting for Java applications. It allows users to measure the code coverage of their tests and generate reports on which parts of the code are covered by tests.

    Email Extension: This plugin provides advanced email notification capabilities for Jenkins. It allows users to customize the content and format of email notifications, including attachments, and send notifications to specific users or groups based on build results.

    Artifactory: This plugin provides integration with Artifactory, a popular artifact repository for storing and managing binaries and dependencies. It allows users to publish and retrieve artifacts from Artifactory as part of their build process.

    SonarQube: This plugin provides integration with SonarQube, a popular code quality analysis tool. It allows users to run code quality checks and generate reports on code quality metrics such as code complexity, code duplication, and code coverage.
</b></details>

<details>
<summary>Have you used Jenkins for CI or CD processes? Can you describe them?</summary><br><b>

Let's assume we have a web application built using Node.js, and we want to automate its build and deployment process using Jenkins. Here is how we can set up a simple CI/CD pipeline using Jenkins:

1. Install Jenkins: We can install Jenkins on a dedicated server or on a cloud platform such as AWS or Google Cloud.
2. Install necessary plugins: Depending on the specific requirements of the project, we may need to install plugins such as NodeJS, Git, Docker, and any other plugins required by the project.
3. Create a new job: In Jenkins, a job is a defined set of instructions for automating a particular task. We can create a new job and configure it to build our Node.js application.
4. Configure the job: We can configure the job to pull the latest code from the Git repository, install any necessary dependencies using Node.js, run unit tests, and build the application using a build script.
5. Set up a deployment environment: We can set up a separate environment for deploying the application, such as a staging or production environment. We can use Docker to create a container image of the application and deploy it to the environment.
6. Set up continuous deployment: We can configure the job to automatically deploy the application to the deployment environment if the build and tests pass.
7. Monitor and troubleshoot: We can monitor the pipeline for errors or failures and troubleshoot any issues that arise.

This is just a simple example of a CI/CD pipeline using Jenkins, and the specific implementation details may vary depending on the requirements of the project.
</b></details>

<details>
<summary>What type of jobs are there? Which types have you used?</summary><br><b>

In Jenkins, there are various types of jobs, including:

1. Freestyle job: This is the most common type of job in Jenkins, which allows users to define custom build steps and configure various options, including build triggers, SCM polling, and post-build actions.
2. Pipeline job: Pipeline job is a newer feature in Jenkins that allows users to define a pipeline of jobs that can be executed in a specific order. The pipeline can be defined using a Jenkinsfile, which provides a script-like syntax for defining the pipeline stages, steps, and conditions.
3. Multi-configuration job: This type of job allows users to execute the same job with multiple configurations, such as different operating systems, browsers, or devices. Jenkins will execute the job for each configuration specified, providing a matrix of results.
4. Maven job: This type of job is specifically designed for building Java applications using the Maven build tool. Jenkins will execute the Maven build process, including compiling, testing, and packaging the application.
5. Parameterized job: This type of job allows users to define parameters that can be passed into the build process at runtime. Parameters can be used to customize the build process, such as specifying the version number or target environment.
</b></details>

<details>
<summary>How did you report build results to users? What ways are there to report the results?</summary><br><b>

You can report via:
  * Emails
  * Messaging apps
  * Dashboards

Each has its own disadvantages and advantages. Emails for example, if sent too often, can be eventually disregarded or ignored.
</b></details>

<details>
<summary>You need to run unit tests every time a change submitted to a given project. Describe in details how your pipeline would look like and what will be executed in each stage</summary><br><b>

The pipelines will have multiple stages:

  * Clone the project
  * Install test dependencies (for example, if I need tox package to run the tests, I will install it in this stage)
  * Run unit tests
  * (Optional) report results (For example an email to the users)
  * Archive the relevant logs/files
</b></details>

<details>
<summary>How to secure Jenkins?</summary><br><b>

 [Jenkins documentation](https://www.jenkins.io/doc/book/security/securing-jenkins/) provides some basic intro for securing your Jenkins server.
</b></details>

<details>
<summary>Describe how do you add new nodes (agents) to Jenkins</summary><br><b>

You can describe the UI way to add new nodes but better to explain how to do in a way that scales like a script or using dynamic source for nodes like one of the existing clouds.
</b></details>

<details>
<summary>How to acquire multiple nodes for one specific build?</summary><br><b>

To acquire multiple nodes for a specific build in Jenkins, you can use the "Parallel" feature in the pipeline script. The "Parallel" feature allows you to run multiple stages in parallel, and each stage can run on a different node.

Here is an example pipeline script that demonstrates how to acquire multiple nodes for a specific build:

```tsx
pipeline {
    agent any
    stages {
        stage('Build') {
            parallel {
                stage('Node 1') {
                    agent { label 'node1' }
                    steps {
                        // Run build commands on Node 1
                    }
                }
                stage('Node 2') {
                    agent { label 'node2' }
                    steps {
                        // Run build commands on Node 2
                    }
                }
                stage('Node 3') {
                    agent { label 'node3' }
                    steps {
                        // Run build commands on Node 3
                    }
                }
            }
        }
        stage('Deploy') {
            agent any
            steps {
                // Deploy the built artifacts
            }
        }
    }
}
```

In this example, the "Build" stage has three parallel stages, each running on a different node labeled as "node1", "node2", and "node3". The "Deploy" stage runs after the build is complete and runs on any available node.

To use this pipeline script, you will need to have the three nodes (node1, node2, and node3) configured in Jenkins. You will also need to ensure that the necessary build commands and dependencies are installed on each node.
</b></details>

<details>
<summary>Whenever a build fails, you would like to notify the team owning the job regarding the failure and provide failure reason. How would you do that?</summary><br><b>

In Jenkins, you can use the "Email Notification" plugin to notify a team when a build fails. Here are the steps to set up email notifications for failed builds:

1. Install the "Email Notification" plugin if it's not already installed in Jenkins.
2. Go to the Jenkins job configuration page and click on "Configure".
3. Scroll down to the "Post-build Actions" section and click on "Add post-build action".
4. Select "Editable Email Notification" from the list of options.
5. Fill out the required fields, such as the recipient email addresses, subject line, and email content. You can use Jenkins environment variables, such as ${BUILD_URL} and ${BUILD_LOG}, to include build-specific information in the email content.
6. In the "Advanced Settings" section, select the "Send to recipients" option and choose "Only on failure" from the dropdown menu.
7. Click "Save" to save the job configuration.

With this setup, Jenkins will send an email notification to the specified recipients whenever a build fails, providing them with the failure reason and any other relevant information.
</b></details>

<details>
<summary>There are four teams in your organization. How to prioritize the builds of each team? So the jobs of team x will always run before team y for example</summary><br><b>

In Jenkins, you can prioritize the builds of each team by using the "Priority Sorter" plugin. Here are the steps to set up build prioritization:

1. Install the "Priority Sorter" plugin if it's not already installed in Jenkins.
2. Go to the Jenkins system configuration page and click on "Configure Global Security". Scroll down to the "Access Control" section and click on "Per-project basis".
3. In the "Project default actions" section, select "Configure build triggers and execution" from the dropdown menu. Click on "Add user or group" and add the groups that represent each team in your organization.
4. Go to each Jenkins job configuration page and click on "Configure". Scroll down to the "Build Environment" section and click on "Add build step". Select "Set build priority with Priority Sorter" from the list of options.
5. Set the priority of the job based on the team that owns it. For example, if Team X owns the job, set the priority to a higher value than the jobs owned by Team Y. Click "Save" to save the job configuration.

With this setup, Jenkins will prioritize the builds of each team based on the priority value set in the job configuration. Jobs owned by Team X will have a higher priority than jobs owned by Team Y, ensuring that they are executed first.
</b></details>

<details>
<summary>If you are managing a dozen of jobs, you can probably use the Jenkins UI. But how do you manage the creation and deletion of hundreds of jobs every week/month?</summary><br><b>

Managing the creation and deletion of hundreds of jobs every week/month in Jenkins can be a daunting task if done manually through the UI. Here are some approaches to manage large numbers of jobs efficiently:

1. Use job templates
2. Use Job DSL
3. Use Jenkins REST API
4. Use a configuration management tool
5. Use a Jenkins job management tool
</b></details>

<details>
<summary>What are some of Jenkins limitations?</summary><br><b>

  * Testing cross-dependencies (changes from multiple projects together)
  * Starting builds from any stage (although Cloudbees implemented something called checkpoints)
</b></details>

<details>
<summary>What is the different between a scripted pipeline to declarative pipeline? Which type are you using?</summary><br><b>

Jenkins supports two types of pipelines: Scripted pipelines and Declarative pipelines.

Scripted pipelines use Groovy syntax and provide a high degree of flexibility and control over the build process. Scripted pipelines allow developers to write custom code to handle complex scenarios, but can be complex and hard to maintain.

Declarative pipelines are a newer feature and provide a simpler way to define pipelines using YAML syntax. Declarative pipelines provide a more structured and opinionated way to define builds, making it easier to get started with pipelines and reducing the risk of errors.

Some key differences between the two types of pipelines are:

1. Syntax: Scripted pipelines use Groovy syntax while declarative pipelines use YAML syntax.
2. Structure: Declarative pipelines have a more structured format and define specific stages, while scripted pipelines provide more flexibility in defining build stages and steps.
3. Error handling: Declarative pipelines provide a more comprehensive error handling system with built-in conditions and actions, while scripted pipelines require more manual error handling.
4. Ease of use: Declarative pipelines are easier to use for beginners and provide a simpler syntax, while scripted pipelines require more expertise in Groovy and can be more complex.
5. Maintenance: Declarative pipelines are easier to maintain and can be modified with less effort compared to scripted pipelines, which can be more difficult to modify and extend over time.

I am familiar with both types of pipelines, but generally prefer declarative pipelines for their ease of use and simplicity.
</b></details>

<details>
<summary>How would you implement an option of a starting a build from a certain stage and not from the beginning?</summary><br><b>

To implement an option of starting a build from a certain stage and not from the beginning in a Jenkins pipeline, we can use the `when` directive along with a custom parameter to determine the starting stage. Here are the steps to implement this:

1. Add a custom parameter to the pipeline. This parameter can be a simple string or a more complex data type like a map.
    
    ```tsx
    parameters {
        string(name: 'START_STAGE', defaultValue: '', description: 'The name of the stage to start the build from')
    }
    ```
    
2. Use the `when` directive to conditionally execute stages based on the value of the `START_STAGE` parameter.
    
    ```tsx
    stage('Build') {
        when {
            expression {
                params.START_STAGE == '' || currentStage.name == params.START_STAGE
            }
        }
        // Build steps go here
    }
    
    stage('Test') {
        when {
            expression {
                params.START_STAGE == '' || currentStage.name == params.START_STAGE || previousStage.result == 'SUCCESS'
            }
        }
        // Test steps go here
    }
    
    stage('Deploy') {
        when {
            expression {
                params.START_STAGE == '' || currentStage.name == params.START_STAGE || previousStage.result == 'SUCCESS'
            }
        }
        // Deploy steps go here
    }
    ```
    

  In this example, we use the `when` directive to execute each stage only if the `START_STAGE` parameter is empty or matches the current stage's name. Additionally, for the `Test` and `Deploy` stages, we also check if the previous stage executed successfully before running.

3. Trigger the pipeline and pass the `START_STAGE` parameter as needed.
    
    ```tsx
    pipeline {
        agent any
        parameters {
            string(name: 'START_STAGE', defaultValue: '', description: 'The name of the stage to start the build from')
        }
        stages {
            stage('Build') {
                // Build steps go here
            }
            stage('Test') {
                // Test steps go here
            }
            stage('Deploy') {
                // Deploy steps go here
            }
        }
    }
    ```
    

When triggering the pipeline, you can pass the `START_STAGE` parameter to start the build from a specific stage.

For example, if you want to start the build from the `Test` stage, you can trigger the pipeline with the `START_STAGE` parameter set to `'Test'`:

```tsx
pipeline?START_STAGE=Test
```

This will cause the pipeline to skip the `Build` stage and start directly from the `Test` stage.
</b></details>

<details>
<summary>Do you have experience with developing a Jenkins plugin? Can you describe this experience?</summary><br><b>

Developing a Jenkins plugin requires knowledge of Java and familiarity with Jenkins API. The process typically involves setting up a development environment, creating a new plugin project, defining the plugin's extension points, and implementing the desired functionality using Java code. Once the plugin is developed, it can be packaged and deployed to Jenkins.

The Jenkins plugin ecosystem is extensive, and there are many resources available to assist with plugin development, including documentation, forums, and online communities. Additionally, Jenkins provides tools such as Jenkins Plugin POM Generator and Jenkins Plugin Manager to help with plugin development and management.
</b></details>

<details>
<summary>Have you written Jenkins scripts? If yes, what for and how they work?</summary><br><b>
</b></details>

#### CI/CD - GitHub Actions

<details>
<summary>What is a Workflow in GitHub Actions?</summary><br><b>

A YAML file that defines the automation actions and instructions to execute upon a specific event.<br>
The file is placed in the repository itself.

A Workflow can be anything - running tests, compiling code, building packages, ...
</b></details>

<details>
<summary>What is a Runner in GitHub Actions?</summary><br><b>

A workflow has to be executed somewhere. The environment where the workflow is executed is called Runner.<br>
A Runner can be an on-premise host or GitHub hoste
</b></details>

<details>
<summary>What is a Job in GitHub Actions?</summary><br><b>

A job is a series of steps which are executed on the same runner/environment.<br>
A workflow must include at least one job.
</b></details>

<details>
<summary>What is an Action in GitHub Actions?</summary><br><b>

An action is the smallest unit in a workflow. It includes the commands to execute as part of the job.
</b></details>

<details>
<summary>In GitHub Actions workflow, what the 'on' attribute/directive is used for?</summary><br><b>

Specify upon which events the workflow will be triggered.<br>
For example, you might configure the workflow to trigger every time a changed is pushed to the repository.
</b></details>

<details>
<summary>True or False? In Github Actions, jobs are executed in parallel by default</summary><br><b>

True
</b></details>

<details>
<summary>How to create dependencies between jobs so one job runs after another?</summary><br><b>

Using the "needs" attribute/directive.

```
jobs:
  job1:
  job2:
    needs: job1
```

In the above example, job1 must complete successfully before job2 runs
</b></details>

<details>
<summary>How to add a Workflow to a repository?</summary><br><b>
CLI:

1. Create the directory `.github/workflows` in the repository
2. Add a YAML file

UI:

1. In the repository page, click on "Actions"
2. Choose workflow and click on "Set up this workflow"
</b></details>

#### Zuul

<details>
<summary>In Zuul, What are the <code>check</code> pipelines?</summary><br><b>

`check` pipeline are triggered when a patch is uploaded to a code review system (e.g. Gerrit).<br>
</b></details>

<details>
<summary>In Zuul, What are the <code>gate</code> pipelines?</summary><br><b>

`gate` pipeline are triggered when a code reviewer approves the change in a code review system (e.g. Gerrit)
</b></details>

<details>
<summary>True or False? <code>gate</code> pipelines run after the <code>check</code> pipelines</summary><br><b>

True. `check` pipeline run when the change is uploaded, while the `gate` pipelines run when the change is approved by a reviewer
</b></details>
