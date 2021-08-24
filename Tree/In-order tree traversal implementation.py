class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data)
        inorder(node.right)


# create root
root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)
'''
		           4 
		       /       \ 
		      5	        6 
	      /  \      /   \ 
       7   None  None  None
      / \
  None   None
'''
inorder(root)
