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
