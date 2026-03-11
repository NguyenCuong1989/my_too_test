class ParallelScheduler:
    def schedule(self, plan):
        tasks = {t["id"]: t for t in plan["tasks"]}
        edges = plan["edges"]
        incoming = {tid: 0 for tid in tasks}
        for e in edges:
            incoming[e["to"]] += 1
        layers = []
        queue = [tid for tid, c in incoming.items() if c == 0]
        while queue:
            layers.append(list(queue))
            next_queue = []
            for node in queue:
                for e in edges:
                    if e["from"] == node:
                        incoming[e["to"]] -= 1
                        if incoming[e["to"]] == 0:
                            next_queue.append(e["to"])
            queue = next_queue
        return layers
