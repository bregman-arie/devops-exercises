#!/bin/bash
# These are the same steps we are running in Travis CI

python tests/syntax_lint.py
flake8 --exclude venv --max-line-length=100 . && echo "PEP8 Passed"
