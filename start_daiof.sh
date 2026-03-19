#!/bin/bash

# Navigate to project root
cd /Users/andy/my_too_test || exit

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d "venv_new" ]; then
    source venv_new/bin/activate
fi

# Set python path
export PYTHONPATH=$PYTHONPATH:$(pwd):$(pwd)/autonomous_operator

# Run Orchestrator in background using nohup
echo "🚀 Kích hoạt Hệ thống Tự trị DAIOF PHOENIX (Kernel v1.1)..."
nohup python3 -u start_phoenix_daiof.py > /tmp/system_stdout.log 2>&1 &

PID=$!
echo $PID > /tmp/orchestrator.pid

echo "✅ Hệ thống đang chạy ngầm với PID: $PID"
echo "📊 Master có thể xem log tại: tail -f /tmp/orchestrator.log"
