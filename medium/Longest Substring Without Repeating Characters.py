"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        ans = 0
        left = 0
        right = 0
        n = len(s)
        while left < n and right < n:
            el = s[right]
            if el in m:
                left = max(left, m[el] + 1)

            m[el] = right
            ans = max(ans, right - left + 1)
            right += 1
        return ans


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # time complexity O(n)
        # we get a set to store the characters we have seen
        char_set = set()
        # we use sliding window technique
        # our left pointer will be the beginning of the window and right will keep changing
        l = 0
        res = 0  # will store the max len here

        # the right pointer will go through every single char
        for r in range(len(s)):
            # if we get to a duplicate char then we have to update our window and our set
            while s[r] in char_set:  # meaning the char is a duplicate
                char_set.remove(s[l])  # removing the left most char
                l += 1  # increment pointer
            char_set.add(s[r])  # after we remove duplicates we can add it to our set
            # at this point we know for sure there are no duplicates in the set so update result
            res = max(res, r - l + 1)
        return res


s = Solution()
s2 = Solution2()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s2.lengthOfLongestSubstring("abcabcbb"))
