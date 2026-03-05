import uuid

class DAGPlanner:
    def build_task(self, capability, skill, input_data, phase):
        return {
            "id": str(uuid.uuid4()),
            "phase": phase,
            "capability": capability,
            "skill": skill,
            "input": input_data
        }

    def build_plan(self, state, goal, context, allowed_caps):
        tasks = []
        edges = []
        t1 = self.build_task("phoenix", "analysis", {"dataset": state}, "origin")
        t2 = self.build_task("factory", "deploy", {"target": "runtime", "artifact": goal, "environment": "prod"}, "event")
        tasks.append(t1)
        tasks.append(t2)
        edges.append({"from": t1["id"], "to": t2["id"]})
        return {"id": str(uuid.uuid4()), "tasks": tasks, "edges": edges}
