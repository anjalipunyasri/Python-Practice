# Given function is to rotate the list by k position
# Input - [1,2,3,4,5], k = 3
# Output - [3,4,5,1,2]
def RotateList(lst,k):
    n = len(lst)
    k = k % n
    return lst[-k:] + lst[:-k]
print(RotateList([1,2,3,4,5],3))