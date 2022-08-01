# Apache Kafka

## Kafka Exercises

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|

## Kafka Self Assessment

* [Kafka 101](#questions-kafka-101)

<a name="questions-kafka-101"></a>
### Kafka 101

<details>
<summary>What is Kafka?</summary><br><b>

[kafka.apache.org](https://kafka.apache.org): "Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications."

In other words, Kafka is a sort of distributed log where you can store events, read them and distribute them to different services and do it in high-scale and real-time.
</b></details>

<details>
<summary>What Kafka is used for?</summary><br><b>

- Real-time e-commerce
- Banking
- Health Care
- Automotive (traffic alerts, hazard alerts, ...)
- Real-time Fraud Detection
</b></details>

<details>
<summary>What is a "Producer" in regards to Kafka?</summary><br><b>

An application that publishes data to the Kafka cluster.
</b></details>

<a name="questions-kafka-architecture"></a>
### Kafka Architecture

<details>
<summary>What's in a Kafka cluster?</summary><br><b>

- Broker: a server with kafka process running on it. Such server has local storage. In a single Kafka clusters there are usually multiple brokers.
</b></details>
