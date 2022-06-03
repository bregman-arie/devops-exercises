## AWS Databases - Aurora DB

### Objectives

1. Create an Aurora database with the following properties
  * Edition: MySQL
  * Instance type: db.t3.small
  * A reader node in a different AZ
  * Public access should be enabled
  * Port should be set to 3306
  * DB name: 'db'
  * Backup retention: 10 days

2. How many instances does your DB cluster has?

### Solution

#### Console

1. Go to RDS service
2. Click on "Databases" in the left side menu and click on the "Create database" button
3. Choose "standard create"
4. Choose "Aurora DB"
5. Choose "MySQL" edition and "Provisioned" as capacity type
6. Choose "single-master"
7. Specify Credentials (master username and password)
8. Choose DB instance type: Burstable classes, db.t3.small
9. Choose "Create an Aurora Replica or Reader node in a different AZ"
10. Choose a default VPC and subnet
11. Check "Yes" for public access
12. Database port should be 3306
13. For authentication, choose "Password and IAM database authentication"
14. Set initial database name as "db"
15. Increase backup retention period to 10 days
16. Click on "Create database" button

1. Two instances - one reader and one writer
