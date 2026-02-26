#!/bin/bash
set -e

# Ensure state and logs directories exist
mkdir -p /app/autonomous_operator/logs
mkdir -p /app/autonomous_operator/state

if [ "$1" = 'orchestrator' ]; then
    echo "Starting DAIOF Orchestrator..."
    exec python3 -u autonomous_operator/orchestrator_v3.py
elif [ "$1" = 'monitor' ]; then
    echo "Starting DAIOF Monitor..."
    exec python3 -u autonomous_operator/eternal_monitor.py
else
    exec "$@"
fi
