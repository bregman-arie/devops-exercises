#!/bin/bash
# These are the same steps we are running in Travis CI

python $(dirname "$0")/../tests/syntax_lint.py
flake8 --max-line-length=100 . && echo "PEP8 Passed"
