# Argo

## ArgoCD Exercises

TODO

## Argo Questions

### ArgoCD 101

<details>
<summary>What is Argo CD?</summary><br><b>

[ArgoCD](https://argo-cd.readthedocs.io/en/stable): "Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes."

As to why Argo CD, they provide the following explanation: "Application definitions, configurations, and environments should be declarative and version controlled. Application deployment and lifecycle management should be automated, auditable, and easy to understand."

</b></details>

<details>
<summary>There been a lot of CI/CD systems before ArgoCD (Jenkins, Teamcity, CircleCI, etc.) What added value ArgoCD brought?</summary><br><b>

Simply said, ArgoCD is running on Kubernetes, it's part of its ecosystem, as opposed to some other CI/CD systems.

Easier to explain the need for ArgoCD by direct comparison to another CI/CD system. Let's use Jenkins for this.

With Jenkins, you need make sure to install k8s related tools and set access for commands like kubectl.
With ArgoCD you simply need to install it in your namespace but no need to install additional tools as it's part of k8s.

With Jenkins, managing access is usually done per pipeline and even if set globally in Jenkins, you still need to configure each pipeline to use that access configuration.
With ArgoCD access management to k8s and other resources is given as it runs already on the cluster, in one or multiple namespaces.

With Jenkins, tracking the status of what got deployed to k8s can be done only as an extra step, by running the pipeline. This is because Jenkins isn't part of the k8s cluster.
With ArgoCD you get much better tracking and visibility of what gets deployed as it runs in the same cluster and the same namespace.

With ArgoCD it's really easy to roll back to a previous version because all the changes done, are done to git which is a versioned source control. So it's enough to get to a previous commit for ArgoCD to detect a change and sync to the cluster. Worth to mention, this point specifically is true for Jenkins as well :)
</b></details>

<details>
<summary>Describe an example of workflow where ArgoCD is used</summary><br><b>

1. A developer submitted change to an application repository
2. Jenkins pipeline is triggered to run CI on the change
3. If the Jenkins Pipeline completed successfully, build an image out of the new code
4. Push to image to a registry
5. Update K8S manifest file(s) in a separate app config repository
6. ArgoCD tracks changes in the app config repository. Since there was a change in the repository, it will apply the changes from the repo
7. 
</b></details>

<details>
<summary>True or False? ArgoCD support Kubernetes YAML files but not other manifests formats like Helm Charts and Kustomize</summary><br><b>

False. It supports Kubernetes YAML files as well as Helm Charts and Kustomize.

</b></details>

<details>
<summary>What "GitOps Repository" means in regards to ArgoCD?</summary><br><b>

It's the repository that holds app configuration, the one updated most of the time by CI/CD processes or DevOps, SRE engineers. In regards to ArgoCD it's the repository ArgoCD tracks for changes and apply them when they are detected.

</b></details>

<details>
<summary>What are the advantages in using GitOps approach/repository?</summary><br><b>

* Your whole configuration is one place, defined as code so it's completely transparent, adjustable for changes and easily reproducible
* Everyone go through the same interface hence you have more people experiencing and testing the code, even if not intentionally
* Engineers can use it for testing, development, ... there is no more running manual commands and hoping to reach the same status as in the cluster/cloud.
* 
</b></details>

<details>
<summary>What are the advantages in using GitOps approach/repository?</summary><br><b>

* Your whole configuration is one place, defined as code so it's completely transparent, adjustable for changes and easily reproducible
* Everyone go through the same interface hence you have more people experiencing and testing the code, even if not intentionally
* Engineers can use it for testing, development, ... there is no more running manual commands and hoping to reach the same status as in the cluster/cloud.
* Single source of truth: you know that your GitOps is the repo from which changes can be done to the cluster. So even if someone tries to manually override it, it won't work.
</b></details>

<details>
<summary>Sorina, one of the engineers in your team, made manual changes to the cluster that override some of the configuration in a repo traced by ArgoCD. What will happen?</summary><br><b>

Once Sorina made the modifications, ArgoCD will detect the state diverged and will sync the changes from the GitOps repository, overwriting the manual changes done by Sorina.

</b></details>

<details>
<summary>Nate, one of the engineers in your organization, asked whether it's possible if ArgoCD didn't sync for changes done manually to the cluster. What would be your answer?</summary><br><b>

The answer is yes, it's possible. You can configure ArgoCD to sync to desired state when changes done manually and instead do something like sending alerts.

</b></details>

<details>
<summary>How cluster disaster recovery becomes easier with ArgoCD?</summary><br><b>

Imagine you have a cluster in the cloud, in one of the regions. Something happens to that cluster and it's either crashes or simply no longer opertional.

If you have all your cluster configuration in a GitOps repository, ArgoCD can be pointed to that repository while be configured to use a new cluster you've set up and apply that configuration so your cluster is again up and running with the same status as o
</b></details>


### Access Control

<details>
<summary>What is Argo CD?</code></summary><br><b>

[ArgoCD](https://argo-cd.readthedocs.io/en/stable): "Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes."

As to why Argo CD, they provide the following explanation: "Application definitions, configurations, and environments should be declarative and version controlled. Application deployment and lifecycle management should be automated, auditable, and easy to understand."

</b></details>
