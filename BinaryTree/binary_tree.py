from tree import TreeUtils, Node
from math import inf

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

binaryTree = TreeUtils(node)
print("Tree printed in order - left, root, right")
binaryTree.printInOrder()
print()
print("Tree printed pre-order - root, left, right")
binaryTree.printPreOrder()
print()
print("Height of the tree is " + str(binaryTree.height()))
print()
print("Level order traversal - breadth first")
binaryTree.printLevelOrder()
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
newTreeNode = buildTree(inOrder, preOrder)
newTree = TreeUtils(newTreeNode)
print("Confirm new tree in-order")
binaryTree.printInOrder()
print()
print("Confirm new tree pre-order")
binaryTree.printPreOrder()
print()

# Find min element in the binary tree
def findMin(root: Node):
    if(root is None):
        return inf
    leftMin = findMin(root.left)
    rightMin = findMin(root.right)
    min = int(root.data)
    if(leftMin < min):
        min = leftMin
    if(rightMin < min):
        min = rightMin
    return min

print("Minimum node value in tree is " + str(findMin(newTreeNode)))