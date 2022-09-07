### Set up a CDK Project - Solution

### Exercise

Initialize a CDK project and set up files required to build a CDK project.

### Solution

#### Initialize a CDK project

1. Install CDK on your machine by running `npm install -g aws-cdk`.
2. Create a new directory named `sample` for your project and run `cdk init app --language typescript` to initialize a CDK project. You can choose lanugage as csharp, fsharp, go, java, javascript, python or typescript.
3. You would see the following files created in your directory:
   1. `cdk.json`, `tsconfig.json`, `package.json`  - These are configuration files that are used to define some global settings for your CDK project.
   2. `bin/sample.ts` - This is the entry point for your CDK project. This file is used to define the stack that you want to create.
   3. `lib/sample-stack.ts` - This is the main file that will contain the code for your CDK project.

#### Create a Sample lambda function

1. In `lib/sample-stack.ts` file, add the following code to create a lambda function:

```typescript
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import { Construct } from 'constructs';

export class SampleStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const hello = new lambda.Function(this, 'SampleLambda', {
      runtime: lambda.Runtime.NODEJS_14_X,
      code: lambda.Code.fromInline('exports.handler = async () => "hello world";'),
      handler: 'index.handler'
    });
  }
}

```

This will create a sample lambda function that returns "hello world" when invoked.

#### Bootstrap the CDK project

Before you deploy your project. You need to bootstrap your project. This will create a CloudFormation stack that will be used to deploy your project. You can bootstrap your project by running `cdk bootstrap`.

Learn more about bootstrapping [here](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html).

##### Deploy the Project

1. Run `npm install` to install all the dependencies for your project whenever you make changes.
2. Run `cdk synth` to synthesize the CloudFormation template for your project. You will see a new file called `cdk.out/CDKToolkit.template.json` that contains the CloudFormation template for your project.
3. Run `cdk diff` to see the changes that will be made to your AWS account. You will see a new stack called `SampleStack` that will create a lambda function and all the changes associated with it.
4. Run `cdk deploy` to deploy your project. You should see a new stack called created in your AWS account under CloudFormation.
5. Go to Lambda console and you will see a new lambda function called `SampleLambda` created in your account.

