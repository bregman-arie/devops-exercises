#!/bin/bash

# We dont care about non alphanumerics filenames so we just ls | grep to shorten the script.

echo $(( $(grep \</summary\> -c README.md) + $(grep -i Solution README.md | grep \.md -c) ))
