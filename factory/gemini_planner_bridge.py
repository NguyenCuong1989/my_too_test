# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

#!/usr/bin/env python3
"""
Gemini Planner Bridge for Telegram Control App
Connects Telegram queries to the Gemini Orchestrator logic.
"""

import sys
import logging
import json
from pathlib import Path
from typing import List

# Add parent directory to path to reach autonomous_operator
sys.path.append(str(Path(__file__).parent.parent))

try:
    from autonomous_operator.gemini_orchestrator import GeminiOrchestrator
except ImportError:
    # Fallback/Debug if path is different
    class GeminiOrchestrator:
        def __init__(self, *args, **kwargs): pass
        def create_plan(self, goal): return {"steps": [{"skill": "debug_skill", "payload": f"Simulated plan for {goal}"}]}

from enum import Enum, auto
from kernel.quota_guard_v1 import QuotaGuard

class GovernanceState(Enum):
    IDLE = auto()
    PLANNING = auto()
    EXECUTING = auto()
    OBSERVING = auto()
    DRIFT_DETECTED = auto()
    HEALING = auto()
    COMPLETED = auto()

try:
    import google.generativeai as genai
except ImportError:
    genai = None
from autonomous_operator.key_manager import GeminiKeyManager

logger = logging.getLogger("GeminiPlannerBridge")

