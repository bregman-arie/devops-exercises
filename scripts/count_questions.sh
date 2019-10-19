#!/bin/bash

# 5 is the number of scenario questions.
expr 5 + $(cat README.md | grep \<\/summary\> | wc -l)
