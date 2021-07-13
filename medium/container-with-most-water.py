from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        max_area = 0
        while l < r:
            max_area = max(max_area,
                           min(height[l], height[r]) * (r - l)
                           # Select the smaller building to calculate area (y-axis),then r - l to find x axis, area= x*y
                           )
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


s = Solution()

print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
