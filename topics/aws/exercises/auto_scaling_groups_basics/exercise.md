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
