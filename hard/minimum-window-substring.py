"""
Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t (including duplicates)
is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string."
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # handle the empty string edge case
        if t == "":
            return ""

        count_t, window = {}, {}

        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)  # if c does not exist it will return 0

        # initialize the window
        have, need = 0, len(count_t)
        # res will have left and right pointer and res_len is infinity because we want to find the smallest window
        res, res_len = [-1, -1], float("infinity")
        l = 0  # left pointer

        # r will tell the right boundary of our current window
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # we need to check if c is even a character in t and they appear the same number of times
            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                # update our result if we have found potential sub str
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # while the condition is being met we need to keep shrinking the string
                # because we need the smallest sub str
                # so pop from the left of our window
                window[s[l]] -= 1
                # we need to check if s[l] is even a character in t meaning  if they are
                # one of our characters that satisfy our needs
                # and by removing if we made it less than what we needed
                # then we need to decrement our have counter
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                # shift the left pointer
                l += 1
                # then we check the have and need condition again
                # we are taking character and adding it to our window map
                # checking if the condition is met
                # updating the window accordingly
                # by the end if the result exists it will be stored in our res variable

        l, r = res
        # if result does not exist res_len will be infinity and we will return empty string
        return s[l:r + 1] if res_len != float("infinity") else ""


s = Solution()
print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
