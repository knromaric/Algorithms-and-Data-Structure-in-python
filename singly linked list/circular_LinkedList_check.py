from singly_linked_list import Node


def cycle_check(node): 
    
    marker1 = node
    marker2 = node


    while marker1 != None and marker2.nextnode != None: 
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        #check if the markers have crossed 
        if marker1 == marker2: 
            return True 

    # Case where the marker ahead reaches the end of the list
    return False 

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b 
b.nextnode = c
c.nextnode = a # Cycle List


x = Node('ro')
y = Node('mo')
z = Node('to')

x.nextnode = y
y.nextnode = z 

print(cycle_check(a)) # circular
print(cycle_check(x)) # not circular
