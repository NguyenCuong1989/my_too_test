# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

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

# Path to existing DAIOF DB (Migrated to /tmp due to disk pressure)
DAIOF_DB = Path("/tmp/daiof_data/databases_v2/autonomous_todo.db")

class NeuralLink:
    """Cầu nối thần kinh giữa Autonomous Operator và DAIOF-Framework + Notion Sync"""
    def __init__(self):
        self.logger = logging.getLogger("NeuralLink")
        self.db_path = DAIOF_DB
        # Ensure directory exists
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.notion = None
        self.notion_db_id = None
        self._init_neural_tables()
        self._init_notion()

    def _init_notion(self):
        try:
            from config import NOTION_TOKEN, NOTION_DB_ID
            from notion_client import Client
            if NOTION_TOKEN and NOTION_DB_ID:
                self.notion = Client(auth=NOTION_TOKEN)
                self.notion_db_id = NOTION_DB_ID
                self.logger.info("🏛️ NeuralLink: Universal Notion Sync Enabled.")
            else:
                self.logger.warning("⚠️ Notion Token/DB ID missing. Universal sync disabled.")
        except Exception as e:
            self.logger.error(f"Failed to init Notion inside NeuralLink: {e}")

    def _sync_to_notion(self, event_type, service, content, priority="Medium"):
        if not self.notion or not self.notion_db_id:
            return
        try:
            self.notion.pages.create(
                parent={"database_id": self.notion_db_id},
                properties={
                    "Command Name": {"title": [{"text": {"content": f"[{service}] {event_type}"}}]},
                    "Status": {"select": {"name": "Log"}},
                    "Target": {"select": {"name": "NotionDB"}},
                    "Arguments": {"rich_text": [{"text": {"content": content[:1500]}}]}
                }
            )
        except Exception as e:
            # Silently fail or log to local to prevent infinite loops
            self.logger.debug(f"Notion Sync soft-fail: {e}")

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
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS agent_discourse (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    source_node TEXT NOT NULL,
                    discourse_type TEXT NOT NULL,
                    content TEXT NOT NULL,
                    reasoning TEXT,
                    status TEXT DEFAULT 'open', -- open, committed, archived
                    timestamp TEXT NOT NULL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS service_governance_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    service_name TEXT NOT NULL,
                    event_type TEXT NOT NULL, -- SLA_BREACH, TASK_HANDOVER, CAPABILITY_EXEC, STATUS
                    content TEXT NOT NULL,
                    metadata TEXT, -- JSON metadata
                    timestamp TEXT NOT NULL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS node_capabilities (
                    service_name TEXT PRIMARY KEY,
                    capabilities TEXT NOT NULL, -- Comma separated list
                    sla_standard TEXT,
                    last_audit TEXT
                )
            """)
            # Initialize default capabilities
            cursor.execute("INSERT OR IGNORE INTO node_capabilities VALUES ('BizService', 'OAUTH_GMAIL,NOTION_SYNC,REASONING_LEAD', '99.9% Up-time', ?)", (datetime.now().isoformat(),))
            cursor.execute("INSERT OR IGNORE INTO node_capabilities VALUES ('WebScoutService', 'DYNAMIC_SCRAPING,EVALUATION_STATIC,ADAPTIVE_PROXY', '99.5% Success Rate', ?)", (datetime.now().isoformat(),))
            cursor.execute("INSERT OR IGNORE INTO node_capabilities VALUES ('GuardianService', 'CODE_AUDIT,RESOURCE_WATCHDOG,SECURITY_RECOVERY', 'Real-time Monitoring', ?)", (datetime.now().isoformat(),))

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

            # Optional: Sync critical pulses to Notion
            if intensity >= 1.0:
                self._sync_to_notion(f"Pulse: {pulse_type}", node_name, content)

        except Exception as e:
            self.logger.error(f"Failed to send neural pulse: {e}")

    def add_discourse(self, session_id: str, node: str, d_type: str, content: str, reasoning: str = ""):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO agent_discourse (session_id, source_node, discourse_type, content, reasoning, timestamp)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (session_id, node, d_type, content, reasoning, datetime.now().isoformat()))
            conn.commit()
            conn.close()
            self.logger.info(f"🎙️ Discourse added to session {session_id} by {node}")
        except Exception as e:
            self.logger.error(f"Failed to add discourse: {e}")

    def get_active_discourse(self, session_id: str = None):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            if session_id:
                cursor.execute("SELECT * FROM agent_discourse WHERE session_id = ? ORDER BY timestamp ASC", (session_id,))
            else:
                cursor.execute("SELECT * FROM agent_discourse WHERE status = 'open' ORDER BY timestamp ASC")

            rows = cursor.fetchall()
            conn.close()
            return rows
        except Exception as e:
            self.logger.error(f"Failed to fetch discourse: {e}")
            return []

    def commit_discourse(self, session_id: str):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("UPDATE agent_discourse SET status = 'committed' WHERE session_id = ?", (session_id,))
            conn.commit()
            conn.close()
            self.logger.info(f"⚖️ Discourse session {session_id} COMMITTED.")
        except Exception as e:
            self.logger.error(f"Failed to commit discourse: {e}")

    def log_service_event(self, service: str, e_type: str, content: str, meta: str = "{}"):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO service_governance_logs (service_name, event_type, content, metadata, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (service, e_type, content, meta, datetime.now().isoformat()))
            conn.commit()
            conn.close()
            self.logger.info(f"🏢 [SaaS Event] {service}: {e_type}")

            # 🌐 Sync to Notion (Universal Integration)
            self._sync_to_notion(e_type, service, content)

        except Exception as e:
            self.logger.error(f"Failed to log service event: {e}")

    def check_capability(self, service: str, required_capability: str) -> bool:
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT capabilities FROM node_capabilities WHERE service_name = ?", (service,))
            row = cursor.fetchone()
            conn.close()
            if row:
                caps = [c.strip() for c in row[0].split(',')]
                return required_capability in caps
            return False
        except Exception as e:
            self.logger.error(f"Failed to check capability: {e}")
            return False

    def get_service_logs(self, limit: int = 20):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM service_governance_logs ORDER BY timestamp DESC LIMIT ?", (limit,))
            rows = cursor.fetchall()
            conn.close()
            return rows
        except Exception as e:
            self.logger.error(f"Failed to fetch service logs: {e}")
            return []

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

    def complete_task_with_audit(self, task_id: str, log_message: str):
        """
        Attempts to complete a task and write an audit log.
        *V2 FINAL - STRICT CANON LY COMPLIANCE*
        Transactions are atomic. If the audit log fails, the state MUST NOT mutate.
        """
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()

            # 1. Start explicit transaction
            cursor.execute("BEGIN TRANSACTION")

            # 2. Mutate State
            cursor.execute("UPDATE tasks SET status = 'completed' WHERE id = ?", (task_id,))

            # 3. Insert the Log (This MUST succeed for state to be saved)
            cursor.execute("""
                INSERT INTO service_governance_logs (service_name, event_type, content, timestamp)
                VALUES (?, ?, ?, ?)
            """, ('NeuralLink', 'TASK_COMPLETED', log_message, datetime.now().isoformat()))

            # 4. Commit ONLY if both succeed
            conn.commit()
            self.logger.info(f"⚖️ Task {task_id} COMPLETED with Proof.")
        except Exception as e:
            # 5. CANON LY: No log = No Progress
            conn.rollback()
            self.logger.error(f"🚨 Audit Governance Failure! Action reverted: {e}")
            raise e
        finally:
            conn.close()
