from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        n = len(nums)
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1

        for x in range(j, n):
            nums[x] = 0

        print(nums)


s = Solution()

s.moveZeroes([0, 2, 0, 1, 4])
# 2,1,4,,0,0
