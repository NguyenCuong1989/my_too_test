class SkillExecutor:
    def run(self, skill, input_data):
        raise NotImplementedError

class FactoryExecutor(SkillExecutor):
    def run(self, skill, input_data):
        if skill == "deploy":
            self.deploy(input_data)
    def deploy(self, data):
        print(f"[EXECUTOR] Deploying: {data}")

class AXControlExecutor(SkillExecutor):
    def run(self, skill, input_data):
        print(f"[EXECUTOR] AXControl running {skill}")

class PhoenixExecutor(SkillExecutor):
    def run(self, skill, input_data):
        print(f"[EXECUTOR] Phoenix running {skill}")

class CapabilityGraph:
    def __init__(self):
        self.executors = {
            "factory": FactoryExecutor(),
            "axcontrol": AXControlExecutor(),
            "phoenix": PhoenixExecutor()
        }
    def get_executor(self, capability):
        return self.executors[capability]

class OmniOrchestrator:
    def __init__(self, capability_graph):
        self.capability_graph = capability_graph
    def execute(self, plan):
        for task in plan["tasks"]:
            capability = task["capability"]
            skill = task["skill"]
            input_data = task["input"]
            executor = self.capability_graph.get_executor(capability)
            executor.run(skill, input_data)
