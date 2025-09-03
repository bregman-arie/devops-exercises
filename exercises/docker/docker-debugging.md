# Docker Scenario-Based Exercises

This file contains scenario-based Docker questions to help DevOps engineers practice real-world troubleshooting and configuration tasks. Each question simulates a practical scenario with a step-by-step answer.

## Question 1: Debugging a Docker Container Failure

### Question
You’re a DevOps engineer deploying a Node.js application using Docker. You run `docker run -d -p 3000:3000 my-node-app`, but the container exits immediately. Using `docker ps -a`, you see the container status as `Exited`. How would you troubleshoot and resolve this issue?

### Answer
To troubleshoot a container exiting immediately:
1. **Check Logs**: Run `docker logs my-node-app` to view error messages. Common issues include missing dependencies (e.g., `npm install` failed) or an incorrect command.
2. **Inspect the Container**: Use `docker inspect my-node-app` to check `Config.Cmd` or `Config.Entrypoint`. Ensure the command (e.g., `node app.js`) is valid.
3. **Verify the Dockerfile**: Check if `CMD` or `ENTRYPOINT` is correct, e.g., `CMD ["node", "app.js"]`. Update and rebuild if needed: `docker build -t my-node-app .`.
4. **Test Interactively**: Run `docker run -it my-node-app sh` to debug manually (e.g., `node app.js`).
5. **Check Resources**: Ensure the host has enough memory/CPU using `docker stats`.

**Example Fix**: If logs show `node: command not found`, update the Dockerfile to use `FROM node:18`, rebuild, and rerun.

### Additional Notes
- Always start with `docker logs` for error clues.
- Use `docker ps -a` to check container status and ID.
- Common issues include missing dependencies or crashing apps.


---


## Question 2: Configuring a Multi-Container Application

### Question
As a DevOps engineer, you need to deploy a web application with a Node.js backend and a MySQL database using Docker. The Node.js app connects to MySQL on `localhost:3306`, but running `docker run` for each container separately fails because they can’t communicate. How would you set up these containers to work together?

### Answer
To make the Node.js and MySQL containers communicate:
1. **Use Docker Compose**: Create a `docker-compose.yml` file to define and link both services:
   ```yaml
   version: '3.8'
   services:
     node-app:
       image: my-node-app
       build: .
       ports:
         - "3000:3000"
       depends_on:
         - mysql-db
       environment:
         - DB_HOST=mysql-db
         - DB_PORT=3306
     mysql-db:
       image: mysql:8.0
       environment:
         - MYSQL_ROOT_PASSWORD=secret
       ports:
         - "3306:3306"
   ```
2. **Run the Application**: Execute `docker-compose up -d` to start both containers. The `node-app` service connects to `mysql-db` using the service name (`mysql-db`) as the hostname, not `localhost`.
3. **Verify Connectivity**: Check logs with `docker-compose logs node-app` to ensure the Node.js app connects to MySQL. If it fails, verify the environment variables and MySQL’s readiness.
4. **Alternative Without Compose**: Use a custom network:
   - Create a network: `docker network create my-app-network`
   - Run MySQL: `docker run -d --name mysql-db --network my-app-network -e MYSQL_ROOT_PASSWORD=secret mysql:8.0`
   - Run Node.js: `docker run -d --name node-app --network my-app-network -p 3000:3000 -e DB_HOST=mysql-db my-node-app`

### Additional Notes
- Docker Compose simplifies multi-container setups by managing networks and dependencies.
- Always set environment variables for database credentials to avoid hardcoding.


---


## Question 3: Optimizing a Dockerfile for CI/CD

### Question
You’re a DevOps engineer integrating a Dockerized Python application into a Jenkins CI/CD pipeline. The Dockerfile builds slowly, causing pipeline delays. How would you optimize the Dockerfile to speed up builds while maintaining functionality?

### Answer
To optimize a Dockerfile for faster CI/CD builds:
1. **Use a Smaller Base Image**: Replace heavy images like `python:3.9` with `python:3.9-slim` to reduce size and download time.
   ```dockerfile
   FROM python:3.9-slim
   ```
2. **Leverage Layer Caching**: Order instructions from least to most likely to change. Copy `requirements.txt` and install dependencies before copying the app code:
   ```dockerfile
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   ```
3. **Minimize Layers**: Combine related commands with `&&` to reduce layers:
   ```dockerfile
   RUN pip install -r requirements.txt && rm -rf /root/.cache/pip
   ```
4. **Use Multi-Stage Builds**: If the app needs build tools, use a multi-stage build to keep the final image small:
   ```dockerfile
   FROM python:3.9 AS builder
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   FROM python:3.9-slim
   COPY --from=builder /usr/local/lib/python3.9 /usr/local/lib/python3.9
   COPY . .
   CMD ["python", "app.py"]
   ```
5. **Test in Jenkins**: Update the Jenkins pipeline to rebuild the image only when `Dockerfile` or code changes, using a cached image otherwise:
   ```groovy
   pipeline {
       agent any
       stages {
           stage('Build Docker Image') {
               when { changeset "Dockerfile,**.py" }
               steps { sh 'docker build -t my-python-app .' }
           }
       }
   }
   ```

### Additional Notes
- Use `.dockerignore` to exclude unnecessary files (e.g., `.git`, `tests/`) from the build context.
- Monitor build times in Jenkins to confirm improvements.


*Contributed by Lahiru Galhena*
