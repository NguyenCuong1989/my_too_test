class SkillExecutor:
    def run(self, skill, input_data):
        print(f"[EXEC] {self.__class__.__name__} -> {skill} with {input_data}")

class FactoryExecutor(SkillExecutor):
    pass

class AXControlExecutor(SkillExecutor):
    pass

class PhoenixExecutor(SkillExecutor):
    pass

class CapabilityGraph:
    def __init__(self):
        self.executors = {
            "factory": FactoryExecutor(),
            "axcontrol": AXControlExecutor(),
            "phoenix": PhoenixExecutor()
        }
    def get_executor(self, capability):
        return self.executors[capability]
