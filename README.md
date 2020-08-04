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


### Largest Continuous Sum 

* Directions   

Given an array of integers(positive and negative) find the largest continous sum.   

* Examples    

large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) >>>  29   

### Sentence Reversal 

* Directions   

Given a string of words, reverse all the words.   

* Examples: 
    'welcome to python land' >>> 'land python to welcome'

### String compression

* Directions   
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. for instance, It is okay for 'AAB' to return 'A2B1' even though this technically takes more spaces   

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'



### Unique Characters In String

* Directions   

Given a string, determine if it is compreised of all unique characters.   

* Examples:   
    uni_char('abcde') >>> True   
    uni_char('aabcd') >>> False

### Build STEPS 

* Directions   

Write a function that accepts a positive number N.
The function should console log a step shape with N levels using # character. Make sure the step has spaces on the right hand side!   

* Examples   
    Steps(2):    
        '# '
        '##'   
    steps(3):   
        '#  '
        '## '
        '###'   
    steps(4):   
        '#   '
        '##  '
        '### '
        '####'    

### Build pyramid shape 

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

### Vowels   

* Directions   

Write a function that returns the number of vowels used in a string. Vowels are the characters 'a', 'e', 'u', 'i', 'o'   

* Examples   
    vowels('Hi There') >>> 3
    vowels('Why do you ask?') >>> 4
    vowels('Why') >>> 0


### Spiral Matrix 

* Directions   

write a function that accepts an integer N and returns a NxN SPIRAL MATRIX.    

* Examples    
    spiral_matrix(3) >>>
        [[1,2,3],
         [8,9,4],
         [7,6,5]]   
    
    spiral_matrix(4) >>>   
        [[1, 2, 3, 4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9, 8, 7]]


### Stack class implementation 

A stack is defined as an ordered collection of items where items are added to and removed from the end called the "top". Stacks are ordered LIFO(Last In First Out). The stack operations are given below.   

* **stack()** creates a new stack that is empty. it returns an empty stack    
* **push(item)** adds a new item to the top of the stack. it takes the item and returns nothing   
* **pop()** removes the top item from teh stack. it needs no parameters and returns the item. The stack is modified.   
* **peek()** returns the top item from the stack but does not remove it. It needs no parameters. the stack is not modified   
* **is_empty()** tests to see whether the stack is empty. it needs no parameters and returns a boolean value   
* **size()** returns the number of items on the stack. it needs no parameters and returns an integer.   

### Queue class implementation  

our Queue class must contain the following methods :   
* **Queue()** creates a new queue that is empty and returns and empty queue

* **enqueue(item)** adds a new item to the rear of the queue. it needs the item and returns nothing. 
* **is_empty()** tests to see whether the queue is empty. it needs no parameters and returns a boolean value.   
* **size()** returns the number of items in the queue. it needs no parameters and returns an integer.   

### Deque class implementation  

here are the Deque methods and Attributes:    
* Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.  
* addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.  
* addRear(item) adds a new item to the rear of the deque. it needs the item and returns nothing .
* removeFront() removes the front item from the deque. it takes no parameters and return the item. The deque is modified.
* removeRear() removes the rear item from the Deque. it needs no parameters and returns the item. The deque is modified 
* isEmpty() test to see whether the deque is empty. it takes no parameters and returns a boolean value   
* size() returns the number of items in the deque. it needs no parameters and returns an integer.   


### Balanced Parenthesis Check

* Directions 

Given a string of opening and closing parentheses, check whether it's balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. Assume that the string doesn't contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example '([]) is balanced but '([)]' is not.

You can assume the input string has no spaces.   

### Implement a Queue - Using Two Stacks

Given the stack class below, Implement a queue class using two stacks! Use a python list data structure as your stack. 


### Singly Linked List Implementation   

A singly linked list - an ordered list of items as individual Nodes that have pointers to other Nodes. Here we implement the Node class.   

### Doubly Linked List Implementation

Implementation of doubly linked list


### Singly Linked List Cycle Check

* Directions   
Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.   


### Linked List Reversal

* Directions   
Write a function to reverse a Linked List in place. The function will take in the head of the list as input and return the new head of list.     




### Linked List Nth to Last Node

Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list.



