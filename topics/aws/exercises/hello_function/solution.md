## Hello Function - Solution

### Exercise

Create a basic AWS Lambda function that when given a name, will return "Hello <NAME>"

### Solution

#### Define a function

1. Go to Lambda console panel and click on `Create function`
  1. Give the function a name like `BasicFunction`
  2. Select `Python3` runtime
  3. Now to handle function's permissions, we can attach IAM role to our function either by setting a role or creating a new role. I selected "Create a new role from AWS policy templates"
  4. In "Policy Templates" select "Simple Microservice Permissions"

1. Next, you should see a text editor where you will insert a code similar to the following

#### Function's code
```
import json


def lambda_handler(event, context):
    firstName = event['name']
    return 'Hello ' + firstName
```
2. Click on "Create Function"

#### Define a test

1. Now let's test the function. Click on "Test".
2. Select "Create new test event"
3. Set the "Event name" to whatever you'd like. For example "TestEvent"
4. Provide keys to test

```
{
  "name": 'Spyro'
}
```
5. Click on "Create"

#### Test the function

1. Choose the test event you've create (`TestEvent`)
2. Click on the `Test` button
3. You should see something similar to `Execution result: succeeded`
4. If you'll go to AWS CloudWatch, you should see a related log stream 
