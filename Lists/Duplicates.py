# Given function is to find the duplicate elements in a list
# Input - [1,2,3,4,1,2,3,4,6,5]
# Output - [1, 2, 3, 4]

# Approach 1 - Using for loop
def duplicatesList(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

print(duplicatesList([1,2,3,4,1,2,3,4,6,5]))

# Approach 2 - Using Counter
from collections import Counter
def find_duplicates(lst):
    counter = Counter(lst)
    return [key for key, value in counter.items() if value > 1]
print(find_duplicates([1,2,3,4,1,2,3,4,6,5]))