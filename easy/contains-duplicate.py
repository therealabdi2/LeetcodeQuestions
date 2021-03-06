"""
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = defaultdict(int)

        for num in nums:
            if m[num]:
                return True
            m[num] += 1
        return False


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False


class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_num = {}
        for num in nums:
            if num in dict_num:
                return True

            if num not in dict_num:
                dict_num[num] = num
        return False


s = Solution2()
print(s.containsDuplicate([1, 2, 3, 4, 1]))
