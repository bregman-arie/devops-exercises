## Working with Images - Solution

### Objective

Learn how to work with containers images

### Requirements

Make sure Podman, Docker (or any other containers engine) is installed on your system

### Instructions

1. List the containers images in your environment - `podman image ls`
2. Pull the latest ubuntu image - `podman image pull ubuntu:latest`
3. Run a container with the image you just pulled  - `podman container run -it ubuntu:latest /bin/bash`
4. Remove the image. Did it work? - No. There is a running container which is using the image we try to remove
5. Do whatever is needed in order to remove the image - `podman rm <container_id>; podman image rm ubuntu`
