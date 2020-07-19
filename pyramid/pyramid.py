'''
* Directions   

Write a function that accepts a positive number N.
The function should console log a pyramid shape with N levels using # character. Make sure the pyramid has spaces on both the left *and* right hand sides!   

* Examples   
    Steps(1):    
        '#'
   
    steps(2):   
        ' # '
        '###'   

    steps(3):   
        '  #  '
        ' ### '
        '#####' 
'''


def pyramid_iter(n):
    space = ' '
    pound = '#'
    mid = (2*n - 1)//2
    for row in range(n):
        stair = ''
        for col in range(2*n-1):
            if mid-row <= col <= mid+row:
                stair += pound
            else:
                stair += space

        print(stair)


# pyramid_iter(5)


def pyramid_recursive(n, row=0, stair=''):
    col_length = 2*n - 1
    mid = col_length // 2
    pound = '#'
    space = ' '

    if row == n: 
        return 

    if len(stair) == col_length: 
        print(stair)
        pyramid_recursive(n, row+1)
        return 
    
    if mid-row <= len(stair) <= mid + row: 
        stair += pound
    else: 
        stair += space
    
    pyramid_recursive(n, row, stair)


pyramid_recursive(5)
