'''
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what.
Its maximum jump length is 0, which makes it impossible to reach the last index.

'''
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # time complexity: O(n)
        # space complexity: O(1)

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            # we need to check if jump length (nums[i]) starting at pos i taking a max jump greater or equal
            # to the goal because if it is than that means we can reach the goal
            if i + nums[i] >= goal:
                # shift the goal closer to us
                goal = i

        # now at this point if goal is 0 then that means we can reach the goal from pos 0 else we cant
        return True if goal == 0 else False


s = Solution()
print(s.canJump([2, 3, 1, 0, 4]))
