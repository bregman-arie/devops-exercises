#!/bin/bash

echo $((6 + $(cat README.md | grep \<\/summary\> | wc -l)))
