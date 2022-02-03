'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time complexity: O(nlogn) + O(n^2) -> O(n^2)
        # space complexity: O(n)

        res = []
        # we sort the numbers to avoid duplicates
        nums.sort()

        for i, val in enumerate(nums):
            # since nums are sorted we can skip the same value and avoid duplicates
            if i > 0 and val == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            # here we just apply the concept of two sum
            while l < r:
                three_sum = val + nums[l] + nums[r]
                # so we need to decrease the sum here
                if three_sum > 0:
                    r -= 1
                # and increase in this case
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    # so after appending we need to update our pointer
                    # only need to shift one pointer (of your choice)
                    l += 1
                    # we dont want the same sum so we have to use a loop i.e
                    # [-2,-2,0,0,2,2] here we need to keep moving the pointer so we dont add same sum
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
