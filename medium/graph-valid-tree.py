'''
Given n nodes labeled from 0 to n - 1 and a
list of undirected edges (each edge is a pair of nodes),
 write a function to check whether these edges make up a valid tree.

You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0]
and thus will not appear together in edges.

Example
Example 1:

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
Example 2:

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
'''


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        if not n:
            return True

        adj = {i: [] for i in range(n)}  # {0: [], 1: [], 2: [], 3: [], 4: []}

        for n1, n2 in edges:
            adj[n1].append(n2)  # {0: [1, 2, 3], 1: [4], 2: [], 3: [], 4: []}
            adj[n2].append(n1)  # {0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]}

        visited = set()

        def dfs(i, prev):
            # duplicate detected
            if i in visited:
                return False

            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n


s = Solution()
print(s.validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]))
