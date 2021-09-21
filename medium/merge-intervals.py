'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # time complexity O(nlogn) because we sorting,
        # n is the number of intervals given

        intervals.sort(key=lambda i: i[0])  # i is the interval and we will use its first value to sort by
        output = [intervals[0]]  # we are inserting the first interval to avoid and edge case

        # we are not considering the first interval as we have already added to the output
        # start contains the first value and end contains the second value
        for start, end in intervals[1:]:
            # from our output we can get the most recent interval and get the end value of it to check overlapping
            # this is also the reason we added the first interval (edge case)
            last_end = output[-1][1]

            if start <= last_end:
                # we are taking max for cases like [1,5], [2,4], here 5 is larger so we dont merge with 4
                output[-1][1] = max(last_end, end)
            else:
                # if non overlapping than we still need to add it to our otuput
                output.append([start, end])

        return output


s = Solution()
print(s.merge([[1, 3], [8, 10], [15, 18], [2, 6]]))
