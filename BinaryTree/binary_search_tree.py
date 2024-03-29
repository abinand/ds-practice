from tree import TreeUtils,Node

def insertNode(key: int, root: Node):
    if (root is None):
        return Node(key)
    if (root.data > key): # insert into left subtree
        root.left = insertNode(key, root.left)
    elif (root.data < key): # insert into right subtee
        root.right = insertNode(key, root.right)
    return root


node = Node(50)
node = insertNode(10, node)
node = insertNode(20, node)
node = insertNode(60, node)
node = insertNode(90, node)
node = insertNode(30, node)
node = insertNode(40, node)


#         40 
#      /      \
#    20        50 
#   /  \      /   \
# 10    30  60    90

bst = TreeUtils(node)
print("In Order Traversal")
bst.printInOrder()
print("Pre Order Traversal")
bst.printPreOrder()
