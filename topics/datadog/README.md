# DataDog

- [DataDog](#datadog)
  - [Questions](#questions)
    - [Basics](#basics)
  - [Datadog Agent](#datadog-agent)
  - [Datadog Integrations](#datadog-integrations)

## Questions

### Basics


<details>
<summary>Describe at least three use cases for using something like Datadog. Can be as specific as you would like</summary><br><b>

* Monitor instances/servers downtime
* Detect anomalies and send an alert when it happens
* Service request or response latency

</b></details>

<details>
<summary>What ways are there to collect or send data to Datadog?</summary><br><b>

* Datadog agent installed on the device or location which you would like to monitor
* Using Datadog API
* Built-in integrations

</b></details>

<details>
<summary>What is a host in regards to Datadog?</summary><br><b>

Any physical or virtual instance that is monitored with Datadog. Few examples:

- Cloud Instance, Virtual Machine
- Bare metal node
- Platform or service specific nodes like Kubernetes node

Basically any device or location that has Datadog agent installed and running on.
</b></details>

<details>
<summary>What is a Datadog agent?</summary><br><b>

A software runs on a Datadog host. Its purpose is to collect data from the host and sent it to Datadog (data like metrics, logs, etc.)
</b></details>

<details>
<summary>What are Datadog tags?</summary><br><b>

Datadog tags are used to mark different information with unique properties. For example, you might want to tag some data with "environment: production" while tagging information from staging or dev environment with "environment: staging".
</b></details>

## Datadog Agent

<details>
<summary>What are the component of a Datadog agent?</summary><br><b>

* Collector: its role is to collect data from the host on which it's installed. The default period of time as of today is every 15 seconds.
* Forwarder: responsible for sending the data to Datadog over HTTPS
</b></details>

## Datadog Integrations


<details>
<summary>What can you tell about Datadog integrations?</summary><br><b>

- Datadog has many supported integrations with different services, platforms, etc.
- Each integration includes information on how to apply it, how to use it and what configuration options it supports
</b></details>

<details>
<summary>What opening some of the integrations windows/pages, there is a ection called "Monitors". What can be found there?</summary><br><b>

Usually you can find there some anomaly types that Datadog suggests to monitor and track.
</b></details>