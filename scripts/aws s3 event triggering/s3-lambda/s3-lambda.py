import boto3
import json

def lambda_handler(event, context):

  # i want to know that event thing
  print(event)

  # extract relevant information from the s3 event trigger
  bucket_name=event['Records'][0]['s3']['bucket']['name']
  object_key=event['Records'][0]['s3']['object']['key']

  # perform desired operations with the upload file
  print(f"File '{object_key}' was uploaded to bucket '{bucket_name}'")

  # example: send a notification via sns
  sns_client=boto3.client('sns')
  topic_arn='arn:aws:sns:us-east-1:<account-id>:s3-lambda-sns'
  sns_client.publish(
    TopicArn=topic_arn,
    Subject='s3 object created !!',
    Message=f"File '{object_key}' was uploaded to bucket '{bucket_name}"
  )

  # Example: Trigger another Lambda function
  # lambda_client = boto3.client('lambda')
  # target_function_name = 'my-another-lambda-function'
  # lambda_client.invoke(
  #    FunctionName=target_function_name,
  #    InvocationType='Event',
  #    Payload=json.dumps({'bucket_name': bucket_name, 'object_key': object_key})
  # )
  # in case of queuing and other objective similar to the netflix flow of triggering

  return {
    'statusCode': 200,
    'body': json.dumps("Lambda function executed successfully !!")
  }
