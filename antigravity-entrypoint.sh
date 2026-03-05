#!/bin/bash
echo "🚀 Starting Σ_APΩ Runtime: Antigravity Mode thỏ..."

# Start Factory Worker in background
echo "👷 Launching Execution Plane (Factory Worker)..."
python3 -u factory/factory_worker.py &

# Start Telegram Bot in foreground
echo "🤖 Launching Control Plane (Antigravity Bot)..."
python3 -u factory/telegram_bot.py

# Wait for all processes to finish
wait
