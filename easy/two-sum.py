"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 """
from typing import List


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for num in nums:
            goal = target - num

            if goal in m:
                index_num = [i for i, e in enumerate(nums) if e == num]
                return [m[goal], index_num[-1]]

            m[num] = nums.index(num)


class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in m:
                return [m[goal], i]
            m[nums[i]] = i


class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time complexity: O(n)
        # space complexity: O(n)
        prev_map = {}  # every element that comes before the current element is gonna be stored in this map val:index

        # we get the index and actual value of the element
        for i, num in enumerate(nums):
            diff = target - num

            # we can check if the diff is already in the map
            if diff in prev_map:
                # we return the pair
                return [prev_map[diff], i]
            # if we dont find the solution then we need to update the map
            prev_map[num] = i


s = Solution()
print(s.twoSum([3, 3, 4], target=6))

s2 = Solution2()
print(s.twoSum([3, 2, 4], target=6))

s3 = Solution3()
print(s.twoSum([3, 3], target=6))
