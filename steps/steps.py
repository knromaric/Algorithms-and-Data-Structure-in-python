'''
* Directions   

Write a function that accepts a positive number N.
The function should console log a step shape with N 
levels using # character. Make sure the step has spaces on the 
right hand side!   

* Examples   
    Steps(2):    
        '# '
        '##'   
    steps(3):   
        '#  '
        '## '
        '###'   
    steps(3):   
        '#   '
        '##  '
        '### '
        '####' 
'''


def steps(n):
    if n < 0:
        return 'Argument should be a positive integer'

    if n < 2:
        return '#'

    space = ' '
    pound = '#'

    for i in range(1, n+1):
        stair = ''
        for j in range(1, n+1):
            if j <= i:
                stair += pound
            else:
                stair += space
        print(stair)


# steps(5)



def steps_recursive(n, row=0, stair=''): 
    if n == row: 
        return 
    
    if n == len(stair): 
        print(stair)
        steps_recursive(n, row+1)
        return

    if len(stair) <= row: 
        stair += '#'
    else: 
        stair += ' '
    
    steps_recursive(n, row, stair)


steps_recursive(5)

    
