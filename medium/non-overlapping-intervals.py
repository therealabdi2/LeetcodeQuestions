'''
Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
'''
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # time: O(nlogn)
        # space: O(n)
        intervals.sort()

        res = 0
        # [1,2] [2,3] [3,4] [1,3]
        prev_end = intervals[0][1]  # 2

        for start, end in intervals[1:]:
            # this means the current interval is not overlapping with the previous one
            # and we just need to update the prev_end
            if start >= prev_end:
                prev_end = end
            # this means the current interval is overlapping with the previous one
            # so we need to remove one interval
            else:
                # increment the res we just need to count the number of intervals we need to remove
                res += 1
                # this determines which overlapping interval to remove
                # we keep the one with the smallest end value as a bigger one can overlap again
                # and we need the minimum number of intervals to remove
                prev_end = min(end, prev_end)
        return res


s = Solution()
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(s.eraseOverlapIntervals(intervals))
