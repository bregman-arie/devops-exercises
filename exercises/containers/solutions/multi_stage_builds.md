## Multi-Stage Builds

### Objective

Learn about multi-stage builds

### Instructions

1. Without actually building an image or running any container, use the following Dockerfile and convert it to use multi-stage:

```
FROM nginx
RUN apt-get update \
 && apt-get install -y curl python build-essential \
 && apt-get install -y nodejs \
 && apt-get clean -y
RUN mkdir -p /my_app
ADD ./config/nginx/docker.conf /etc/nginx/nginx.conf
ADD ./config/nginx/k8s.conf /etc/nginx/nginx.conf.k8s
ADD app/ /my_cool_app
WORKDIR /my_cool_app
RUN npm install -g ember-cli
RUN npm install -g bower
RUN apt-get update && apt-get install -y git \
 && npm install \
 && bower install \
RUN ember build — environment=prod
CMD [ “/root/nginx-app.sh”, “nginx”, “-g”, “daemon off;” ]
```

2. What are the benefits of using multi-stage builds?

### Solution

1. One possible solution (the emphasize is on passing the app from the first stage):

```
FROM node:6
RUN mkdir -p /my_cool_app
RUN npm install -g ember-cli
RUN npm install -g bower
WORKDIR /my_cool_app
RUN npm install
ADD app/ /my_cool_app
RUN bower install
RUN ember build — environment=prod

FROM nginx
RUN mkdir -p /my_cool_app
ADD ./config/nginx/docker.conf /etc/nginx/nginx.conf
ADD ./config/nginx/k8s.conf /etc/nginx/nginx.conf.k8s
# Copy build artifacts from the first stage
COPY — from=0 /my_cool_app/dist /my_cool_app/dist
WORKDIR /my_cool_app
CMD [ “/root/nginx-app.sh”, “nginx”, “-g”, “daemon off;” ]
```

2. Multi-stages builds allow you to produce smaller container images by splitting the build process into multiple stages as we did above. The app image doesn't contain anything related to the build process except the actual app.
