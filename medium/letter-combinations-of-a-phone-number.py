'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.





Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 '''
from typing import List


class Solution:

    def backtrack(self, ans, m, digits, comb='', index=0):

        if index > len(digits):
            return

        if len(comb) == len(digits):
            ans.append(comb)
            return

        curDigit = digits[index]
        curChar = m[curDigit]

        for i in range(len(curChar)):
            self.backtrack(ans, m, digits, comb + curChar[i], index + 1)

    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        ans = []

        m = {}

        m['2'] = "abc"
        m['3'] = "def"
        m['4'] = "ghi"
        m['5'] = "jkl"
        m['6'] = "mno"
        m['7'] = "pqrs"
        m['8'] = "tuv"
        m['9'] = "wxyz"

        self.backtrack(ans, m, digits)
        return ans

s= Solution()
print(s.letterCombinations('23'))