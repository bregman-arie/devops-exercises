import pulumi
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("exercise-vpc", cidr_block="10.0.0.0/16")

pulumi.export("vpc_id", vpc.vpc_id)
pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
pulumi.export("privateSubnetIds", vpc.private_subnet_ids)

# Run 'pulumi up' to create it
