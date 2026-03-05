class CanonValidator:
    PHASE_ORDER = [
        "origin", "event", "propagation", "observe", "interface", "failure", "boundary"
    ]
    VALID_CAPABILITIES = {
        "factory": ["deploy","filesystem","networking","automation"],
        "axcontrol": ["control","infrastructure","runtime"],
        "phoenix": ["reasoning","memory","analysis"]
    }
    def validate(self, plan):
        for task in plan["tasks"]:
            cap = task["capability"]
            skill = task["skill"]
            if cap not in self.VALID_CAPABILITIES:
                raise Exception(f"Invalid capability: {cap}")
            if skill not in self.VALID_CAPABILITIES[cap]:
                raise Exception(f"Invalid skill: {skill}")
        return plan
