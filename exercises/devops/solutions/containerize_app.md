## Containerize an Application

1. Clone an open source project you would like to containerize. A couple of suggestions:

```
https://github.com/bregman-arie/node-hello-world
https://github.com/bregman-arie/flask-hello-world
```

`git clone https://github.com/bregman-arie/node-hello-world`

2. Write a Dockerfile you'll use for building an image of the application (you can use any base image you would like)

```
FROM alpine
LABEL maintainer="your name/email"
RUN apk add --update nodejs npm
COPY . /src
WORKDIR /src
RUN npm install
EXPOSE 3000
ENTRYPOINT ["node", "./app.js"]
```

3. Build an image using the Dockerfile you've just wrote

`docker image build -t web_app:latest .`

4. Verify the image exists

`docker image ls`

5. [Optional] Push the image you've just built to a registry

```
docker login
docker image tag web_app:latest <your username>/web_app:latest
# Verify with "docker image ls"
docker image push <your username>/web_app:latest
```

6. Run the application

```
docker container run -d -p 80:3000 web_app:latest
```

7. Verify the app is running

```
docker container ls
docker logs <container ID/name>
# In the browser, go to 127.0.0.1:80
```
