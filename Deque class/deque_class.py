"""
Here are the Deque methods and Attributes:    
* Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.  
* addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.  
* addRear(item) adds a new item to the rear of the deque. it needs the item and returns nothing .
* removeFront() removes the front item from the deque. it takes no parameters and return the item. The deque is modified.
* removeRear() removes the rear item from the Deque. it needs no parameters and returns the item. The deque is modified 
* isEmpty() test to see whether the deque is empty. it takes no parameters and returns a boolean value   
* size() returns the number of items in the deque. it needs no parameters and returns an integer.
"""

class Deque(object): 
    def __init__(self): 
        self.items = []

    def is_empty(self): 
        return self.items == []

    def size(self):
        return len(self.items)

    def add_front(self, item): 
        self.items.append(item)
    
    def add_rear(self, item): 
        self.items.insert(0, item)

    def remove_front(self): 
        return self.items.pop()

    def remove_rear(self): 
        return self.items.pop(0)
     

d = Deque()

d.add_front('hello')
d.add_rear('world')
print(d.size())

print(f'{d.remove_front()} {d.remove_rear()}')
print(d.size())
print(d.is_empty())