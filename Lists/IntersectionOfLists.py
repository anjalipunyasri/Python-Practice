# Given the function is to find the intersection of the two lists.
# Input - [1, 2, 3, 4], [3, 4, 5, 6]
# Output - [3, 4]
def ListIntersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
print(ListIntersection([1, 2, 3, 4], [3, 4, 5, 6]))


