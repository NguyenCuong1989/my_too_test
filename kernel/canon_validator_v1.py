VALID_CAPABILITIES = {
    "factory": ["deploy", "filesystem", "networking", "automation"],
    "axcontrol": ["control", "infrastructure", "runtime"],
    "phoenix": ["reasoning", "memory", "analysis"],
    "github": ["list_repos", "audit_repo", "sync_logic"],
    "memory": ["status", "sync"],
    "system": ["health"],
    "asana": ["create_task", "get_status", "update_audit_task"]
}

PHASE_ORDER = [
    "origin",
    "event",
    "propagation",
    "observe",
    "interface",
    "failure",
    "boundary"
]


class CanonValidator:
    """
    Canon Validator (V)
    Enforces capability and phase constraints on the generated plan.
    """

    def validate_capability(self, task: dict):
        capability = task["capability"]
        skill = task["skill"]

        if capability not in VALID_CAPABILITIES:
            raise Exception(f"Invalid capability: {capability}")

        if skill not in VALID_CAPABILITIES[capability]:
            raise Exception(f"Invalid skill: {skill} for capability: {capability}")

    def validate_phase(self, tasks: list):
        last_index = -1

        for t in tasks:
            phase = t["phase"]
            if phase not in PHASE_ORDER:
                raise Exception(f"Invalid phase: {phase}")

            idx = PHASE_ORDER.index(phase)

            if idx < last_index:
                raise Exception(f"Phase order violation: {phase} cannot follow phase at index {last_index}")

            last_index = idx

    def validate(self, plan: dict):
        """
        Ensures the entire plan is canonical.
        """
        for task in plan["tasks"]:
            self.validate_capability(task)

        self.validate_phase(plan["tasks"])

        return True
