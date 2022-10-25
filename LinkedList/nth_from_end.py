from linked_list import LinkedList,Node

list1 = LinkedList()
list1.append(1)
list1.append(5)
list1.append(8)
list1.append(8)
list1.append(10)
list1.append(15)
list1.append(21)
list1.append(10)
list1.append(15)
list1.append(21)
list1.printList()


node_end = list1.head

n = int(input("Enter a number"))

while(n > 0):
    node_end = node_end.next
    n-=1

node_n = list1.head

while (node_end != None):
    node_end = node_end.next
    node_n = node_n.next

print("The Nth element from the end of the list is" + str(node_n.data))