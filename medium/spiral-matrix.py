'''
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # time complexity is O(n*m) where n and m are dimensions of the matrox
        # space complexity is O(1) because we are not saving any memory (not counting res as extra memory)
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # we are always going to start at the top left position
        while left < right and top < bottom:
            # go left to right and get every value in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1  # by inc we are shifting top to down by 1

            # get every value in the right column
            for i in range(top, bottom):
                # right - 1 coz right is out of bounds and -1 will get us in bounds
                res.append(matrix[i][right - 1])
            right -= 1  # by dec we are shifting right to the left by 1

            # this specific condition is for e.g like [1,2,3] or [1,
            #                                                     2,
            #                                                     3]
            # which does happen everytime we are at the end of the matrix
            if not (left < right and top < bottom):
                break

            # get every value in bottom row
            # we are going right to left in reverse order
            # right - 1 because it is out of bounds and left - 1 so it can be in range (python stuff)
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])  # bottom - 1 because it is also out of bounds
            bottom -= 1  # by dec we are shifting bottom to up by 1

            # get every value from left col (bottom to top)
            # this is also where putting out bottom out of bounds initially comes in handy
            # no need to check for left < right and top < bottom logic as putting bottom out of bounds handles it
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res


s = Solution()
print(s.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
