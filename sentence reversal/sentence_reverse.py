'''
* Directions   

Given a string of words, reverse all the words.   

* Examples: 

    'welcome to python land' >>> 'land python to welcome'
'''


def reverse_sentence1(s):
    return ' '.join(reversed(s.split()))


def reverse_sentence2(s):
    return ' '.join(s.split()[::-1])


def reverse_sentence4(s):
    text_to_array = s.split()
    text_reversed = ''
    for word in text_to_array:
        text_reversed = word + ' ' + text_reversed

    return text_reversed.strip()


def reverse_sentence(s):
    words = []
    length = len(s)
    space = ' '

    i = 0

    while i < length:

        if s[i] != space:
            word_start = i

            while i < length and s[i] != space:
                i += 1

            words.append(s[word_start: i])

        i += 1

    return ' '.join(reversed(words))


print(reverse_sentence('welcome to python land'))
print(reverse_sentence('This is the best'))
print(reverse_sentence('   space here      '))
