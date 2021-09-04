'''iven the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.



Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, node, arr):
        if node is None:
            return
        if node is not None:
            self.inorder(node.left, arr)
            arr.append(node.st)
            self.inorder(node.right, arr)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.inorder(root, arr)
        return arr[k-1]



def main1(root):
    s = Solution()
    k_small = s.kthSmallest(root, 3)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.right = TreeNode(4)

    main1(root)
