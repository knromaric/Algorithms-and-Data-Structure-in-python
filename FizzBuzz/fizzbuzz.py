'''
    --- Directions 
    Write a program that console logs the numbers from 1 to n. 
    but for multiples of three print "fizz" instead of the number
    and for the multiples of five print "buzz". For numbers which are multiples
    of both three and five print "fizzbuzz".

    --- examples
    fizzbuzz(5) >>
    1
    2
    fizz
    4
    buzz
'''

def fizzbuzz(numb): 
    for i in range(1, numb+1): 
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz') 
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0: 
            print('buzz')
        else: 
            print(i)

fizzbuzz(30)      

