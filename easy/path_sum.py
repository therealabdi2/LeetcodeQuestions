'''Given the root of a binary tree and an integer targetSum, return true if the tree has
a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Example 3:

Input: root = [1,2], targetSum = 0
Output: false'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check_sum(self, root, target, cur):
        if root is None:
            return False

        cur += root.val
        if cur == target and root.left is None and root.right is None:
            return True

        return self.check_sum(root.right, target, cur) or self.check_sum(root.left, target, cur)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.check_sum(root, targetSum, 0)

def main1(root):
    s = Solution()
    has_sum = s.hasPathSum(root, 11)
    print(has_sum)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(2)
    root.right = TreeNode(3)

    main1(root)
