'''
iven an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 '''
from typing import List


class Solution:
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    def solution(self, board, word, x, y, cur):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]) or board[x][y] == '':
            return False

        cur += board[x][y]
        if len(cur) > len(word):
            return False

        if cur[len(cur) - 1] != word[len(cur) - 1]:
            return False

        if cur == word:
            return True

        temp = board[x][y]
        board[x][y] = ''

        for i in range(4):
            if self.solution(board, word, x + self.dx[i], y + self.dy[i], cur):
                return True

        board[x][y] = temp
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)

        for i in range(n):
            m = len(board[i])
            for j in range(m):
                if word[0] == board[i][j] and self.solution(board, word, i, j, ""):
                    return True

        return False


class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # time O(n * m * 4^n)
        ROWS, COLS = len(board), len(board[0])

        # we use a set because we can not reuse variables
        path = set()

        # r and c will be current position i would be current word
        def dfs(r, c, i):
            if i == len(word):
                return True

            # 1st and 2nd conditions are for out of bounds
            # 3rd condition is for if the word we are looking for isn't the word in board
            # 4th condition is for if the word already exists in our path (r,c)
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path:
                return False
            # this condition is reached only when we find the character we are looking for
            path.add((r, c))
            # we are running dfs on all four adjacent cells
            # if any returns true then our result will return true
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            # we remove the path from our set since we are no longer visiting that position
            path.remove((r, c))
            return res

        # we will go through the whole board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


s = Solution2()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(s.exist(board, word))
