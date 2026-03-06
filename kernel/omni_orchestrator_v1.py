class OmniOrchestrator:

    def __init__(self, capability_graph: dict):
        """
        Ω (Omni Orchestrator)
        Executes validated DAG tasks against the capability graph.
        """
        self.capability_graph = capability_graph

    def execute(self, plan: dict):
        """
        Iterates through the tasks in the plan and executes their corresponding skills.
        """
        print(f"Ω Orchestrator: Starting execution of {len(plan['tasks'])} tasks.")

        for task in plan["tasks"]:
            capability = task["capability"]
            skill = task["skill"]
            payload = task.get("input", {})

            print(f"Ω Executing: [{capability}.{skill}] with payload: {payload}")

            # Retrieve the executor from the capability graph
            executor = None
            if capability in self.capability_graph and skill in self.capability_graph[capability]:
                executor = self.capability_graph[capability][skill]

            if callable(executor):
                try:
                    executor(**payload)
                except Exception as e:
                    print(f"Ω Error executing {capability}.{skill}: {e}")
                    raise e
            else:
                # Attempt remote execution via HubWorkerBridge
                from kernel.hub_worker_bridge import HubWorkerBridge
                print(f"Ω Capability local miss (or None). Attempting remote bridge for {capability}.{skill}...")
                try:
                    result = HubWorkerBridge.execute_remote(capability, skill, payload)
                    print(f"Ω Remote Result: {result.get('status', 'unknown')}")
                except Exception as e:
                    print(f"Ω Bridge Failure: {e}")
                    raise Exception(f"Ω Linkage Failure: Executor for {capability}.{skill} not found locally or remotely.")

        print("Ω Orchestrator: Plan execution complete.")
