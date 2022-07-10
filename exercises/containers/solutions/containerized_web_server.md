# Containerized Web Server

1. Run a containerized web server in the background and bind its port (8080) to a local port
2. Verify the port (8080) is bound
3. Reach the webserver from your local host
4. Now run the same web application but bound it to the local port 8080

## Solution

```
$ podman run -d -p 8080 httpd # run the container and bind the port 8080 to a local port
$ podman port -l 8080 # show to which local port the port 8080 on the container, binds to
0.0.0.0:41203
$ curl http://0.0.0.0:41203 # use the port from the output of the previous command

!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
	<head>
		<title>Test Page for the HTTP Server on Red Hat Enterprise Linux</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

$ podman run -d -p 8080:8080 httpd
```
