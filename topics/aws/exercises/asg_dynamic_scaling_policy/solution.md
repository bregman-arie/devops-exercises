## AWS Auto Scaling Groups - Dynamic Scaling Policy

### Requirements

1. Existing Auto Scaling Group with maximum capacity set to at least 3
2. One running EC2 instance with max of 4 CPUs

### Objectives

1. Create a dynamic scaling policy with the following properties
  1. Track average CPU utilization
  2. Target value should be 70%
2. Increase the CPU utilization to at least 70%
  1. Do you see change in number of instances?
1. Decrease CPU utilization to less than 70%
  1. Do you see change in number of instances?

### Solution

#### Console

1. Go to EC2 service -> Auto Scaling Groups and click on the tab "Automating scaling"
2. Choose "Target tracking scaling" under "Policy Type"
3. Set metric type to Average CPU utilization
4. Set target value to 70% and click on "Create"

1. If you are using Amazon Linux 2, you can stress the instance with the following:

```
sudo amazon-linux-extras install epel -y
sudo yum install stress -y
stress -c 4  # assuming you have 4 CPUs
```
2. Yes, additional EC2 instance was added

1. Simply stop the stress command
2. Yes, one of the EC2 instances was terminated
