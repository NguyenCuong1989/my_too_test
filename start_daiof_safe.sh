#!/bin/bash
# Navigate to project root
cd /Users/andy/my_too_test || exit

# Set python path
export PYTHONPATH=$PYTHONPATH:$(pwd):$(pwd)/autonomous_operator

# Run Orchestrator in background
echo "🚀 Kích hoạt Hệ thống Tự trị DAIOF PHOENIX (Safe Mode)..."
nohup python3 -u start_phoenix_daiof.py > /tmp/daiof_stdout.log 2>&1 &

PID=$!
echo $PID > /tmp/daiof_orchestrator.pid
echo "✅ Hệ thống đang chạy ngầm với PID: $PID"
echo "📊 Master có thể xem log tại: tail -f /tmp/orchestrator.log"
