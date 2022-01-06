'''
You are given a string s and an integer k.
You can choose any character of the string and change
it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter
you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity: O(n*26)
        # Space Complexity: O(n)
        count = {}
        res = 0
        left = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            # windows_size = r - left + 1
            while r - left + 1 - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, r - left + 1)

        return res


class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        count = {}
        res = 0
        left = 0
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            # windows_size = r - left + 1
            while r - left + 1 - max_freq > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, r - left + 1)
        return res


s = Solution()
print(s.characterReplacement("ABAB", 2))

s = Solution2()
print(s.characterReplacement("AABABBA", 1))
