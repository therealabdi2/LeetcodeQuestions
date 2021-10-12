'''
Given an integer array nums, find a contiguous non-empty subarray within the array
that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n) time , O(1) memory
        # in case we have an array with just one number so we store max in res
        res = max(nums)
        # init to 1 because we cant multiply with 0 and 1 is a neutral value
        cur_min, cur_max = 1, 1

        for n in nums:
            # if we get a zero we want to ignore it
            # this if statement is unnecessary and is just for explanation purposes
            # if n == 0:
            #     cur_min, cur_max = 1, 1
            #     continue

            # if n is -ve and cur_min is -ve then we could get a max product
            # we take n as max for cases like [-1, 8] if our current number is 8 then
            # we dont wanna multiply
            tmp = cur_max * n
            cur_max = max(tmp, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)

            res = max(res, cur_max, cur_min)
        return res


s = Solution()
print(s.maxProduct(nums=[2, 3, -2, 4]))
