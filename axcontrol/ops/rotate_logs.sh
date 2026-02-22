#!/bin/bash
set -euo pipefail

ROOT="/Users/andy/my_too_test/axcontrol"
LOG_DIR="$ROOT/logs"
ROTATE_DIR="$LOG_DIR/archive"
DATE_TAG="$(date '+%Y%m%d-%H%M%S')"
KEEP_DAYS="${AXCONTROL_LOG_KEEP_DAYS:-7}"

mkdir -p "$ROTATE_DIR"

rotate_file() {
  local src="$1"
  local base
  base="$(basename "$src")"
  if [[ -f "$src" && -s "$src" ]]; then
    local dst="$ROTATE_DIR/${base}.${DATE_TAG}.gz"
    gzip -c "$src" > "$dst"
    : > "$src"
  fi
}

rotate_file "$LOG_DIR/observe.ndjson"
rotate_file "$LOG_DIR/ci-cron.log"
rotate_file "$LOG_DIR/backup-cron.log"

find "$ROTATE_DIR" -type f -mtime +"$KEEP_DAYS" -delete

echo "[$(date '+%Y-%m-%d %H:%M:%S')] rotation complete (keep_days=$KEEP_DAYS)" >> "$LOG_DIR/maintenance.log"
