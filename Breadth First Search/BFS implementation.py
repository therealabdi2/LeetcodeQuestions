from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def insert_edge(self, v1, v2):
        self.graph[v1].append(v2)

    def bfs(self, startNode):
        visited = set()

        queue = [startNode]

        visited.add(startNode)

        while queue:
            cur = queue.pop(0)
            print(cur, end=' ')


            for vertex in self.graph[cur]:
                if vertex not in visited:
                    queue.append(vertex)
                    visited.add(cur)


g = Graph()
g.insert_edge(2, 1)
g.insert_edge(2, 5)
g.insert_edge(5, 6)
g.insert_edge(5, 8)
g.insert_edge(6, 9)

g.bfs(2)
