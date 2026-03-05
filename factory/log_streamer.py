#!/usr/bin/env python3
"""
Log Streamer for Telegram Control App
Tails logs and provides filtered updates.
"""

import os
import time
import logging
from pathlib import Path
from typing import List, Generator

logger = logging.getLogger("LogStreamer")

class LogStreamer:
    def __init__(self, log_path: str = "/Users/andy/my_too_test/autonomous_operator/logs/orchestrator.log"):
        self.log_path = Path(log_path)

    def tail(self, n: int = 10) -> List[str]:
        """Returns the last n lines of the log file."""
        if not self.log_path.exists():
            return [f"⚠️ Log file not found at {self.log_path}"]

        try:
            with open(self.log_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                return [line.strip() for line in lines[-n:]]
        except Exception as e:
            logger.error(f"Error reading log: {e}")
            return [f"❌ Error reading log: {e}"]

    def follow(self) -> Generator[str, None, None]:
        """Generator that yields new lines as they are added to the log (like tail -f)."""
        if not self.log_path.exists():
            yield f"⚠️ Log file not found at {self.log_path}"
            return

        with open(self.log_path, "r", encoding="utf-8") as f:
            # Go to end of file
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(1)
                    continue
                yield line.strip()

if __name__ == "__main__":
    streamer = LogStreamer()
    print("\n".join(streamer.tail(5)))
