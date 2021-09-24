'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's,
and return the matrix.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(1) memory sol, o(n.m) time
        ROWS, COLS = len(matrix), len(matrix[0])
        # we dont need extra arrays but we need 1 extra var to tell if the first row is 0 or not
        row_zero = False

        # determine which rows/columns need to be zeroed
        # go through every row and column
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # then we set the first row in this column to zero
                    matrix[0][c] = 0

                    # we need to set col pos to 0 as well, except we dont do this for top/left most position
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        # this means we got a zero in the first row
                        row_zero = True

        # now we need to zero out
        # we are skipping first row and col, we will handle it later
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                # here we are zeroing out the first column of our matrix
                matrix[r][0] = 0

        # here we are zeroing out the first row of our matrix if need be
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0

        print(matrix)


s = Solution()
s.setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
