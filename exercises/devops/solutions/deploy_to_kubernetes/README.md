## Deploy to Kubernetes

Note: this exercise can be solved in various ways. The solution described here is just one possible way.

1. Install Jenkins on one system (follow up the standard Jenkins installation procedure)
2. Deploy Kubernetes on a remote host (minikube can be an easy way to achieve it)
3. Create a simple web app or [page](html)

4. Create Kubernetes [resoruces](helloworld.yml) - Deployment, Service and Ingress (for HTTPS access)
5. Create an [Ansible inventory](inventory) and insert the address of the Kubernetes cluster
6. Write [Ansible playbook](deploy.yml) to deploy the Kubernetes resources and also generate 
7. Create a [pipeline](Jenkinsfile)

8. Run the pipeline :)
9. Try to access the web app remotely
