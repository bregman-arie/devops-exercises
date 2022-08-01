## AWS IAM - Password Policy & MFA

Note: DON'T perform this exercise unless you understand what you are doing and what is the outcome of applying these changes to your account

### Objectives

1. Create password policy with the following settings:
  1. At least minimum 8 characters
  2. At least one number
  3. Prevent password reuse

2. Then enable MFA for the account.

### Solution

Password Policy:

1. Go to IAM service in AWS
2. Click on "Account settings" under "Access management"
3. Click on "Change password policy"
  1. Check "Enforce minimum password length" and set it to 8 characters
  1. Check "Require at least one number"
  1. Check "Prevent password reuse"
4. Click on "Save changes"

MFA:

1. Click on the account name
2. Click on "My Security Credentials"
3. Expand "Multi-factor authentication (MFA)" and click on "Activate MFA"
4. Choose one of the devices
5. Follow the instructions to set it up and click on "Assign MFA"
