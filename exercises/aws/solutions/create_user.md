## IAM AWS - Create a User

### Objectives

As you probably know at this point, it's not recommended to work with the root account in AWS. For this reason you are going to create a new account which you'll use regularly as the admin account.

1. Create a user with password credentials
2. Add the newly created user to a group called "admin" and attach to it the policy called "Administrator Access"
3. Make sure the user has a tag called with the key `Role` and the value `DevOps`


### Solution

1. Go to the AWS IAM service
2. Click on "Users" in the right side menu (right under "Access Management")
3. Click on the button "Add users"
4. Insert the user name (e.g. mario)
5. Select the credential type: "Password"
6. Set console password to custom and click on "Next"
7. Click on "Add user to group"
8. Insert "admin" as group name
9. Check the "AdministratorAccess" policy and click on "Create group"
10. Click on "Next: Tags"
11. Add a tag with the key `Role` and the value `DevOps`
12. Click on "Review" and then create on "Create user"
