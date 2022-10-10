## OpenShift - Projects 101

### Objectives

In a newly deployed cluster (preferably) perform the following:

1. Login to the OpenShift cluster
2. List all the projects
3. Create a new project called 'neverland'
4. Check the overview status of the current project

### Solution

```
oc login -u YOUR_USER -p YOUR_PASSWORD_OR_TOKEN
oc get projects # Empty output in new cluster
oc new-project neverland
oc status
```
