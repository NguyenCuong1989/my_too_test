#!/usr/bin/env python3
"""
Command Router for Telegram Control App
Parses commands and validates against security rules.
"""

import logging
import re
from typing import Optional, Dict, List, Any

logger = logging.getLogger("CommandRouter")

class CommandRouter:
    def __init__(self, whitelist: List[int]):
        self.whitelist = whitelist
        # Governance & Monitoring Patterns
        self.patterns = {
            "goal": r"^/goal\s+(.+)$",
            "plan": r"^/plan\s+(.+)$",
            "runtime": r"^/runtime\s+(goal\s+.+|start|stop|status|heal)$",
            "monitor": r"^/monitor\s+(logs|tasks|workers)$",
            "state": r"^/state\s+(runtime|workers|queue|logs)$",
            "dag": r"^/dag\s+(show|run)$",
            "sys_status": r"^/sys status$",
            "log_tail": r"^/log tail(?:\s+(\d+))?$",
            "task_inject": r"^/task inject\s+(\S+)(?:\s+(.+))?$",
            "task_run": r"^/task run\s+(\S+)(?:\s+(.+))?$"
        }

    def is_authorized(self, user_id: int) -> bool:
        return user_id in self.whitelist

    def route(self, user_id: int, text: str) -> Dict[str, Any]:
        """
        Routes the command text to a category and extracts arguments.
        Returns: {"category": "...", "args": [...], "valid": True/False}
        """
        if not self.is_authorized(user_id):
            logger.warning(f"🚫 Unauthorized access attempt by user_id: {user_id}")
            return {"valid": False, "reason": "unauthorized"}

        text = text.strip()
        for category, pattern in self.patterns.items():
            match = re.match(pattern, text)
            if match:
                return {
                    "valid": True,
                    "category": category,
                    "args": match.groups(),
                    "text": text
                }

        # If it doesn't match any /command, treat it as natural language for AI Planner
        return {
            "valid": True,
            "category": "ai_chat",
            "args": (text,),
            "text": text
        }

if __name__ == "__main__":
    router = CommandRouter(whitelist=[123456])
    print(router.route(123456, "/task inject hello_world {\"key\": \"val\"}"))
    print(router.route(123456, "plan a deploy"))
    print(router.route(999, "/sys status"))
