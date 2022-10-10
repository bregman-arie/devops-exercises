## Empty Files

### Objectives

1. Write a script to remove all the empty files in a given directory (including nested directories)

### Solution

```
#! /bin/bash
for x in *
do
    if [ -s $x ]
    then
        continue
    else
        rm -rf $x
    fi
done
```
