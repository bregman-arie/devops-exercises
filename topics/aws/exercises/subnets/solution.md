# AWS VPC - Subnets

## Requirements

1. Single newly created VPC
2. Region with more than two availability zones

## Objectives

1. Create a subnet in your newly created VPC
   1. CIDR: 10.0.0.0/24
   1. Name: NewSubnet1
2. Create additional subnet
   1. CIDR: 10.0.1.0/24
   2. Name: NewSubnet2
   3. Different AZ compared to previous subnet
3. Create additional subnet
   4. CIDR: 10.0.2.0/24
   5. Name: NewSubnet3
   6. Different AZ compared to previous subnets

## Solution

### Console

1. Click on "Subnets" under "Virtual Private Cloud"
2. Make sure you filter by your newly created VPC (to not see the subnets in all other VPCs). You can do this in the left side menu
3. Click on "Create subnet"
4. Choose your newly created VPC
5. Set the subnet name to "NewSubnet1"
6. Choose AZ
7. Set CIDR to 10.0.0.0/24
8. Click on "Add new subnet"
9. Set the subnet name to "NewSubnet2"
10. Choose a different AZ
11. Set CIDR to 10.0.1.0/24
12. Click on "Add new subnet"
13. Set the subnet name to "NewSubnet3"
14. Choose a different AZ
15. Set CIDR to 10.0.2.0/24

### Terraform

Click [here](terraform/main.tf) to view the solution

### Pulumi - Python

Click [here](pulumi/__main__.py) to view the solution