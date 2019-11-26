#!/bin/bash

# 6 is the number of scenario questions.
expr 6 + $(cat README.md | grep \<\/summary\> | wc -l)
