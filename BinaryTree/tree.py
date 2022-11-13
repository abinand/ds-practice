class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def printNode(self):
        print(self.data, end=" ")

class TreeUtils:
    def __init__(self, root: Node) -> None:
        self.root = root

    def printInOrder(self):
        self.printInOrderRec(self.root)
        print()

    def printInOrderRec(self, node:Node):
        if(node):
            self.printInOrderRec(node.left)
            node.printNode()
            self.printInOrderRec(node.right)

    def printPreOrder(self):
        self.printPreOrderRec(self.root)
        print()

    def printPreOrderRec(self,node:Node):
        if (node):
            node.printNode()
            self.printPreOrderRec(node.left)
            self.printPreOrderRec(node.right)