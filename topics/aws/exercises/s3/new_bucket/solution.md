# Create buckets

## Objectives

1. Create the following buckets:
   1. Private bucket
      1. eu-west-2 region
      2. Upload a single file to the bucket. Any file.
   2. Public bucket
      1. eu-west-1 region
      2. Versioning should be enabled

## Solution

### Console

For the first bucket:

1. Go to S3 service in the AWS console. If not in buckets page, click on "buckets" in the left side menu
2. Click on "Create bucket" 
3. Give a globally unique name for your bucket
4. Choose the region "eu-west-2"
5. Click on "Create bucket"
6. Click on the bucket name
7. Under "objects" click on "Upload" -> "Add files" -> Choose file to upload -> Click on "Upload"

For the second bucket:

1. Go to S3 service in the AWS console. If not in buckets page, click on "buckets" in the left side menu
2. Click on "Create bucket" 
3. Give a globally unique name for your bucket
4. Choose the region "eu-west-1"
5. Make sure to uncheck the box for "Private bucket" to make it public
6. Make sure to check the enable box for "Bucket Versioning"
7. Click on "Create bucket"

### Terraform

Click [here](terraform/main.tf) to view the solution

### Pulumi - Python

Click [here](pulumi/__main__.py) to view the solution