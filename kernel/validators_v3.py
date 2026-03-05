class CanonValidator:
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

class CanonPhaseValidator:
    ORDER = ["origin", "event", "propagation", "observe", "interface", "failure", "boundary"]
    def validate_phases(self, tasks):
        last_index = -1
        # Assumes tasks are sorted by dependency in this simplified validator
        for task in tasks:
            phase = task["phase"]
            if phase not in self.ORDER:
                raise Exception(f"Invalid phase: {phase}")
            idx = self.ORDER.index(phase)
            if idx < last_index:
                raise Exception("Phase order violation")
            last_index = idx
        return True
