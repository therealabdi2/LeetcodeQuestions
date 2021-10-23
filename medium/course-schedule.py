'''
There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0,
and to take course 0 you should also have finished course 1. So it is impossible.
'''
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # time O(n+p)
        # map each course to prereq list
        pre_map = {i: [] for i in range(numCourses)}  # {0: [], 1: []}

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)  # {0: [], 1: [0]}
            # visitSet = all courses along the curr DFS path
        visit_set = set()

        def dfs(crs):
            # if course is already in visited set then we have detected a loop so this course can not be completed
            if crs in visit_set:
                return False
            if pre_map[crs] == []:
                return True

            visit_set.add(crs)

            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visit_set.remove(crs)
            # so it returns true immediately no need to check pre reqs again
            pre_map[crs] = []
            return True

            # we are looping like dis coz there could be cases where graphs arent connected like 1 ->2, 3->4

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


s = Solution()
print(s.canFinish(numCourses=2, prerequisites=[[1, 0]]))
