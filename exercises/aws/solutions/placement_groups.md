## AWS EC2 - Placement Groups          

### Objectives                      

A. Create a placement group. It should be one with a low latency network. Make sure to launch an instance as part of this placement group.
B. Create another placement group. This time high availability is a priority

### Solution                        

A.
1. Go to EC2 service
2. Click on "Placement Groups" under "Network & Security"
3. Click on "Create placement group"
4. Give it a name and choose the "Cluster" placement strategy because the requirement is low latency network
5. Click on "Create group"
6. Go to "Instances" and click on "Launch an instance". Choose any properties you would like, just make sure to check "Add instance to placement group" and choose the placement group you've created

B.
1. Go to EC2 service
2. Click on "Placement Groups" under "Network & Security"
3. Click on "Create placement group"
4. Give it a name and choose the "Spread" placement strategy because the requirement is high availability as top priority
5. Click on "Create group"
