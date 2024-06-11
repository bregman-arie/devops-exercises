## AWS - Launch EC2 Web Instance

### Objectives

Launch one EC2 instance with the following requirements:

1. Amazon Linux 2 image
2. Instance type: pick up one that has 1 vCPUs and 1 GiB memory
3. Instance storage should be deleted upon the termination of the instance
4. When the instance starts, it should install:
  1. Install the httpd package
  2. Start the httpd service
  3. Make sure the content of /var/www/html/index.html is `I made it! This is is awesome!`
5. It should have the tag: "Type: web" and the name of the instance should be "web-1"
6. HTTP traffic (port 80) should be accepted from anywhere

### Solution

1. Choose a region close to you 
2. Go to EC2 service
3. Click on "Instances" in the menu and click on "Launch instances"
4. Choose image: Amazon Linux 2
5. Choose instance type: t2.micro 
6. Make sure "Delete on Termination" is checked in the storage section
7. Under the "User data" field the following:

```
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>I made it! This is is awesome!</h1>" > /var/www/html/index.html
```
8. Add tags with the following keys and values:
  * key "Type" and the value "web"
  * key "Name" and the value "web-1"
9. In the security group section, add a rule to accept HTTP traffic (TCP) on port 80 from anywhere
10. Click on "Review" and then click on "Launch" after reviewing.
11. If you don't have a key pair, create one and download it.

12. ### Solution using Terraform

```
 
provider "aws" {
  region = "us-east-1" // Or your desired region
}

resource "aws_instance" "web_server" {
  ami           = "ami-12345678" // Replace with the correct AMI for Amazon Linux 2
  instance_type = "t2.micro" // Or any instance type with 1 vCPU and 1 GiB memory

  tags = {
    Name = "web-1"
    Type = "web"
  }

  root_block_device {
    volume_size           = 8 // Or any desired size
    delete_on_termination = true
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y httpd",
      "sudo systemctl start httpd",
      "sudo bash -c 'echo \"I made it! This is awesome!\" > /var/www/html/index.html'",
      "sudo systemctl enable httpd"
    ]

    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("~/.ssh/your_private_key.pem") // Replace with the path to your private key
      host        = self.public_ip
    }
  }

  security_group_ids = [aws_security_group.web_sg.id]
}

resource "aws_security_group" "web_sg" {
  name        = "web_sg"
  description = "Security group for web server"
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```