# Reverse Proxy Log Diagnostics

## Objective
A production alert indicates that users are receiving a `502 Bad Gateway` when trying to access the internal dashboard. The Nginx reverse proxy is running, but it cannot establish a connection with the upstream backend application listening on port `5000`.

Using the mock log file `nginx_error.log` in this directory:
1. Write a shell command to parse the logs and extract the specific connection refusal event.
2. What are the logical next steps in a Linux system environment using `systemd` to verify and resolve this connection outage?

# Solution
Click [here](solution.md) to view the step-by-step diagnostic solution.
