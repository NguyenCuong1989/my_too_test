#!/bin/bash
set -euo pipefail

cd /Users/andy/my_too_test/axcontrol
git add -A
if git diff --cached --quiet; then
  echo "No changes to backup."
  exit 0
fi
git commit -m "Auto backup from local $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main
