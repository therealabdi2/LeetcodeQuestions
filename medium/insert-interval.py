'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end]
that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
'''
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # now we wanna take care of couple of edge cases
            # 1. if end value of newInterval is less than start value of current interval
            # then that means they arent overlapping and we add the newInterval to the result at the start
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # after we append the newInterval to the result we can just return the result
                # as other intervals are not overlapping with the newInterval
                # this is the python way of doing it
                # we are taking the intervals and appending it (+) to the result
                return res + intervals[i:]
            # 2. the other edge case is that this newInterval can come after the current interval
            # in this case we just append the current interval since its not overlapping with newInterval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                # we wont append the newInterval yet because it could still overlap with other intervals
            else:
                # this condition is for overlapping with current interval
                # in this case we merge it
                # we take min of the left value of both the intervals, and max of the right value of both the intervals
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # we still dont append because this new interval could still overlap with other intervals on the right

        # here we append in case the first if condition doesn't execute
        # hence the newInterval wont be added to the result
        res.append(newInterval)
        return res


s = Solution()
print(s.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 6]))
