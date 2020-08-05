'''
    write a recursive function which takes an integer and computes the cumulative sum
    of 0 to that integer

    for example: if n=4 > return 4+3+2+1+0 which is 10
'''

def rec_sum(n): 
    if n == 0: 
        return 0 

    return n+rec_sum(n-1)    

# Testing: rec_sum
# print(rec_sum(4))


'''
    Given an integer, create a function which returns the sum of all the individual
    digits in that integer. For example: if n=4321, return 4+3+2+1
'''

def sum_func(n): 
    if n//10 == 0: 
        return n

    return n%10 + sum_func(n//10)

# Testing: sum_func
# print(sum_func(4321)) 



'''
    create a function called word_split() which takes in an string phrase and a set
    list_of_words. The function will then determine if it is possible to split the string 
    in a way in which words can be made from the list of words. You can assume the phrase
    will only contain words found in the list_of_words if it is completely splittable

    for example: 
    word_split('themanran', ['the', 'ran', 'man']) 
            >> ['the', 'ran', 'man']
    word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John'])
            >> ['i', 'love', 'dogs', 'John']

    
'''


def word_split(phrase, list_of_words, output=None):
    
    if output is None: 
        output = []

    for word in list_of_words:

        if phrase.startswith(word): 
            output.append(word)

            return word_split(phrase[len(word):], list_of_words, output)

    return output


# Testing: word_split

print(word_split('themanran', ['the', 'ran', 'man']) )
print(word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']))
print( word_split('themanran', ['clown', 'ran', 'man']))