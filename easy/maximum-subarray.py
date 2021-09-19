'''
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sub = max(max_sub, cur_sum)
        return max_sub



s = Solution()
print(s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
