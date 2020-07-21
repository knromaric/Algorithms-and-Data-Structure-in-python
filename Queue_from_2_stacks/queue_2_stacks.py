'''
Implement a Queue - Using Two Stacks

Given the stack class below, Implement a queue class using two stacks! 
Use a python list data structure as your stack.  
'''


class Queue2Stacks(object):

    def __init__(self):
        # two stacks
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()


qs = Queue2Stacks()

qs.enqueue(1)
qs.enqueue(2)
qs.enqueue(3)
print(qs.dequeue())
print(qs.dequeue())
print(qs.dequeue())
