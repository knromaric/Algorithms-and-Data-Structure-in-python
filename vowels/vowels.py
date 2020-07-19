'''

* Directions   

Write a function that returns the number of vowels used in a string. Vowels are the characters 'a', 'e', 'u', 'i', 'o'   

* Examples   
    vowels('Hi There') >>> 3
    vowels('Why do you ask?') >>> 4
    vowels('Why') >>> 0
'''


def vowels(s):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for ch in s.lower():
        if ch in vowels:
            count += 1

    return count


print(vowels('Hi There'))
print(vowels('Why do you ask?'))
print(vowels('Why'))
