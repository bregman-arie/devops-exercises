# Chaos Engineering

- [Chaos Engineering](#chaos-engineering)
  - [Chaos Engineering Questions](#chaos-engineering-questions)
    - [Basics](#basics)

## Chaos Engineering Questions

### Basics

<details>
<summary>What is Chaos Engineering?</summary><br><b>

[Wikipedia](https://en.wikipedia.org/wiki/Chaos_engineering): "Chaos Engineering is the discipline of experimenting on a system in order to build confidence in the system's capability to withstand turbulent conditions in production."

[TechTarget](https://www.techtarget.com/searchitoperations/definition/chaos-engineering): "Chaos engineering is the process of testing a distributed computing system to ensure that it can withstand unexpected disruptions."

</b></details>

<details>
<summary>What's a typical Chaos Engineering workflow?</summary><br><b>

According to [Gremlin](gremlin.com) there are three steps:

1. Planning an experiment where you design and choose a scenario in which your system should fail to operate properly
2. You execute the smallest possible experiment to test your theory
3. If nothing goes wrong, you scale your experiment and make the blast radius bigger. If your system breaks, you better understand why and start dealing with it

The process then repeats itself either with same scenario or a new one.

</b></details>

<details>
<summary>Cite a few tools used to operate Chaos exercises</summary><br><b>

- AAWS Fault Injection Simulator: inject failures in AWS resources
- Azure Chaos Studio: inject failures in Azure resources
- Chaos Monkey: one of the most famous tools to orchestrate Chaos on diverse Cloud providers
- Litmus - A Framework for Kubernetes 
- Chaos Mesh: for Cloud Kubernetes platforms


See an extensive list [here](https://github.com/dastergon/awesome-chaos-engineering)

</b></details>