import time

class Telemetry:
    def __init__(self):
        self.metrics = {}
    def record(self, name, value):
        if name not in self.metrics: self.metrics[name] = []
        self.metrics[name].append(value)
    def measure(self, name):
        start = time.time()
        return lambda: self.record(name, time.time() - start)

class FailureManager:
    def handle(self, task_id, error, phase):
        print(f"[FAILURE] Task:{task_id} | Phase:{phase} | Error:{error}")
