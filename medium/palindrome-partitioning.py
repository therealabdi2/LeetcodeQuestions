'''Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]'''
from typing import List


class Solution:
    def isPalindrom(self, seg):
        return seg == seg[::-1]

    def solution(self, s, temp, ans):
        if len(s) == 0 and len(temp) > 0:
            ans.append(temp[:])
            return

        n = len(s) + 1
        for i in range(1, n):
            seg = s[0:i]
            if self.isPalindrom(seg):
                temp.append(seg)
                self.solution(s[i:], temp, ans)
                temp.pop()

        return

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.solution(s, [], ans)
        return ans
