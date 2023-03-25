# Observability

- [Observability](#observability)
  - [Monitoring](#monitoring)
  - [Data](#data)
  - [Application Performance Management](#application-performance-management)

<details>
<summary>What's Observability?</summary><br><b>
</b></details>

## Monitoring

<details>
<summary>What's monitoring? How is it related to Observability?</summary><br><b>

Google: "Monitoring is one of the primary means by which service owners keep track of a system’s health and availability".
</b></details>

<details>
<summary>What types of monitoring outputs are you familiar with and/or used in the past?</summary><br><b>

Alerts<br>
Tickets<br>
Logging<br>
</b></details>

## Data

<details>
<summary>Can you mention what type of things are often montiored in the IT industry?</summary><br><b>

- Hardware (CPU, RAM, ...)
- Infrastructure (Disk capacity, Network latency, ...)
- App (Status code, Errors in logs, ...)
</b></details>

<details>
<summary>Explain "Time Series" data</summary><br><b>

Time series data is sequenced data, measuring certain parameter in ordered (by time) way.

An example would be CPU utilization every hour:

```
08:00   17
09:00   22
10:00   91
```
</b></details>

<details>
<summary>Explain data aggregation</summary><br><b>

In monitoring, aggregating data is basically combining collection of values. It can be done in different ways like taking the average of multiple values, the sum of them, the count of many times they appear in the collection and other ways that mainly depend on the type of the collection (e.g. time-series would be one type).

</b></details>


## Application Performance Management

<details>
<summary>What is Application Performance Management?</summary><br><b>

- IT metrics translated into business insights
- Practices for monitoring applications insights so we can improve performances, reduce issues and improve overall user experience

</b></details>

<details>
<summary>Name three aspects of a project you can monitor with APM (e.g. backend)</summary><br><b>

- Frontend
- Backend
- Infra
- ...

</b></details>

<details>
<summary>What can be collected/monitored to perform APM monitoring?</summary><br><b>

- Metrics
- Logs
- Events
- Traces

</b></details>
