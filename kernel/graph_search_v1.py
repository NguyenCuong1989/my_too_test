from collections import deque


class GraphSearchPlanner:

    def __init__(self, graph: dict):
        self.graph = graph

    def search(self, start: str, goal: str):

        queue = deque([[start]])
        visited = set()

        while queue:

            path = queue.popleft()
            node = path[-1]

            if node == goal:
                return path

            if node not in visited:

                visited.add(node)

                for neighbor in self.graph.get(node, []):

                    new_path = list(path)
                    new_path.append(neighbor)

                    queue.append(new_path)

        raise Exception(f"No path found in capability graph from {start} to {goal}")
