'''
* Directions  

Consider an array of non-negative integers. A second array is formed by 
shuffling the elements of the first array and deleting a random element.
Given these two arrays, find which element is missing in the second array.  

* Examples  

Here is an example input, the first array is shuffled and the number 5 is 
removed to construct the second array.   

    **input**
    finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

    **output**
    >> 5 is the missing number
'''
from collections import defaultdict


def finder1(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


def finder2(arr1, arr2):
    for num in arr2:
        if num in arr1:
            arr1.remove(num)

    return arr1[0]


def finder3(arr1, arr2):
    d = defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


def finder4(arr1, arr2):
    result = 0

    # perform an XOR between the numbers in the arrays
    for num in arr1 + arr2:
        result ^= num
        #print(result)

    return result


# arr1 = [1, 2, 3, 4, 5, 6, 7]
# arr2 = [3, 7, 2, 1, 4, 6]
# print(finder4(arr1, arr2))

arr1 = [5, 5, 7, 7]
arr2 = [5, 5, 7]
print(finder4(arr1, arr2))
