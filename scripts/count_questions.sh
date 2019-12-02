#!/bin/bash

echo $((8 + $(cat README.md | grep \<\/summary\> | wc -l)))
