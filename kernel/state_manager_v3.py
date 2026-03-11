import time

class StateManager:
    def __init__(self):
        self.state = {
            "system": {"uptime": 0, "health": "OK", "mode": "STRICT"},
            "capabilities": {
                "factory": {"status": "READY", "last_execution": None},
                "axcontrol": {"status": "READY", "last_execution": None},
                "phoenix": {"status": "READY", "last_execution": None}
            },
            "runtime": {"active_tasks": 0, "queue_depth": 0},
            "memory": {"objects": [], "vectors": []}
        }
        self.start_time = time.time()

    def get_state(self):
        self.state["system"]["uptime"] = int(time.time() - self.start_time)
        return self.state

    def observe(self):
        return {"runtime": {"active_tasks": 0, "queue_depth": 0}}

    def update(self, observation):
        self.state.update(observation)

    def goal_reached(self, goal):
        # Deterministic exit for demo
        return self.state["system"]["uptime"] > 0
