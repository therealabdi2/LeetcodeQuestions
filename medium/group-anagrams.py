"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""
import collections
from typing import List


class Solution:
    def findHash(self, s):
        return ''.join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for s in strs:
            hashed = self.findHash(s)  # returns a sorted version of our string s
            if hashed not in m:
                m[hashed] = []
            m[hashed].append(s)

        return list(m.values())


class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = collections.defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(str))
            m[sorted_str].append(str)

        return list(m.values())


class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)  # mapping the char count of each input string to the list of anagrams

        for s in strs:
            count = [0] * 26  # a..z

            for c in s:
                # get the ascii values of char e.g a - a =0 so it will be stored in 1st cell
                count[ord(c) - ord('a')] += 1

            # our count is a list but in python lists can not be keys
            # so we change it to a tuple because tuples are non mutable
            res[tuple(count)].append(s)

        return res.values()

    # time complexity O(m * n) where m is the number of strings given and n is he average length of each string


s = Solution()

print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
