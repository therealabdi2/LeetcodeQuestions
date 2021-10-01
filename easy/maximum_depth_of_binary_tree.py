'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1
'''

# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


class Solution2:
    # recursion O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution3:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative BFS, not really good its the same time complexity as recursion
        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1
        return level


class Solution4:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative preorder DFS, without recursion same time and space compexity
        stack = [[root, 1]]
        res = 0
        while stack:
            # we are getting 2 values here
            node, depth = stack.pop()

            # if node is not null we do
            if node:
                res = max(res, depth)
                # the children can be null but the if statement will prevent us from using it
                # so null nodes are ignored
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


def main1(root):
    s = Solution4()
    maxDepth = s.maxDepth(root)
    print(maxDepth)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(2)
    root.right = TreeNode(3)

    main1(root)
