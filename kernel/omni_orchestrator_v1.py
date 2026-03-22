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
            from kernel.connector_mesh import connector_context, resolve_connector
            connector = resolve_connector(capability)
            context = connector_context(capability, task_id=task.get("id"))

            print(f"Ω Executing: [{capability}.{skill}] via connector [{connector}] with payload: {payload}")

            # Retrieve the executor from the capability graph
            executor = None
            if connector in self.capability_graph and skill in self.capability_graph[connector]:
                executor = self.capability_graph[connector][skill]
            elif capability in self.capability_graph and skill in self.capability_graph[capability]:
                executor = self.capability_graph[capability][skill]

            if callable(executor):
                try:
                    executor(**payload)
                except Exception as e:
                    print(f"Ω Error executing {connector}.{skill}: {e}")
                    raise e
            else:
                # Attempt remote execution via HubWorkerBridge
                from kernel.hub_worker_bridge import HubWorkerBridge
                print(f"Ω Capability local miss (or None). Attempting remote bridge for {connector}.{skill}...")
                try:
                    remote_payload = {**payload, "_connector_context": context}
                    result = HubWorkerBridge.execute_remote(connector, skill, remote_payload)
                    print(f"Ω Remote Result: {result.get('status', 'unknown')}")
                except Exception as e:
                    print(f"Ω Bridge Failure: {e}")
                    raise Exception(f"Ω Linkage Failure: Executor for {connector}.{skill} not found locally or remotely.")

        print("Ω Orchestrator: Plan execution complete.")
