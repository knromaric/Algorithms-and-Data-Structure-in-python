'''
    given a string, return a new string with 
    the reversed order of characters
    ---- examples
    reverse('apple') === 'elppa'

'''
from functools import reduce

def reverse_v0(text): 
    return ''.join(reversed(text))

def reverse_v1(text): 
    return text[::-1]

def reverse_v2(text):
    reversed = ''
    for char in text: 
        reversed = char + reversed
    return reversed

def reverse_v3(text): 
    return reduce(lambda result, char: char + result, text, '')

print(reverse_v0('apple'))
print(reverse_v1('apple'))
print(reverse_v2('apple'))
print(reverse_v3('apple'))



