"""
--- Directions 
Given an array and chunk size, divide the array into many
subarrays where each subarray is of length size

--- examples
chunk([1,2,3,4], 2) --> [[1, 2], [3, 4]]
chunk([1,2,3,4,5], 2) --> [[1,2], [3, 4], [5]]
chunk([1,2,3,4,5,6,7,8], 3) -->[[1,2,3],[4,5,6],[7,8]]
chunk([1,2,3,4,5], 4) --> [[1,2,3,4],[5]]
chunk([1,2,3,4,5], 10) --> [[1,2,3,4,5]]

"""

def chunk(array, size): 
    chunked = []

    for item in array: 
        if len(chunked) == 0 or len(chunked[-1]) == size:
            chunked.append([item])
        else: 
            chunked[-1].append(item) 

    return chunked


def chunk_v2(array, size): 
    chunked = []
    index = 0

    while index < len(array): 
        chunked.append(array[index : index + size])
        index += size
    
    return chunked

## Testing
print(chunk([1,2,3,4], 2))
print(chunk([1,2,3,4,5], 2))
print(chunk([1,2,3,4,5,6,7,8], 3))
print(chunk([1,2,3,4,5], 4))
print(chunk([1,2,3,4,5], 10))

print(chunk_v2([1,2,3,4], 2))
print(chunk_v2([1,2,3,4,5], 2))
print(chunk_v2([1,2,3,4,5,6,7,8], 3))
print(chunk_v2([1,2,3,4,5], 4))
print(chunk_v2([1,2,3,4,5], 10))






