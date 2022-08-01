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

Click [here to view the solution](solutions/commit_image.md)
