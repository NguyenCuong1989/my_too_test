#!/bin/bash

# Navigate to project root
cd /Users/andy/my_too_test || exit || exit

# Activate virtual environment
source venv_new/bin/activate

# Set python path
export PYTHONPATH
PYTHONPATH=$PYTHONPATH:$(pwd):$(pwd)/autonomous_operator

# Run Orchestrator in background using nohup
echo "🚀 Kích hoạt Hệ thống Tự trị DAIOF PHOENIX (Kernel v1.1)..."
nohup python3 -u start_phoenix_daiof.py > autonomous_operator/logs/system_stdout.log 2>&1 &

PID=$"!"
echo $PID > autonomous_operator/state/orchestrator.pid

echo "✅ Hệ thống đang chạy ngầm với PID: $PID"
echo "📊 Master có thể xem log tại: tail -f autonomous_operator/logs/orchestrator.log"
