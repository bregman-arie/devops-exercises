# Unique Count

## Objectives

In this directory you have a file with list of IP addresses called `ip_list`. Using the file, determine which IP address is the most recurring (listed the most times).

# Solution

`sort ip_list | cut -d' ' -f1 | uniq -c | sort -n | tail -1`