from typing import Set
from linked_list import LinkedList, Node

list1 = LinkedList()
list1.append(1)
list1.append(5)
list1.append(8)
list1.append(10)
list1.append(15)
list1.append(21)
list1.printList()

list2 = LinkedList()
list2.append(3)
list2.append(8)
list2.append(12)
list2.append(13)
list2.append(19)
list2.append(21)
list2.append(23)
list2.append(25)
list2.printList()

print("Merge two sorted lists")
merged_list = LinkedList()
node1 = list1.head
node2 = list2.head

while (node1 != None and node2 != None):
    if (node1.data < node2.data):
        merged_list.append(node1.data)
        node1 = node1.next
    else:
        merged_list.append(node2.data)
        node2 = node2.next
while (node1 != None):
    merged_list.append(node1.data)
    node1 = node1.next
while (node2 != None):
    merged_list.append(node2.data)
    node2 = node2.next

merged_list.printList()

print("Intersection of two sorted lists")
intersection_list = LinkedList()
node1 = list1.head
node2 = list2.head

while(node1 != None and node2 != None):
    if (node1.data == node2.data):
        intersection_list.append(node1.data)
        node1 = node1.next
        node2 = node2.next
    elif (node1.data > node2.data):
        node2 = node2.next
    else:
        node1 = node1.next

intersection_list.printList()

def sorted_intersection(a:Node, b:Node):
    if (a == None or b == None):
        return None

    if (a.data > b.data):
        return sorted_intersection(a, b.next)

    if (a.data < b.data):
        return sorted_intersection(a.next, b)

    # if a.data == b.data
    temp = Node(a.data)
    temp.next = sorted_intersection(a.next, b.next)
    return temp

print("Intersection of two sorted lists with recursion")
intersection_list = LinkedList()
intersection_list.head = sorted_intersection(list1.head, list2.head)
intersection_list.printList()


