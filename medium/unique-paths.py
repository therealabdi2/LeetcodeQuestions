'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for x in range(m)] for y in range(n)]

        for i in range(m):
            dp[0][i] = 1
        for i in range(n):
            dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                # adding the number of ways we can reach a cell in dp
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]


s = Solution()
print(s.uniquePaths(m=3, n=7))
