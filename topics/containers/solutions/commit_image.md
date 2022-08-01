# Create Images on The Fly

## Requirements

Have at least one image locally (run `podman image ls` to confirm).<br>
If you don't have images locally, run simply `podman pull nginx:alpine`.

## Objectives

1. Run a container using a web server image (e.g. httpd, nginx, ...)
  - Bind container's port 80 to local port 80
  - Run it in detached mode
  - Name should nginx_container
2. Verify the web server runs and accessible
3. Create an HTML file with the following content and copy it to the container to the container to path where it will be accessed as an index file

```
<html>
<head>
<title>It's a me</title>
</head>
<body>
<h1>Mario</h1>
</body>
```

4. Create an image out of the running container and call it "nginx_mario"
5. Tag the container with "mario" tag
6. Remove the original container (container_nginx) and verify it was removed
7. Create a new container out of the image you've created (the same way as the original container)
8. Run `curl 127.0.0.1:80`. What do you see?
9. Run `podman diff` on the new image. Explain the output

## Solution

```
# Run the container
podman run --name nginx_container -d -p 80:80 nginx:alpine

# Verify web server is running
curl 127.0.0.1:80
    #  <!DOCTYPE html>
    #  <html>
    #  <head>
    #  <title>Welcome to nginx!</title>

# Create index.html file
cat <<EOT >>index.html
<html>
<head>
<title>It's a me</title>
</head>
<body>
<h1>Mario</h1>
</body>
EOT

# Copy index.html to the container
podman cp index.html nginx_container:/usr/share/nginx/html/index.html

# Create a new image out of the running container
podman commit nginx_container nginx_mario

# Tag the image
podman image ls
# localhost/nginx_mario     latest   dc7ed2343521   52 seconds ago   25 MB
podman tag dc7ed2343521 mario

# Remove the container
podman stop nginx_container
podman rm nginx_container
podman ps -a # no container 'nginx_container'

# Create a container out of the image 
podman run -d -p 80:80 nginx_mario

# Check the container created from the new image
curl 127.0.0.1:80
#<html>
#<head>
#<title>It's a me</title>
#</head>
#<body>
#<h1>Mario</h1>
#</body>

# Run diff
podman diff nginx_mario

C /etc
C /etc/nginx/conf.d
C /etc/nginx/conf.d/default.conf
A /run/nginx.pid
C /usr/share/nginx/html
C /usr/share/nginx/html/index.html
C /var/cache/nginx
C /var
C /var/cache
A /var/cache/nginx/client_temp
A /var/cache/nginx/fastcgi_temp
A /var/cache/nginx/proxy_temp
A /var/cache/nginx/scgi_temp
A /var/cache/nginx/uwsgi_temp

# We've set new index.html which explains why it's changed (C)
# We also created the image while the web server is running, which explains all the files created under /var
```
