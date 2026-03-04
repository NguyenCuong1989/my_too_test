import sqlite3
import unittest
import shutil
import tempfile
import os
from pathlib import Path
from autonomous_operator.neural_link import NeuralLink

class TestCanonLy(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.db_path = Path(self.test_dir) / "test_todo.db"
        self.link = NeuralLink()
        self.link.db_path = self.db_path
        self.link._init_neural_tables()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_canon_ly_no_log_no_progress(self):
        """
        CANON: LY (HỎA) — CHỨNG.
        No log = No progress. Proof is mandatory.
        If the system fails to write the audit log, the state mutation MUST rollback.
        """
        # 1. Setup initial state: a pending task
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                title TEXT,
                status TEXT,
                hash TEXT,
                created_at TEXT,
                updated_at TEXT
            )
        """)
        cursor.execute("""
            INSERT INTO tasks (id, title, status, hash, created_at, updated_at)
            VALUES ('task_1', 'Proof of Concept Task', 'pending', 'hash1', 'now', 'now')
        """)
        conn.commit()

        # 2. Add an environmental fault that absolutely prevents logging
        cursor.execute("""
            CREATE TRIGGER force_log_failure BEFORE INSERT ON service_governance_logs
            BEGIN
                SELECT RAISE(ABORT, 'Simulated audit log write failure');
            END;
        """)
        conn.commit()
        conn.close()

        # 3. Execution: Attempt to complete the task with an audit log
        try:
            self.link.complete_task_with_audit('task_1', log_message="I have completed the task")
        except Exception:
            pass # Expected to catch the trigger failure

        # 4. Proof: State must not change!
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM tasks WHERE id = 'task_1'")
        status = cursor.fetchone()[0]
        conn.close()

        self.assertEqual(status, 'pending', "ARCHITECTURAL RULE VIOLATED (LY): Task mutated state without successfully generating an audit log!")

if __name__ == '__main__':
    unittest.main()
