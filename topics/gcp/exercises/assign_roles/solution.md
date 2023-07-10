# Assign Roles

## Objectives

1. Assign the following roles to a member in your organization
   1. Compute Storage Admin
   2. Compute Network Admin
   3. Compute Security Admin
2. Verify roles were assigned

## Solution

### Console

1. Go to IAM & Admin
2. Click on IAM and then on the "Add" button
   1. Choose the member account to whom the roles will be added
   2. Under select role, search for the specified roles under "Objectives" and click on "Save"
2. The member should now be able to go to the compute engine API and see the resources there.

### Terraform

Click [here](main.tf) to view the Terraform main.tf file