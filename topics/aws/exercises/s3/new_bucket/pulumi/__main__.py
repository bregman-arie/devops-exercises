import pulumi_aws as aws

# Private Bucket
private_bucket = aws.s3.Bucket("my-first-private-bucket",
                               acl="private",
                               tags={
                                   "Environment": "Exercise",
                                   "Name": "My First Private Bucket"},
                               region="eu-west-2"
                               )

# Bucket Object
aws.s3.BucketObject("bucketObject",
                    key="some_object_key",
                    bucket=private_bucket.id,
                    content="object content")

# Public Bucket
aws.s3.Bucket("my-first-public-bucket",
              acl="public-read",
              tags={
                  "Environment": "Exercise",
                  "Name": "My First Public Bucket"},
              region="eu-west-1",
              versioning=aws.s3.BucketVersioningArgs(enabled=True))
