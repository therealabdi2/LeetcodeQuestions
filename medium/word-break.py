'''
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # +1 for our base case which is the last position (out of bounds of str)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        # starting from the last index (bottom up approach)
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # first we have to see, starting at pos i if str s has enough chars for w to be compared to it
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]


s = Solution()
print(s.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
