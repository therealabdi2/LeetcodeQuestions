'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
'''


class Solution(object):
    def isValid(self, s):
        stack = []
        # we are mapping the closing parenthesis with its opening parenthesis
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            # that means its a closing parenthesis
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:  # should be matching our map
                    stack.pop()
                else:
                    return False
            else:
                # if we get an open parenthesis we add it to our stack
                stack.append(char)

        return True if not stack else False
