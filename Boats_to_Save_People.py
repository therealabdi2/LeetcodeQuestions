from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            if left == right:
                boats += 1
                break
            elif people[left] + people[right] <= limit:
                left += 1
                right -= 1
                boats += 1
            else:
                right -= 1
                boats += 1
        return boats


s = Solution()

print(s.numRescueBoats([1, 2, 3, 4], 3))
