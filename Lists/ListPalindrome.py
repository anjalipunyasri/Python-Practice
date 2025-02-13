# Given function to find the given list is palindrome or not.
# Input - [1,2,3,2,1]
# Output - Palindrome
def ListPalindrome(lst):
    n = len(lst)
    pal_lst = lst[::-1]
    if lst == pal_lst:
        print("palindrome")
    else:
        print("not a palindrome")
print(ListPalindrome([1,2,3,2,1,4]))