# Algorithms-and-Data-Structure-in-python

Here are some popular algorithms and data structures with in python

### reverse string
given a string, return a new string with 
    the reversed order of characters
    - examples
    reverse('apple') === 'elppa'

### Palindrome
given a string, return true if the string is a palindrome or false if it is not. Palindromes are string that formthe same word if it is reversed.

**Do not include spaces and punctuation in determining if the string is a palindrome**

 * examples   

palindrome("abba") -> True  

palindrome("abcde") -> False

### Reverse Integers

Given an integer, return an integer that is the reverse ordering numbers.

* examples:

reverse_int(15) -> 51  

reverse_int(981) -> 189   

reverse_int(500) -> 5   

reverse_int(-15) -> -51   

reverse_int(-90) -> -9   

### Finding the most repetitive character in a string
 * Directions   

given a string, return the character that is most commonly used in the string   

 * examples:   

max_char('abccccccc') -> 'c'  

max_char('apple 1231111') -> '1'

### FizzBuzz problem

* Directions  

Write a program that console logs the numbers from 1 to n. but for multiples of three print "fizz" instead of the number and for the multiples of five print "buzz". For numbers which are multiples of both three and five print "fizzbuzz".

* examples  

fizzbuzz(5) >>
1
2
fizz
4
buzz

### Chunking array

* Directions  

Given an array and chunk size, divide the array into many subarrays where each subarray is of length size

* examples  

chunk([1,2,3,4], 2) --> [[1, 2], [3, 4]]  

chunk([1,2,3,4,5], 2) --> [[1,2], [3, 4], [5]]  

chunk([1,2,3,4,5,6,7,8], 3) -->[[1,2,3],[4,5,6],[7,8]]  

chunk([1,2,3,4,5], 4) --> [[1,2,3,4],[5]]  

chunk([1,2,3,4,5], 10) --> [[1,2,3,4,5]]  

### Anagrams problem  

* Directions   

Check to see if two provided strings are anagrams of eachother
One string is anagram of another if it uses same character in 
the same quantity. Only consider characters, not spaces or punctuations
Consider capital letters to be the same as lower letters

* examples  

anagrams('rail safety', 'fairy tales') --> True  

anagrams('RAIL! SAFETY!',  'fairy tales') --> True  

anagrams('Hi There', 'Bye there') --> False   


### Capitalize 
* Directions
Write a function that accepts a string. The function should capitalize
the first letter of each word in the string then return the capitalized 
string 

* examples
capitalize('a short sentence') ---> 'A Short Sentence'  

capitalize('a lazy fox') ---> 'A Lazy Fox'  

capitalize('look, it is working!') ---> 'Look, It Is Working!'



### Dynamic Array (list-like)
* Directions
Create a custom Dynamic array class!
Use the built in library (ctypes). check out the documentation for more info. but its basically going to be used here as a raw array from the ctypes module.   

** create methods **

* len - to get the length of the array
* append - to add element to array
* _resize - private method to resize the array.


### Array Pair of sum
* Directions
Given an integer array, output all the **unique** pairs that sum up to a specific value **k**.  

so the input:   
        pair_sum([1,3,2,2], 4)  

would return **2 pairs**:   
        (1,3)  
        (2,2)

### Find The Missing Element   

* Directions  

Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.  

* Examples  

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.   

    **input**
    finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

    **output**
    >> 5 is the missing number

