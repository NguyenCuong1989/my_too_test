# Local Operations Guide

## Purpose
Run AXCONTROL in local-first mode with deterministic no-drift checks, periodic backups, and log maintenance.

## Daily Commands
- Run invariants manually: `make ci`
- Start bridge: `AXCONTROL_SIM=1 python3 core/bridge/http_server.py`
- Send probe request:
  - `curl -X POST http://127.0.0.1:5140/chat -H 'Content-Type: application/json' -d '{"text":"status?"}'`

## Commit Safety
Pre-commit hook runs no-drift invariants before every commit:
- `python3 -m unittest tests.test_bridge_no_drift -v`

## Cron Schedule
Installed cron entries:
- Hourly CI: `make ci`
- 30-minute backup: `ops/auto-backup-to-github.sh`
- Daily rotation: `ops/rotate_logs.sh`

Check active cron:
- `crontab -l`

## Log Files
- Runtime audit: `logs/observe.ndjson`
- CI cron output: `logs/ci-cron.log`
- Backup cron output: `logs/backup-cron.log`
- Rotation maintenance: `logs/maintenance.log`
- Rotated archives: `logs/archive/`

## Recovery Actions
- Reinstall hooks: `make install-hooks`
- Re-run invariants: `make ci`
- Verify latest audit writes:
  - `tail -n 5 logs/observe.ndjson`
