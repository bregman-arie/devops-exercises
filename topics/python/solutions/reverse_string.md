## Reverse a String - Solution

```
my_string[::-1]
```

A more visual way is:<br>
<i>Careful: this is very slow</i>

```
def reverse_string(string):
    temp = ""
    for char in string:
        temp =  char + temp
    return temp
```
