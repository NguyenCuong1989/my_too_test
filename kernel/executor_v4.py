import concurrent.futures
from scheduler_v4 import ParallelScheduler

class ParallelDAGExecutor:
    def __init__(self, capability_graph):
        self.capability_graph = capability_graph
    def run_task(self, task):
        executor = self.capability_graph.get_executor(task["capability"])
        executor.run(task["skill"], task["input"])
    def execute(self, plan):
        scheduler = ParallelScheduler()
        layers = scheduler.schedule(plan)
        task_map = {t["id"]: t for t in plan["tasks"]}
        for layer in layers:
            with concurrent.futures.ThreadPoolExecutor() as pool:
                futures = [pool.submit(self.run_task, task_map[tid]) for tid in layer]
                for f in futures: f.result()
