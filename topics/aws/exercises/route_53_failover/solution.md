## AWS Route 53 - Failover

### Requirements

A running EC2 web instance with an health check defined for it in Route 53

### Objectives

1. Create a failover record that will failover to another record if an health check isn't passing
  1. Make sure TTL is 30
  2. Associate the failover record with the health check you have

### Solution

#### Console

1. Go to Route 53 service
2. Click on "Hosted Zones" in the left-side menu
3. Click on your hosted zone
4. Click on "Created record"
5. Insert "failover" in record name and set record type to A
6. Insert the IP of your instance
7. Set the routing policy to failover
8. Set TTL to 30
9. Associate with an health check
10. Add another record with the same properties as the previous one
11. Click on "Create records"
12. Go to your EC2 instance and edit its security group to remove the HTTP rules
13. Use your web app and if you print the hotsname of your instance then you will notice, a failover was performed and a different EC2 instance is used
