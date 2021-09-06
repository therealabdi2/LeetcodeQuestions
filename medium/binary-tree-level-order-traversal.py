'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans

        q = deque([root])
        while q:
            n = len(q)
            temp = []  # this will act as current lvl array

            for i in range(0, n):
                f = q.popleft()
                temp.append(f.val)
                if f.left:
                    q.append(f.left)
                if f.right:
                    q.append(f.right)
            if len(temp) > 0:
                ans.append(temp[:])
                temp.clear()
        return ans
