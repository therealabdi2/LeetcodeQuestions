'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
Example 3:

Input: matrix = [[1]]
Output: [[1]]
Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # time complexity: O(n^2)
        # space complexity: O(1)

        l, r = 0, len(matrix) - 1

        # we are doing the rotation anti clockwise because it requires only one temp variable
        while l < r:
            # or from l to r - 1
            for i in range(r - l):
                top, bottom = l, r

                # the i variable will help in moving pos left, down, right, up, so we can rotate other cells
                # save the top left value
                top_left = matrix[top][l + i]

                # move the bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move the bottom right into the bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move the top right into the bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move the top left into top right
                matrix[top + i][r] = top_left

            # after computing the outer square we need to take care of inner squares

            r -= 1
            l += 1
        print(matrix)


class Solution2:
    '''
    clockwise rotate
    first reverse up to down, then swap the symmetry
    1 2 3     7 8 9     7 4 1
    4 5 6  => 4 5 6  => 8 5 2
    7 8 9     1 2 3     9 6 3
    '''

    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)


s = Solution()
s.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])

s2 = Solution2()
s2.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
