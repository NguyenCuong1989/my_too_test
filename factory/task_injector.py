#!/usr/bin/env python3
"""
Task Injector Utility
Safely creates .task files in the factory/inbox/ directory.
"""

import os
import json
import logging
import tempfile
from pathlib import Path

logger = logging.getLogger("TaskInjector")

class TaskInjector:
    def __init__(self, inbox_dir: str = "/Users/andy/my_too_test/factory/inbox"):
        self.inbox_dir = Path(inbox_dir)
        self.inbox_dir.mkdir(parents=True, exist_ok=True)

    def inject(self, skill_name: str, payload: any = "", task_id: str = None) -> Path:
        """
        Inject a task into the inbox.
        Returns the path to the created task file.
        """
        if not task_id:
            import time
            task_id = f"tele_task_{int(time.time())}"

        filename = f"{task_id}.task"
        temp_file = self.inbox_dir / f"{filename}.tmp"
        final_file = self.inbox_dir / filename

        # Prepare content: <skill_name>\n<payload>
        if not isinstance(payload, str):
            payload = json.dumps(payload)

        content = f"{skill_name}\n{payload}"

        try:
            with open(temp_file, "w", encoding="utf-8") as f:
                f.write(content)

            # Atomic rename
            temp_file.replace(final_file)
            logger.info(f"✅ Task {task_id} injected into inbox.")
            return final_file
        except Exception as e:
            logger.error(f"❌ Failed to inject task {task_id}: {e}")
            if temp_file.exists():
                temp_file.unlink()
            raise

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    injector = TaskInjector()
    injector.inject("hello_world_skill", {"message": "Test from TaskInjector"})
