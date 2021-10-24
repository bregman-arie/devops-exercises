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
2. Run `docker container ls` - Is the container running? What about after 15 seconds, is it still running? why?
3. How then can we stop the container from running?
4. Remove the container you've created
5. Run the same container again but this time with `sleep 600` and verify it runs
6. Restart the Docker service. Is the container still running? why?
8. Update the policy to `unless-stopped`
9. Stop the container
10. Restart the Docker service. Is the container running? why?
