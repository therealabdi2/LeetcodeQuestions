"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1  # get the current value that corresponds to num from our dictionary m, if we dont find anything then we consider it zero
        for num in nums:
            if m[num] > len(nums) / 2:
                return num


s = Solution()
print(s.majorityElement([3, 2, 3]))
