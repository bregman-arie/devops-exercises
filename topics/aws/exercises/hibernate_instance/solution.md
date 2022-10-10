## AWS EC2 - Hibernate an Instance

### Objectives

1. Create an instance that supports hibernation
2. Hibernate the instance
3. Start the instance
4. What way is there to prove that instance was hibernated from OS perspective?

### Solution

1. Create an instance that supports hibernation
  1. Go to EC2 service
  2. Go to instances and create an instance
  3. In "Configure instance" make sure to check "Enable hibernation as an additional stop behavior"
  4. In "Add storage", make sure to encrypt EBS and make sure the size > instance RAM size (because hibernation saves the RAM state)
  5. Review and Launch

2. Hibernate the instance
  1. Go to the instance page
  2. Click on "Instance state" -> "Hibernate instance" -> Hibernate

3. Instance state -> Start

4. Run the "uptime" command, which will display the amount of time the system was up
