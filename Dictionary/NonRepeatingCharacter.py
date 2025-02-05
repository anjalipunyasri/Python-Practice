# Given function is to check the first non repeating character
# Input - aabblcacadnahdfafh
# Output - l
def NonRepeatingCharacter(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char,0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

print(NonRepeatingCharacter('aabblcacadnahdfafh'))
