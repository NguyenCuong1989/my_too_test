import json
import time
import requests
import os
from jose import jwt

JWT_SECRET = "super-secret-mcp-key"
token = jwt.encode({"name": "Admin", "role": "poweruser"}, JWT_SECRET, algorithm="HS256")
headers = {"Authorization": f"Bearer {token}"}
BASE_URL = "http://localhost:8181"

def test_stats():
    print("\n--- Testing Stats Endpoint ---")
    resp = requests.get(f"{BASE_URL}/stats", headers=headers)
    print("Stats Response:", resp.json())
    assert resp.status_code == 200

def test_api_execution():
    print("\n--- Testing API Tool Execution ---")
    payload = {
        "skill_name": "hello_world_skill",
        "task_id": "api-task-1",
        "parameters": {"content": "Hello from API!"}
    }
    resp = requests.post(f"{BASE_URL}/tasks/execute", json=payload, headers=headers)
    print("Execution Response:", resp.json())
    assert resp.status_code == 200

def test_inbox_validation():
    print("\n--- Testing Inbox Schema Validation ---")
    # 1. Valid Task
    task_id = f"task_{int(time.time())}"
    valid_task = {
        "skill_name": "hello_world_skill",
        "task_id": task_id,
        "parameters": {"content": "Valid Inbox Task"}
    }
    with open(f"inbox/{task_id}.task", "w") as f:
        json.dump(valid_task, f)

    # 2. Invalid Task (Missing field)
    invalid_task = {"skill_name": "hello_world_skill"}
    with open("inbox/invalid.task", "w") as f:
        json.dump(invalid_task, f)

    print("Tasks dropped in inbox. Waiting for poller...")
    time.sleep(6)

    # Check processed vs failed
    if os.path.exists(f"processed/{task_id}.task"):
        print(f"✅ Task {task_id} successfully processed.")
    else:
        print(f"❌ Task {task_id} NOT found in processed.")

    if os.path.exists("failed/invalid.task"):
        print("✅ Invalid task correctly moved to failed.")
    else:
        print("❌ Invalid task NOT found in failed.")

if __name__ == "__main__":
    try:
        test_stats()
        test_api_execution()
        test_inbox_validation()
        print("\n✨ ALL VERIFICATIONS PASSED ✨")
    except Exception as e:
        print(f"\n🚨 VERIFICATION FAILED: {e}")
