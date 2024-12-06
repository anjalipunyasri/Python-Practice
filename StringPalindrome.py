# Function to check the given string is a palindrome or not.
# Approach 1:
def StringPalindrome(s):
    return s == s[::-1]

input = "malayalam"
if StringPalindrome(input):
    print(input, "is a string palindrome")
else:
    print(input, "is not a string palindrome")

# Approach 2 - Checking on the reverse string to find out the given string is a palindrome or not.
def StringPalindrome(s):
    reverse_String = ''.join(reversed(s))
    if s == reverse_String:
        print("Given string is a palindrome")
    else:
        print("Given string is not a palindrome")
StringPalindrome("malayalam")

# Approach 3 - Using for loop
def StringPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

print(StringPalindrome("malayalam"))