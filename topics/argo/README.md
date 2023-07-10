# Argo

<!-- {% raw %} -->

- [Argo](#argo)
  - [ArgoCD Exercises](#argocd-exercises)
    - [ArgoCD 101](#argocd-101)
    - [ArgoCD Secrets](#argocd-secrets)
    - [ArgoCD Helm](#argocd-helm)
    - [Argo Rollouts](#argo-rollouts)
  - [ArgoCD Questions](#argocd-questions)
    - [ArgoCD 101](#argocd-101-1)
    - [Practical ArgoCD 101](#practical-argocd-101)
      - [CLI](#cli)
    - [ArgoCD Configuration](#argocd-configuration)
    - [Advanced ArgoCD](#advanced-argocd)
    - [ArgoCD Application Health](#argocd-application-health)
    - [ArgoCD Syncs](#argocd-syncs)
    - [ArgoCD and Helm](#argocd-and-helm)
  - [Argo Rollouts Questions](#argo-rollouts-questions)
    - [Argo Rollouts 101](#argo-rollouts-101)
    - [Argo Advanced Rollouts](#argo-advanced-rollouts)
    - [Argo Rollouts Commands](#argo-rollouts-commands)

## ArgoCD Exercises

### ArgoCD 101

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Creating an App | App | [Exercise](exercises/app_creation/exercise.md) | [Solution](exercises/app_creation/solution.md)
| Syncing App - Git | Sync | [Exercise](exercises/sync_app_git/exercise.md) | [Solution](exercises/sync_app_git/solution.md)
| Syncing App - Cluster | Sync | [Exercise](exercises/sync_app_cluster/exercise.md) | [Solution](exercises/sync_app_cluster/solution.md)

### ArgoCD Secrets

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Secrets 101 | Secrets | [Exercise](exercises/secrets_101/exercise.md) | [Solution](exercises/secrets_101/solution.md)

### ArgoCD Helm

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Helm ArgoCD App | Secrets | [Exercise](exercises/argocd_helm_app/exercise.md) | [Solution](exercises/argocd_helm_app/solution.md)

### Argo Rollouts

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Blue/Green Rollout | Rollouts | [Exercise](exercises/blue_green_rollout/exercise.md) | [Solution](exercises/blue_green_rollout/solution.md)
| Canary Rollout | Rollouts | [Exercise](exercises/canary_rollout/exercise.md) | [Solution](exercises/canary_rollout/solution.md)

## ArgoCD Questions

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
</b></details>

<details>
<summary>True or False? ArgoCD supports Kubernetes YAML files but not other manifests formats like Helm Charts and Kustomize</summary><br><b>

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

<details>
<summary>Explain what is an "Application" in regards to ArgoCD</summary><br><b>

It's a custom resource definitions which responsible for the deployment and synchronization of application resources to a Kubernetes cluster.
</b></details>

<details>
<summary>How ArgoCD makes access management in the cluster easier?</summary><br><b>

Instead of creating Kubernetes resources, you can use Git to manage who is allowed to push code, to review it, merge it, etc - either human users or 3rd party systems and services. There is no need to use ClusterRole or User resources in Kubernetes hence the management of access is much more simplified.

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

<details>
<summary>True or False? ArgoCD sync period is 3 hours</summary><br><b>

False. ArgoCD sync period is 3 minutes as of today (and not hours).
</b></details>

<details>
<summary>Describe shortly what ArgoCD does every sync period</summary><br><b>

1. Gathers list of all the apps to sync (those that are marked with "auto-sync")
2. Gets Git state for each repository
3. Performs comparison between the repository Git state and the Kubernetes cluster state
  1. If states are different, the application marked as "out-of-sync" and further action might be taken (based on the configuration)
  2. If states are equal, the application marked as "synced"
</b></details>

<details>
<summary>You deployed a new application in a namespace called "yay" but when running <code>kubectl get ns yay</code> you see there is no such namespace. What happened?</summary><br><b>

Deploying applications in non-existing namespaces doesn't create the namespace. For that you have to explicitly mark "Auto-create namespace".

To fix it, you can simply run `kubectl create namespace NAMESPACE_NAME` but it's better of course to have it stored in Git rather than running kubectl commands.
</b></details>

#### CLI

<details>
<summary>Create a new application with the following properties:

* app name: some-app
* repo: https://fake.repo.address
* app path: ./app_path
* namespace: default
* cluster: my.kubernetes.cluster
</summary><br><b>

```
argocd app create some-app \
--project  \
--repo https://fake.repo.address \
--path ./app_path \
--dest-namespace default \
--dest-server my.kubernetes.cluster
```

</b></details>

<details>
<summary>List all argocd apps</summary><br><b>

`argocd app list`
</b></details>

<details>
<summary>Print detailed information on the app called "some-app"</summary><br><b>

`argocd app get some-app`
</b></details>

<details>
<summary>How to add an additional (external) cluster for ArgoCD to manage?</summary><br><b>

`argocd cluster add CLUSTER_ADDRESS/NAME`
</b></details>

<details>
<summary>How to list all the clusters ArgoCD manage?</summary><br><b>

`argocd cluster list`
</b></details>

### ArgoCD Configuration

<details>
<summary>Is it possible to change default sync period of ArgoCD?</summary><br><b>

Yes, it is possible by adding the following to the argocd-cm (ConfigMap):

```
data:
  timeout.reconciliation: 300s
```

The value can be any number of seconds you would like to set.
</b></details>

<details>
<summary>What will be the result of setting <code>timeout.reconciliation: 0s</code>?</summary><br><b>

sync functionality will be disabled.
</b></details>

### Advanced ArgoCD

<details>
<summary>What is the "App of Apps Patterns"?</summary><br><b>

A solution from Argo community in regards to managing multiple similar applications.

Basically a pattern where you have root application that consists of other child applications.

So instead of creating multiple separate applications, you have the root application pointing to a repository with additional applications.
</b></details>

<details>
<summary>Can you provide some use cases for using "App of Apps Patterns"?</summary><br><b>

* Cluster Preparation: You would like to deploy multiple applications at once to bootstrap a Kubernetes cluster

TODO: add more :)
</b></details>

<details>
<summary>True or False? If you have multiple Kubernetes clusters you want to manage sync applications to with ArgoCD then, you must have ArgoCD installed on each one of them</summary><br><b>

False, it can be deployed on one of them. ArgoCD is able to manage external clusters on which it doesn't run.
</b></details>

<details>
<summary>You've three clusters - dev, staging and prod. Whenever you update the application GitOps repo, all three clusters are being updated. What's the problem with that and how to deal with it?</summary><br><b>

You don't usually want to go and update all of your clusters at once, especially when some for testing and development purposes and some for actual production usage.

There are multiple ways to deal with it:

1. Branch driven: Have branches for your GitOps repo where you push first to development, do some testing, merge it then to staging and if everything works fine in staging, you merge it to production.

2. Use overlays and Kustomize to control the context of where your changes synced based on the CI process/pipeline used.
</b></details>

### ArgoCD Application Health

<details>
<summary>What are some possible health statuses for an ArgoCD application?</summary><br><b>

* Healthy
* Missing: resource doesn't exist in the cluser
* Suspended: resource is paused
* Progressing: resources isn't healthy but will become healthy or has the chance to become healthy
* Degraded: resource isn't healthy
* Unknown: it's not known what's the app health
</b></details>

<details>
<summary>True or False? A Deployment considered to be healthy if the Pods are running</summary><br><b>

Not exactly. A Deployment (as well as StatefulSet, ReplicaSet and DaemonSet) considered healthy  if the desired state equals to actual/current state (this includes the number of replicas).
</b></details>

<details>
<summary>True or False? An ingress is considered healthy if status.loadBalancer.ingress list includes at least one value</summary><br><b>

True.
</b></details>

<details>
<summary>What can you tell about the health of custom Kubernetes resources?</summary><br><b>

The health of custom Kubernetes resources is defined by writing Lua scripts.

You find such list of scripts here: https://github.com/argoproj/argo-cd/tree/master/resource_customizations
</b></details>

### ArgoCD Syncs

<details>
<summary>Explain manual syncs vs. automatic syncs</summary><br><b>

Automatic syncs means that once ArgoCD detected a change or a new version of your app in Git, it will apply the changes so the current/actual state can be equal to desired state.

With manual syncs, ArgoCD will identify there is a difference, but will do nothing to correct it.
</b></details>

<details>
<summary>Explain auto-pruning</summary><br><b>

If enabled, auto-pruning will remove resources when files or content is removed from a tracked Git repository.

If disabled, ArgoCD will not remove anything, even when content or files are removed.
</b></details>

<details>
<summary>Explain self-heal in regards to ArgoCD</summary><br><b>

Self-heal is the process of correcting the cluster state based on the desired state, when someone makes manual changes to the cluster.
</b></details>

### ArgoCD and Helm

<details>
<summary>What support is provided in ArgoCD for Helm?</summary><br><b>

ArgoCD is able to track packaged Helm chart in a sense where it will monitor for new versions.
</b></details>

<details>
<summary>True or False? When ArgoCD tracks Helm chart the chart is no longer an Helm application and it's a ArgoCD app</summary><br><b>

True. Trying to execute commands like `helm ls` will fail because helm metadata doesn't exist anymore and the application is tracked as ArgoCD app.
</b></details>

## Argo Rollouts Questions

### Argo Rollouts 101

<details>
<summary>What is Argo Rollouts?</summary><br><b>

A controller for Kubernetes to perform application deployments using different strategies like Blue/Green deployments, Canary deployments, etc.

In addition, it supports A/B tests, automatic rollbacks and integrated metric analysis.
</b></details>

<details>
<summary>What happens when you rollout a new version of your app with argo rollouts?</summary><br><b>

- Argo Rollouts creates a new replicaset (that is the new app version)
  - Old version is still alive
- ArgoCD marks the app as out-of-sync 
</b></details>

<details>
<summary>True or False? You need to install ArgoCD in order to use Argo Rollouts</summary><br><b>

False. Quite common misconception today but both cab be used independency even though they work nicely together.
</b></details>

### Argo Advanced Rollouts

<details>
<summary>Scott, an engineer in your team, executes manually some smoke tests and monitors rollouts every time a new version is deployed. This way, if there is an issue he detects, he performs a rollback. What better approach you might suggest him to take?</summary><br><b>

Shift towards fully automated rollbacks. Argo Rollouts supports multiple metric providers (Datadog, NewRelic, etc.) so you can use data and metrics for automating the rollbacks based on different conditions

</b></details>

<details>
<summary>Explain the concept of "Analysis" in regards to Argo Rollouts</summary><br><b>

Analysis is a resource deployed along a Rollout resources and defines the conditions and metrics threshols for performing a rollback

</b></details>

<details>
<summary>Explain the following configuration

```yaml
apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: success-rate
spec:
  args:
  - name: service-name
  metrics:
  - name: success-rate
    interval: 4m
    count: 3
    successCondition: result[0] >= 0.90
    provider:
      prometheus:
        address: http:/some-prometheus-instance:80
        query: sum(response_status{app="{{args.service-name}}",role="canary",status=~"2.*"})/sum(response_status{app="{{args.service-name}}",role="canary"}
```
</summary><br><b>

It's an Analysis resource that fetches response status from Prometheus (monitoring instance). If it's more than 0.90 the rollout will continue, if it's less than 0.90 a rollback will be performed meaning the canary deployment failed.

</b></details>

### Argo Rollouts Commands

<details>
<summary>How to list rollouts?</summary><br><b>

`kubectl argo rollouts list rollouts`
</b></details>

<details>
<summary>How to list the rollouts of a given application?</summary><br><b>

`kubectl argo rollouts get rollout SOME-APP`
</b></details>

<details>
<summary>How to check the status of a rollout?</summary><br><b>

`kubectl argo rollouts status SOME-APP`
</b></details>

<details>
<summary>How to rollout a new version (with new container tag)?</summary><br><b>

`kubectl argo rollouts set image SOME-APP web-app=some/registry/and/image:v2.0`
</b></details>

<details>
<summary>How to manually promote to new app version?</summary><br><b>

`kubectl argo rollouts promote SOME-APP`
</b></details>

<details>
<summary>How do you monitor a rollout?</summary><br><b>

`kubectl argo rollouts get rollout SOME-APP --watch`
</b></details>

<!-- {% endraw %} -->