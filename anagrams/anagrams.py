'''
    --- Directions 
    Check to see if two provided strings are anagrams of eachother
    One string is anagram of another if it uses same character in 
    the same quantity. Only consider characters, not spaces or punctuations
    Consider capital letters to be the same as lower letters

    --- examples
    anagrams('rail safety', 'fairy tales') --> True
    anagrams('RAIL! SAFETY!',  'fairy tales') --> True
    anagrams('Hi There', 'Bye there') --> False
'''

def anagrams(string_a, string_b): 
    char_map_a = build_char_map(string_a)
    char_map_b = build_char_map(string_b)

    if len(char_map_b.keys()) != len(char_map_a.keys()):
        return False

    for char in char_map_a.keys(): 
        if char_map_a[char] != char_map_b[char]:
            return False
    
    return True

def anagrams_v1(string_a, string_b): 
    clean_string_a = ''.join(sorted([e for e in string_a.lower() if e.isalnum()]))
    clean_string_b = ''.join(sorted([e for e in string_b.lower() if e.isalnum()]))
    print(clean_string_a, clean_string_b)
    return clean_string_a == clean_string_b



def build_char_map(string): 
    char_map = {}

    for char in string.lower(): 
        char_map[char] = char_map[char]+1 if char in char_map and char.isalnum() else 1

    return char_map


# Testing

print(anagrams('rail safety', 'fairy tales') )
print(anagrams('RAIL! SAFETY!',  'fairy tales'))
print(anagrams('Hi There', 'Bye there') )

print(anagrams_v1('rail safety', 'fairy tales') )
print(anagrams_v1('RAIL! SAFETY!',  'fairy tales'))
print(anagrams_v1('Hi There', 'Bye there') )