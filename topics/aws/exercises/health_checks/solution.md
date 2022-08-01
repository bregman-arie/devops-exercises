## AWS Route 53 - Health Checks

## Requirements

3 web instances in different AZs.

## Objectives 

1. For each instance create a health checks with the following properties:
  1. Name it after the AZ where the instance resides
  2. Failure threshold should be 5

2. Edit the security group of one of your instances and remove HTTP rules.
  1. Did it change the status of the health check?

### Solution

#### Console

1. Go to Route 53
2. Click on "Health Checks" in the left-side menu
3. Click on "Create health check"
4. Insert the name: us-east-2
5. What to monitor: endpoint
6. Insert the IP address of the instance
7. Insert the endpoint /health if your web instance supports that endpoint
8. In advanced configuration, set Failure threshold to 5
9. Click on "next" and then on "Create health check"
10. Repeat steps 1-9 for the other two instances you have

1. Go to security group of one of your instances
2. Click on "Actions" -> Edit inbound rules -> Delete HTTP based rules
3. Go back to health checks page and after a couple of seconds you should see that the status becomes "unhealthy"
