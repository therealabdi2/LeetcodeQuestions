'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
in the sequence has an edge connecting them.
A node can only appear in the sequence at most once.
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.



Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = -float("inf")

    def solution(self, node):
        if node is None:
            return 0
        left = self.solution(node.left)
        right = self.solution(node.right)

        mxSide = max(node.val, max(left, right) + node.val)
        mxTop = max(mxSide, left + right + node.val)
        self.ans = max(self.ans, mxTop)
        return mxSide

    def maxPathSum(self, root: TreeNode) -> int:
        self.solution(root)
        return self.ans


class Solution2:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # return max path sum without splitting
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # we dont wanna add -ve numbers so just take zero if -ve
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max sum path WITH splitting
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # cant chose both because then that means we are splitting
            # here we take the max path without split
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
