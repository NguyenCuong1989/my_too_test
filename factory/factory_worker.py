import os
import time
import json
import re
import importlib.util
import logging
import signal
import sys
import shutil
import hashlib
from pathlib import Path
from typing import Dict, Any
from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from jsonschema import validate, ValidationError
from jose import jwt, JWTError

# Import local config
import config

# --- Structured Logging ---
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "module": "%(name)s", "message": "%(message)s"}'
)
logger = logging.getLogger("ACE_WORKER")

app = FastAPI(title="ACE Factory Worker Node")

# --- Security & State ---
circuit_breaker: Dict[str, int] = {}
is_running = True

def signal_handler(sig, frame):
    global is_running
    logger.info("Graceful shutdown initiated...")
    is_running = False
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# --- Helper Functions ---
def verify_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, config.JWT_SECRET, algorithms=["HS256"])
        return payload
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid or expired token")

def safe_execute_skill(skill_name: str, parameters: Dict[str, Any]) -> Any:
    # 1. Validation
    if skill_name not in config.WHITELISTED_SKILLS:
        raise ValueError(f"Skill '{skill_name}' is not whitelisted")

    if not re.match(r"^[a-zA-Z0-9_]+$", skill_name):
        raise ValueError(f"Invalid skill name format: {skill_name}")

    # 2. Circuit Breaker Check
    if circuit_breaker.get(skill_name, 0) >= config.CIRCUIT_BREAKER_THRESHOLD:
        raise RuntimeError(f"Circuit breaker active for skill: {skill_name}")

    # 3. Hash Integrity Check
    skill_path = Path(config.TOOLS_DIR) / f"{skill_name}.py"
    if not skill_path.exists():
        raise FileNotFoundError(f"Skill file not found: {skill_path}")

    expected_hash = config.SKILL_REGISTRY.get(skill_name)
    if not expected_hash:
        raise ValueError(f"Skill '{skill_name}' not found in integrity registry")

    sha256_hash = hashlib.sha256()
    with open(skill_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    actual_hash = sha256_hash.hexdigest()
    if actual_hash != expected_hash:
        logger.error(f"INTEGRITY FAILURE: Skill {skill_name} hash mismatch!")
        logger.error(f"Expected: {expected_hash}")
        logger.error(f"Actual:   {actual_hash}")
        raise RuntimeError(f"Integrity violation detected for skill: {skill_name}")

    # 4. Resource Governance (Tasks per hour check)
    # Simple bucket check for MVP
    current_hour = int(time.time() / 3600)
    hour_key = f"tasks_{current_hour}"
    tasks_this_hour = circuit_breaker.get(hour_key, 0)
    if tasks_this_hour >= config.MAX_TASKS_PER_HOUR:
        raise RuntimeError(f"Global task limit reached for this hour ({config.MAX_TASKS_PER_HOUR})")
    circuit_breaker[hour_key] = tasks_this_hour + 1

    # 5. Dynamic Import & Isolation

    try:
        spec = importlib.util.spec_from_file_location(skill_name, str(skill_path))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "run"):
            start_time = time.time()
            result = module.run(parameters)
            duration = time.time() - start_time
            logger.info(f"Skill {skill_name} executed in {duration:.2f}s")

            # Clear from sys.modules to ensure fresh import next time (Isolation)
            if skill_name in sys.modules:
                del sys.modules[skill_name]

            return result
        else:
            raise AttributeError(f"Skill '{skill_name}' lacks a 'run' function")
    except Exception as e:
        circuit_breaker[skill_name] = circuit_breaker.get(skill_name, 0) + 1
        logger.error(f"Execution failed for {skill_name}: {str(e)}")
        raise e

# --- REST API Endpoints ---
class TaskRequest(BaseModel):
    skill_name: str
    task_id: str
    parameters: Dict[str, Any]

@app.get("/health")
def health_check():
    return {"status": "ok", "timestamp": time.time()}

@app.get("/stats")
def get_stats(user=Depends(verify_token)):
    return {
        "circuit_breaker": circuit_breaker,
        "whitelisted_skills": config.WHITELISTED_SKILLS,
        "is_running": is_running
    }

@app.post("/tasks/execute")
def execute_task(task: TaskRequest, user=Depends(verify_token)):
    try:
        result = safe_execute_skill(task.skill_name, task.parameters)
        return {"task_id": task.task_id, "status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- Background Inbox Loop ---
def process_inbox():
    logger.info("Inbox poller started...")
    try:
        with open(config.SCHEMA_PATH, "r") as f:
            schema = json.load(f)
    except Exception as e:
        logger.error(f"Failed to load schema: {e}")
        return

    while is_running:
        try:
            inbox_path = Path(config.INBOX_DIR)
            for task_file in inbox_path.glob("*.task"):
                logger.info(f"Processing inbox task: {task_file.name}")

                try:
                    with open(task_file, "r") as f:
                        data = json.load(f)

                    # Schema Validation
                    from jsonschema import validate
                    validate(instance=data, schema=schema)

                    # Atomic State Move: Inbox -> Processing
                    processing_file = Path(config.PROCESSING_DIR) / task_file.name
                    shutil.move(str(task_file), str(processing_file))
                    logger.info(f"Task moved to processing: {task_file.name}")

                    # Execution from processing
                    skill_name = data["skill_name"]
                    parameters = data["parameters"]

                    safe_execute_skill(skill_name, parameters)

                    # Success: Move to processed
                    shutil.move(str(processing_file), str(Path(config.PROCESSED_DIR) / task_file.name))
                    logger.info(f"Task {task_file.name} moved to processed")

                except Exception as e:
                    logger.error(f"Error processing {task_file.name}: {e}")
                    shutil.move(str(task_file), str(Path(config.FAILED_DIR) / task_file.name))

            time.sleep(config.SLEEP_INTERVAL)
        except Exception as e:
            logger.error(f"Critical error in inbox loop: {e}")
            time.sleep(5)

if __name__ == "__main__":
    import uvicorn
    import threading

    # Run inbox poller in background thread
    t = threading.Thread(target=process_inbox, daemon=True)
    t.start()

    uvicorn.run(app, host="0.0.0.0", port=8181)
