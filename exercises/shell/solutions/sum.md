## Sum

### Objectives

1. Write a script that gets two numbers and prints their sum
3. Make sure the input is valid (= you got two numbers from the user)
2. Test the script by running and passing it two numbers as arguments 

### Constraints

1. Use functions

### Solution

```
#!/usr/bin/env bash

re='^[0-9]+$'

if ! [[ $1 =~ $re && $2 =~ $re ]]; then
    echo "Oh no...I need two numbers"
    exit 2
fi

function sum {
    echo $(( $1 + $2 ))
}

sum $1 $2
```
