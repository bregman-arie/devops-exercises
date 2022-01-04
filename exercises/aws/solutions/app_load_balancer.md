## AWS ELB - Application Load Balancer 

### Requirements

Two EC2 instances with a simple web application that shows the web page with the string "Hey, it's a me, `<HOSTNAME>`!"

### Objectives

1. Create an application load balancer for the two instances you have, with the following properties
  1. healthy threshold: 3
  2. unhealthy threshold: 3
  3. interval: 10 seconds
2. Verify load balancer is working  (= you get reply from both instances at different times)

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
  5. Click on "Next" and choose the two of the instances you've created
  6. Click on "Create target group"
9. Refresh target groups and choose the one you've just created
10. Click on "Create load balancer" and wait for it to be provisioned
11. Copy DNS address and paste it in the browser. If you refresh, you should see different message based on the instance where the traffic was routed to
