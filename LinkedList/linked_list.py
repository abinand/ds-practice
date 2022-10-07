class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def printNode(self):
        print(self.data, end=" -> ")

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        tempNode = self.head
        while (tempNode != None):
            tempNode.printNode()
            tempNode = tempNode.next
        print("None") # for the last node
        print() # prints a new line

    def prepend(self, data):
        node = Node(data=data)
        node.next = self.head
        self.head = node

    def insertAfter(self, newValue, afterValue):
        tempNode = self.head
        while (tempNode != None and tempNode.data != afterValue):
            tempNode = tempNode.next
        if (tempNode == None):
            print(str(afterValue) + " was not found")
        else:
            newNode = Node(data=newValue)
            newNode.next = tempNode.next
            tempNode.next = newNode
    
    def append(self, data):
        if (self.head == None):
            self.head = Node(data)
            return
        tempNode = self.head
        while(tempNode.next != None):
            tempNode = tempNode.next
        newNode = Node(data)
        tempNode.next = newNode
    
    def delete(self, data):
        if(self.head.data == data):
            self.head = self.head.next
        else:
            tempNode = self.head
            while(tempNode.next != None and tempNode.next.data != data):
                tempNode = tempNode.next
            if (tempNode.next == None):
                print(str(data) + "was not found")
                return
            tempNode.next = tempNode.next.next
    
    def reverse(self):
        current = self.head
        prev = None
        while(current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def __getCount(self, node:Node):
        if (node == None):
            return 0
        return 1 + self.__getCount(node.next)
    
    def getLength(self):
        return self.__getCount(self.head)

    def findLoop(self):
        slowPointer = self.head
        fastPointer = self.head
        while (fastPointer.next != None):
            fastPointer = fastPointer.next.next #moves twice
            slowPointer = slowPointer.next      #moves once
            if (slowPointer == fastPointer):    # if they meet, it is a loop
                tempNode = slowPointer
                counter = 1 #to find length of the loop
                while (tempNode.next != slowPointer):
                    counter += 1
                    tempNode = tempNode.next
                print("Loop after " + str(slowPointer.data) + " of length " + str(counter))
                return True
        return False
