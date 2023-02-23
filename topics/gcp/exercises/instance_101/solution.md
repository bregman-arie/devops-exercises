# Create an Instance

## Objectives

1. Create a VM instance with the following properties
   1. name: instance-1
   2. type: e2-micro
   3. labels:
      1. app: web
      2. env: dev
2. Using the CLI (gcloud) perform the following operations:
   1. Update "app" label to "db"
   2. Remove "env" label

## Solution

### Console

1. Go to Compute Engine -> VM instances
2. Click on "Create Instance"
   1. Insert the name "instance-1"
   2. Click on "Add label" and add the following labels:
      1. app: web
      2. env: dev
   3. Choose machine type: e2-micro
3. Click on "Create"
4. Selected the created instance and click on "show info panel"
   1. Click on "labels" tab and change the value of "app" label to "db"
   2. Remove the "env" label

### Shell

```
gcloud config set project <PROJECT_ID>
gcloud config set compute/region <REGION NAME>
gcloud config set compute/zone <ZONE NAME>

gcloud compute instances create instance-1 --labels app=web,env=dev --machine-type=e2-micro
gcloud compute instances update instance-1 --update-labels app=db
gcloud compute instances update instance-1 --remove-labels env
```

### Terraform

Click [here](main.tf) to view the main.tf file