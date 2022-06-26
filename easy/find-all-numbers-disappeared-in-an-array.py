'''
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
'''
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # mark existing values
        for num in nums:
            index = abs(num) - 1
            nums[index] = -1 * abs(nums[index])

        res = []
        for i, num in enumerate(nums):
            # if num is positive, it is not in the list
            if num > 0:
                res.append(i + 1)

        return res


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        disappeared_nums = []
        for i in range(1, num_len + 1):
            if i not in nums:
                disappeared_nums.append(i)
        return disappeared_nums


s = Solution()
print(s.findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
