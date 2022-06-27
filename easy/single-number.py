"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor cancels out duplicates so we are only left with binary of unique value
        res = 0
        for n in nums:
            res = n ^ res
        return res


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


s = Solution()
print(s.singleNumber([2, 2, 1, 1, 4]))
