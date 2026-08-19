# Appcircle

## Appcircle Questions

### Appcircle 101

<details>
<summary>What is Appcircle?</summary><br><b>

[Appcircle](https://appcircle.io/) is a mobile CI/CD platform for building, signing,
testing, distributing, and publishing iOS and Android applications.
</b></details>

<details>
<summary>What makes mobile CI/CD different from general-purpose CI/CD?</summary><br><b>

Mobile pipelines require platform-specific toolchains and runners, such as macOS and
Xcode for iOS, as well as platform-specific code signing. Delivery also extends past
deployment into tester distribution, store metadata, third-party review, and
store-specific release controls. A faulty release also cannot be rolled back the way a
server deployment can.
</b></details>

<details>
<summary>What is a clean build environment, and why does it matter?</summary><br><b>

Each build runs on a newly created, isolated machine that is destroyed once the build
finishes. Source code is fetched at build time rather than stored, and credentials are
pulled from a vault. This keeps builds consistent, since no leftover state can affect the
result, and prevents signing material and caches from being exposed to subsequent builds.
</b></details>

<details>
<summary>What are Signing Identities and why are they managed centrally?</summary><br><b>

[Signing Identities](https://docs.appcircle.io/signing-identities) are the credentials
used to digitally sign an application: certificates and provisioning profiles on iOS,
keystores on Android. They are long lived secrets, so they belong in a secure vault and
should be injected at build time rather than living on developer machines. Central
management also records credential activity in audit logs and reports, and notifies on
expiring certificates so they can be renewed before they break the pipeline.
</b></details>

<details>
<summary>What is the difference between Testing Distribution, Enterprise App Store and Publish to Stores?</summary><br><b>

They are three distribution paths, each with a different audience:

* [Testing Distribution](https://docs.appcircle.io/testing-distribution): internal
  testers, through testing groups that can install the pre-release build on their devices
* [Enterprise App Store](https://docs.appcircle.io/enterprise-app-store): in-house
  distribution to employees, through a private store the organization runs itself instead
  of a public one
* [Publish to Stores](https://docs.appcircle.io/publish-to-stores-module): external
  distribution through App Store Connect, Google Play Console, Huawei AppGallery and
  Microsoft Intune. The publish flow is defined as a sequence of steps, so it can be
  shaped around the organization's release process
</b></details>

### Appcircle Hands-On 101

<details>
<summary>How do you customize the build pipeline steps in Appcircle?</summary><br><b>

Through the [workflow](https://docs.appcircle.io/build/build-process-management/build-workflows),
which is the ordered set of steps a build runs. Steps can be reordered and configured
through their inputs. CI integrations can be added, or a custom script for extra
flexibility.
</b></details>

<details>
<summary>How can a build be started automatically?</summary><br><b>

Through triggers configured on the build profile: on every push, on a pull or merge
request, or only on tag pushes. Builds can also be scheduled to start at a set time,
without depending on repository activity.
</b></details>

<details>
<summary>Why would an organization choose to run mobile CI/CD on self-hosted infrastructure instead of the cloud?</summary><br><b>

Data sovereignty and control over the deployment. The pipeline runs entirely on the
organization's own infrastructure, and the platform can be configured to align with
existing enterprise systems, security protocols, authentication methods and network
policies.
</b></details>

<details>
<summary>How is store metadata handled in Appcircle?</summary><br><b>

App name, descriptions, screenshots and the other listing fields are edited per version
in the Publish to Stores module, separately for each locale, with the exact set of
fields depending on the target store. Updating the listing is a publish flow step, so it
can run in the same flow that submits the binary, and an approval step can be placed
before it so designated reviewers sign off on the listing first.
</b></details>
