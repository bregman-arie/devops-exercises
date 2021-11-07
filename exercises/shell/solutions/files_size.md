## Files Size

### Objectives

1. Print the name and size of every file and directory in current path

Note: use at least one for loop!

### Solution

```
#!/usr/bin/env bash

for i in $(ls -S1); do
    echo $i: $(du -sh "$i" | cut -f1)
done 
```
