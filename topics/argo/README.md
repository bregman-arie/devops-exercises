# Argo

- [Argo](#argo)
  - [ArgoCD Exercises](#argocd-exercises)
  - [Argo Questions](#argo-questions)
    - [ArgoCD 101](#argocd-101)
    - [Practical ArgoCD 101](#practical-argocd-101)
    - [Multi-Cluster Environment](#multi-cluster-environment)
    - [Access Control](#access-control)

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

Simply said, ArgoCD is CD, not CI. We still need CI systems. Secondly, ArgoCD is running on Kubernetes, it's part of its ecosystem, as opposed to some other CI/CD systems. Finally, ArgoCD was built specifically for Kubernetes, not other platforms and systems.

Easier to explain the need for ArgoCD by direct comparison to another system that can do CD. Let's use Jenkins for this.

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

<details>
<summary>Ella, an engineer in your team, claims ArgoCD benefit is that it's an extension Kubernetes, it's part of the cluster. Sarah, also an engineer in your team, claims it's not a real benefit as Jenkins can be also deployed in the cluster hence being part of it. What's your take?</summary><br><b>

Ella is right, ArgoCD is an extension of the cluster, that is very different from simply being deployed in the cluster as other CI/CD systems like Jenkins. ArgoCD uses existing k8s resources like K8s controllers (for monitoring and state differences) and etcd for storing data.
</b></details>

<details>
<summary>How the main resource in ArgoCD called?</summary><br><b>

"Application"
</b></details>

### Practical ArgoCD 101

<details>
<summary>Describe the purpose of the following section in a an Application YAML file

```YAML
source:
  repoURL: https://github.com/bregman-arie/devops-exercises
  targetRevision: HEAD
  path: main
```
</summary><br><b>

This section of an Application in ArgoCD, defines which Git repository should be synced
</b></details>

<details>
<summary>Describe the purpose of the following section in a an Application YAML file

```YAML
destination:
  server: http://some.kubernetes.cluster.svc
  namespace: devopsExercises
```
</summary><br><b>

This section defines with which Kubernetes cluster the app in the tracked Git repository should be synced with.
</b></details>

<details>
<summary>What CRD would you use if you have multiple applications and you would like to group them together logically?</code></summary><br><b>

AddProject
</b></details>


### Multi-Cluster Environment

<details>
<summary>True or False? If you have multiple Kubernetes clusters you want to manage sync applications to with ArgoCD then, you must have ArgoCD installed on each one of them</summary><br><b>

False, it can be deployed on one of them. ArgoCD is able to manage external clusters on which it doesn't run.
</b></details>

<details>
<summary>You've three clusters - dev, staging and prod. Whenever you update the application GitOps repo, all three clusters are being updated. What's the problem with that and how to deal with it?</summary><br><b>

You don't usually want to go and update all of your clusters at once, especially when some for testing and development purposes and some for actual production usage.

There are multiple ways to deal with it:

1. Branch Drived: Have branches for your GitOps repo where you push first to development, do some testing, merge it then to staging and if everything works fine in staging, you merge it to production.

2. Use overlays and Kustomize to control the context of where your changes synced based on the CI process/pipeline used.
</b></details>

### Access Control

<details>
<summary>How ArgoCD makes access management in the cluster easier?</summary><br><b>

Instead of creating Kubernetes resources, you can use Git to manage who is allowed to push code, to review it, merge it, etc - either human users or 3rd party systems and services. There is no need to use ClusterRole or User resources in Kubernetes hence the management of access is much more simplified.

</b></details>
