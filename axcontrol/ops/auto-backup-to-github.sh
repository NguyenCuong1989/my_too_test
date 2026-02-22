#!/bin/bash
set -euo pipefail

cd /Users/andy/my_too_test/axcontrol
# Backup tracked changes only to avoid sweeping large untracked dirs.
git add -u
if git diff --cached --quiet; then
  echo "No changes to backup."
  exit 0
fi
git commit -m "Auto backup from local $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main
