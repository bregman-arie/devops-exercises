## Argument Check

### Objectives

Note: assume the script is executed with an argument

1. Write a script that will check if a given argument is the string "pizza"
 1. If it's the string "pizza" print "with pineapple?"
 2. If it's not the string "pizza" print "I want pizza!"

### Solution

```
/usr/bin/env bash

arg_value=${1:-default}

if [ $arg_value = "pizza" ]; then
    echo "with pineapple?"
else
    echo "I want pizza!"
fi
```
