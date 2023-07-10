## URL Function

Create a basic AWS Lambda function that will be triggered when you enter a URL in the browser

### Solution

#### Define a function

1. Go to Lambda console panel and click on `Create function`
  1. Give the function a name like `urlFunction`
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

#### Define a trigger

We'll define a trigger in order to trigger the function when inserting the URL in the browser

1. Go to "API Gateway console" and click on "New API Option"
2. Insert the API name, description and click on "Create"
3. Click on Action -> Create Resource
4. Insert resource name and path (e.g. the path can be /hello) and click on "Create Resource"
5. Select the resource we've created and click on "Create Method"
6. For "integration type" choose "Lambda Function" and insert the lambda function name we've given to the function we previously created. Make sure to also use the same region
7. Confirm settings and any required permissions
8. Now click again on the resource and modify "Body Mapping Templates" so the template includes this:

```
{ "name": "$input.params('name')" }
```
9. Finally save and click on Actions -> Deploy API

#### Running the function

1. In the API Gateway console, in stages menu, select the API we've created and click on the GET option
2. You'll see an invoke URL you can click on. You might have to modify it to include the input so it looks similar to this: `.../hello?name=mario`
3. You should see in your browser `Hello Mario`
