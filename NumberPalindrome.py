# Function to check the given number is palindrome or not.
# Approach 1 - Using str() + String slicing
def NumberPalindrome(n):
    result = str(n) == str(n)[::-1]
    print(result)
NumberPalindrome(1232)

# Approach 2
n = input("Enter a number")
if n == n[::-1]:
    print(" Yes it is a palindrome")
else:
    print("No it is not a palindrome")