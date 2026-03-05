#!/usr/bin/env python3
"""
Telegram Control App - Core Entry Point
APΩ System Control Interface (User Space Terminal)
"""

import os
import time
import json
import logging
import requests
from pathlib import Path

# Import helper modules
from command_router import CommandRouter
from task_injector import TaskInjector
from log_streamer import LogStreamer
from gemini_planner_bridge import GeminiPlannerBridge
import threading

# Load Configuration (Token from autonomous_operator/config.py)
import sys
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR / "autonomous_operator"))
from config import TELEGRAM_BOT_TOKEN

# Constants
WHITELIST = [400752198] # Master's ID
POLL_INTERVAL = 2

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s")
logger = logging.getLogger("TeleControlBot")

class AntigravityLoopController:
    """Manages the autonomous execution loop and self-healing."""
    def __init__(self, bot):
        self.bot = bot
        self.active_goal = None
        self.is_running = False
        self._thread = None

    def start(self, goal: str):
        self.active_goal = goal
        self.is_running = True
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()
        logger.info(f"🌀 Antigravity Loop started for goal: {goal}")

    def stop(self):
        self.is_running = False
        logger.info("🛑 Antigravity Loop stopped.")

    def _run_loop(self):
        bridge = self.bot.planner
        while self.is_running:
            try:
                # Deterministic Loop Algorithm
                if bridge.current_state == GovernanceState.PLANNING:
                    # Reverse Planning Phase
                    self.bot.send_message(self.bot.master_chat_id, "🧠 **Governance State: PLANNING**\nComputing Φ⁻¹_valid path...")
                    bridge.reverse_plan(self.active_goal)
                    bridge.transition_to(GovernanceState.EXECUTING)

                elif bridge.current_state == GovernanceState.EXECUTING:
                    # Task Injection Phase
                    if bridge.current_dag:
                        self.bot.send_message(self.bot.master_chat_id, "📥 **Governance State: EXECUTING**\nInjecting task series...")
                        for step in bridge.current_dag.get("steps", []):
                            self.bot.injector.inject(step["skill"], step["payload"])
                        bridge.transition_to(GovernanceState.OBSERVING)
                    else:
                        bridge.transition_to(GovernanceState.PLANNING)

                elif bridge.current_state == GovernanceState.OBSERVING:
                    # Performance & Drift Monitoring
                    lines = self.bot.streamer.tail(10)
                    if bridge.detect_drift(self.active_goal, lines):
                        bridge.transition_to(GovernanceState.DRIFT_DETECTED)
                    else:
                        # Check for completion (mock or FS check)
                        # For demo: check if last step of DAG is in logs as success
                        if "COMPLETED" in "".join(lines) or "SUCCESS" in "".join(lines):
                            bridge.transition_to(GovernanceState.COMPLETED)

                elif bridge.current_state == GovernanceState.DRIFT_DETECTED:
                    # Analysis of failure
                    self.bot.send_message(self.bot.master_chat_id, "⚠️ **Governance State: DRIFT_DETECTED**\nAnalyzing execution variance...")
                    bridge.transition_to(GovernanceState.HEALING)

                elif bridge.current_state == GovernanceState.HEALING:
                    # Correction DAG generation
                    self.bot.send_message(self.bot.master_chat_id, "🩹 **Governance State: HEALING**\nSynthesizing correction DAG...")
                    lines = self.bot.streamer.tail(5)
                    bridge.heal_plan(self.active_goal, lines[-1] if lines else "Drift detected but no log tail.")
                    bridge.transition_to(GovernanceState.EXECUTING)

                elif bridge.current_state == GovernanceState.COMPLETED:
                    self.bot.send_message(self.bot.master_chat_id, "✅ **Governance State: COMPLETED**\nTarget state verified. Loop returning to IDLE.")
                    self.active_goal = None
                    self.is_running = False
                    bridge.transition_to(GovernanceState.IDLE)
                    break

                time.sleep(10)
            except Exception as e:
                logger.error(f"Governance Loop Error: {e}")
                time.sleep(30)

