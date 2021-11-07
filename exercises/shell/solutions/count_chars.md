## Count Chars

### Objectives

1. Read input from the user until you get empty string
2. For each of the lines you read, count the number of characters and print it

### Constraints

1. You must use a while loop
2. Assume at least three lines of input

### Solution

```
#!/usr/bin/env bash

echo -n "Please insert your input: "

while read line; do
    echo -n "$line" | wc -c
    echo -n "Please insert your input: "
done
```
