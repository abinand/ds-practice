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

    # Breadth first traversal - preorder, inorder, postorder
    def printInOrder(self):
        self.__printInOrderRec(self.root)
        print()

    def __printInOrderRec(self, node:Node):
        if(node):
            self.__printInOrderRec(node.left)
            node.printNode()
            self.__printInOrderRec(node.right)

    def printPreOrder(self):
        self.__printPreOrderRec(self.root)
        print()

    def __printPreOrderRec(self,node:Node):
        if (node):
            node.printNode()
            self.__printPreOrderRec(node.left)
            self.__printPreOrderRec(node.right)

    # Height
    def height(self):
        return self.__heightRec(self.root)

    def __heightRec(self, node:Node):
        if node is None:
            return 0
        ltreeHeight = self.__heightRec(node.left)
        rtreeHeight = self.__heightRec(node.right)
        if (ltreeHeight > rtreeHeight):
            return ltreeHeight + 1
        else:
            return rtreeHeight + 1

    # Depth first traversal
    def printLevelOrderDFS(self):
        queue = []
        queue.append(self.root)
        while (len(queue) > 0):
            node:Node = queue.pop(0)
            node.printNode()
            if (node.left is not None):
                queue.append(node.left)
            if (node.right is not None):
                queue.append(node.right)
        print()

