## Containers

### Containers Exercises

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
|Running Containers|Intro|[Exercise](running_containers.md)|[Solution](solutions/running_containers.md)
|Working with Images|Image|[Exercise](working_with_images.md)|[Solution](solutions/working_with_images.md)
|My First Dockerfile|Dockerfile|[Exercise](write_dockerfile_run_container.md)|
|Run, Forest, Run!|Restart Policies|[Exercise](run_forest_run.md)|[Solution](solutions/run_forest_run.md)
|Layer by Layer|Image Layers|[Exercise](image_layers.md)|[Solution](solutions/image_layers.md)
|Containerize an application | Containerization |[Exercise](containerize_app.md)|[Solution](solutions/containerize_app.md)
|Multi-Stage Builds|Multi-Stage Builds|[Exercise](multi_stage_builds.md)|[Solution](solutions/multi_stage_builds.md)

### Containers Self Assesment

<details>
<summary>What is a Container?</summary><br><b>

This can be tricky to answer since there are many ways to create a containers:

  - Docker
  - systemd-nspawn
  - LXC

If to focus on OCI (Open Container Initiative) based containers, it offers the following [definition](https://github.com/opencontainers/runtime-spec/blob/master/glossary.md#container): "An environment for executing processes with configurable isolation and resource limitations. For example, namespaces, resource limits, and mounts are all part of the container environment."
</b></details>

<details>
<summary>Why containers are needed? What is their goal?</summary><br><b>

OCI provides a good [explanation](https://github.com/opencontainers/runtime-spec/blob/master/principles.md#the-5-principles-of-standard-containers): "Define a unit of software delivery called a Standard Container. The goal of a Standard Container is to encapsulate a software component and all its dependencies in a format that is self-describing and portable, so that any compliant runtime can run it without extra dependencies, regardless of the underlying machine and the contents of the container."
</b></details>

<details>
<summary>How are containers different from virtual machines (VMs)?</summary><br><b>

The primary difference between containers and VMs is that containers allow you to virtualize
multiple workloads on a single operating system while in the case of VMs, the hardware is being virtualized to run multiple machines each with its own guest OS.
You can also think about it as containers are for OS-level virtualization while VMs are for hardware virtualization.

* Containers don't require an entire guest operating system as VMs. Containers share the system's kernel as opposed to VMs. They isolate themselves via the use of kernel's features such as namespaces and cgroups
* It usually takes a few seconds to set up a container as opposed to VMs which can take minutes or at least more time than containers as there is an entire OS to boot and initialize as opposed to containers which has share of the underlying OS
* Virtual machines considered to be more secured than containers
* VMs portability considered to be limited when compared to containers
</b></details>

<details>
<summary>Do we need virtual machines in the edge of containers? Are they still relevant?</summary><br><b>
</b></details>

<details>
<summary>In which scenarios would you use containers and in which you would prefer to use VMs?</summary><br><b>

You should choose VMs when:
  * You need run an application which requires all the resources and functionalities of an OS
  * You need full isolation and security

You should choose containers when:
  * You need a lightweight solution
  * Running multiple versions or instances of a single application
</b></details>

<details>
<summary>Describe the process of containerizing an application</summary><br><b>

1. Write a Dockerfile that includes your app (including the commands to run it) and its dependencies
2. Build the image using the Dockefile you wrote
3. You might want to push the image to a registry
4. Run the container using the image you've built
</b></details>

#### Containers - OCI

<details>
<summary>What is the OCI?</summary><br><b>

OCI (Open Container Initiative) is an open governance established in 2015 to standardize container creation - mostly image format and runtime. At that time there were a number of parties involved and the most prominent one was Docker.

Specifications published by OCI:

  - [image-spec](https://github.com/opencontainers/image-spec)
  - [runtime-spec](https://github.com/opencontainers/runtime-spec)
</b></details>

<details>
<summary>Which operations OCI based containers must support?</summary><br><b>

Create, Kill, Delete, Start and Query State.
</b></details>

#### Containers - Basic Commands

<details>
<summary>How to list all the containers on a given host?</summary><br><b>

In the case of Docker, use: `docker container ls`<br>
In the case of Podman, it's not very different: `podman container ls`
</b></details>

<details>
<summary>How to run a container?</summary><br><b>

Docker: `docker container run ubuntu`<br>
Podman: `podman container run ubuntu`
</b></details>

<details>
<summary>Why after running <code>podman container run ubuntu</code> the output of <code>podman container ls</code> is empty?</summary><br><b>

Because the container immediately exits after running the ubuntu image. This is completely normal and expected as containers designed to run a service or a app and exit when they are done running it.<br>

If you want the container to keep running, you can run a command like `sleep 100` which will run for 100 seconds or you can attach to terminal of the container with a command similar: `podman container run -it ubuntu /bin/bash`
</b></details>

<details>
<summary>How to attach your shell to a terminal of a running container?</summary><br><b>

`podman container exec -it [container id/name] bash`

This can be done in advance while running the container: `podman container run -it [image:tag] /bin/bash`
</b></details>

<details>
<summary>True or False? You can remove a running container if it doesn't running anything</summary><br><b>

False. You have to stop the container before removing it.
</b></details>

<details>
<summary>How to stop and remove a container?</summary><br><b>

`podman container stop <container id/name> && podman container rm <container id/name>`
</b></details>

<details>
<summary>What happens when you run <code>docker container run ubuntu</code>?</summary><br><b>

1. Docker client posts the command to the API server running as part of the Docker daemon
2. Docker daemon checks if a local image exists
  1. If it exists, it will use it
  2. If doesn't exists, it will go to the remote registry (Docker Hub by default) and pull the image locally
3. containerd and runc are instructed (by the daemon) to create and start the container
</b></details>

<details>
<summary>How to run a container in the background?</summary><br><b>

With the -d flag. It will run in the background and will not attach it to the terminal.

`docker container run -d httpd` or `podman container run -d httpd`
</b></details>

#### Containers - Images

<details>
<summary>What is a container image?</summary><br><b>

* An image of a container contains the application, its dependencies and the operating system where the application is executed.<br>
* It's a collection of read-only layers. These layers are loosely coupled
  * Each layer is assembled out of one or more files
</b></details>

<details>
<summary>Why container images are relatively small?</summary><br><b>

* Most of the images don't contain Kernel. They share and access the one used by the host on which they are running
* Containers intended to run specific application in most cases. This means they hold only what the application needs in order to run
</b></details>

<details>
<summary>How to list the container images on certain host?</summary><br><b>

`podman image ls`<br>
`docker image ls`

Depends on which containers engine you use.
</b></details>

<details>
<summary>How the centralized location, where images are stored, is called?</summary><br><b>

Registry
</b></details>

<details>
<summary>A registry contains one or more <code>____</code> which in turn contain one or more <code>____</code></summary><br><b>

A registry contains one or more repositories which in turn contain one or more images.
</b></details>

<details>
<summary>How to find out which registry do you use by default from your environment?</summary><br><b>

Depends on the containers technology you are using. For example, in case of Docker, it can be done with `docker info`

```
> docker info
Registry: https://index.docker.io/v1
```
</b></details>

<details>
<summary>How to retrieve the latest ubuntu image?</summary><br><b>

`docker image pull ubuntu:latest`
</b></details>

<details>
<summary>True or False? It's not possible to remove an image if a certain container is using it</summary><br><b>

True. You should stop and remove the container before trying to remove the image it uses.
</b></details>

<details>
<summary>True or False? If a tag isn't specified when pulling an image, the 'latest' tag is being used</summary><br><b>

True
</b></details>

<details>
<summary>True or False? Using the 'latest' tag when pulling an image means, you are pulling the most recently published image</summary><br><b>

False. While this might be true in some cases, it's not guaranteed that you'll pull the latest published image when using the 'latest' tag.<br>
For example, in some images, 'edge' tag is used for the most recently published images.
</b></details>

<details>
<summary>Where pulled images are stored?</summary><br><b>

Depends on the container technology being used. For example, in case of Docker, images are stored in `/var/lib/docker/`
</b></details>

<details>
<summary>Explain container image layers</summary><br><b>

  - The layers of an image is where all the content is stored - code, files, etc.
  - Each layer is independent
  - Each layer has an ID that is an hash based on its content
  - The layers (as the image) are immutable which means a change to one of the layers can be easily identified
</b></details>

<details>
<summary>True or False? Changing the content of any of the image layers will cause the hash content of the image to change</summary><br><b>

True. These hashes are content based and since images (and their layers) are immutable, any change will cause the hashes to change.
</b></details>

<details>
<summary>How to list the layers of an image?</summary><br><b>

In case of Docker, you can use `docker image inspect <name>`
</b></details>

<details>
<summary>True or False? In most cases, container images contain their own kernel</summary><br><b>

False. They share and access the one used by the host on which they are running.
</b></details>

<details>
<summary>True or False? A single container image can have multiple tags</summary><br><b>

True. When listing images, you might be able to see two images with the same ID but different tags.
</b></details>

<details>
<summary>What is a dangling image?</summary><br><b>

It's an image without tags attached to it.
One way to reach this situation is by building an image with exact same name and tag as another already existing image. It can be still referenced by using its full SHA.
</b></details>

<details>
<summary>How to see changes done to a given image over time?</summary><br><b>

In the case of Docker, you could use `docker history <name>`
</b></details>

<details>
<summary>True or False? Multiple images can share layers</summary><br><b>

True.<br>
One evidence for that can be found in pulling images. Sometimes when you pull an image, you'll see a line similar to the following:<br>
`fa20momervif17: already exists`

This is because it recognizes such layer already exists on the host, so there is no need to pull the same layer twice.
</b></details>

<details>
<summary>What is the digest of an image? What problem does it solves?</summary><br><b>

Tags are mutable. This is mean that we can have two different images with the same name and the same tag. It can be very confusing to see two images with the same name and the same tag in your environment. How would you know if they are truly the same or are they different?<br>

This is where "digests` come handy. A digest is a content-addressable identifier. It isn't mutable as tags. Its value is predictable and this is how you can tell if two images are the same content wise and not merely by looking at the name and the tag of the images.
</b></details>

<details>
<summary>True or False? A single image can support multiple architectures (Linux x64, Windows x64, ...)</summary><br><b>

True.
</b></details>

<details>
<summary>What is a distribution hash in regards to layers?</summary><br><b>

  - Layers are compressed when pushed or pulled
  - distribution hash is the hash of the compressed layer
  - the distribution hash used when pulling or pushing images for verification (making sure no one tempered with image or layers)
  - It's also used for avoiding ID collisions (a case where two images have exactly the same generated ID)
</b></details>

<details>
<summary>How multi-architecture images work? Explain by describing what happens when an image is pulled</summary><br><b>

1. A client makes a call to the registry to use a specific image (using an image name and optionally a tag)
2. A manifest list is parsed (assuming it exists) to check if the architecture of the client is supported and available as a manifest
3. If it is supported (a manifest for the architecture is available) the relevant manifest is parsed to obtain the IDs of the layers
4. Each layer is then pulled using the obtained IDs from the previous step
</b></details>

<details>
<summary>How to check which architectures a certain container image supports?</summary><br><b>

`docker manifest inspect <name>`
</b></details>

<details>
<summary>How to check what a certain container image will execute once we'll run a container based on that image?</summary><br><b>

Look for "Cmd" or "Entrypoint" fields in the output of `docker image inspec <image name>`
</b></details>

<details>
<summary>How to view the instructions that were used to build image?</summary><br><b>

`docker image history <image name>:<tag>`
</b></details>

<details>
<summary>How <code>docker image build</code> works?</summary><br><b>

1. Docker spins up a temporary container
2. Runs a single instruction in the temporary container
3. Stores the result as a new image layer
4. Remove the temporary container
5. Repeat for every instruction
</b></details>

<details>
<summary>What is the role of cache in image builds?</summary><br><b>

When you build an image for the first time, the different layers are being cached. So, while the first build of the image might take time, any other build of the same image (given that Dockerfile didn't change or the content used by the instructions) will be instant thanks to the caching mechanism used.

In little bit more details, it works this way:
1. The first instruction (FROM) will check if base image already exists on the host before pulling it 
2. For the next instruction, it will check in the build cache if an existing layer was built from the same base image + if it used the same instruction
  1. If it finds such layer, it skips the instruction and links the existing layer and it keeps using the cache.
  2. If it doesn't find a matching layer, it builds the layer and the cache is invalidated.

Note: in some cases (like COPY and ADD instructions) the instruction might stay the same but if the content of what being copied is changed then the cache is invalidated. The way this check is done is by comparing the checksum of each file that is being copied.
</b></details>

<details>
<summary>What ways are there to reduce container images size?</summary><br><b>

  * Reduce number of instructions - in some case you may be able to join layers by installing multiple packages with one instructions for example or using `&&` to concatenate RUN instructions
  * Using smaller images - in some cases you might be using images that contain more than what is needed for your application to run. It is good to get overview of some images and see whether you can use smaller images that you are usually using.
  * Cleanup after running commands - some commands, like packages installation, create some metadata or cache that you might not need for running the application. It's important to clean up after such commands to reduce the image size
  * For Docker images, you can use multi-stage builds
</b></details>

<details>
<summary>What are the pros and cons of squashing images?</summary><br><b>

Pros:
  * Smaller image
  * Reducing number of layers (especially if the image has lot of layers)
Cons:
  * No sharing of the image layers
  * Push and pull can take more time (because no matching layers found on target)
</b></details>

#### Containers - Volume

<details>
<summary>How to create a new volume?</summary><br><b>

`docker volume create some_volume`
</b></details>

#### Containers - Dockerfile

<details>
<summary>What is a Dockerfile?</summary><br><b>

Different container engines (e.g. Docker, Podman) can build images automatically by reading the instructions from a Dockerfile. A Dockerfile is a text file that contains all the instructions for building an image which containers can use.
</b></details>

<details>
<summary>What is the instruction in all Dockefiles and what does it mean?</summary><br><b>

The first instruction is `FROM <image name>`<br>
It specifies the base layer of the image to be used. Every other instruction is a layer on top of that base image.
</b></details>

<details>
<summary>List five different instructions that are available for use in a Dockerfile</summary><br><b>

  * WORKDIR: sets the working directory inside the image filesystems for all the instructions following it
  * EXPOSE: exposes the specified port (it doesn't adds a new layer, rather documented as image metadata)
  * ENTRYPOINT: specifies the startup commands to run when a container is started from the image
  * ENV: sets an environment variable to the given value
  * USER: sets the user (and optionally the user group) to use while running the image
</b></details>

<details>
<summary>What are some of the best practices regarding container images and Dockerfiles that you are following?</summary><br><b>

  * Include only the packages you are going to use. Nothing else.
  * Specify a tag in FROM instruction. Not using a tag means you'll always pull the latest, which changes over time and might result in unexpected result.
  * Do not use environment variables to share secrets
  * Use images from official repositories
  * Keep images small! - you want them only to include what is required for the application to run successfully. Nothing else.
  * If are using the apt package manager, you might use 'no-install-recommends' with `apt-get install` to install only main dependencies (instead of suggested, recommended packages)
</b></details>

<details>
<summary>What is the "build context"?</summary><br><b>

[Docker docs](https://docs.docker.com/engine/reference/commandline/build): "A build’s context is the set of files located in the specified PATH or URL"
</b></details>

<details>
<summary>What is the difference between ADD and COPY in Dockerfile?</summary><br><b>

COPY takes in a source and destination. It lets you copy in a file or directory from the build context into the Docker image itself.<br>
ADD lets you do the same, but it also supports two other sources. You can use a URL instead of a file or directory from the build context. In addition, you can extract a tar file from the source directly into the destination.

Although ADD and COPY are functionally similar, generally speaking, COPY is preferred. That’s because it’s more transparent than ADD. COPY only supports the basic copying of files from build context into the container, while ADD has some features (like local-only tar extraction and remote URL support) that are not immediately obvious.
</b></details>

<details>
<summary>What is the difference between CMD and RUN in Dockerfile?</summary><br><b>

RUN lets you execute commands inside of your Docker image. These commands get executed once at build time and get written into your Docker image as a new layer.
CMD is the command the container executes by default when you launch the built image. A Dockerfile can only have one CMD.
You could say that CMD is a Docker run-time operation, meaning it’s not something that gets executed at build time. It happens when you run an image. A running image is called a container.
</b></details>

<details>
<summary>How to create a new image using a Dockerfile?</summary><br><b>

The following command is executed from within the directory where Dockefile resides:

`docker image build -t some_app:latest .`
`podman image build -t some_app:latest .`
</b></details>

<details>
<summary>Do you perform any checks or testing on your Dockerfiles?</summary><br><b>

One option is to use [hadolint](https://github.com/hadolint/hadolint) project which is a linter based on Dockerfile best practices.
</b></details>

<details>
<summary>Which instructions in Dockerfile create new layers?</summary><br><b>

Instructions such as FROM, COPY and RUN, create new image layers instead of just adding metadata.
</b></details>

<details>
<summary>Which instructions in Dockerfile create image metadata and don't create new layers?</summary><br><b>

Instructions such as ENTRYPOINT, ENV, EXPOSE, create image metadata and they don't create new layers.
</b></details>

<details>
<summary>Is it possible to identify which instruction create a new layer from the output of <code>docker image history</code>?</summary><br><b>
</b></details>

#### Containers - Architecture

<details>
<summary>How container achieve isolation from the rest of the system?</summary><br><b>

Through the use of namespaces and cgroups. Linux kernel has several types of namespaces:

  - Process ID namespaces: these namespaces include independent set of process IDs
  - Mount namespaces: Isolation and control of mountpoints
  - Network namespaces: Isolates system networking resources such as routing table, interfaces, ARP table, etc.
  - UTS namespaces: Isolate host and domains
  - IPC namespaces: Isolates interprocess communications
  - User namespaces: Isolate user and group IDs
  - Time namespaces: Isolates time machine
</b></details>

<details>
<summary>Describe in detail what happens when you run `podman/docker run hello-world`?</summary><br><b>

Docker/Podman CLI passes your request to Docker daemon.
Docker/Podman daemon downloads the image from Docker Hub
Docker/Podman daemon creates a new container by using the image it downloaded
Docker/Podman daemon redirects output from container to Docker CLI which redirects it to the standard output
</b></details>

<details>
<summary>Describe difference between cgroups and namespaces </summary><br><b>
cgroup: Control Groups provide a mechanism for aggregating/partitioning sets of tasks, and all their future children, into hierarchical groups with specialized behaviour.
namespace: wraps a global system resource in an abstraction that makes it appear to the processes within the namespace that they have their own isolated instance of the global resource.

In short:

Cgroups = limits how much you can use;
namespaces = limits what you can see (and therefore use)

Cgroups involve resource metering and limiting:
memory
CPU
block I/O
network

Namespaces provide processes with their own view of the system

Multiple namespaces: pid,net, mnt, uts, ipc, user

</b></details>

#### Containers - Docker Architecture

<details>
<summary>Which components/layers compose the Docker technology?</summary><br><b>

1. Runtime - responsible for starting and stopping containers
2. Daemon - implements the Docker API and takes care of managing images (including builds), authentication, security, networking, etc.
3. Orchestrator
</b></details>

<details>
<summary>What components are part of the Docker engine?</summary><br><b>

  - Docker daemon
  - containerd
  - runc
</b></details>

<details>
<summary>What is the low-level runtime?</summary><br><b>

  - The low level runtime is called runc
  - It manages every container running on Docker host
  - Its purpose is to interact with the underlying OS to start and stop containers
  - Its reference implementation is of the OCI (Open Containers Initiative) container-runtime-spec
  - It's a small CLI wrapper for libcontainer
</b></details>

<details>
<summary>What is the high-level runtime?</summary><br><b>

  - The high level runtime is called containerd
  - It was developed by Docker Inc and at some point donated to CNCF
  - It manages the whole lifecycle of a container - start, stop, remove and pause
  - It take care of setting up network interfaces, volume, pushing and pulling images, ...
  - It manages the lower level runtime (runc) instances
  - It's used both by Docker and Kubernetes as a container runtime
  - It sits between Docker daemon and runc at the OCI layer

Note: running `ps -ef | grep -i containerd` on a system with Docker installed and running, you should see a process of containerd
</b></details>

<details>
<summary>True or False? The docker daemon (dockerd) performs lower-level tasks compared to containerd</summary><br><b>

False. The Docker daemon performs higher-level tasks compared to containerd.<br>
It's responsible for managing networks, volumes, images, ...
</b></details>

<details>
<summary>Describe in detail what happens when you run `docker pull image:tag`?</summary><br><b>
Docker CLI passes your request to Docker daemon. Dockerd Logs shows the process

docker.io/library/busybox:latest resolved to a manifestList object with 9 entries; looking for a unknown/amd64 match

found match for linux/amd64 with media type application/vnd.docker.distribution.manifest.v2+json, digest sha256:400ee2ed939df769d4681023810d2e4fb9479b8401d97003c710d0e20f7c49c6

pulling blob \"sha256:61c5ed1cbdf8e801f3b73d906c61261ad916b2532d6756e7c4fbcacb975299fb Downloaded 61c5ed1cbdf8 to tempfile /var/lib/docker/tmp/GetImageBlob909736690

Applying tar in /var/lib/docker/overlay2/507df36fe373108f19df4b22a07d10de7800f33c9613acb139827ba2645444f7/diff" storage-driver=overlay2

Applied tar sha256:514c3a3e64d4ebf15f482c9e8909d130bcd53bcc452f0225b0a04744de7b8c43 to 507df36fe373108f19df4b22a07d10de7800f33c9613acb139827ba2645444f7, size: 1223534
</b></details>

<details>
<summary>Describe in detail what happens when you run a container</summary><br><b>

1. The Docker client converts the run command into an API payload
2. It then POST the payload to the API endpoint exposed by the Docker daemon
3. When the daemon receives the command to create a new container, it makes a call to containerd via gRPC
4. containerd converts the required image into an OCI bundle and tells runc to use that bundle for creating the container
5. runc interfaces with the OS kernel to pull together the different constructs (namespace, cgroups, etc.) used for creating the container
6. Container process is started as a child-process of runc
7. Once it starts, runc exists
</b></details>

<details>
<summary>True or False? Killing the Docker daemon will kill all the running containers</summary><br><b>

False. While this was true at some point, today the container runtime isn't part of the daemon (it's part of containerd and runc) so stopping or killing the daemon will not affect running containers.
</b></details>

<details>
<summary>True or False? containerd forks a new instance runc for every container it creates</summary><br><b>

True
</b></details>

<details>
<summary>True or False? Running a dozen of containers will result in having a dozen of runc processes</summary><br><b>

False. Once a container is created, the parent runc process exists.
</b></details>

<details>
<summary>What is shim in regards to Docker?</summary><br><b>

shim is the process that becomes the container's parent when runc process exists. It's responsible for:

  - Reporting exit code back to the Docker daemon
  - Making sure the container doesn't terminate if the daemon is being restarted. It does so by keeping the stdout and stdin open
</b></details>

<details>
<summary>What `podman commit` does?. When will you use it?</summary><br><b>

Create a new image from a container’s changes
</b></details>

<details>
<summary>How would you transfer data from one container into another?</summary><br><b>
</b></details>

<details>
<summary>What happens to data of the container when a container exists?</summary><br><b>
</b></details>

<details>
<summary>Explain what each of the following commands do:

  * docker run
  * docker rm
  * docker ps
  * docker pull
  * docker build
  * docker commit
</summary><br><b>
</b></details>

<details>
<summary>How do you remove old, non running, containers?</summary><br><b>

1. To remove one or more Docker images use the docker container rm command followed by the ID of the containers you want to remove.
2. The docker system prune command will remove all stopped containers, all dangling images, and all unused networks
3. docker rm $(docker ps -a -q) - This command will delete all stopped containers. The command docker ps -a -q will return all existing container IDs and pass them to the rm command which will delete them. Any running containers will not be deleted.
</b></details>

<details>
<summary>How the Docker client communicates with the daemon?</summary><br><b>

Via the local socket at `/var/run/docker.sock`
</b></details>

<details>
<summary>Explain Docker interlock</summary><br><b>
</b></details>

<details>
<summary>What is Docker Repository?</summary><br><b>
</b></details>

<details>
<summary>Explain image layers</summary><br><b>

A Docker image is built up from a series of layers. Each layer represents an instruction in the image’s Dockerfile. Each layer except the very last one is read-only.
Each layer is only a set of differences from the layer before it. The layers are stacked on top of each other. When you create a new container, you add a new writable layer on top of the underlying layers. This layer is often called the “container layer”. All changes made to the running container, such as writing new files, modifying existing files, and deleting files, are written to this thin writable container layer.
The major difference between a container and an image is the top writable layer. All writes to the container that add new or modify existing data are stored in this writable layer. When the container is deleted, the writable layer is also deleted. The underlying image remains unchanged.
Because each container has its own writable container layer, and all changes are stored in this container layer, multiple containers can share access to the same underlying image and yet have their own data state.
</b></details>

<details>
<summary>What best practices are you familiar related to working with containers?</summary><br><b>
</b></details>

<details>
<summary>How do you manage persistent storage in Docker?</summary><br><b>
</b></details>

<details>
<summary>How can you connect from the inside of your container to the localhost of your host, where the container runs?</summary><br><b>
</b></details>

<details>
<summary>How do you copy files from Docker container to the host and vice versa?</summary><br><b>
</b></details>

#### Containers - Docker Compose

<details>
<summary>Explain what is Docker compose and what is it used for</summary><br><b>

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

For example, you can use it to set up ELK stack where the services are: elasticsearch, logstash and kibana. Each running in its own container.<br>
In general, it's useful for running applications which composed out of several different services. It let's you manage it as one deployed app, instead of different multiple separate services.
</b></details>

<details>
<summary>Describe the process of using Docker Compose</summary><br><br>

* Define the services you would like to run together in a docker-compose.yml file
* Run `docker-compose up` to run the services
</b></details>

#### Containers - Docker Images

<details>
<summary>What is Docker Hub?</summary><br><b>

One of the most common registries for retrieving images.
</b></details>

<details>
<summary>How to push an image to Docker Hub?</summary><br><b>

`docker image push [username]/[image name]:[tag]`

For example:

`docker image mario/web_app:latest`
</b></details>

<details>
<summary>What is the difference between Docker Hub and Docker cloud?</summary><br><b>

Docker Hub is a native Docker registry service which allows you to run pull
and push commands to install and deploy Docker images from the Docker Hub.

Docker Cloud is built on top of the Docker Hub so Docker Cloud provides
you with more options/features compared to Docker Hub. One example is
Swarm management which means you can create new swarms in Docker Cloud.
</b></details>

<details>
<summary>Explain Multi-stage builds</summary><br><b>

Multi-stages builds allow you to produce smaller container images by splitting the build process into multiple stages.

As an example, imagine you have one Dockerfile where you first build the application and then run it. The whole build process of the application might be using packages and libraries you don't really need for running the application later. Moreover, the build process might produce different artifacts which not all are needed for running the application.

How do you deal with that? Sure, one option is to add more instructions to remove all the unnecessary stuff but, there are a couple of issues with this approach:
1. You need to know what to remove exactly and that might be not as straightforward as you think
2. You add new layers which are not really needed

A better solution might be to use multi-stage builds where one stage (the build process) is passing the relevant artifacts/outputs to the stage that runs the application.
</b></details>

<details>
<summary>True or False? In multi-stage builds, artifacts can be copied between stages</summary><br><b>

True. This allows us to eventually produce smaller images.
</b></details>

<details>
<summary>What <code>.dockerignore</code> is used for?</summary><br><b>

By default, Docker uses everything (all the files and directories) in the directory you use as build context.<br>
`.dockerignore` used for excluding files and directories from the build context
</b></details>

#### Containers - Networking

<details>
<summary>What container network standards or architectures are you familiar with?</summary><br><b>

CNM (Container Network Model):
  * Requires distrubited key value store (like etcd for example) for storing the network configuration
  * Used by Docker
CNI (Container Network Interface):
  * Network configuration should be in JSON format
</b></details>

#### Containers - Docker Networking

<details>
<summary>What network specification Docker is using and how its implementation is called?</summary><br><b>

Docker is using the CNM (Container Network Model) design specification.<br>
The implementation of CNM specification by Docker is called "libnetwork". It's written in Go.
</b></details>

<details>
<summary>Explain the following blocks in regards to CNM:

  * Networks 
  * Endpoints
  * Sandboxes</summary><br><b>

  * Networks: software implementation of an switch. They used for grouping and isolating a collection of endpoints.
  * Endpoints: Virtual network interfaces. Used for making connections.
  * Sandboxes: Isolated network stack (interfaces, routing tables, ports, ...)
</b></details>

<details>
<summary>True or False? If you would like to connect a container to multiple networks, you need multiple endpoints</summary><br><b>

True. An endpoint can connect only to a single network.
</b></details>

<details>
<summary>What are some features of libnetwork?</summary><br><b>

* Native service discovery
* ingress-based load balancer
* network control plane and management plane
</b></details>

#### Containers - Security

<details>
<summary>What security best practices are there regarding containers?</summary><br><b>

  * Install only the necessary packages in the container
  * Don't run containers as root when possible
  * Don't mount the Docker daemon unix socket into any of the containers
  * Set volumes and container's filesystem to read only
  * DO NOT run containers with `--privilged` flag
</b></details>

<details>
<summary>A container can cause a kernel panic and bring down the whole host. What preventive actions can you apply to avoid this specific situation?</summary><br><b>

  * Install only the necessary packages in the container
  * Set volumes and container's filesystem to read only
  * DO NOT run containers with `--privilged` flag
</b></details>

#### Containers - Docker in Production

<details>
<summary>What are some best practices you following in regards to using containers in production?</summary><br><b>

Images:
  * Use images from official repositories
  * Include only the packages you are going to use. Nothing else.
  * Specify a tag in FROM instruction. Not using a tag means you'll always pull the latest, which changes over time and might result in unexpected result.
  * Do not use environment variables to share secrets
  * Keep images small! - you want them only to include what is required for the application to run successfully. Nothing else.
Components:
  * Secured connection between components (e.g. client and server)
</b></details>

<details>
<summary>True or False? It's recommended for production environments that Docker client and server will communicate over network using HTTP socket</summary><br><b>

False. Communication between client and server shouldn't be done over HTTP since it's insecure. It's better to enforce the daemon to only accept network connection that are secured with TLS.<br>
Basically, the Docker daemon will only accept secured connections with certificates from trusted CA.
</b></details>

<details>
<summary>What forms of self-healing options available for Docker containers?</summary><br><b>

Restart Policies. It allows you to automatically restart containers after certain events.
</b></details>

<details>
<summary>What restart policies are you familiar with?</summary><br><b>

  * always: restart the container when it's stopped (not with `docker container stop`)
  * unless-stopped: restart the container unless it was in stopped status
  * no: don't restart the container at any point (default policy)
  * on-failure: restart the container when it exists due to an error (= exit code different than zero)
</b></details>

#### Containers - Docker Misc
<details>
<summary>Explain what is Docker Bench</summary><br><b>
</b></details>

