'''
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

'''


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s  # ["leet", "codes"] -> 4#leet#5codes
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        res, i = [], 0  # the pointer i tells us where we are in the string

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1  # j is the length of the string
            l = str[i:j]
            length = int(l)  # go from i to j but not include j (the #), and convert it to an int

            res.append(str[j + 1: j + 1 + length])  # j is the #, so we go to the next character
            i = j + 1 + length  # could be the start or the end of another string
        return res


s = Solution()
print(s.encode(["leet", "codes"]))
print(s.decode("4#leet#5codes"))

