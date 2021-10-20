'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected and i
t will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, r
eturn the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        dp = [0] * n  # this will store the maximum money we can steal upto a specific house
        dp[0] = nums[0]  # the first cell will be whatever money is in the first house

        for i in range(1, n):
            # if this is the second house we can calc the max we can steal by comparing with house#1
            if i == 1:
                dp[i] = max(nums[0], nums[1])
            else:
                # for other generic cases
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # the last pos in the array contains max amount we can steal
        return dp[-1]


class Solution2:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            # now we need to compute the max we can rob up until n
            # rob2 is the last house we robbed, rob1 was the one before that
            # [rob1, rob2, n, n+1, ...] so if we want to rob n we have to rob rob1 as well
            # but if we are robbing rob2 we cant include n because its right next to it
            # so when we get to n+1 we update rob1 to equal rob2
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        # by the end rob2 will be equal to the max value
        return rob2


s = Solution2()
print(s.rob([2, 7, 9, 3, 1]))
