'''
Implementation of a Stack class with all its method : 

* stack() creates a new stack that is empty. it returns an empty stack    
* push(item) adds a new item to the top of the stack. it takes the item and returns nothing   
* pop() removes the top item from teh stack. it needs no parameters and returns the item. The stack is modified.   
* peek() returns the top item from the stack but does not remove it. It needs no parameters. the stack is not modified   
* is_empty() tests to see whether the stack is empty. it needs no parameters and returns a boolean value   
* size() returns the number of items on the stack. it needs no parameters and returns an integer.   

'''


class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self): 
        return len(self.items)


s = Stack()

print(s.is_empty())
s.push(1)
s.push('two')
s.push('three')
print(s.peek())
s.push(False)
print(s.size())
print(s.is_empty())
print(s.pop())
print(s.pop())
