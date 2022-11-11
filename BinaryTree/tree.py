class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def printNode(self):
        print(self.data, end=" ")

class TreeUtils:
    def __init__(self) -> None:
        pass

    def printInOrder(self, node:Node):
        if(node):
            self.printInOrder(node.left)
            node.printNode()
            self.printInOrder(node.right)

    def printPreOrder(self,node:Node):
        if (node):
            node.printNode()
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)