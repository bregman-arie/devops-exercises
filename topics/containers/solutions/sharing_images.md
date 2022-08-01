# Sharing Images

## Requirements

Have at least one image locally (run `podman image ls` to confirm).<br>
If you don't have images locally, run simply `podman pull httpd`.

## Objectives

1. Choose an image and create an archive out of it
2. Check the archive size. Is it different than the image size? If yes, what's the difference? If not, why?
3. Copy the generated archive to a remote host
4. Load the image
5. Verify it was loaded and exists on the remote host

## Solution

```
# Save image as an archive
podman save -o httpd.tar httpd

# Check archive and image sizes
du -sh httpd.tar # output: 143MB
podman image ls | grep httpd # output: 149MB
# The archive is obviously smaller than the image itself (6MB difference)

# Copy the archive to a remote host
rsync -azc httpd.tar USER@REMOTE_HOST_FQDN:/tmp/

# Load the image
podman load -i /tmp/httpd.tar

# Verify it exists on the system after loading
podman image ls
```
