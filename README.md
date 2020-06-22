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
