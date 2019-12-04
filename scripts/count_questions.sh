#!/bin/bash

echo $((7 + $(cat README.md | grep \<\/summary\> | wc -l)))
