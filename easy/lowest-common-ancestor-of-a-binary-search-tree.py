'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the
lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a
descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        # loop until cur is None
        while cur:
            # if p is smaller than cur, go left
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # if p is bigger than cur, go right
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur


node = TreeNode(6)
node.left = TreeNode(2)
node.right = TreeNode(8)
node.left.left = TreeNode(0)
node.left.right = TreeNode(4)
node.right.left = TreeNode(7)
node.right.right = TreeNode(9)
node.left.left.left = TreeNode(3)
node.left.left.right = TreeNode(5)

s = Solution()
print(s.lowestCommonAncestor(node, node.right, node.left).val)
