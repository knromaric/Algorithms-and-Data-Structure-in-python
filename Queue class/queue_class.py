'''
Implementation of Queue Class

* Queue() creates a new queue that is empty and returns and empty queue
* enqueue(item) adds a new item to the rear of the queue. it needs the item and returns nothing. 
* is_empty() tests to see whether the queue is empty. it needs no parameters and returns a boolean value.   
* size() returns the number of items in the queue. it needs no parameters and returns an integer.

'''

class Queue(object): 
    def __init__(self): 
        self.items = []

    def enqueue(self, item): 
        self.items.insert(0, item)

    def dequeue(self): 
        return self.items.pop()

    def is_empty(self): 
        return self.items == []

    def size(self): 
        return len(self.items)

    
q = Queue()
print(q.is_empty())
print(q.size())
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.is_empty())