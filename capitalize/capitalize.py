'''
    --- Directions
    Write a function that accepts a string. The function should capitalize
    the first letter of each word in the string then return the capitalized 
    string 

    --- examples
    capitalize('a short sentence') ---> 'A Short Sentence'
    capitalize('a lazy fox') ---> 'A Lazy Fox'
    capitalize('look, it is working!') ---> 'Look, It Is Working!'

'''

# Using the capitalize() function
def capitalize(text): 
    return  ' '.join([s.capitalize() for s in text.split()])

def capitalize_v2(text): 
    words_list_cap = []
    for word in text.split(): 
        words_list_cap.append(word[0].upper() + word[1:])
    
    return ' '.join(words_list_cap)

# Testing 

print(capitalize('a short sentence') )
print(capitalize('a lazy fox') )
print(capitalize('look, it is working!') )

print(capitalize_v2('a short sentence') )
print(capitalize_v2('a lazy fox') )
print(capitalize_v2('look, it is working!') )
