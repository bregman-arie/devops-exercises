## Layer by Layer

### Objective

Learn about image layers

### Requirements

Make sure Docker is installed on your system and the service is started

```
# Fedora/RHEL/CentOS
rpm -qa | grep docker
systemctl status docker
```

### Instructions

1. Write a Dockefile. Any Dockefile! :) (just make sure it's a valid one)

```
FROM ubuntu
EXPOSE 212
ENV foo=bar
WORKDIR /tmp
RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024
RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024
RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024
```

2. Build an image using the Dockerfile you've wrote

`docker image build -t super_cool_app:latest .`

3. Which of the instructions you've used, created new layers and which added image metadata?

```
FROM, RUN -> new layer
EXPOSE, ENV, WORKDIR -> metadata
```

4. What ways are there to confirm your answer to the last question?

You can run `docker image history super_cool_app`. It will show you each instruction and its size. Usually instructions that create new layers has non-zero size, but this is not something you can rely on by itself since, some run commands can have size of zero in `docker image history` output (e.g. `ls -l`).

You can also use `docker image inspect super_cool_appl` and see if in the output, under "RootFS", there are the number of layers that matches the instructions that should create new layers.

5. Can you reduce the size of the image you've created?

yes, for example, use all the RUN instructions as a single RUN instruction this way:

`RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024 && dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024 && dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024`

The change in size might not be dramatic in this case, but in some cases it will make a big impact on the image size.
