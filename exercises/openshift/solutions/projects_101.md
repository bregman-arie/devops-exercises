## OpenShift - Projects 101

### Objectives

1. Login to the OpenShift cluster -> `oc login -u YOUR_USER -p YOUR_PASSWORD_OR_TOKEN`
2. List all the projects -> `oc get projects`(The output should be empty in a newly created cluster)
3. Create a new project called 'neverland' -> `oc new-project neverland`
4. Check the overview status of the current project -> `oc status`
