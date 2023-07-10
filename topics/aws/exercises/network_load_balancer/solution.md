## AWS ELB - Network Load Balancer

### Requirements                   

Two running EC2 instances

### Objectives

1. Create a network load balancer 
  1. healthy threshold: 3
  2. unhealthy threshold: 3
  3. interval: 10 seconds
  4. Listener should be using TCP protocol on port 80

### Solution

#### Console

1. Go to EC2 service
2. Click in the left side menu on "Load balancers" under "Load balancing"
3. Click on "Create load balancer"
4. Choose "Network Load Balancer"
5. Insert a name for the LB
6. Choose AZs where you want the LB to operate
7. Choose a security group
8. Under "Listeners and routing" click on "Create target group" and choose "Instances"
  1. Provide a name for the target group
  2. Set healthy threshold to 3
  3. Set unhealthy threshold to 3
  4. Set interval to 10 seconds
  5. Set protocol to TCP and port to 80
  6. Click on "Next" and choose two instances you have
  7. Click on "Create target group"
9. Refresh target groups and choose the one you've just created
10. Click on "Create load balancer" and wait for it to be provisioned
