## Run, Forest, Run!

### Objective

Learn what restart policies do and how to use them

### Requirements

Make sure Docker is installed on your system and the service is started

```
# Fedora/RHEL/CentOS
rpm -qa | grep docker
systemctl status docker
```

### Instructions

1. Run a container with the following properties:
  * image: alpine
  * name: forest
  * restart policy: always
  * command to execute: sleep 15

`docker run --restart always --name forest alpine sleep 15`

2. Run `docker container ls` - Is the container running? What about after 15 seconds, is it still running? why?


It runs even after it completes to run `sleep 15` because the restart policy is "always". This means that Docker will keep restarting the **same** container even after it exists.


3. How then can we stop the container from running?

The restart policy doesn't apply when the container is stopped with the command `docker container stop`

4. Remove the container you've created

```
docker container stop forest
docker container rm forest
```

5. Run the same container again but this time with `sleep 600` and verify it runs

```
docker run --restart always --name forest alpine sleep 600
docker container ls
```

6. Restart the Docker service. Is the container still running? why?

```
sudo systemctl restart docker
```
Yes, it's still running due to the restart policy `always` which means Docker will always bring up the container after it exists or stopped (not with the stop command).

8. Update the policy to `unless-stopped`

`docker update --restart unless-stopped forest`

9. Stop the container

`docker container stop forest`

10. Restart the Docker service. Is the container running? why?

```
sudo systemctl restart docker
```
No, the container is not running. This is because we changed the policy to `unless-stopped` which will run the container unless it was in stopped status. Since before the restart we stopped the container, Docker didn't continue running it after the restart.
