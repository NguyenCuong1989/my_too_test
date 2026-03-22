import sqlite3
import json
import uuid
from datetime import datetime
from pathlib import Path

class PersistenceLayer:
    def __init__(self, db_path="/Users/andy/my_too_test/runtime.db"):
        self.db_path = db_path
        self._init_db()
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Section 38 - Database Schema
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS runtime_state (
            id TEXT PRIMARY KEY,
            runtime_id TEXT,
            cycle INTEGER,
            state_hash TEXT,
            state_json TEXT,
            created_at TIMESTAMP
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS runtime_plan (
            id TEXT PRIMARY KEY,
            runtime_id TEXT,
            cycle INTEGER,
            plan_hash TEXT,
            plan_json TEXT,
            created_at TIMESTAMP
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS task_execution (
            id TEXT PRIMARY KEY,
            plan_id TEXT,
            task_id TEXT,
            capability TEXT,
            skill TEXT,
            input_json TEXT,
            status TEXT,
            result_json TEXT,
            started_at TIMESTAMP,
            finished_at TIMESTAMP
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS capability_registry (
            capability_id TEXT PRIMARY KEY,
            skills TEXT,
            status TEXT,
            updated_at TIMESTAMP
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS artifact_store (
            artifact_id TEXT PRIMARY KEY,
            artifact_type TEXT,
            metadata TEXT,
            location TEXT,
            created_at TIMESTAMP
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS convergence_log (
            id TEXT PRIMARY KEY,
            runtime_id TEXT,
            cycle INTEGER,
            state_hash TEXT,
            plan_hash TEXT,
            goal_converged BOOLEAN,
            timestamp TIMESTAMP
        )""")

        conn.commit()
        conn.close()

    def save_state(self, runtime_id, cycle, state_hash, state):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO runtime_state VALUES (?, ?, ?, ?, ?, ?)",
            (str(uuid.uuid4()), runtime_id, cycle, state_hash, json.dumps(state), datetime.utcnow()))
        self.conn.commit()

    def save_plan(self, runtime_id, cycle, plan_hash, plan):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO runtime_plan VALUES (?, ?, ?, ?, ?, ?)",
            (str(uuid.uuid4()), runtime_id, cycle, plan_hash, json.dumps(plan), datetime.utcnow()))
        self.conn.commit()

    def save_task(self, plan_id, task):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO task_execution VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (str(uuid.uuid4()), plan_id, task["id"], task["capability"], task["skill"],
              json.dumps(task.get("input", {})), "completed", json.dumps(task.get("result", {})),
              datetime.utcnow(), datetime.utcnow()))
        self.conn.commit()

    def save_convergence(self, runtime_id, cycle, state_hash, plan_hash, converged):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO convergence_log VALUES (?, ?, ?, ?, ?, ?, ?)",
            (str(uuid.uuid4()), runtime_id, cycle, state_hash, plan_hash, converged, datetime.utcnow()))
        self.conn.commit()

class CheckpointManager:
    def __init__(self, persistence):
        self.persistence = persistence

    def checkpoint(self, runtime_id, cycle, state_hash, state):
        self.persistence.save_state(runtime_id, cycle, state_hash, state)

    def restore_latest(self):
        cursor = self.persistence.conn.cursor()
        cursor.execute("SELECT state_json FROM runtime_state ORDER BY created_at DESC LIMIT 1")
        row = cursor.fetchone()
        return json.loads(row["state_json"]) if row else None
