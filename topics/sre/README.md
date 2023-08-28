# Site Reliability Engineering

## SRE Questions

<details>
<summary>What is an SLI (Service-Level Indicator)?</summary>
<b>
An SLI is a measurement used to assess the actual performance or reliability of a service. It serves as the basis for defining SLOs.

Examples:
- Request latency
- Processing throughput
- Request failures per unit of time

Read more: [Google SRE Handbook](https://sre.google/sre-book/table-of-contents/)
</b>
</details></br>

<details>
<summary>What is an SLO (Service-Level Objective)?</summary>
<b>

An SLO is a target value or range of values for a service level that is measured by an SLI

Example: 99% across 30 days for a specific collection of SLIs.

It's also worthy to note that the SLO also serves as a lower bound, indicating that there is no requirement to be more reliable than necessary because doing so can delay the rollout of new features.

Read more: [Google SRE Handbook](https://sre.google/sre-book/table-of-contents/)
</b>
</details><br>

<details>
<summary>What is an SLA (Service-Level Agreement)?</summary>
<b>

AN SLA is a formal agreement between a service provider and customers, specifying the expected service quality and consequences for not meeting it.

SRE doesn't typically get involved in constructing SLAs, because SLAs are closely tied to business and product decisions

Read more: [Google SRE Handbook](https://sre.google/sre-book/table-of-contents/)
</b>
</details><br>

<details>
<summary>What is an Error Budget?</summary>
<b>

An Error Budget represents the acceptable amount of downtime or errors a service can experience while still meeting its SLO.

An error budget is 1 minus the SLO of the service. A 99.9% SLO service has a 0.1% error budget.

If our service receives 1,000,000 requests in four weeks, a 99.9% availability SLO gives us a budget of 1,000 errors over that period.

The error budget is a mechanism for balancing innovation and stability. If the SRE cannot enforce the error budget, the whole system breaks down.

Read more: [Google SRE Handbook](https://sre.google/sre-book/table-of-contents/)
</b>
</details></br>

<details>
<summary>What is Toil?</summary>
<b>

Toil is the kind of work that tends to be manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows.

If you can be automate a task, you should probably automate the task.

Automation significantly reduces Toil. Investing in automation results in valuable work with lasting impact, offering scalability potential with minimal adjustments as your system expands.

Read more: [Google SRE Handbook](https://sre.google/sre-book/table-of-contents/)
</b>
</details>