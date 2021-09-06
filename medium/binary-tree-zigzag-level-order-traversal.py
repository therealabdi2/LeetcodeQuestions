'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
'''

# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans

        q = deque()
        q.appendleft(root)
        zigzag = False

        while q:
            n = len(q)
            level = []  # this will act as current lvl array

            for i in range(0, n):
                if zigzag:
                    f = q.pop()
                    level.append(f.val)
                    if f.right:
                        q.appendleft(f.right)
                    if f.left:
                        q.appendleft(f.left)

                else:
                    f = q.popleft()
                    level.append(f.val)
                    if f.left:
                        q.append(f.left)
                    if f.right:
                        q.append(f.right)

            ans.append(level[:])
            level.clear()
            zigzag = not zigzag

        return ans