class GeminiPlannerBridge:
    def __init__(self):
        self.quota_guard = QuotaGuard()
        self.quota_state = self.quota_guard.read_state()

        # Initialize Key Manager and Config (Phase 11)
        base_dir = Path("/Users/andy/my_too_test")
        self.km = GeminiKeyManager(base_dir=base_dir)
        self.model = None

        allow_cloud, _, _ = self.quota_guard.allow_cloud("cloud-required")
        if allow_cloud and genai is not None:
            active_key = self.km.get_active_key()
            if active_key:
                genai.configure(api_key=active_key)
                self.model = genai.GenerativeModel('gemini-pro-latest')

        self.orchestrator = GeminiOrchestrator()
        self.current_dag = None
        self.current_state = GovernanceState.IDLE
        self.logger = logger

        self.system_prompt = (
            "You are Antigravity, the State-of-the-art AI OS Control Plane for the Σ_APΩ Runtime. "
            "You serve the Master (Operator) with deterministic precision and natural intelligence. "
            "Maintain a professional, helpful, and slightly advanced persona. "
            "If the Master defines a goal or a task, suggest using structured planning. "
            "Respond concisely and clearly."
        )

    def chat(self, user_input: str) -> str:
        """Handles natural language chat using Gemini."""
        self.logger.info(f"💬 Natural Chat: {user_input}")
        allow_cloud, reason, state = self.quota_guard.allow_cloud("cloud-preferred")
        if not allow_cloud:
            return (
                "⚠️ Quota Guard denied cloud chat.\n"
                f"- gemini: `{state.get('gemini', 'unknown')}`\n"
                f"- overage_strategy: `{state.get('overage_strategy', 'unknown')}`\n"
                f"- reason: `{reason}`\n"
                "Use local-safe planning/review flow instead."
            )

        if genai is None:
            return "⚠️ Gemini SDK is unavailable; cloud chat path is disabled."

        if self.model is None:
            return "⚠️ Gemini model is unavailable after quota guard check."

        try:
            # Simple stateless chat for now (can be expanded with history)
            prompt = f"{self.system_prompt}\n\nOperator: {user_input}\nAntigravity:"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            self.logger.error(f"Chat Error: {e}")
            return f"⚠️ Antigravity Chat Encountered an Error: {e}"

    def transition_to(self, new_state: GovernanceState):
        self.logger.info(f"🚦 State Transition: {self.current_state.name} -> {new_state.name}")
        self.current_state = new_state

    def reverse_plan(self, result: str) -> str:
        """
        Antigravity Result-First: Φ⁻¹_valid(result) -> S₀
        Computes the execution path backward from a desired state.
        """
        self.logger.info(f"🔄 Reverse Planning for result: {result}")
        # Logic: result -> needs_verification -> needs_file -> needs_generation -> S0
        # For simulation/demo:
        steps = [
            {"skill": "fs_check", "payload": f"Verify {result} exists"},
            {"skill": "gen_logic", "payload": f"Generate path to ensure {result}"},
            {"skill": "verify_state", "payload": "Confirm valid start state S0"}
        ]
        self.current_dag = {"steps": steps[::-1], "goal": f"Result: {result}"}
        return self._format_plan(self.current_dag)

    def synthesize_dag(self, goal: str) -> str:
        """
        Decomposes a goal into a Directed Acyclic Graph of tasks.
        """
        self.logger.info(f"🌵 Synthesizing DAG for: {goal}")
        # Prefer a local planning path that survives quota exhaustion.
        if hasattr(self.orchestrator, "create_plan"):
            plan = self.orchestrator.create_plan(goal)
        elif hasattr(self.orchestrator, "resolve_module") and hasattr(self.orchestrator, "create_execution_plan"):
            try:
                task_type = "deploy" if "deploy" in goal.lower() else "execution"
                module_path = self.orchestrator.resolve_module(task_type)
                execution_plan = self.orchestrator.create_execution_plan(
                    {"id": f"goal::{goal}", "parameters": {"goal": goal}},
                    module_path,
                )
                plan = {
                    "goal": goal,
                    "steps": [
                        {
                            "skill": "local_execution_plan",
                            "payload": json.dumps(execution_plan, ensure_ascii=False),
                        }
                    ],
                }
            except Exception as e:
                self.logger.error(f"Local DAG synthesis fallback failed: {e}")
                plan = None
        else:
            plan = None

        if not plan or "steps" not in plan:
            return "❌ AI could not synthesize a DAG for this goal."

        self.current_dag = plan
        return self._format_plan(plan)

    def validate_plan(self, plan: dict) -> dict:
        """
        Validates skill availability and system health before execution.
        """
        self.logger.info("🛡️ Validating plan safety and compatibility...")
        # Simulated validation logic
        for step in plan.get("steps", []):
            if step["skill"] == "unknown":
                return {"valid": False, "reason": f"Skill {step['skill']} is not registered."}
        return {"valid": True}

    def detect_drift(self, goal: str, logs: List[str]) -> bool:
        """
        Checks if the system state has diverged from the goal based on logs.
        """
        self.logger.info(f"🔍 Checking for drift in goal: {goal}")
        for line in logs:
            if "ERROR" in line or "FAILED" in line:
                self.logger.warning(f"🚨 Drift detected: Failure in logs -> {line}")
                return True
        return False

    def heal_plan(self, goal: str, failure_log: str) -> str:
        """
        Recomputes the plan backward to fix errors.
        """
        self.logger.info(f"🩹 Attempting self-healing for: {goal}")
        # Logic: error analysis -> Φ⁻¹_valid(target) -> new DAG
        healing_steps = [
            {"skill": "sys_reverify", "payload": f"Analyze failure: {failure_log}"},
            {"skill": "fix_env", "payload": "Restore missing dependencies/files"},
            {"skill": "retry_task", "payload": f"Repath for: {goal}"}
        ]
        self.current_dag = {"steps": healing_steps, "goal": f"HEAL: {goal}"}
        return self._format_plan(self.current_dag)

    def _format_plan(self, plan: dict) -> str:
        formatted = f"🧠 **Antigravity Plan for: {plan.get('goal', 'Unknown')}**\n\n"
        for i, step in enumerate(plan.get("steps", []), 1):
            skill = step.get("skill", "unknown")
            payload = step.get("payload", "")
            formatted += f"{i}. `{skill}`: {payload}\n"
        formatted += "\n*Use `/dag show` to inspect or `/dag run` to execute.*"
        return formatted

    def plan_goal(self, goal: str) -> str:
        return self.synthesize_dag(goal)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bridge = GeminiPlannerBridge()
    print(bridge.plan_goal("deploy a landing page"))
