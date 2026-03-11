import uuid
import time


class TaskGraphBuilder:

    PHASES = [
        "origin",
        "event",
        "propagation",
        "observe",
        "interface",
        "failure",
        "boundary"
    ]

    def build(self, path):

        tasks = []
        edges = []

        for i, node in enumerate(path):

            capability, skill = node.split(".")

            task_id = f"t{i+1}"

            phase = self.PHASES[min(i, len(self.PHASES)-1)]

            task = {
                "id": task_id,
                "phase": phase,
                "capability": capability,
                "skill": skill,
                "input": {}
            }

            tasks.append(task)

            if i > 0:
                edges.append({
                    "from": f"t{i}",
                    "to": task_id
                })

        return {
            "plan_id": str(uuid.uuid4()),
            "created_at": int(time.time()),
            "planner_version": "adaptive_v1",
            "tasks": tasks,
            "edges": edges
        }
