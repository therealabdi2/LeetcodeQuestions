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
import collections
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res

        q = collections.deque()
        q.append(root)

        while q:
            # this len will make sure we go through one level at a time
            q_len = len(q)
            # we will add this list to our result
            level = []
            for i in range(q_len):
                # first in first out
                node = q.popleft()
                if node:
                    level.append(node.val)
                    # the children can be null that's why we've got the if statement
                    q.append(node.left)
                    q.append(node.right)

            # our queue can have null nodes so we dont wanna add them
            if level:
                res.append(level)

        return res
