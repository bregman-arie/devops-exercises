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
RUN apk add --update nodejs nodejs-npm
COPY . /src
WORKDIR /src
RUN npm install
EXPOSE 8080
ENTRYPOINT ["node", "./app.js"]
```
