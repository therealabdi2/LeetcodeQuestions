'''You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.



Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 '''

# this is actually the direct implementaion dijkstra' Algorithm
import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = collections.defaultdict(list)

        for u, v, cost in times:
            g[u].append((cost, v))

        min_heap = [(0, k)]  # we will start from k and its cost is 0

        visited = set()
        distance = {i: float('inf') for i in range(1, n + 1)}  # setting distance to infinite

        distance[k] = 0  # starting with k so its distance is set to 0

        while min_heap:
            cur_dist, u = heapq.heappop(min_heap)
            if u in visited:
                continue

            visited.add(u)

            if len(visited) == n:
                return cur_dist

            for direct_dist, v in g[u]:
                if cur_dist + direct_dist < distance[v] and v not in visited:
                    distance[v] = cur_dist + direct_dist

                    heapq.heappush(min_heap, (distance[v], v))

        return -1


s = Solution()
s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
