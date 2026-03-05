#!/usr/bin/env python3
"""
TELEGRAM BOT PROVISIONING GUIDE
APΩ Antigravity Execution Layer - Governance Interface Setup

Author: Gordon (Docker AI)
Date: 2026-03-05
Status: PRODUCTION-READY

This guide walks you through:
1. Creating bot via BotFather
2. Configuring token
3. Verifying all invariants
4. Starting services
5. Testing end-to-end
"""

import requests
import json
from pathlib import Path

class TelegramBotProvisioning:
    """
    Step-by-step provisioning for Σ_APΩ Telegram Governance Interface
    """

    PHASE_1_BOTFATHER = """
    ╔════════════════════════════════════════════════════════════════════╗
    ║                    PHASE 1: BOTFATHER CREATION                     ║
    ╚════════════════════════════════════════════════════════════════════╝

    STEP 1: Open Telegram
    ├─ Search for: @BotFather
    └─ Start chat

    STEP 2: Create New Bot
    ├─ Send: /newbot
    │
    ├─ BotFather asks: "Alright, a new bot. How are we going to call it?"
    └─ Reply: "Antigravity APO Bot"

    STEP 3: Choose Username
    ├─ BotFather asks: "Good. Now let's choose a username..."
    │
    ├─ Reply: "Antigravity_APO_Bot"
    │  (Must be unique, end with "bot")
    │
    └─ Example accepted usernames:
       ✅ Antigravity_APO_Bot
       ✅ Antigravity_APO_Runtime_Bot
       ✅ SigmaAPO_Bot

    STEP 4: Copy Token
    ├─ BotFather will send:
    │  "Done! Congratulations on your new bot. You will find it at
    │   https://t.me/Antigravity_APO_Bot
    │   Use this token to access the HTTP API:
    │   8524726075:AAE2LB7rshE4hMyBrA5WjGFJvErZ2ml92mE"
    │
    └─ 📋 SAVE THIS TOKEN (used in config.py)

    ✅ PHASE 1 COMPLETE
    ════════════════════════════════════════════════════════════════════
    """

    PHASE_2_CONFIG = """
    ╔════════════════════════════════════════════════════════════════════╗
    ║                    PHASE 2: CONFIGURATION SETUP                    ║
    ╚════════════════════════════════════════════════════════════════════╝

    STEP 1: Update autonomous_operator/config.py

    Location:
    /Users/andy/my_too_test/autonomous_operator/config.py

    Find:
    ────────────────────────────────────────────────────────────────────
    # API Keys & Secrets
    TELEGRAM_BOT_TOKEN = "YOUR_TOKEN_HERE"
    ────────────────────────────────────────────────────────────────────

    Replace with:
    ────────────────────────────────────────────────────────────────────
    TELEGRAM_BOT_TOKEN = "8524726075:AAE2LB7rshE4hMyBrA5WjGFJvErZ2ml92mE"
    ────────────────────────────────────────────────────────────────────

    STEP 2: Verify Whitelist

    File: factory/telegram_bot.py

    Find:
    ────────────────────────────────────────────────────────────────────
    WHITELIST = [400752198]  # Master's ID
    ────────────────────────────────────────────────────────────────────

    ✅ YOUR USER ID (400752198) is already in whitelist

    STEP 3: Environment Variables (Optional)

    For production, use environment variables:

    export TELEGRAM_BOT_TOKEN="8524726075:AAE2LB7rshE4hMyBrA5WjGFJvErZ2ml92mE"
    export MASTER_USER_ID="400752198"

    Then in config.py:

    import os
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "...")
    MASTER_USER_ID = int(os.getenv("MASTER_USER_ID", "400752198"))

    ✅ PHASE 2 COMPLETE
    ════════════════════════════════════════════════════════════════════
    """

    PHASE_3_VERIFICATION = """
    ╔════════════════════════════════════════════════════════════════════╗
    ║                 PHASE 3: PRE-DEPLOYMENT VERIFICATION               ║
    ╚════════════════════════════════════════════════════════════════════╝

    CHECKLIST:

    File System:
    ☐ /Users/andy/my_too_test/factory/inbox/          ← Directory exists
    ☐ /Users/andy/my_too_test/factory/logs/           ← Directory exists
    ☐ /Users/andy/my_too_test/factory/tools/          ← At least 1 skill
    ☐ /Users/andy/my_too_test/autonomous_operator/
      config.py                                         ← Token updated

    Services:
    ☐ BalanceHub API running: http://localhost:8000
    ☐ PostgreSQL running: localhost:5432
    ☐ Redis running: localhost:6379

    Python Dependencies:
    ☐ python-telegram-bot (installed)
    ☐ google-generativeai (for Gemini)
    ☐ requests (HTTP calls)
    ☐ fastapi, sqlalchemy (for BalanceHub)

    Install missing:
    pip install python-telegram-bot google-generativeai requests fastapi

    Gemini API:
    ☐ Google Generative AI key available
    ☐ Key manager can access ~/.config/google/
      (or set via GeminiKeyManager.get_active_key())

    ✅ PHASE 3 COMPLETE (All checks passing)
    ════════════════════════════════════════════════════════════════════
    """

    PHASE_4_START = """
    ╔════════════════════════════════════════════════════════════════════╗
    ║                    PHASE 4: START SERVICES                         ║
    ╚════════════════════════════════════════════════════════════════════╝

    TERMINAL 1: Start Factory Worker Kernel

    cd /Users/andy/my_too_test
    python factory/factory_worker.py

    Expected output:
    ────────────────────────────────────────────────────────────────────
    2026-03-05 ... [INFO] - FactoryWorkerNode - 🤖 Minimal Factory Worker
    Initialized. Polling...
    2026-03-05 ... [INFO] - FactoryWorkerNode - 📥 Found new task: ...
    ────────────────────────────────────────────────────────────────────

    ✅ Factory Worker is polling factory/inbox/ every 2 seconds


    TERMINAL 2: Start Telegram Bot (Governance Interface)

    cd /Users/andy/my_too_test
    python factory/telegram_bot.py

    Expected output:
    ────────────────────────────────────────────────────────────────────
    2026-03-05 ... [INFO] - TeleControlBot - 🚀 Telegram Control App
    Started. Polling updates...
    2026-03-05 ... [INFO] - TeleControlBot - 📥 Message from 400752198:
    /sys status
    ────────────────────────────────────────────────────────────────────

    ✅ Telegram Bot is listening for commands


    TERMINAL 3 (Optional): Monitor Logs

    tail -f /Users/andy/my_too_test/factory/logs/orchestrator.log

    This shows real-time execution logs and drift detection.

    ✅ PHASE 4 COMPLETE (All services running)
    ════════════════════════════════════════════════════════════════════
    """

    PHASE_5_TEST = """
    ╔════════════════════════════════════════════════════════════════════╗
    ║                    PHASE 5: END-TO-END TESTING                     ║
    ╚════════════════════════════════════════════════════════════════════╝

    TEST 1: Bot Status Check
    ────────────────────────────────────────────────────────────────────
    In Telegram, send to @Antigravity_APO_Bot:

    /sys status

    Expected response:
    ────────────────────────────────────────────────────────────────────
    🤖 **Σ_APΩ Status:** Nominal. Antigravity Layer Active.
    ────────────────────────────────────────────────────────────────────

    ✅ Bot is responding


    TEST 2: Runtime Status Query
    ────────────────────────────────────────────────────────────────────
    Send: /runtime status

    Expected response:
    ────────────────────────────────────────────────────────────────────
    🏢 **Antigravity Governance Core**
    State: `IDLE`
    Objective: `None`
    Strategy: `Result-First (Φ⁻¹)`
    ────────────────────────────────────────────────────────────────────

    ✅ Governance state machine is initialized


    TEST 3: Queue Status
    ────────────────────────────────────────────────────────────────────
    Send: /state queue

    Expected response:
    ────────────────────────────────────────────────────────────────────
    📊 **Queue Metrics:**
    Pending: `0`
    Processing: `0`
    Success Rate: `100%`
    ────────────────────────────────────────────────────────────────────

    ✅ Task injector and inbox are operational


    TEST 4: Simple Task Execution
    ────────────────────────────────────────────────────────────────────
    Send: /task inject hello_world

    Expected response:
    ────────────────────────────────────────────────────────────────────
    ✅ Task `hello_world` injected.
    ────────────────────────────────────────────────────────────────────

    In Terminal 1 (Factory Worker), you should see:
    ────────────────────────────────────────────────────────────────────
    📥 Found new task: tele_task_XXXXXXXXX.task
    ✅ Skill hello_world execution complete. Result: ...
    🗑️ Task tele_task_XXXXXXXXX.task completed and removed.
    ────────────────────────────────────────────────────────────────────

    ✅ Task execution (Inbox-First Rule) working


    TEST 5: Governance Loop (Full Cycle)
    ────────────────────────────────────────────────────────────────────
    Send: /runtime goal "test automated backup"

    Expected responses (sequence):
    ────────────────────────────────────────────────────────────────────
    📝 **Governance Objective Set:** `test automated backup`
    Loop starting in PLANNING state.

    🧠 **Governance State: PLANNING**
    Computing Φ⁻¹_valid path...

    [Plan synthesis from Gemini AI...]

    📥 **Governance State: EXECUTING**
    Injecting task series...

    [Tasks being executed...]

    🏢 **Antigravity Governance Core**
    State: `OBSERVING`
    Objective: `test automated backup`
    Strategy: `Result-First (Φ⁻¹)`

    [After 10-30 seconds...]

    ✅ **Governance State: COMPLETED**
    Target state verified. Loop returning to IDLE.
    ────────────────────────────────────────────────────────────────────

    ✅ Complete governance loop execution (PLANNING → EXECUTING → OBSERVING → COMPLETED)


    TEST 6: Drift Detection & Healing (Failure Scenario)
    ────────────────────────────────────────────────────────────────────
    Send: /runtime goal "intentional_failure_test"

    Factory Worker encounters non-existent skill:
    ────────────────────────────────────────────────────────────────────
    ❌ Skill intentional_failure_test not found.
    ────────────────────────────────────────────────────────────────────

    Bot detects ERROR in logs:
    ────────────────────────────────────────────────────────────────────
    ⚠️ **Governance State: DRIFT_DETECTED**
    Analyzing execution variance...

    🩹 **Governance State: HEALING**
    Synthesizing correction DAG...

    [Healing plan generated, attempting retry...]
    ────────────────────────────────────────────────────────────────────

    ✅ Drift detection and healing cycle working


    TEST 7: Log Monitoring
    ────────────────────────────────────────────────────────────────────
    Send: /monitor logs

    Expected response:
    ────────────────────────────────────────────────────────────────────
    📺 **Log Monitoring: ENABLED**
    ────────────────────────────────────────────────────────────────────

    Then each execution will stream logs to chat in real-time.

    Send again to disable:
    ────────────────────────────────────────────────────────────────────
    📺 **Log Monitoring: DISABLED**
    ────────────────────────────────────────────────────────────────────

    ✅ Real-time log streaming working


    TEST 8: Natural Language Chat (NLP Mode)
    ────────────────────────────────────────────────────────────────────
    Send (without /command): "what is my system status"

    Bot routes to Gemini AI:
    ────────────────────────────────────────────────────────────────────
    Your system is healthy and operational. The Σ_APΩ runtime is active
    with Antigravity governance layer enabled. No drift detected...
    ────────────────────────────────────────────────────────────────────

    ✅ Natural language interface working


    ✅ PHASE 5 COMPLETE (All tests passing)
    ════════════════════════════════════════════════════════════════════
    """

    PHASE_6_PRODUCTION = """
    ╔════════════════════════════════════════════════════════════════════╗
    ║                    PHASE 6: PRODUCTION DEPLOYMENT                  ║
    ╚════════════════════════════════════════════════════════════════════╝

    FOR CONTINUOUS OPERATION:

    Option 1: SystemD Service (Linux/macOS)
    ────────────────────────────────────────────────────────────────────
    Create: /etc/systemd/system/apo-factory-worker.service

    [Unit]
    Description=APΩ Factory Worker Kernel
    After=network.target

    [Service]
    Type=simple
    User=andy
    WorkingDirectory=/Users/andy/my_too_test
    ExecStart=/usr/bin/python3 factory/factory_worker.py
    Restart=always
    RestartSec=10

    [Install]
    WantedBy=multi-user.target

    Then:
    sudo systemctl enable apo-factory-worker
    sudo systemctl start apo-factory-worker


    Option 2: Process Manager (supervisor, pm2)
    ────────────────────────────────────────────────────────────────────
    Using pm2:

    pm2 start factory/factory_worker.py --name "apo-factory"
    pm2 start factory/telegram_bot.py --name "apo-telegram"
    pm2 save
    pm2 startup


    Option 3: Docker Container
    ────────────────────────────────────────────────────────────────────
    FROM python:3.11-slim

    WORKDIR /app
    COPY factory/requirements.txt .
    RUN pip install -r requirements.txt
    COPY factory/ .

    CMD ["python", "telegram_bot.py"]

    Build & run:
    docker build -t apo-telegram-bot .
    docker run -d --name apo-bot -v /data:/app/logs apo-telegram-bot


    MONITORING IN PRODUCTION:

    ☐ Set up log aggregation (ELK, CloudWatch)
    ☐ Configure alerts on ERROR/DRIFT in logs
    ☐ Monitor factory/inbox/ for stuck tasks
    ☐ Track response time of /runtime commands
    ☐ Set up health check endpoint:
       - /health → {"status": "ok", "uptime": "23h 45m"}
    ☐ Backup PostgreSQL audit logs regularly
    ☐ Rotate logs (logs/orchestrator.log gets large)


    BACKUP STRATEGY:

    Daily: backup autonomous_operator/state/
    Weekly: backup balancehub PostgreSQL data
    On-demand: manual checkpoint via /runtime status


    SECURITY IN PRODUCTION:

    ☐ Store tokens in environment variables (not config.py)
    ☐ Use VPN/firewall for BalanceHub API access
    ☐ Enable HTTPS for bot communication
    ☐ Rotate Telegram token periodically
    ☐ Audit log access (who ran what command)
    ☐ Rate limit commands (10 per minute per user)
    ☐ Whitelist updates (add/remove users dynamically)

    Example token rotation:
    1. Go to BotFather
    2. Send: /mybots → select bot → API Token
    3. New token generated
    4. Update config.py + restart bot

    ✅ PHASE 6 COMPLETE (Production deployment ready)
    ════════════════════════════════════════════════════════════════════
    """

    TROUBLESHOOTING = """
    ╔════════════════════════════════════════════════════════════════════╗
    ║                         TROUBLESHOOTING                            ║
    ╚════════════════════════════════════════════════════════════════════╝

    ISSUE: "Bot not responding to commands"
    ────────────────────────────────────────────────────────────────────
    Check:
    ✓ Token is correct in config.py
    ✓ telegram_bot.py is running (check Terminal 2)
    ✓ User ID (400752198) is in WHITELIST
    ✓ Internet connection is active
    ✓ Telegram API not rate-limited

    Fix:
    1. Verify token: curl https://api.telegram.org/bot<TOKEN>/getMe
    2. Check logs: tail -f factory/logs/orchestrator.log
    3. Restart bot: Ctrl+C then run again


    ISSUE: "Tasks not executing (factory/inbox/ empty but no execution)"
    ────────────────────────────────────────────────────────────────────
    Check:
    ✓ factory_worker.py is running (check Terminal 1)
    ✓ factory/tools/ has the skill file
    ✓ Skill name in .task matches filename (without .py)
    ✓ No Python syntax errors in skill

    Fix:
    1. Manually test skill: python factory/tools/hello_world.py
    2. Check factory_worker.py logs
    3. Restart worker


    ISSUE: "Gemini planning not working"
    ────────────────────────────────────────────────────────────────────
    Check:
    ✓ Gemini API key available (from key_manager)
    ✓ GeminiKeyManager can read from ~/.config/google/
    ✓ google-generativeai installed: pip list | grep generativeai
    ✓ Internet connectivity for API calls

    Fix:
    1. Test Gemini directly: python -c "import google.generativeai as genai; ..."
    2. Check key_manager.py for correct path
    3. Ensure GEMINI_API_KEY environment variable set


    ISSUE: "BalanceHub API not responding"
    ────────────────────────────────────────────────────────────────────
    Check:
    ✓ BalanceHub running: curl http://localhost:8000/
    ✓ PostgreSQL running: psql -U hub -d balancehub
    ✓ Redis running: redis-cli ping
    ✓ Port 8000 not blocked by firewall

    Fix:
    1. Restart BalanceHub: cd balancehub && docker-compose up
    2. Check database: psql -U hub -d balancehub -c "SELECT * FROM connector_state;"
    3. Check logs: docker-compose logs balancehub-api


    ISSUE: "Logs not streaming / /monitor logs shows nothing"
    ────────────────────────────────────────────────────────────────────
    Check:
    ✓ logs/orchestrator.log exists
    ✓ log_streamer.py can read file permissions
    ✓ Tasks are executing (should generate logs)
    ✓ LogStreamer.tail() not reaching EOF

    Fix:
    1. Manually check: cat factory/logs/orchestrator.log | tail -20
    2. Ensure factory_worker.py is writing logs
    3. Check file permissions: chmod 644 factory/logs/orchestrator.log


    ISSUE: "Drift detected every execution (false positives)"
    ────────────────────────────────────────────────────────────────────
    Check:
    ✓ Skill output format (should not contain ERROR unless actual error)
    ✓ Log parsing logic (factory_worker.py logging)
    ✓ Threshold for drift detection (in log_streamer.py)

    Fix:
    1. Review skill output: python factory/tools/hello_world.py
    2. Update log format to be more explicit
    3. Adjust detect_drift() logic in gemini_planner_bridge.py


    ISSUE: "Governance loop stuck in EXECUTING state"
    ────────────────────────────────────────────────────────────────────
    Check:
    ✓ Task actually executed (check logs)
    ✓ Log contains SUCCESS or COMPLETED keyword
    ✓ State transition timeout (10s per phase)

    Fix:
    1. Send /runtime stop to halt loop
    2. Check logs for actual task result
    3. Manually set goal with clear completion criteria
    4. Restart loop with /runtime start


    ISSUE: "Unauthorized user trying to access bot"
    ────────────────────────────────────────────────────────────────────
    This is EXPECTED behavior - security feature working ✅

    Response to unauthorized user: 🚫 Access Denied. Your ID: `XXXX`

    To add new authorized user:
    1. Get their user ID
    2. Update WHITELIST in factory/telegram_bot.py:
       WHITELIST = [400752198, NEW_USER_ID]
    3. Restart telegram_bot.py


    ════════════════════════════════════════════════════════════════════
    """

    @staticmethod
    def print_all():
        """Print all provisioning phases"""
        print(TelegramBotProvisioning.PHASE_1_BOTFATHER)
        print(TelegramBotProvisioning.PHASE_2_CONFIG)
        print(TelegramBotProvisioning.PHASE_3_VERIFICATION)
        print(TelegramBotProvisioning.PHASE_4_START)
        print(TelegramBotProvisioning.PHASE_5_TEST)
        print(TelegramBotProvisioning.PHASE_6_PRODUCTION)
        print(TelegramBotProvisioning.TROUBLESHOOTING)

if __name__ == "__main__":
    TelegramBotProvisioning.print_all()
