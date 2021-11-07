## Number of Arguments

### Objectives

* Write a script that will print "Got it: <argument value>" in case of one argument
* In case no arguments were provided, it will print "Usage: ./<program name> <argument>"
* In case of more than one argument, print "hey hey...too many!"

### Solution

```
#!/usr/bin/env bash

set -eu

main() {
  case $# in
    0) printf "%s" "Usage: ./<program name> <argument>"; return 1 ;;
    1) printf "%s" "Got it: $1"; return 0 ;;
    *) return 1 ;;
  esac
}

main "$@"
```

