## Directories Comparison

### Objectives

1. You are given two directories as arguments and the output should be any difference between the two directories

### Solution

Suppose the name of the bash script is ```dirdiff.sh```

```
#!/bin/bash

if test $# -ne 2
then
	echo -e "USAGE: ./dirdiff.sh directory1 directory2"
	exit 1
fi

diff -q $1 $2
```