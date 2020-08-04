'''
    Linked List Reversal implementation
'''

from singly_linked_list import Node


def reverse(head): 
    current = head
    prevNode = None
    nextNode = None 

    while current: 
        nextNode = current.nextnode
        current.nextnode = prevNode
        prevNode = current
        current = nextNode

    return 



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c 
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

# Reversing the Linked List
print("##################")
reverse(a)
print("##################")

print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)


    

