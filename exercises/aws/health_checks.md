## AWS Route 53 - Health Checks

## Requirements

3 web instances in different AZs.

## Objectives 

1. For each instance create a health checks with the following properties:
  1. Name it after the AZ where the instance resides
  2. Failure threshold should be 5

2. Edit the security group of one of your instances and remove HTTP rules.
  1. Did it change the status of the health check?
