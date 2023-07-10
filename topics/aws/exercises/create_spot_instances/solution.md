## AWS EC2 - Spot Instances                                                                                                                                                  
### Objectives             

A. Create two Spot instances using a Spot Request with the following properties:

* Amazon Linux 2 AMI
* 2 instances as target capacity (at any given point of time) while each one has 2 vCPUs and 3 GiB RAM

B. Create a single Spot instance using Amazon Linux 2 and t2.micro

### Solution               

A. Create Spot Fleets:

1. Go to EC2 service
2. Click on "Spot Requests"
3. Click on "Request Spot Instances" button
4. Set the following values for parameters:
  * Amazon Linux 2 AMI
  * Total target capacity -> 2
  * Check "Maintain target capacity"
  * vCPUs: 2
  * Memory: 3 GiB RAM
5. Click on Launch

B. Create a single Spot instance:

1. Go to EC2 service
2. Click on "Instances"
3. Click on "Launch Instances"
4. Choose "Amazon Linux 2 AMI" and click on "Next"
5. Choose t2.micro and click on "Next: Configure Instance Details"
6. Select "Request Spot instances" 
7. Set Maximum price above current price
8. Click on "Review and Launch"
