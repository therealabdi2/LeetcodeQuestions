'''
Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Time Complexity: O(m*n)
        # Space Complexity: O(m*n)
        # here we use a 2D array to store the longest common subsequence
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # we are going through every cell in the 2D array
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # if the characters are the same, we add 1 to the longest common subsequence
                if text1[i] == text2[j]:
                    # we store the value in diagonal and add 1 because the characters are the same
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    # if the characters are not the same, we store the max of the bottom and the right
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # once the matrix is filled our result will be at the top left corner
        return dp[0][0]


s = Solution()
print(s.longestCommonSubsequence("abcde", "ace"))
