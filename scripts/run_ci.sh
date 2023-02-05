#!/bin/bash
# These are the same steps we are running in Travis CI


find . -name "*.md" -not -path "./tests/*" | \
   xargs -I {} \
   python $(dirname "$0")/../tests/syntax_lint.py {} > /dev/null
mdPassed=$?
flake8 --max-line-length=100 . && echo "PEP8 Passed"
pyPassed=$?
if [ $pyPassed -eq 0 ] && [ $mdPassed -eq 0 ];then
   exit 0
else
   exit 1
fi
