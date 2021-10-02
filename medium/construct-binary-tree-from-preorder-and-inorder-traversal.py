'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal
of a binary tree and inorder is the inorder traversal of the same tree,
construct and return the binary tree.



Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # the root will always be the 1st value in preorder array
        root = TreeNode(preorder[0])
        # then we want the index of that root in our inorder array
        mid = inorder.index(preorder[0])
        # now we build the subtree
        # mid tells us how many node we want in the left subtree
        # we start at index 1 because we have already created root node for the 0th index
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # starting at mid + 1 and going till the end of the sublist
        # and for inorder we want every node to right of mid in inorder
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root


s = Solution()
print(s.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]).val)
