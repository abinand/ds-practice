from linked_list import LinkedList

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
print("Initial list:")
llist.printList()

print("Prepend 5")
llist.prepend(5)
llist.printList()

print("Insert value 8 after value 2")
llist.insertAfter(newValue=8, afterValue=2)
llist.printList()

print("Insert value 10 after value 9")
llist.insertAfter(newValue=10, afterValue=9)
llist.printList()

print("Append 6")
llist.append(6)
llist.printList()

print("Delete 5 at the head of the list")
llist.delete(5)
llist.printList()

print("Delete 8 in the middle of the list")
llist.delete(8)
llist.printList()

print("Delete 6 at the end of list")
llist.delete(6)
llist.printList()

print("Length of list: " + str(llist.getLength()))

print("Is there a loop in this list ? - " + str(llist.findLoop()))
print("Create a loop")
llist.append(4)
llist.append(5)
llist.append(6)
llist.head.next.next.next.next.next = llist.head.next.next
print("Is there a loop in this list ? - " + str(llist.findLoop()))


print()
print("List 1")
llist1 = LinkedList()
llist1.prepend(5)
llist1.prepend(4)
llist1.prepend(3)
llist1.prepend(2)
llist1.prepend(1)
llist1.printList()


print("List 2")
llist2 = LinkedList()
llist2.prepend(10)
llist2.prepend(7)
llist2.prepend(6)
llist2.prepend(5)
llist2.prepend(4)
llist2.printList()

print("Introduce an intetersection")
llist1.head.next.next.next.next = llist2.head.next.next
llist1.printList()

print("Find intersection point")
list1Length = llist1.getLength()
list2Length = llist2.getLength()
intersectionLength = abs(list1Length - list2Length)
# len(list1) - len(list2) = len(intersecting part)
# then traverse the first list upto intersection
list1Intersection = list1Length - intersectionLength
tempNode = llist1.head
while( intersectionLength >= 0):
    tempNode = tempNode.next
    intersectionLength -= 1
print(str(tempNode.data) + " is the intersection point")