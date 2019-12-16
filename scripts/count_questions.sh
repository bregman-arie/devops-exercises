#!/bin/bash

# We dont care about non alphanumerics filenames so we just ls | grep to shortern the script.

echo $(( $(ls ./scenarios/ | grep ".*md" -c) + $(grep \</summary\> -c README.md) ))
