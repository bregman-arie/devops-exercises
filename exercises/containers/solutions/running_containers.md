## Running Containers

### Objective

Learn how to run, stop and remove containers

### Requirements

Make sure Podman or Docker (or any other containers engine) is installed on your system

### Instructions

1. Run a container using the latest nginx image - `podman container run nginx:latest`
2. List the containers to make sure the container is running - `podman container ls`
3. Run another container but this time use ubuntu latest and attach to the terminal of the container - `podman container run -it ubuntu:latest /bin/bash`
4. List again the containers. How many containers are running? - `podman container ls` -> 2
5. Stop the containers - WARNING: the following will stop all the containers on the host: `podman stop $(podman container ls -q)` or for each container `podman stop [container id/name]`
6. Remove the containers - WARNING: the following will remove other containers as well if such are running: `podman rm $(podman container ls -q -a)` or for each container `podman rm [container id/name]`
