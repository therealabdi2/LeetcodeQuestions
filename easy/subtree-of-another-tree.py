'''
Given the roots of two binary trees root and subRoot,
return true if there is a subtree of root with the same structure
and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.



Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # time: O(n)
        # space: O(n)
        # subroot is empty then it will be a subroot of any tree,
        if not subRoot:
            return True

        # but if root tree is empty and subroot is not empty then it will not be a subroot of any tree
        # the order of the conditions matter here
        if not root:
            return False

        # at this point we know that both root and subroot are not empty
        # so we need to check if the root and subroot have the same value
        if self.sameTree(root, subRoot):
            return True

        # but if they are not the same then we need to check if the root has a subtree with the same structure
        # if either of the below conditions return true then it will be a subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        # if both are empty, then they technically are the same
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            # now we compare the rest of the tree recursively
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

        # if neither of the above conditions execute, then that means one of the trees is empty and the other is not
        return False


s = Solution()
# root = [3,4,5,1,2]
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
# subRoot = [4,1,2]
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(s.isSubtree(root, subRoot))
