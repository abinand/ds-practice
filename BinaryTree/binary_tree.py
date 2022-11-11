from tree import TreeUtils, Node

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)

#        1
#     /    \
#    2      3
#   / \    /  \
# 4    5   6   none

binaryTree = TreeUtils()
print("Tree printed in order - left, root, right")
binaryTree.printInOrder(node)
print()
print("Tree printed pre-order - root, left, right")
binaryTree.printPreOrder(node)
print()


# Tree construction using pre-order and in-order notations
preOrder = ["1", "2", "4", "5", "3", "6"]
inOrder  = ["4", "2", "5", "1", "6", "3"]

def buildTree(inOrder, preOrder):

    # if in-order array is empty, we have reached a leaf node
    if (len(inOrder) == 0): 
        return None

    # get the next value in pre-order
    preOrderValue = preOrder[buildTree.preOrderIndex]
    tNode = Node(preOrderValue) # root node
    buildTree.preOrderIndex += 1 # increase static counter

    # the root from pre-order splits the in-order into left and right subtrees
    indexOfValue = inOrder.index(preOrderValue)
    leftSubtreeInOrder = inOrder[0:indexOfValue]
    rightSubtreeInOrder = inOrder[indexOfValue+1:]

    # recursion for left and right subtrees 
    tNode.left = buildTree(leftSubtreeInOrder,preOrder)
    tNode.right = buildTree(rightSubtreeInOrder, preOrder)
    return tNode

# index counter should be static to always count up inside recursive function
buildTree.preOrderIndex = 0

print("Creating new tree with in-order and pre-order arrays")
newTree = buildTree(inOrder, preOrder)

print("Confirm new tree in-order")
binaryTree.printInOrder(newTree)
print()
print("Confirm new tree pre-order")
binaryTree.printPreOrder(newTree)
print()