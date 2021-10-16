'''
Write a function that takes an unsigned integer
and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

'''


class Solution:
    # time O(32) -> O(1)
    # the downside is it has to look at every bit even the ones that arent 1's e.g 1000001 will look at all 0 too
    # which wastes time
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # if n is 1 we get 1 if 0 then add 0
            res += n % 2
            n = n >> 1
        return res


class Solution2:
    def hammingWeight(self, n: int) -> int:
        # the time and space complexity is the same but this is just a lil trick
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res
