"""Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output:'10101' """


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        print(f"{i}, {j}")
        # 010101 => a
        # 111111 => b we want to start from right most bit

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            print(f"total is: {total}")
            result.append(str(total % 2))
            carry = total // 2
            print(f"carry is: {carry}")
            print(result)

        return ''.join(reversed(result))


s = Solution()
print(s.addBinary(a="11", b="1"))
