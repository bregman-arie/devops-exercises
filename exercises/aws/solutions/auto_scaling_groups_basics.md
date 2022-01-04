## AWS Auto Scaling Groups - Basics

### Requirements

Zero EC2 instances running

### Objectives

A. Create a scaling group for web servers with the following properties:
  * Amazon Linux 2 AMI
  * t2.micro as the instance type
  * user data:
```
yum install -y httpd
systemctl start httpd
systemctl enable httpd
```

B. Were new instances created since you created the auto scaling group? How many? Why?
C. Change desired capacity to 2. Did it launch more instances?
D. Change back the desired capacity to 1. What is the result of this action?

### Solution

#### Console

A.
1. Go to EC2 service
2. Click on "Auto Scaling Groups" under "Auto Scaling"
3. Click on "Create Auto Scaling Group"
4. Insert a name
5. Click on "Create a launch template"
  1. Insert a name and a version for the template
  2. Select an AMI to use (Amazon Linux 2)
  3. Select t2.micro instance type
  4. Select a key pair
  5. Attach a security group
  6. Under "Advanced" insert the user data
  7. Click on "Create"
6. Choose the launch template you've just created and click on "Next"
7. Choose "Adhere to launch template"
8. Choose in which AZs to launch and click on "Next"
9. Link it to ALB (if you don't have one, create it)
10. Mark ELB health check in addition to EC2. Click on "Next" until you reach the review page and click on "Create auto scaling group"

B. One instance was launched to met the criteria of the auto scaling group we've created. The reason it launched only one is due to "Desired capacity" set to 1.
C. Change it by going to your auto scaling group -> Details -> Edit -> "2 desired capacity". This should create another instance if only one is running
D. Reducing desired capacity back to 1 will terminate one of the instances (assuming 2 are running).
