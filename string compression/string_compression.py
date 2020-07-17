'''
* Directions  

Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it 
to become 'A4B4C5D2E4'. For this problem, you can falsely 
"compress" strings of single or double letters. for instance, 
It is okay for 'AAB' to return 'A2B1' even though this technically 
takes more spaces   

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'

'''


def string_compression(s):
    str_map = {}
    str_compressed = ''

    if len(s) == 0:
        return ''

    if len(s) == 1:
        return s + '1'

    for ch in s:
        if ch in str_map:
            str_map[ch] += 1
        else:
            str_map[ch] = 1

    for ch in str_map:
        str_compressed += str(ch) + str(str_map[ch])

    return str_compressed


def string_compression_1(s):
    run = ''
    length = len(s)

    if length == 0:
        return ""

    if length == 1:
        return s + '1'

    count = 1
    i = 1

    while i < length:
        if s[i] == s[i-1]:
            count += 1
        else:
            run = run + s[i-1] + str(count)
            count = 1

        i += 1

    run = run + s[i-1] + str(count)

    return run


print(string_compression_1('AAAABBBBCCCCCDDEEEE'))
print(string_compression_1('AAAaaa'))
