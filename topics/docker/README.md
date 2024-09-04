# Docker



<details>
<summary>1. What is Docker and how does it differ from a virtual machine?</summary><br><b>
Docker is a platform that allows developers to automate the deployment of applications inside lightweight, portable containers. Unlike virtual machines, which run a full operating system, Docker containers share the host OS kernel, making them more efficient in terms of resource usage and startup time.

</b></details>


<details>
<summary>2. What are the key components of Docker?</summary><br><b>
The key components of Docker include:
- **Docker Engine:** The core service for building and running containers.
- **Docker Images:** Read-only templates used to create containers.
- **Docker Containers:** Executable instances of Docker images.
- **Docker Hub:** A cloud-based registry for sharing Docker images.

</b></details>

<details>
<summary>3. What is a Dockerfile?</summary><br><b>
A Dockerfile is a text file that contains a series of instructions for building a Docker image. It defines the base image, sets up the environment, and specifies the commands to run when creating the container.

</b></details>

<details>
<summary>4. How do you create a Docker image from a Dockerfile?</summary><br><b>
You can create a Docker image from a Dockerfile using the command- docker build -t 

</b></details>

<details> 
<summary>5. What is the difference between a Docker image and a Docker container?</summary><br><b> A Docker image is a read-only template that defines the environment and filesystem for a container. A Docker container is a running instance of a Docker image, containing everything needed to run an application, including the code, libraries, and environment variables. 

</b></details> 

<details> <summary>6. How can you list all Docker containers running on your system?</summary><br><b> You can list all running Docker containers using the command: ```bash docker ps ``` To list all containers, including stopped ones, use: ```bash docker ps -a ``` 

</b></details> 

<details> <summary>7. What is Docker Compose and how is it used?</summary><br><b> Docker Compose is a tool for defining and running multi-container Docker applications. With a `docker-compose.yml` file, you can configure all of your application's services, networks, and volumes, and then start them with a single command: ```bash docker-compose up ``` 

</b></details> <details> 

<summary>8. How do you scale services in Docker Compose?</summary><br><b> You can scale services in Docker Compose by using the `--scale` flag followed by the service name and the desired number of instances. For example: ```bash docker-compose up --scale <service_name>=<number_of_instances> ``` This command will start the specified number of instances of the service. 

</b></details> 

<details> <summary>9. What is Docker Swarm?</summary><br><b> Docker Swarm is Docker's native clustering and orchestration tool. It allows you to manage a cluster of Docker engines as a single swarm, providing high availability, load balancing, and scaling capabilities for your Dockerized applications.

 </b></details> 

<details> <summary>10. How do you initialize a Docker Swarm?</summary><br><b> You can initialize a Docker Swarm using the command: ```bash docker swarm init ``` This command sets up the current Docker engine as the swarm manager. You can then add worker nodes to the swarm using the token provided by the `docker swarm join-token` command.

 </b></details> 

<details> <summary>11. What is the purpose of Docker volumes?</summary><br><b> Docker volumes are used to persist data generated and used by Docker containers. Volumes provide a way to store data outside the container's filesystem, allowing it to be shared between containers or preserved after the container stops or is deleted.

 </b></details> 

<details> <summary>12. How can you create and manage Docker volumes?</summary><br><b> You can create a Docker volume using the command: ```bash docker volume create <volume_name> ``` To list all Docker volumes, use: ```bash docker volume ls ``` To remove a volume, use: ```bash docker volume rm <volume_name> ```

 </b></details> 

<details> <summary>13. What is a Docker network and how do you create one?</summary><br><b> A Docker network allows containers to communicate with each other. You can create a custom Docker network using the command: ```bash docker network create <network_name> ``` This command creates a new bridge network that you can connect containers to, enabling communication between them.

 </b></details> 

<details> <summary>14. How do you connect a container to a Docker network?</summary><br><b> You can connect a container to a Docker network using the command: ```bash docker network connect <network_name> <container_name_or_id> ``` This command connects the specified container to the specified network, allowing it to communicate with other containers on the same network.

 </b></details> 

<details> <summary>15. What is the difference between a bind mount and a volume in Docker?</summary><br><b> A bind mount is a mapping between a directory on the host machine and a directory in the container. The data in the container directly reflects the data in the host directory. A Docker volume, on the other hand, is managed by Docker and stored in a specific location on the host. Volumes are generally preferred for persistent data as they are easier to manage and portable across different environments. 

</b></details> 

<details> <summary>16. How can you share data between containers in Docker?</summary><br><b> You can share data between containers in Docker by using volumes. Multiple containers can be configured to use the same volume, allowing them to read and write to the shared storage. This can be done by specifying the same volume in the `docker run` or `docker-compose.yml` file for each container. 

</b></details> 

<details> <summary>17. What is the purpose of the `docker exec` command?</summary><br><b> The `docker exec` command is used to run a command in an already running container. It is often used to access the container's shell or to run additional processes inside the container. For example: ```bash docker exec -it <container_name_or_id> /bin/bash ``` This command opens an interactive shell session in the specified container. 

</b></details> 

<details> <summary>18. How do you remove unused Docker objects, such as images, containers, and volumes?</summary><br><b> You can remove unused Docker objects using the `docker system prune` command. This command removes all stopped containers, unused networks, dangling images, and unused volumes. You can use the `-a` flag to remove all unused images, not just dangling ones: ```bash docker system prune -a ```

 </b></details> 

<details> <summary>19. What are Docker tags and how are they used?</summary><br><b> Docker tags are labels that can be applied to Docker images to help identify different versions or variants of the image. Tags are typically used to specify the version of the application or the environment (e.g., `latest`, `1.0`, `stable`). You can tag an image during the build process using the `-t` option: ```bash docker build -t <image_name>:<tag> <path_to_dockerfile> ``` 

</b></details> 

<details> <summary>20. How do you push a Docker image to Docker Hub?</summary><br><b> To push a Docker image to Docker Hub, you first need to log in using the `docker login` command. Then, you can push the image using the `docker push` command: ```bash docker push <username>/<image_name>:<tag> ``` Make sure that the image is tagged with your Docker Hub username before pushing. 

</b></details>