## Packages Install

### Objectives

1. Install packages mentioned in a text file.

### Solution 1

Suppose the name of the bash script is ```packages_install.sh``` and 
the text file is ```install-packages.txt```.

```
#!/bin/bash

for package in $(cat install-packages.txt)
do
	echo "INSTALLING $package"
	sudo apt-get -y install $package
done
```