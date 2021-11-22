## AWS ELB - ALB Multiple Target Groups

### Requirements                   

Two EC2 instances with a simple web application that shows the web page with the string "Hey, it's a me, `<HOSTNAME>`!"
One EC2 instance with a simple web application that shows the web page with the string "Hey, it's only a test..." under the endpoint /test

### Objectives

1. Create an application load balancer for the two instances you have, with the following properties
  1. healthy threshold: 3
  2. unhealthy threshold: 3
  3. interval: 10 seconds
2. Create another target group for the third instance
  1. Traffic should be forwarded to this group based on the "/test" path

### Solution

#### Console

1. Go to EC2 service
2. Click in the left side menu on "Load balancers" under "Load balancing"
3. Click on "Create load balancer"
4. Choose "Application Load Balancer"
5. Insert a name for the LB
6. Choose an AZ where you want the LB to operate
7. Choose a security group
8. Under "Listeners and routing" click on "Create target group" and choose "Instances"
  1. Provide a name for the target group
  2. Set healthy threshold to 3
  3. Set unhealthy threshold to 3
  4. Set interval to 10 seconds
  5. Click on "Next" and choose two out of three instances you've created
  6. Click on "Create target group"
9. Refresh target groups and choose the one you've just created
10. Click on "Create load balancer" and wait for it to be provisioned

11. In the left side menu click on "Target Groups" under "Load Balancing"
12. Click on "Create target group"
13. Set it with the same properties as previous target group but this time, add the third instance that you didn't include in the previous target group
14. Go back to your ALB and under "Listeners" click on "Edit rules" under your current listener
  1. Add a rule where if the path is "/test" then traffic should be forwarded to the second target group you've created
  2. Click on "Save"
15. Test it by going to the browser, insert the address and add "/test" to the address
