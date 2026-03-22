class CapabilityGraphLoader:

    def __init__(self, persistence):
        self.persistence = persistence

    def load(self):

        cursor = self.persistence.conn.cursor()

        cursor.execute(
            "SELECT from_node, to_node FROM capability_edges"
        )

        graph = {}

        for row in cursor.fetchall():

            src = row[0]
            dst = row[1]

            if src not in graph:
                graph[src] = []

            graph[src].append(dst)

        return graph
