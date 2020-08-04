from singly_linked_list import Node

def nth_to_last_node(n, head): 
    slow = head
    fast = head

    for _ in range(n): 

        if not slow.nextnode: 
            raise LookupError('Error: n is larger than the linked List')
        
        fast = fast.nextnode

    while fast.nextnode: 
        slow = slow.nextnode
        fast = fast.nextnode

    
    return slow



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)


a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e


target_node = nth_to_last_node(3, a)
print(target_node.value)