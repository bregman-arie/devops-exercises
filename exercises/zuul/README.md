# Zuul

## Questions

### Basics

<details>
<summary>Describe shortly what is Zuul</summary><br><b>

From [Zuul's docs](https://zuul-ci.org/docs/zuul/about.html): "Zuul is a Project Gating System. That’s like a CI or CD system, but the focus is on testing the future state of code repositories...

Zuul itself is a service which listens to events from various code review systems, executes jobs based on those events, and reports the results back to the code review system."
</b></details>

<details>
<summary>What is Nodepool and how is it related to Zuul?</summary><br><b>

"Nodepool is a system for managing test node resources. It supports launching single-use test nodes from cloud providers as well as managing access to pre-defined pre-existing nodes."

"Zuul uses a separate component called Nodepool to provide the resources to run jobs. Nodepool works with several cloud providers as well as statically defined nodes (again, simultaneously)."
</b></details>

<details>
<summary>What is a Pipeline in Zuul?</summary><br><b>

A pipeline in Zuul is a workflow. This workflow can be executed based on different events - when a change is submitted to a project, when it's merged, etc.<br>
The pipeline itself can be applied on one or more different projects (= repositories in hosted or private source control)
</b></details>

<details>
<summary>What is a project in Zuul?</summary><br><b>
</b></details>
