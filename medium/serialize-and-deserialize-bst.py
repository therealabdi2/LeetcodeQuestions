'''
Serialization is converting a data structure or object into
a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link
to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You need to ensure that a binary search tree can be serialized to a string,
and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.



Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import Optional


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []

        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        vals = data.split(",")
        self.index = 0

        def dfs():
            if vals[self.index] == 'N':
                # move on to next node
                self.index += 1
                return None
            # create node for that value
            node = TreeNode(int(vals[self.index]))
            # move on to next node
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

s = Codec()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(s.serialize(root))
print(s.deserialize(s.serialize(root)).val)
print(s.deserialize(s.serialize(root)).left.val)
print(s.deserialize(s.serialize(root)).right.val)

