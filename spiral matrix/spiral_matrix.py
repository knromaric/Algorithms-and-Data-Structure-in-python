'''
write a function that accepts an integer N and returns a NxN SPIRAL MATRIX.    

* Examples    
    spiral_matrix(3) >>>
        [[1,2,3],
         [8,9,4],
         [7,6,5]]   
    
    spiral_matrix(4) >>>   
        [[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]
'''

from pprint import pprint 

def spiral_matrix(n):
    row_start, col_start = 0, 0
    row_end, col_end = n-1, n-1
    count = 1
    result = [[0 for x in range(n)] for y in range(n)]

    while row_start <= row_end and col_start <= col_end:
        for i in range(col_start, col_end + 1):
            result[row_start][i] = count
            count += 1

        row_start += 1

        for i in range(row_start, row_end + 1):
            result[i][col_end] = count
            count += 1

        col_end -= 1

        for i in range(col_end, col_start-1, -1): 
            result[row_end][i] = count
            count += 1

        row_end -= 1

        for i in range(row_end, row_start-1, -1): 
            result[i][col_start] = count
            count += 1

        col_start += 1

    
    pprint(result)


spiral_matrix(8)
