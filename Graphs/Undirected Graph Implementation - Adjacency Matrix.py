'''Initally, our "graph" is represented by this 2d list full of zeroes, the "0 1 2 3 4 5" at the edges are just indices that I added to make it easier to visualize when inserting an edge later on

[        0  1  2  3  4  5
0     [ 0, 0, 0, 0, 0, 0 ],
1     [ 0, 0, 0, 0, 0, 0 ],
2     [ 0, 0, 0, 0, 0, 0 ],
3     [ 0, 0, 0, 0, 0, 0 ],
4     [ 0, 0, 0, 0, 0, 0 ],
5     [ 0, 0, 0, 0, 0, 0 ]
]

now, say we want to insert and edge between node 1 and 2, node 1 is the node with index 1, and node 2 is the node with index 2, so, to indicate that there is an edge from node 1 to node 2, we can set graph[1][2] to be 1,

[        0  1  2  3  4  5
0     [ 0, 0, 0, 0, 0, 0 ],
1     [ 0, 0, 1, 0, 0, 0 ],
2     [ 0, 0, 0, 0, 0, 0 ],
3     [ 0, 0, 0, 0, 0, 0 ],
4     [ 0, 0, 0, 0, 0, 0 ],
5     [ 0, 0, 0, 0, 0, 0 ]
]

this is a way for us to say that we have an edge from 1 to 2.

now what if we want to say that we have an edge from node 2 to node 1, well in that case we can represent this by setting graph[2][1] to be 1

[        0  1  2  3  4  5
0     [ 0, 0, 0, 0, 0, 0 ],
1     [ 0, 0, 1, 0, 0, 0 ],
2     [ 0, 1, 0, 0, 0, 0 ],
3     [ 0, 0, 0, 0, 0, 0 ],
4     [ 0, 0, 0, 0, 0, 0 ],
5     [ 0, 0, 0, 0, 0, 0 ]
]


and now you can see why we create a 2d list, image each cell in each row as a question that asks (does my row index have an edge pointing to my column index)
'''


class Graph:
    def __init__(self, numberOfNodes):
        self.numberOfNodes = numberOfNodes
        # 4=>0,1,2,3
        self.graph = [[0 for x in range(numberOfNodes + 1)]
                      for y in range(numberOfNodes + 1)]

    def withinbounds(self, v1, v2):
        return (0 <= v1 <= self.numberOfNodes) and (0 <= v2 <= self.numberOfNodes)

    def insertEdge(self, v1, v2):
        if self.withinbounds(v1, v2):
            self.graph[v1][v2] = 1
            self.graph[v2][v1] = 1

    def printGraph(self):
        for i in range(self.numberOfNodes):
            for j in range(len(self.graph[i])):
                if self.graph[i][j]:
                    print(i, "->", j)


g = Graph(5)

g.insertEdge(1, 2)
g.insertEdge(2, 3)
g.insertEdge(4, 5)

g.printGraph()
