from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        # 1:[2,3] Node 1 point to 2 and 3

    # this receives two nodes/ values that we want to create an edge b/w them
    # 1, 2 mean 1 -> 2, one points to two
    def insert_edge(self, v1, v2):
        # the value 1 points to a list that contains 2 1=>[2]
        self.graph[v1].append(v2)
        # with this we get undirected graph
        self.graph[v2].append(v1)

    def print_graph(self):
        for node in self.graph:
            for v in self.graph[node]:
                print(node, "=>", v)


g = Graph()
g.insert_edge(1, 5)
g.insert_edge(5, 2)
g.insert_edge(2, 7)
g.insert_edge(7, 1)

g.print_graph()
# this should look like
# 1=>[5]
# 5=>[2]
# 2=>[7]
# 7=>[1]
