## AWS - Create a Role

### Objectives

Create a basic role to provide EC2 service with Full IAM access permissions.<br>
In the end, run from the CLI (or CloudShell) the command to verify the role was created.

### Solution

1. Go to AWS console -> IAM
2. Click in the left side menu on "Access Manamgement" -> Roles
3. Click on "Create role"
3. Choose "AWS service" as the type of trusted entity and then choose "EC2" as a use case. Click on "Next"
4. In permissions page, check "IAMFullAccess" and click on "Next" until you get to "Review" page
5. In the "Review" page, give the role a name (e.g. IAMFullAcessEC2), provide a short description and click on "Create role"
6. `aws iam list-roles` will list all the roles in the account, including the one we've just created.
