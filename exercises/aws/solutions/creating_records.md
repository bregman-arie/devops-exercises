## AWS Route 53 - Creating Records

### Requirements

At least one registered domain

### Objectives

1. Create the following record for your domain:
  1. Record name: foo
  2. Record type: A
  3. Set some IP in the value field

2. Verify from the shell that you are able to use the record you've created to lookup for the IP address by using the domain name

### Solution

1. Go to Route 53 service -> Hosted zones
2. Click on your domain name
3. Click on "Create record"
4. Insert "foo" in "Record name"
5. Set "Record type" to A
6. In "Value" insert "201.7.20.22"
7. Click on "Create records"

1. In your shell, type `nslookup foo.<YOUR DOMAIN>` or `dig foo.<YOUR NAME`
