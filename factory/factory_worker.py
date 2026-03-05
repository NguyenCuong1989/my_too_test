#!/usr/bin/env python3
"""Minimal Deterministic Kernel Worker (Refactored)"""

import time
import logging
import importlib.util
from pathlib import Path
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s")
logger = logging.getLogger("FactoryWorkerNode")

BASE_DIR = Path(__file__).parent.resolve()
INBOX_DIR = BASE_DIR / "inbox"
TOOLS_DIR = BASE_DIR / "tools"
POLL_INTERVAL = 2

def execute_skill(skill_name, payload):
    skill_path = TOOLS_DIR / f"{skill_name}.py"
    if not skill_path.exists():
        logger.error(f"❌ Skill {skill_name} not found.")
        return
    try:
        spec = importlib.util.spec_from_file_location(skill_name, skill_path)
        skill_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(skill_module)
        result = skill_module.run(payload)
        logger.info(f"✅ Skill {skill_name} execution complete. Result: {result}")
    except Exception as e:
        logger.error(f"❌ Skill execution failed: {e}")

def autonomous_loop():
    logger.info("🤖 Minimal Factory Worker Initialized. Polling...")
    INBOX_DIR.mkdir(exist_ok=True)
    while True:
        try:
            tasks = sorted(INBOX_DIR.glob("*.task"), key=lambda p: p.stat().st_mtime)
            if tasks:
                task_file = tasks[0]
                with open(task_file, "r", encoding="utf-8") as f:
                    content = f.read().strip().split("\n", 1)
                skill_name = content[0].strip()
                payload = content[1] if len(content) > 1 else ""
                logger.info(f"📥 Found new task: {task_file.name}")
                execute_skill(skill_name, payload)
                task_file.unlink()
                logger.info(f"🗑️ Task {task_file.name} completed and removed.")
        except Exception as e:
            logger.error(f"Loop Error: {e}")
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    autonomous_loop()
