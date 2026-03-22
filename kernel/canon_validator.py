from typing import List, Dict

class CanonValidator:
    PHASE_ORDER = {
        "Origin": 0,
        "Event": 1,
        "Propagation": 2,
        "Observe": 3,
        "Interface": 4,
        "Failure": 5,
        "Boundary": 6
    }

    CAPABILITY_MAP = {
        "factory": ["deploy", "filesystem", "networking", "automation"],
        "axcontrol": ["control", "infrastructure", "runtime"],
        "phoenix": ["reasoning", "memory", "analysis"]
    }

    @classmethod
    def validate(cls, plan: Dict) -> Dict:
        tasks = plan.get("tasks", [])
        if not tasks:
            raise ValueError("Invalid Plan: Empty task list.")

        task_ids = set()
        for task in tasks:
            cap = task.get("capability")
            skill = task.get("skill")
            task_ids.add(task.get("id"))

            if cap not in cls.CAPABILITY_MAP:
                raise ValueError(f"Canon Violation: Undefined capability '{cap}'")
            if skill not in cls.CAPABILITY_MAP[cap]:
                raise ValueError(f"Canon Violation: Undefined skill '{skill}' for '{cap}'")

        for task in tasks:
            deps = task.get("dependencies", [])
            for dep in deps:
                if dep not in task_ids:
                    raise ValueError(f"Canon Violation: Missing dependency '{dep}'")

            task_phase_idx = cls.PHASE_ORDER[task.get("phase")]
            for dep_id in deps:
                dep_task = next(t for t in tasks if t["id"] == dep_id)
                dep_phase_idx = cls.PHASE_ORDER[dep_task.get("phase")]
                if dep_phase_idx > task_phase_idx:
                    raise ValueError("Canon Violation: Phase reversal detected.")

        return plan
