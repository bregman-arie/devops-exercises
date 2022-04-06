## AWS Containers - Run Tasks

Note: this costs money

### Objectives

Create a task in ECS to launch in Fargate.

The task itself can be a sample app.

### Solution

#### Console

1. Go to Elastic Container Service page
2. Click on "Get Started"
3. Choose "sample-app"
4. Verify it's using Farget and not ECS (EC2 Instance) and click on "Next"
5. Select "None" in Load balancer type and click on "Next"
6. Insert cluster name (e.g. my_cluster) and click on "Next"
7. Review everything and click on "Create"
8. Wait for everything to complete

1. Go to clusters page and check the status of the task (it will take a couple of seconds/minutes before changing to "Running")

1. Click on the task and you'll see the launch type is Fargate
