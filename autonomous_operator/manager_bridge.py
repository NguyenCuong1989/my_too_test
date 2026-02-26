import sqlite3
import argparse
import sys
import json
from pathlib import Path
from datetime import datetime

# Setup Paths
BASE_DIR = Path("/Users/andy/my_too_test")
DB_PATH = BASE_DIR / "DAIOF-Framework" / "autonomous_todo.db"

def get_summary():
    """Returns a summary of recent activity from the ecosystem."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # 1. Recent Pulses
        cursor.execute("SELECT node_name, pulse_type, content, timestamp FROM neural_pulses ORDER BY timestamp DESC LIMIT 5")
        pulses = cursor.fetchall()

        # 2. Task Status
        cursor.execute("SELECT status, COUNT(*) FROM tasks GROUP BY status")
        task_stats = cursor.fetchall()

        # 3. Pending Critical Tasks
        cursor.execute("SELECT title, priority FROM tasks WHERE status='pending' ORDER BY priority DESC LIMIT 3")
        pending_tasks = cursor.fetchall()

        conn.close()

        summary = {
            "recent_pulses": [{"node": p[0], "type": p[1], "content": p[2], "time": p[3]} for p in pulses],
            "task_stats": {status: count for status, count in task_stats},
            "pending_priority": [{"title": t[0], "priority": t[1]} for t in pending_tasks]
        }
        return summary
    except Exception as e:
        return {"error": str(e)}

def add_task(title, description, action, priority=1):
    """Adds a high-level task from Antigravity to the local queue."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        task_id = f"antigravity_{int(datetime.now().timestamp())}"
        task_hash = f"h_{hash(title + action)}"
        now = datetime.now().isoformat()

        cursor.execute("""
            INSERT OR IGNORE INTO tasks (
                id, title, description, action, priority, estimated_time,
                dependencies, created_at, updated_at, status, cycle_created,
                cycle_last_updated, hash
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            task_id, title, description, action, priority, 600,
            "[]", now, now, "pending", 0, 0, task_hash
        ))

        conn.commit()
        conn.close()
        return {"status": "success", "task_id": task_id}
    except Exception as e:
        return {"error": str(e)}

def add_batch_tasks(batch_data):
    """Adds multiple tasks in a single call to conserve cloud-local roundtrips."""
    results = []
    for task in batch_data:
        res = add_task(task['title'], task['description'], task['action'], task.get('priority', 1))
        results.append(res)
    return results

def get_routing_advice(prompt_summary):
    """
    Heuristics to decide if a task should go to Cloud or Local.
    This is for Antigravity's internal use when deciding how to delegate.
    """
    local_keywords = ["scan", "check", "list", "summarize email", "heartbeat"]
    cloud_keywords = ["architect", "complex bug", "web search", "creative", "strategy"]

    prompt_lower = prompt_summary.lower()

    if any(k in prompt_lower for k in cloud_keywords):
        return "CLOUD (Gemini)"
    if any(k in prompt_lower for k in local_keywords):
        return "LOCAL (Ollama/qwen3)"

    return "LOCAL (Default for safety/quota)"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Antigravity Manager Bridge for DAIOF ecosystem")
    parser.add_argument("--summary", action="store_true", help="Get ecosystem summary")
    parser.add_argument("--add-task", nargs=3, metavar=('TITLE', 'DESC', 'ACTION'), help="Add a new task")
    parser.add_argument("--batch", type=str, help="JSON string of multiple tasks")
    parser.add_argument("--route", type=str, help="Get routing advice for a task description")
    parser.add_argument("--priority", type=int, default=1, help="Priority for new task (default 1)")

    args = parser.parse_args()

    if args.summary:
        print(json.dumps(get_summary(), indent=2))
    elif args.add_task:
        result = add_task(args.add_task[0], args.add_task[1], args.add_task[2], args.priority)
        print(json.dumps(result, indent=2))
    elif args.batch:
        try:
            tasks = json.loads(args.batch)
            print(json.dumps(add_batch_tasks(tasks), indent=2))
        except Exception as e:
            print(json.dumps({"error": f"Invalid JSON batch: {e}"}))
    elif args.route:
        print(json.dumps({"advice": get_routing_advice(args.route)}))
    else:
        parser.print_help()
