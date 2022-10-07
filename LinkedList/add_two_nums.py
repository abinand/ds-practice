from platform import node
from linked_list import Node,LinkedList

list1 = LinkedList()
list1.append(4)
list1.append(9)
list1.append(8)
list1.append(2)

list2 = LinkedList()
list2.append(3)
list2.append(9)
list2.append(7)
list2.append(1)
list2.append(5)
list2.append(4)

print("Adding 4982 and 397154")

list1.reverse()
list2.reverse()
node1 = list1.head
node2 = list2.head
summed_list = LinkedList()
sum = 0
carry = 0
while(node1 != None or node2 != None):
    first_data = 0 if (node1 == None) else node1.data
    second_data = 0 if (node2 == None) else node2.data
    sum = first_data + second_data + carry
    carry = 0
    if (sum > 9):
        carry = 1
        sum %= 10
    summed_list.append(sum)
    node1 = None if (node1 == None) else node1.next
    node2 = None if (node2 == None) else node2.next
if (carry != 0):
    summed_list.append(carry)
summed_list.reverse()
summed_list.printList()