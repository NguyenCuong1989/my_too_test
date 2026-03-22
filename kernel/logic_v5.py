# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỜNG Supreme System Commander
# Status: CANONICAL | ULTIMATE_GOAL_EVALUATOR_V6

import hashlib
import json
import uuid
import os
from datetime import datetime

class RuntimeStateMachine:
    INIT, PLAN, VALIDATE, SCHEDULE, EXECUTE, OBSERVE, UPDATE, TERMINATE = range(8)
    def __init__(self):
        self.state = self.INIT
    def transition(self, next_state):
        self.state = next_state

class ExecutionContext:
    def __init__(self):
        self.runtime_id = str(uuid.uuid4())
        self.cycle = 0
    def next_cycle(self, state, plan):
        self.cycle += 1
        state_hash = hashlib.sha256(json.dumps(state, sort_keys=True).encode()).hexdigest()
        plan_hash = hashlib.sha256(json.dumps(plan, sort_keys=True).encode()).hexdigest()
        return {
            "runtime_id": self.runtime_id,
            "cycle": self.cycle,
            "state_hash": state_hash,
            "plan_hash": plan_hash,
            "timestamp": datetime.now().isoformat()
        }

class PlanHashValidator:
    def __init__(self):
        self.previous = None
    def validate(self, plan):
        h = hashlib.sha256(json.dumps(plan, sort_keys=True).encode()).hexdigest()
        if self.previous is None:
            self.previous = h
            return True
        if h != self.previous:
            raise Exception("Non-deterministic plan detected")
        return True

class GoalEvaluator:
    """Nâng cấp Γ v6: Semantic & Portable Goal Evaluation"""
    def evaluate(self, state, goal_spec):
        # Hỗ trợ cả string legacy và dict-based goal
        if isinstance(goal_spec, str):
            if state.get("goal_achieved") is True: return True
            if "DEPLOY" in goal_spec:
                return os.path.exists(state.get("artifacts", {}).get("runtime_path", ""))
            return False

        # Semantic evaluation
        goal_type = goal_spec.get("type")
        target = goal_spec.get("target")

        if goal_type == "DEPLOYMENT":
            target_path = state.get("artifacts", {}).get(target)
            return os.path.exists(target_path) if target_path else False

        if goal_type == "STABILITY":
            return state.get("system", {}).get("health") == "OK"

        return state.get("goal_achieved") is True
