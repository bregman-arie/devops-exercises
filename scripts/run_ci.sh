#!/usr/bin/env bash

set -euo pipefail

PROJECT_DIR="$(dirname $(readlink -f ${BASH_SOURCE[0]}))/.."

MD_FILES=$(find ${PROJECT_DIR} -name "*.md" -not -path "${PROJECT_DIR}/tests/*")

for file in ${MD_FILES[@]}; do
   python ${PROJECT_DIR}/tests/syntax_lint.py ${file} > /dev/null
done

echo "- Syntax lint tests on MD files passed sucessfully"

flake8 --max-line-length=100 . && echo "- PEP8 Passed"