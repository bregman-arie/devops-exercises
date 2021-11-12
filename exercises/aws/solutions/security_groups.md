## AWS EC2 - Security Groups

### Requirements 

For this exercise you'll need:

1. EC2 instance with web application
2. Security group inbound rules that allow HTTP traffic

### Objectives

1. List the security groups you have in your account, in the region you are using
2. Remove the HTTP inbound traffic rule
3. Can you still access the application? What do you see/get?
4. Add back the rule
5. Can you access the application now?

### Solution

#### Console

1. Go to EC2 service - > Click on "Security Groups" under "Network & Security"
   You should see at least one security group. One of them is called "default"
2. Click on the security group with HTTP rules and click on "Edit inbound rules".
   Remove the HTTP related rules and click on "Save rules"
3. No. There is a time out because we removed the rule allowing HTTP traffic.
4. Click on the security group -> edit inbound rules and add the following rule:
  * Type: HTTP
  * Port range: 80
  * Source: Anywhere -> 0.0.0.0/0
5. yes

#### CLI

1. `aws ec2 describe-security-groups` -> by default, there is one security group called "default", in a new account
2. Remove the rule:

```
aws ec2 revoke-security-group-ingress \
    --group-name someHTTPSecurityGroup
    --protocol tcp \
    --port 80 \
    --cidr 0.0.0.0/0
```
3. No. There is a time out because we removed the rule allowing HTTP traffic.
4. Add the rule we remove:

```
aws ec2 authorize-security-group-ingress \
    --group-name someHTTPSecurityGroup
    --protocol tcp \
    --port 80 \
    --cidr 0.0.0.0/0
```
5. yes
