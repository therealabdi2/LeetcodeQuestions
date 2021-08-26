class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data)


# create root
root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)
root.left.right = Node(8)
'''
		           4 
		       /       \ 
		      5	        6 
	      /  \      /   \ 
       7   8  None  None
      / \
  None   None
'''
postorder(root)
