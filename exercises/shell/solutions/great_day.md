## Great Day

### Objectives

1. Write a script that will print "Today is a great day!" unless it's given a day name and then it should print "Today is <given day>"

Note: no need to check whether the given argument is actually a valid day

### Solution

```
#!/usr/bin/env bash

echo "Today is ${1:-a great day!}"
```