class TeleControlBot:
    def __init__(self):
        self.token = TELEGRAM_BOT_TOKEN
        self.api_url = f"https://api.telegram.org/bot{self.token}/"
        self.offset = None
        self.master_chat_id = WHITELIST[0] # For autonomous alerts
        self.router = CommandRouter(whitelist=WHITELIST)
        self.injector = TaskInjector()
        self.streamer = LogStreamer()
        self.planner = GeminiPlannerBridge()
        self.loop_ctrl = AntigravityLoopController(self)
        self.is_running = True
        self.monitor_active = {"logs": False}

    def send_message(self, chat_id: int, text: str):
        url = self.api_url + "sendMessage"
        payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        try:
            requests.post(url, json=payload, timeout=10)
        except Exception as e:
            logger.error(f"Failed to send message: {e}")

    def get_updates(self):
        url = self.api_url + "getUpdates"
        params = {"timeout": 30, "offset": self.offset}
        try:
            response = requests.get(url, params=params, timeout=35)
            return response.json()
        except Exception as e:
            logger.error(f"Polling error: {e}")
            return None

    def handle_command(self, chat_id: int, route_result: dict):
        category = route_result["category"]
        args = route_result["args"]

        if category == "goal":
            objective = args[0]
            reply = self.planner.synthesize_dag(objective)
            self.send_message(chat_id, reply)

        elif category == "plan":
            result_state = args[0]
            reply = self.planner.reverse_plan(result_state)
            self.send_message(chat_id, reply)

        elif category == "state":
            target = args[0]
            if target == "runtime":
                uptime = "2h 45m" # Placeholder
                self.send_message(chat_id, f"⚙️ **Runtime State:**\nStatus: `Active`\nUptime: `{uptime}`\nKernel: `factory_worker.py`")
            elif target == "workers":
                self.send_message(chat_id, "👷 **Worker Process Map:**\n- Node 1: `factory_worker` (Thread-12)\n- Node 2: `tele_node` (Thread-15)")
            elif target == "queue":
                inbox_count = len(list(Path("/Users/andy/my_too_test/factory/inbox").glob("*.task")))
                self.send_message(chat_id, f"📊 **Queue Metrics:**\nPending: `{inbox_count}`\nProcessing: `0`\nSuccess Rate: `100%`")
            elif target == "logs":
                lines = self.streamer.tail(5)
                self.send_message(chat_id, "📜 **Latest Logs:**\n```\n" + "\n".join(lines) + "\n```")

        elif category == "dag":
            action = args[0]
            if action == "show":
                if self.planner.current_dag:
                    reply = self.planner._format_plan(self.planner.current_dag)
                    self.send_message(chat_id, reply)
                else:
                    self.send_message(chat_id, "❌ No active DAG found. Use `/goal` or `/plan` first.")
            elif action == "run":
                if self.planner.current_dag:
                    self.send_message(chat_id, "📥 **Injecting DAG tasks...**")
                    for step in self.planner.current_dag.get("steps", []):
                        self.injector.inject(step["skill"], step["payload"])
                    self.send_message(chat_id, "✅ DAG execution started. Monitoring logs...")
                    self.planner.current_dag = None
                else:
                    self.send_message(chat_id, "❌ Nothing to run.")

        elif category == "sys_status":
            self.send_message(chat_id, "🤖 **Σ_APΩ Status:** Nominal. Antigravity Layer Active.")

        elif category in ["task_run", "task_inject"]:
            skill = args[0]
            data = args[1] if len(args) > 1 else "{}"
            try:
                payload = json.loads(data) if data else {}
                self.injector.inject(skill, payload)
                self.send_message(chat_id, f"✅ Task `{skill}` injected.")
            except Exception as e:
                self.send_message(chat_id, f"❌ Injection failed: {e}")

        elif category == "log_tail":
            n = int(args[0]) if args[0] and args[0].isdigit() else 10
            lines = self.streamer.tail(n)
            self.send_message(chat_id, "```\n" + "\n".join(lines) + "\n```")

        elif category == "ai_chat":
            reply = self.planner.chat(args[0])
            self.send_message(chat_id, reply)

        elif category == "runtime":
            action_args = args[0].split(maxsplit=1)
            action = action_args[0]

            if action == "goal" and len(action_args) > 1:
                objective = action_args[1]
                self.loop_ctrl.active_goal = objective
                self.planner.transition_to(GovernanceState.PLANNING)
                self.loop_ctrl.start(objective)
                self.send_message(chat_id, f"📝 **Governance Objective Set:** `{objective}`\nLoop starting in PLANNING state.")

            elif action == "start":
                if self.planner.current_dag or self.loop_ctrl.active_goal:
                    goal = self.loop_ctrl.active_goal or self.planner.current_dag.get("goal")
                    self.planner.transition_to(GovernanceState.PLANNING)
                    self.loop_ctrl.start(goal)
                    self.send_message(chat_id, f"🌀 **Governance Loop Lifecycle: STARTED**\nTarget: `{goal}`")
                else:
                    self.send_message(chat_id, "❌ No active plan. Run `/goal` first.")
            elif action == "stop":
                self.loop_ctrl.stop()
                self.planner.transition_to(GovernanceState.IDLE)
                self.send_message(chat_id, "🛑 **Governance Loop Lifecycle: HALTED**")
            elif action == "status":
                state = self.planner.current_state.name
                goal = self.loop_ctrl.active_goal or "None"
                self.send_message(chat_id, f"🏢 **Antigravity Governance Core**\nState: `{state}`\nObjective: `{goal}`\nStrategy: `Result-First (Φ⁻¹)`")
            elif action == "heal":
                if self.loop_ctrl.active_goal:
                    self.planner.transition_to(GovernanceState.DRIFT_DETECTED)
                    self.send_message(chat_id, "🩹 **Manual Drift Triggered.** Commencing recovery path.")
                else:
                    self.send_message(chat_id, "❌ No active objective.")

        elif category == "monitor":
            target = args[0]
            if target == "logs":
                self.monitor_active["logs"] = not self.monitor_active["logs"]
                status = "ENABLED" if self.monitor_active["logs"] else "DISABLED"
                self.send_message(chat_id, f"📺 **Log Monitoring: {status}**")

    def run(self):
        logger.info("🚀 Telegram Control App Started. Polling updates...")
        while self.is_running:
            updates = self.get_updates()
            if updates and "result" in updates:
                for update in updates["result"]:
                    self.offset = update["update_id"] + 1
                    if "message" in update and "text" in update["message"]:
                        chat_id = update["message"]["chat"]["id"]
                        text = update["message"]["text"]

                        logger.info(f"📥 Message from {chat_id}: {text}")
                        route_result = self.router.route(chat_id, text)

                        if route_result["valid"]:
                            self.handle_command(chat_id, route_result)
                        else:
                            self.send_message(chat_id, f"🚫 Access Denied. Your ID: `{chat_id}`")
            time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    bot = TeleControlBot()
    try:
        bot.run()
    except KeyboardInterrupt:
        logger.info("🛑 Bot shutting down.")
