import os
import time
import json
import subprocess
import logging
import signal
import hashlib
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, Any
from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from jsonschema import validate, ValidationError
from jose import jwt, JWTError
import telegram_notifier
import telegram_bot

# Import local config
import config

# --- Structured Logging ---
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "module": "%(name)s", "message": "%(message)s"}'
)
logger = logging.getLogger("ACE_WORKER")

app = FastAPI(title="ACE Factory Worker Node")

@app.on_event("startup")
def startup_event():
    import threading
    t_inbox = threading.Thread(target=process_inbox, daemon=True)
    t_inbox.start()

    # Start Telegram Guardian Bot
    t_bot = threading.Thread(target=telegram_bot.bot_loop, daemon=True)
    t_bot.start()

    logger.info("Background inbox poller and Telegram Guardian threads started.")

# --- Security & State ---
circuit_breaker: Dict[str, int] = {}
is_running = True
task_counter = 0 # Initialize global task counter

def signal_handler(sig, frame):
    global is_running
    logger.info("Graceful shutdown initiated...")
    is_running = False
    # sys.exit(0) # Removed sys.exit(0) to allow background thread to finish if needed, though daemon=True handles it.

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

def get_audit_trail_hash():
    """Reads the last hash from the audit chain."""
    try:
        if os.path.exists(config.LAST_EXECUTION_HASH_PATH):
            with open(config.LAST_EXECUTION_HASH_PATH, "r") as f:
                return f.read().strip()
    except Exception as e:
        logger.error(f"Failed to read last audit hash: {e}")
    return "0" * 64 # Initial root

def update_audit_trail(last_hash, input_data, output_data):
    """Appends to the audit chain and updates the last hash."""
    try:
        timestamp = datetime.utcnow().isoformat() + "Z"
        input_hash = hashlib.sha256(json.dumps(input_data, sort_keys=True).encode()).hexdigest()
        output_hash = hashlib.sha256(str(output_data).encode()).hexdigest()

        new_hash = hashlib.sha256(f"{last_hash}{input_hash}{output_hash}{timestamp}".encode()).hexdigest()

        # Append to log
        audit_entry = {
            "timestamp": timestamp,
            "prev_hash": last_hash,
            "input_hash": input_hash,
            "output_hash": output_hash,
            "hash": new_hash
        }

        os.makedirs(os.path.dirname(config.AUDIT_LOG_PATH), exist_ok=True)
        with open(config.AUDIT_LOG_PATH, "a") as f:
            f.write(json.dumps(audit_entry) + "\n")

        with open(config.LAST_EXECUTION_HASH_PATH, "w") as f:
            f.write(new_hash)

        return new_hash
    except Exception as e:
        logger.error(f"Failed to update audit trail: {e}")
        return last_hash

def safe_execute_skill(skill_name: str, parameters: Dict[str, Any]) -> Any:
    """
    Spawns a subprocess to execute a skill in isolation with resource governance.
    PHASE XV: Infrastructure Hardening
    """
    global task_counter

    # 1. Validation
    if skill_name not in config.WHITELISTED_SKILLS:
        logger.error(f"Skill '{skill_name}' is not whitelisted")
        return {"status": "error", "message": f"Skill '{skill_name}' is not whitelisted"}

    # 2. Circuit Breaker Check (Skill-specific)
    if circuit_breaker.get(skill_name, 0) >= config.CIRCUIT_BREAKER_THRESHOLD:
        logger.error(f"Circuit breaker active for skill: {skill_name}")
        return {"status": "error", "message": f"Circuit breaker active for skill: {skill_name}"}

    # 3. Global Task Limit Check
    if task_counter >= config.MAX_TASKS_PER_HOUR:
        logger.error("MAX_TASKS_PER_HOUR reached. Global circuit breaker active.")
        return {"status": "error", "message": "Global circuit breaker triggered"}

    # 4. Resource Governance (Tasks per hour check - legacy, now global task_counter handles it)
    # The original bucket check for current_hour is now superseded by the global task_counter
    # and MAX_TASKS_PER_HOUR. Keeping the circuit_breaker for skill-specific failures.

    try:
        # 1. Load Metadata & Governance
        metadata_path = Path(config.METADATA_DIR) / f"{skill_name}.json"
        if not metadata_path.exists():
            logger.error(f"Missing metadata for skill: {skill_name}")
            return {"status": "error", "message": "Skill governance failure: No metadata"}

        with open(metadata_path, "r") as f:
            metadata = json.load(f)

        # 2. Verify Integrity Gate (SHA-256)
        skill_path = Path(config.TOOLS_DIR) / f"{skill_name}.py"
        if not skill_path.exists():
            logger.error(f"Skill file not found: {skill_path}")
            return {"status": "error", "message": f"Skill file not found: {skill_path}"}

        sha256_hash = hashlib.sha256()
        with open(skill_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        file_hash = sha256_hash.hexdigest()

        expected_hash = metadata["hash_seal"]["value"]
        if file_hash != expected_hash:
            error_msg = f"🛡️ *INTEGRITY BREACH:* Hash mismatch for skill `{skill_name}`!\nExpected: `{expected_hash}`\nGot: `{file_hash}`"
            logger.critical(error_msg)
            telegram_notifier.send_telegram_message(error_msg)
            return {"status": "error", "message": "Skill integrity check failed"}

        # 3. Subprocess Isolation Spawning
        logger.info(f"Spawning isolated execution for: {skill_name}")

        # Resource Limits from Metadata
        timeout = metadata["resource_limits"].get("timeout_seconds", 30)

        # Command execution
        # We pass parameters as a JSON string argument
        param_str = json.dumps(parameters)

        last_audit_hash = get_audit_trail_hash()

        start_time = time.time()
        result = subprocess.run(
            ["python3", str(skill_path), param_str],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        duration = time.time() - start_time

        # 4. Process Outcome
        if result.returncode != 0:
            logger.error(f"Skill {skill_name} failed with return code {result.returncode}")
            logger.error(f"Stderr: {result.stderr}")
            circuit_breaker[skill_name] = circuit_breaker.get(skill_name, 0) + 1
            return {"status": "error", "message": f"Execution error: {result.stderr}"}

        # 5. Update Audit Trail (Merkle-style chain)
        output_data = result.stdout.strip()
        new_audit_hash = update_audit_trail(last_audit_hash, parameters, output_data)

        logger.info(f"Skill {skill_name} executed successfully in {duration:.2f}s")
        logger.info(f"Audit Hash: {new_audit_hash}")

        task_counter += 1
        return {"status": "success", "data": output_data, "audit_hash": new_audit_hash}

    except subprocess.TimeoutExpired:
        error_msg = f"⚠️ *TIMEOUT ALERT:* Skill `{skill_name}` timed out after {timeout}s."
        logger.error(error_msg)
        telegram_notifier.send_telegram_message(error_msg)
        circuit_breaker[skill_name] = circuit_breaker.get(skill_name, 0) + 1
        return {"status": "error", "message": f"Execution timeout after {timeout}s"}
    except Exception as e:
        circuit_breaker[skill_name] = circuit_breaker.get(skill_name, 0) + 1
        logger.error(f"Skill execution fatal error for {skill_name}: {e}")
        return {"status": "error", "message": str(e)}

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
