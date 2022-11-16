from collections import defaultdict
class Graph:
    def __init__(self) -> None:
        self.adjacencyList = defaultdict(list) 
    def addEdge(self, fromNode, toNode):
        self.adjacencyList[fromNode].append(toNode)

    # Breadth First Traversal
    def breadthFirstTraversal(self, start):
        visited = []
        queue = []
        queue.append(start)
        while(len(queue) > 0):
            current = queue.pop(0)
            print(current, end=" ")
            for adjacentNode in self.adjacencyList[current]:
                if adjacentNode not in visited:
                    visited.append(adjacentNode)
                    queue.append(adjacentNode)
        print()

    # Depth First Traversal
    def depthFirstTraversal(self, start):
        visited = [start]
        self.__depthFirstRecursive(start, visited)
        print()
    def __depthFirstRecursive(self, current, visited):
        print(current, end=" ")
        for adjacentNode in self.adjacencyList:
            if adjacentNode not in visited:
                visited.append(adjacentNode)
                self.__depthFirstRecursive(adjacentNode, visited)


g = Graph()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(3,7)
g.addEdge(7,8)
g.breadthFirstTraversal(1)
g.depthFirstTraversal(1)
