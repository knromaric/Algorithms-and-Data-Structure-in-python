'''
    --- Directions 
    given a string, return the character that is most commonly used in the string 
    --- examples
    max_char('abccccccc') -> 'c'
    max_char('apple 1231111') -> '1'
'''

def max_char(string): 
    char_map = {}

    for char in string: 
        if char in char_map: 
            char_map[char] += 1
        else:
            char_map[char] = 1

    ordered_char = sorted(char_map.items(), key=lambda val: val[1], reverse=True)

    return ordered_char[0][0]

def max_char_v2(string): 
    char_map = {}

    for char in string: 
        char_map[char] = 1 if char not in char_map else char_map[char] + 1

    # ordered the char_map by count value in descending 
    ordered_char = sorted(char_map.items(), key=lambda val: val[1], reverse=True)

    #return the character with the highest count value
    return ordered_char[0][0]

def max_char_v3(string): 
    char_map = {}
    max = 0
    char_result = ''

    for char in string: 
        char_map[char] = 1 if char not in char_map else char_map[char] + 1

    for char, char_count in char_map.items(): 
        if char_count > max: 
            max = char_count
            char_result = char

    return char_result

print(max_char('abccccccc'))
print(max_char('apple 1231111'))

print(max_char_v2('abccccccc'))
print(max_char_v2('apple 1231111'))

print(max_char_v3('abccccccc'))
print(max_char_v3('apple 1231111'))