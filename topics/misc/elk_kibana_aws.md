# Elasticsearch, Kibana and AWS

Your task is to build an elasticsearch cluster along with Kibana dashboard on one of the following clouds:

* AWS
* OpenStack
* Azure
* GCP

You have to describe in details (preferably with some drawings) how you are going to set it up.
Please describe in detail:

- How you scale it up or down
- How you quickly (less 20 minutes) provision the cluster
- How you apply security policy for access control
- How you transfer the logs from the app to ELK
- How you deal with multi apps running in different regions

# Solution

This one out of many possible solutions. This solution is relying heavily on AWS.

* Create a VPC with subnet so we can place Elasticsearch node(s) in internal environment only.
  If required, we will also setup NAT for public access. 

* Create an IAM role for the access to the cluster. Also, create a separate role for admin access.

* To provision the solution quickly, we will use the elasticsearch service directly from AWS for production deployment.
  This way we also cover multiple AZs. As for authentication, we either use Amazon cognito or the organization LDAP server.

* To transfer data, we will have to install logstash agent on the instances. The agent will be responsible
  for pushing the data to elasticsearch.

* For monitoring we will use:

    * Cloud watch to monitor cluster resource utilization
    * Cloud metrics dashboard

* If access required from multiple regions we will transfer all the data to S3 which will allow us to view the data
  from different regions and consolidate it in one dashboard
