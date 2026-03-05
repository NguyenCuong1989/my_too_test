#!/usr/bin/env python3
import json
import logging
import subprocess
from pathlib import Path
from typing import Dict, Any

# Configure Logging (Phase 9)
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [GEMINI_ORCHESTRATOR] %(message)s',
    handlers=[logging.FileHandler(LOG_DIR / "gemini_orchestrator.log"), logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

class GeminiOrchestrator:
    def __init__(self, map_path: str = "/Users/andy/my_too_test/SYSTEM_FILE_INDEX.json"):
        self.map_path = Path(map_path)
        self.capability_map = self._load_map()

    def _load_map(self) -> Dict:
        """Loads the semantic index (Phase 5)."""
        if self.map_path.exists():
            try:
                with open(self.map_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse capability map at {self.map_path}: {e}")
                return {"modules": []}
        logger.error(f"Capability map not found at {self.map_path}")
        return {"modules": {}}

    def resolve_module(self, task_type: str) -> str:
        """Phase 6: Task Resolution - Maps task type to the appropriate module."""
        # Simple heuristic resolution based on keyword matching in module names or roles
        logger.info(f"Resolving module for task type: {task_type}")

        # Hardcoded critical paths based on APΩ specification
        if "scrape" in task_type or "browser" in task_type:
            return "axcontrol/core/browser/mac_ui_observer.py"
        elif "deploy" in task_type or "execution" in task_type:
            return "factory/factory_worker.py"

        # Dynamic search in the capability map (Handles [path] and [category] as per new schema)
        map_data = self.capability_map if isinstance(self.capability_map, list) else self.capability_map.get("modules", [])

        for item in map_data:
            path = item.get("path", "")
            if task_type in path.lower() or task_type in item.get("category", "").lower():
                return path

        raise ValueError(f"Unknown task type: {task_type}. Cannot resolve module. Guard: Fail Closed.")

    def create_execution_plan(self, task: Dict[str, Any], module_path: str) -> Dict[str, Any]:
        """Phase 7: Execution Planning."""
        logger.info(f"Building execution plan for {task.get('id', 'unknown')}")
        plan = {
            "task_id": task.get("id"),
            "target_module": module_path,
            "steps": [
                "validate_dependency",
                f"execute {module_path}",
                "collect_output",
                "validate_result"
            ],
            "parameters": task.get("parameters", {})
        }
        return plan

    def execute_plan(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """Phase 8: Execution via Factory Engine equivalent."""
        logger.info(f"Executing Plan for {plan['task_id']}")
        module_path = plan["target_module"]

        # Safety Guard: Check if file exists before execution
        if not Path(module_path).exists():
            logger.error(f"Module {module_path} not found.")
            return {"status": "FAILED", "reason": "Module missing"}

        # Simulate execution by calling the python module (or specific logic)
        try:
            cmd = ["python3", module_path]
            # Add parameters as JSON string argument if needed by the target script
            if plan.get("parameters"):
                cmd.append(json.dumps(plan["parameters"]))

            res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

            output = res.stdout + res.stderr
            status = "SUCCESS" if res.returncode == 0 else "FAILED"

            # Phase 10: Validation (Implicit based on return code here, can be expanded)
            logger.info(f"Execution {status} with code {res.returncode}")
            return {"status": status, "output": output, "task_id": plan["task_id"]}

        except subprocess.TimeoutExpired:
            logger.error(f"Execution timed out for {plan['task_id']}")
            return {"status": "FAILED", "reason": "Timeout"}
        except Exception as e:
            logger.error(f"Execution error: {e}")
            return {"status": "FAILED", "reason": str(e)}

    def store_result(self, result: Dict[str, Any]):
        """Phase 9: Result Packaging."""
        out_dir = Path("factory/processed")
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{result.get('task_id', 'unknown')}_result.json"

        with open(out_file, "w") as f:
            json.dump(result, f, indent=4)
        logger.info(f"Result stored at {out_file}")

# Example Integration loop (Phase 11 concept)
if __name__ == "__main__":
    orchestrator = GeminiOrchestrator()
    # Mock Task for testing
    mock_task = {
        "id": "test_resolution_001",
        "type": "verify_ace",
        "parameters": {}
    }

    try:
        module = orchestrator.resolve_module(mock_task["type"])
        plan = orchestrator.create_execution_plan(mock_task, module)
        result = orchestrator.execute_plan(plan)
        orchestrator.store_result(result)
        print("✅ End-to-end Orchestration cycle completed successfully.")
    except Exception as e:
        print(f"❌ Orchestration Failed: {e}")
