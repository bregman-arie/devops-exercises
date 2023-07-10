## AWS EC2 - Elastic IP

### Requirements

* An EC2 instance with public IP (not elastic IP)

### Objectives

1. Write down the public IP of your EC2 instance somewhere and stop & start the instance. Does the public IP address is the same? why?
2. Handle this situation so you have the same public IP even after stopping and starting the instance

### Solution

1. Go to EC2 service -> Instances
  1. Write down current public IP address
  2. Click on "Instance state" -> Stop instance -> Stop
  3. Click on "Instance state" -> Start Instance
  4. Yes, the public IP address has changed
2. Let's use an Elastic IP address
  1. In EC2 service, under "Network & Security" click on "Elastic IP"
  2. Click on the "Allocate elastic IP address" button
  3. Make sure you select "Amazon's pool of IPv4 addresses" and click on "Allocate"
  4. Click on "Actions" and then "Associate Elastic IP address"
    1. Select "instance", choose your instance and provide its private IP address
    2. Click on "Associate"
  5. Now, if we go back to the instance page, we can see it is using the Elastic IP address as its public IP

Note: to remove it, use "disassociate" option and don't forget to also release it so you won't be billed.
