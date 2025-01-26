#!/usr/bin/env bash

set -euo pipefail

PROJECT_DIR="$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/.."

# Use the `-print0` option to handle spaces safely, and while-read loop:
find "${PROJECT_DIR}" \
  -name "*.md" \
  -not -path "${PROJECT_DIR}/tests/*" \
  -print0 |
while IFS= read -r -d '' file
do
  python "${PROJECT_DIR}/tests/syntax_lint.py" "${file}" > /dev/null
done

echo "- Syntax lint tests on MD files passed successfully"

flake8 --max-line-length=100 . && echo "- PEP8 Passed"
