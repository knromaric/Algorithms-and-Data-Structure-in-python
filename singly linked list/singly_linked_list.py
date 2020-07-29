"""Implementation of a Singly Linked List
"""


class Node(object): 

    def __init__(self, value): 
        self.value = value
        self.nextnode = None


a = Node(3)
b = Node(5)
c = Node(6)

a.nextnode = b
b.nextnode = c

print(a.nextnode.value)

