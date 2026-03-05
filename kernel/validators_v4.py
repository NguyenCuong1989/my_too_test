from jsonschema import validate

class SkillSchemaValidator:
    def __init__(self, registry):
        self.registry = registry
    def validate(self, capability, skill, payload):
        capability_desc = self.registry.get(capability)
        if not capability_desc: return False
        skill_desc = capability_desc["skills"].get(skill)
        if not skill_desc: return False
        schema = skill_desc["input_schema"]
        validate(instance=payload, schema=schema)
        return True

class PlanStructuralValidator:
    def validate(self, plan):
        task_ids = {t["id"] for t in plan["tasks"]}
        for edge in plan["edges"]:
            if edge["from"] not in task_ids:
                raise Exception(f"Invalid edge source: {edge['from']}")
            if edge["to"] not in task_ids:
                raise Exception(f"Invalid edge target: {edge['to']}")
        return True

class DAGCycleDetector:
    def has_cycle(self, plan):
        graph = {t["id"]: [] for t in plan["tasks"]}
        for e in plan["edges"]:
            graph[e["from"]].append(e["to"])
        visited, stack = set(), set()
        def visit(node):
            if node in stack: return True
            if node in visited: return False
            visited.add(node)
            stack.add(node)
            for neighbor in graph[node]:
                if visit(neighbor): return True
            stack.remove(node)
            return False
        for node in graph:
            if visit(node): return True
        return False

class CanonPhaseValidator:
    ORDER = ["origin", "event", "propagation", "observe", "interface", "failure", "boundary"]
    def validate_phases(self, tasks):
        last_index = -1
        # Simplified: Check linear order in the task list
        for task in tasks:
            phase = task["phase"]
            if phase not in self.ORDER:
                raise Exception(f"Invalid phase: {phase}")
            idx = self.ORDER.index(phase)
            if idx < last_index:
                raise Exception(f"Phase order violation at task {task['id']}")
            last_index = idx
        return True
