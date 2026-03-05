class CanonValidator:

    PHASES = [
        "origin",
        "event",
        "propagation",
        "observe",
        "interface",
        "failure",
        "boundary"
    ]

    def validate(self, plan):

        task_ids = {t["id"] for t in plan["tasks"]}

        # Check edge validity
        for e in plan["edges"]:

            if e["from"] not in task_ids:
                raise Exception(f"Invalid edge source: {e['from']}")

            if e["to"] not in task_ids:
                raise Exception(f"Invalid edge target: {e['to']}")

        # Validate phase ordering
        phases = [t["phase"] for t in plan["tasks"]]

        last_index = -1

        for p in phases:

            try:
                idx = self.PHASES.index(p)
            except ValueError:
                raise Exception(f"Invalid phase: {p}")

            if idx < last_index:
                raise Exception(f"Phase order violation: {p} cannot follow {self.PHASES[last_index]}")

            last_index = idx

        return True
