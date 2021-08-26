class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def insert(root, node):
    if root is None:
        root = node
        return

    if node.data > root.data:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)


def min_value(node):
    while node.left:
        node = node.left
    return node


# key is the value of node we want to delete
def delete_node(node, key):
    if node is None:
        return node

    if key < node.data:
        node.left = delete_node(node.left, key)
    elif key > node.data:
        node.right = delete_node(node.right, key)
    else:
        # this case is for if the node has one child
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        # this case is for when a node has 2 children, we find min in right subtree and that min will replace the
        # deleted node

        temp = min_value(node.right)
        node.data = temp.data

        # now here we will delete the duplicate node
        node.right = delete_node(node.right, temp.data)

    return node


def search(node, key):
    if node is not None:
        print("Current Node is: ", node.data)
    if node is None:
        print("No node found :(")
        return None
    if node.data == key:
        print("Node fond ^_^")
        return node

    if key > node.data:
        return search(node.right, key)

    return search(node.left, key)


def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)


#	         5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8
tree = Node(5)

#	         5
#       /  	      \
#     None	       None

insert(tree, Node(3))

#	         5
#       /  	      \
#     3	            None

insert(tree, Node(2))

#	         5
#       /  	      \
#     3	            None
#   /
#  2
insert(tree, Node(4))

#	         5
#       /  	      \
#     3	            None
#   /   \
#  2     4
insert(tree, Node(7))

#	         5
#       /  	      \
#     3	            7
#   /   \
#  2     4
insert(tree, Node(6))

#	         5
#       /  	      \
#     3	            7
#   /   \        /
#  2     4      6
insert(tree, Node(8))

#	         5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8


# 5 3 2 4 7 6 8

delete_node(tree, 7) # deleting 7

#	           5
#       /  	      \
#     3	            8
#   /   \        /     \
#  2     4      6       None
preorder(tree)

search(tree, 7)
