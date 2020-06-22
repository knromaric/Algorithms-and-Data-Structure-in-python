'''
    Given an integer, return an integer that
    is the reverse ordering numbers.

    *examples:

    reverse_int(15) -> 51 
    reverse_int(981) -> 189 
    reverse_int(500) -> 5 
    reverse_int(-15) -> -51 
    reverse_int(-90) -> -9 
'''

from math import copysign

def reverse_int(numb): 
    reverse = ''.join(reversed(str(numb)))
    if numb < 0: 
        return int(reverse[:-1]) * (-1)
    
    return int(reverse)
    
def reverse_int_v1(numb): 
    reverse = ''.join(reversed(str(numb)))
    return copysign(int(reverse[:-1]), numb)




print(reverse_int(15))
print(reverse_int(981))
print(reverse_int(500))
print(reverse_int(-15))
print(reverse_int(-90))
