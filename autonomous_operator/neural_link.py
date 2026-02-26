import os
import logging
import sqlite3
import json
import sys
from datetime import datetime
from pathlib import Path

# Setup Path
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR / "autonomous_operator"))

try:
    from config import BASE_DIR as CONFIG_BASE_DIR
except ImportError:
    CONFIG_BASE_DIR = BASE_DIR

# Path to existing DAIOF DB
DAIOF_DB = CONFIG_BASE_DIR / "DAIOF-Framework" / "autonomous_todo.db"

class NeuralLink:
    """Cầu nối thần kinh giữa Autonomous Operator và DAIOF-Framework"""
    def __init__(self):
        self.logger = logging.getLogger("NeuralLink")
        self.db_path = DAIOF_DB
        self._init_neural_tables()

    def _init_neural_tables(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS neural_pulses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    node_name TEXT NOT NULL,
                    pulse_type TEXT NOT NULL,
                    content TEXT NOT NULL,
                    intensity REAL DEFAULT 1.0,
                    timestamp TEXT NOT NULL
                )
            """)
            conn.commit()
            conn.close()
        except Exception as e:
            self.logger.error(f"Neural Link init error: {e}")

    def send_pulse(self, node_name: str, pulse_type: str, content: str, intensity: float = 1.0):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO neural_pulses (node_name, pulse_type, content, intensity, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (node_name, pulse_type, content, intensity, datetime.now().isoformat()))
            conn.commit()
            conn.close()
            # self.logger.info(f"🧠 Pulse sent: [{node_name}] {pulse_type}")
        except Exception as e:
            self.logger.error(f"Failed to send neural pulse: {e}")

    def add_autonomous_task(self, title: str, description: str, action: str, priority: int = 1):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            task_id = f"linked_{int(datetime.now().timestamp())}"
            task_hash = f"h_{hash(title+action)}"
            now = datetime.now().isoformat()

            cursor.execute("""
                INSERT OR IGNORE INTO tasks (
                    id, title, description, action, priority, estimated_time,
                    dependencies, created_at, updated_at, status, cycle_created,
                    cycle_last_updated, hash
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                task_id, title, description, action, priority, 300,
                "[]", now, now, "pending", 0, 0, task_hash
            ))
            conn.commit()
            conn.close()
            self.logger.info(f"📋 Linked Task Created: {title}")
        except Exception as e:
            self.logger.error(f"Failed to link task: {e}")
