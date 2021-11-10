## It's Alive!

### Objectives

1. Write a script to determine whether a given host is down or up

### Solution

```
#!/usr/bin/env bash
SERVERIP=<IP Address>
NOTIFYEMAIL=test@example.com

ping -c 3 $SERVERIP > /dev/null 2>&1
if [ $? -ne 0 ]
then
   # Use mailer here:
   mailx -s "Server $SERVERIP is down" -t "$NOTIFYEMAIL" < /dev/null
fi
```
