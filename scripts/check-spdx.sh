#!/usr/bin/env bash
set -euo pipefail

missing=$(grep -L "SPDX-License-Identifier: MIT" $(git ls-files '*.js' '*.cjs' '*.mjs' 2>/dev/null || true) || true)
if [ -n "$missing" ]; then
  echo "Files missing SPDX header:" >&2
  echo "$missing" >&2
  exit 1
fi
echo "All checked files contain SPDX headers."
