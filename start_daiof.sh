#!/bin/bash

# Navigate to project root
cd /Users/andy/my_too_test

# Activate virtual environment
source venv_biz/bin/activate

# Set python path
export PYTHONPATH=$PYTHONPATH:$(pwd)/autonomous_operator

# Run Orchestrator in background using nohup
echo "🚀 Kích hoạt Hệ thống Tự trị DAIOF..."
nohup python3 -u autonomous_operator/orchestrator_v3.py > autonomous_operator/logs/system_stdout.log 2>&1 &

PID=$!
echo $PID > autonomous_operator/state/orchestrator.pid

echo "✅ Hệ thống đang chạy ngầm với PID: $PID"
echo "📊 Master có thể xem log tại: tail -f autonomous_operator/logs/orchestrator.log"
