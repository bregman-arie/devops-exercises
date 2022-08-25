resource "aws_s3_bucket" "private_bucket" {
  bucket = "my-first-private-bucket"
  region = "eu-west-2"
  acl = "private" 

  tags = {
    Name        = "My First Private Bucket"
    Environment = "Exercise"
  }
}

resource "aws_s3_bucket_acl" "private_bucket_acl" {
  bucket = aws_s3_bucket.private_bucket.id
  acl    = "private"
}

resource "aws_s3_bucket" "public_bucket" {
  bucket = "my-first-public-bucket"
  region = "eu-west-1"

  tags = {
    Name        = "My First Public Bucket"
    Environment = "Exercise"
  }

  versioning {
    enabled = true
  }
}

resource "aws_s3_bucket_acl" "public_bucket_acl" {
  bucket = aws_s3_bucket.public_bucket.id
  acl    = "public-read"
}

resource "aws_s3_bucket_object" "bucket_object" {
  bucket   = "my-first-private-bucket"
  key      = "some_object_key"
  content  = "object content"
}