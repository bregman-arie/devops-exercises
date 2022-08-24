# My First VPC

## Objectives

1. Create a new VPC
   1.  It should have a CIDR that supports using at least 60,000 hosts
   2.  It should be named "exercise-vpc"

## Solution

### Console

1. Under "Virtual Private Cloud" click on "Your VPCs"
2. Click on "Create VPC"
3. Insert a name - "exercise-vpc"
4. Insert IPv4 CIDR block: 10.0.0.0/16
5. Keep "Tenancy" at Default
6. Click on "Create VPC"

### Terraform

Click [here](terraform/main.tf) to view the solution

### Pulumi - Python

Click [here](pulumi/__main__.py) to view the solution

### Verify Solution

To verify you've create the VPC, you can run: `aws ec2 describe-vpcs -filters Name=tag:Name,Values=exercise-vpc`