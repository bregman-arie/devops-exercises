## AWS Databases - MySQL DB

### Objectives

1. Create a MySQL database with the following properties
  * Instance type: db.t2.micro
  * gp2 storage
  * Storage Auto scaling should be enabled and threshold should be set to 500 GiB
  * Public access should be enabled
  * Port should be set to 3306
  * DB name: 'db'
  * Backup retention: 10 days

2. Create read replica for the database you've created

### Solution

#### Console

1. Go to RDS service
2. Click on "Databases" in the left side menu and click on the "Create database" button
3. Choose "standard create"
4. Choose "MySQL" and the recommended version
5. Choose "Production" template
6. Specify DB instance identifier
7. Specify Credentials (master username and password)
8. Choose DB instance type: Burstable classes, db.t2.micro
9. Choose "gp2" as storage
10. Enable storage autoscalling: maximum storage threshold of 500 GiB
11. Choose "Do not create a standby instance"
12. Choose a default VPC and subnet
12. Check "Yes" for public access
13. Choose "No preference" for AZ
14. Database port should be 3306
15. For authentication, choose "Password and IAM database authentication"
16. Set initial database name as "db"
17. Increase backup retention period to 10 days
18. Click on "Create database" button

1. Go to the database under "Databases" in the left side menu
2. Click on "Actions" -> Create read replica
3. Click on "Create read replica"
