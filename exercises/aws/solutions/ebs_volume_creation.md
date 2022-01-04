## AWS EC2 - EBS Volume Creation

### Requirements

One EC2 instance that you can get rid of :)

### Objectives

1. Create a volume in the same AZ as your instance, with the following properties:
  1. gp2 volume type
  2. 4 GiB size
2. Once created, attach it to your EC2 instance
3. Remove your EC2 instance. What happened to the EBS volumes attached to the EC2 instance?

### Solution

1. Go to EC2 service
2. Click on "Volumes" under "Elastic Block Store"
3. Click on "Create Volume"
4. Select the following properties 
  1. gp2 volume type
  2. 4 GiB size
  3. The same AZ as your instance
5. Click on "Create volume"
6. Right click on the volume you've just created -> attach volume -> choose your EC2 instance and click on "Attach"
7. Terminate your instance
8. The default EBS volume (created when you launched the instance for the first time) will be deleted (unless you didn't check "Delete on termination"), but the volume you've created as part of this exercise, will remain

Note: don't forget to remove the EBS volume you've created in this exercise
