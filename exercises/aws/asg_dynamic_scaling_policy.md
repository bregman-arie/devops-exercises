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
