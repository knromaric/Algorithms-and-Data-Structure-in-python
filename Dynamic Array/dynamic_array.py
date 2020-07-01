"""
    we will create a custom Dynamic array class!
    we'll be using the built in library ctypes. check out the documentation
    for more info. but its basically going to be used here as a raw array
    from the ctypes module. 
"""

import ctypes

class DynamicArray(object):
    
    
    def __init__(self):
        #count elements in the array
        self.count = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    
    def __len__(self):
        return self.count


    def __getitem__(self, k): 
        
        if not 0<= k < self.count:
            return IndexError('K is out of bounds')

        return  self.A[k]


    def append(self, value): 
        if self.count == self.capacity: 
            self._resize(2 * self.capacity) # 2X capacity of capacity isn't enough

        self.A[self.count] = value
        self.count += 1


    def _resize(self, new_cap):
        
        temp_Array = self.make_array(new_cap)
        
        for k in range(self.count):
            temp_Array[k] = self.A[k]
        
        self.A = temp_Array
        self.capacity = new_cap
        
    
    def make_array(self, new_cap): 
       
       return (new_cap * ctypes.py_object)()
 

arr = DynamicArray()
arr.append(1)
print(len(arr))
arr.append(2)
print(len(arr))
print(arr[1])