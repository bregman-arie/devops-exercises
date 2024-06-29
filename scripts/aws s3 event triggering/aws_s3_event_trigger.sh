#!/bin/bash

# always put up the detail of scripts . version, author, what it does, what event triggers and all .. 

###
# Author: Adarsh Rawat
# Version: 1.0.0
# Objective: Automate Notification for a object uploaded or created in s3 bucket.
###

# debug what is happening
set -x

# all these cmds are aws cli commands | abhishek veermalla day 4-5 devops

# store aws account id in a variable
aws_account_id=$(aws sts get-caller-identity --query 'Account' --output text)

# print the account id from the variable
echo "aws account id: $aws_account_id"

# set aws region, bucket name and other variables
aws_region="us-east-1" 
aws_bucket="s3-lambda-event-trigger-bucket"
aws_lambda="s3-lambda-function-1"
aws_role="s3-lambda-sns"
email_address="adarshrawat8304@gmail.com"

# create iam role for the project
role_response=$(aws iam create-role --role-name s3-lambda-sns --assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [{
    "Action": "sts:AssumeRole",
    "Effect": "Allow",
    "Principal": {
      "Service": [
        "lambda.amazonaws.com",
        "s3.amazonaws.com",
        "sns.amazonaws.com"
      ]
    }
  }]
}')

# jq is json parser here parse the role we created 

# extract the role arn from json resposne and store in variable
role_arn=$(echo "$role_response" | jq -r '.Role.Arn')

# print the role arn
echo "Role ARN: $role_arn"

# attach permissions to the role
aws iam attach-role-policy --role-name $aws_role --policy-arn arn:aws:iam::aws:policy/AWSLambda_FullAccess
aws iam attach-role-policy --role-name $aws_role --policy-arn arn:aws:iam::aws:policy/AmazonSNSFullAccess

# create s3 bucket and get the output in a variable
bucket_output=$(aws s3api create-bucket --bucket "$aws_bucket" --region "$aws_region")

# print the output from the variable 
echo "bucket output: $bucket_output"

# upload a file to the bucket
aws s3 cp ./sample.png s3://"$aws_bucket"/sample.png

# create a zip file to upload lambda function 
zip -r s3-lambda.zip ./s3-lambda

sleep 5

# create a lambda function
aws lambda create-function \
  --region $aws_region \
  --function $aws_lambda \
  --runtime "python3.8" \
  --handler "s3-lambda/s3-lambda.lambda_handler" \
  --memory-size 128 \
  --timeout 30 \
  --role "arn:aws:iam::$aws_account_id:role/$aws_role" \
  --zip-file "fileb://./s3-lambda.zip"

# add permissions to s3 bucket to invoke lambda
LambdaFunctionArn="arn:aws:lambda:us-east-1:$aws_account_id:function:s3-lambda"
aws s3api put-bucket-notification-configuration \
  --region "$aws_region" \
  --bucket "$aws_bucket" \
  --notification-configuration '{
    "LambdaFunctionConfigurations": [{
        "LambdaFunctionArn": "'"$LambdaFunctionArn"'",
        "Events": ["s3:ObjectCreated:*"]
    }]
}'

aws s3api put-bucket-notification-configuration \
  --region "$aws_region" \
  --bucket "$aws_bucket" \
  --notification-configuration '{
    "LambdaFunctionConfigurations": [{
        "LambdaFunctionArn": "'"$LambdaFunctionArn"'",
        "Events": ["s3:ObjectCreated:*"]
    }]
}'

# create an sns topic and save the topic arn to a variable
topic_arn=$(aws sns create-topic --name s3-lambda-sns --output json | jq -r '.TopicArn')

# print the topic arn
echo "SNS Topic ARN: $topic_arn"

# Trigger SNS topic using lambda function

# Add sns topic using lambda function
aws sns subscribe \
  --topic-arn "$topic_arn" \
  --protocol email \
  --notification-endpoint "$email_address"

# publish sns
aws sns publish \
  --topic-arn "$topic_arn" \
  --subject "A new object created in s3 bucket" \
  --message "Hey, a new data object just got delievered into the s3 bucket $aws_bucket" 
