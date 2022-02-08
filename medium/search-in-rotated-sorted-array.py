'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function,
nums is rotated at an unknown pivot index k (0 <= k < nums.length)
such that the resulting
array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # now we need to check which portion of the array are we in... left or right
            if nums[l] <= nums[mid]:
                # then we are in left sorted portion
                if target > nums[mid] or target < nums[l]:
                    # then we search the right most portion
                    l = mid + 1
                else:
                    # that means the target is less than the middle and greater than or equal to the left
                    # so we search the left portion and update our right pointer
                    r = mid - 1
            else:
                # we are in right sorted portion
                if target < nums[mid] or target > nums[r]:
                    # then we search the left most portion
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 2))
