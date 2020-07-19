'''
* Directions   

Given a string, determine if it is compreised of all unique characters.   

* Examples:   
    uni_char('abcde') >>> True   
    uni_char('aabcd') >>> False
'''


def uni_char_v1(s):
    return len(s) == len(set(s))


def uni_char(s):
    temp_list = []
    for ch in s:
        if ch not in temp_list:
            temp_list.append(ch)
        else:
            return False
    return True


print(uni_char_v1('abcde'))
print(uni_char_v1('aabcd'))
