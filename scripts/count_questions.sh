#!/usr/bin/env bash

echo $(( $(grep -E "\[Exercise\]|</summary>" -c README.md topics/*/README.md | awk -F: '{ s+=$2 } END { print s }' )))
