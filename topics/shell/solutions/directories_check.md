## Directories Check

### Objectives

1. Check if the directory exist.

### Solution 1

Suppose the name of the bash script is ```check_dir.sh```

```
#!/bin/bash

DIR="/tmp/downloads"
if [ -d "$DIR" ]; then
 echo "Directory exist"
else
 echo "Directory not found"
 exit 1
fi
```

### Solution 2

```
DIR=/tmp/downloads
[ -d "$DIR" ] && echo "$DIR directory exists."
```

### Solution 3

```
DIR=/tmp/downloads
if [ ! -d "$DIR" ];
then
  echo "$DIR directory does not exist."
else
  echo "$DIR directory exists."
fi
```