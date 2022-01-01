'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to find
the number of connected components in an undirected graph.
Example 1:
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
     0          3
     |          |
     1 --- 2    4
Output: 2
Example 2:
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
     0           4
     |           |
     1 --- 2 --- 3
Output:  1
Note:
You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and
thus will not appear together in edges.
'''
from typing import List


class Solution():
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        # find root parent
        def find(n1):
            res = n1

            # find the root of n1
            while res != par[res]:
                # path compression
                par[res] = par[par[res]]
                # but if we dont have a root parent
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            # if true then that means p2 will be the parent of p1
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


if __name__ == '__main__':
    s = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print(s.countComponents(n, edges))

