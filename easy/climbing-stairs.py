'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for step in range(2, n):
            dp[step] = dp[step - 1] + dp[step - 2]
        return dp[-1]


class Solution2:
    def climbStairs(self, n: int) -> int:
        # time complexity: O(n)
        # space complexity: O(1)
        # we are actually starting from the last staircase and working our way backwards
        one, two = 1, 1

        # similar to fibonacci sequence
        for i in range(n - 1):
            # temp = one
            # one = one + two
            # two = temp
            one, two = one + two, one

        return one


s = Solution()
print(s.climbStairs(5))

s2 = Solution2()
print(s2.climbStairs(5))
