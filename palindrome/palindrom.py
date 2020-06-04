'''
    given a string, return true if the string is a palindrome 
    or false if it is not. Palindromes are string that form
    the same word if it is reversed.
    **Do not include spaces and punctuation in determining if 
    the string is a palindrome.

    --- examples: 
        palindrome("abba") -> True
        palindrome("abcde") -> False
'''

def palindrome_v1(text): 
    reversed = text[::-1]
    return reversed == text

def palindrome_v0(text): 
    for i in range(len(text)): 
        if text[i] != text[-i-1]: 
            return False
    return True



print(palindrome_v1('abba'))
print(palindrome_v1('absc'))
