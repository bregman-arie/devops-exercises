# Circle CI

## Circle CI Questions

### Circle CI 101

<details>
<summary>What is Circle CI?</summary><br><b>

[Circle CI](https://circleci.com): "CircleCI is a continuous integration and continuous delivery platform that can be used to implement DevOps practices."
</b></details>

<details>
<summary>What are some benefits of Circle CI?</summary><br><b>

[Circle CI Docs](https://circleci.com/docs/about-circleci): "SSH into any job to debug your build issues.
Set up parallelism in your .circleci/config.yml file to run jobs faster.
Configure caching with two simple keys to reuse data from previous jobs in your workflow.
Configure self-hosted runners for unique platform support.
Access Arm resources for the machine executor.
Use orbs, reusable packages of configuration, to integrate with third parties.
Use pre-built Docker images in a variety of languages.
Use the API
 to retrieve information about jobs and workflows.
Use the CLI to access advanced tools locally.
Get flaky test detection with test insights."
</b></details>

<details>
<summary>Explain the following:

* Pipeline
* Workflow
* Jobs
* Steps
</summary><br><b>

* Pipeline: the entire CI/CD configuration (.circleci/config.yaml)
* Workflow: primarily used when there is more than one job in the configuration to orchestrate the workflows
* Jobs: One or more steps to execute as part of the CI/CD process
* Steps: The actual commands to execute
</b></details>

<details>
<summary>What is an Orb?</summary><br><b>

[Circle CI Docs](https://circleci.com/developer/orbs): "Orbs are shareable packages of CircleCI configuration you can use to simplify your builds" 

They can come from the public registry or defined privately as part of an organization.
</b></details>

### Circle CI Hands-On 101

<details>
<summary>Where (in what location in the project) Circle CI pipelines are defined?</summary><br><b>

`.circleci/config.yml`
</b></details>

<details>
<summary>Explain the following configuration file


```
version: 2.1

jobs:
  say-hello:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - run:
          name: "Say hello"
          command: "echo Hello, World!"
workflows:
  say-hello-workflow:
    jobs:
      - say-hello
```
</summary><br><b>

This configuration file will set up one job that will checkout the code of the project will run the command `echo Hello, World!`.
It will run in a container using the image `cimg/base:stable`.
</b></details>