"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



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


s = Solution()
print(s.containsDuplicate([1, 2, 3, 4, ]))
