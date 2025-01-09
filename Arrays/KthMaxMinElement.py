# Function to find the kth min and max in the given array
# Scenario - If k =4 it should pick the 4th place of both min and max
# k=4, input --> [1,2,3,4,5,6,7,8], Output --> max = 5, min = 4

# Approach 1 - Using Sorting
def KthMaxMinElement(array,k):
    n = len(array)
    array.sort()
    kth_min = array[k-1]
    kth_max = array[-k]
    return kth_max,kth_min
print(KthMaxMinElement([4,2,6,8,3,1,7,5],4))

# Approach 2 - Min-Heap
import heapq
# Finding large element
def KthMaxElement(array,k):
    return heapq.nlargest(k,array)[-1]
print(KthMaxElement([4,2,6,8,3,1,7,5],4))

# Finding small element
def KthMinElement(array,k):
    return heapq.nsmallest(k,array)[-1]
print(KthMinElement([4,2,6,8,3,1,7,5],4))

# Approach 3 - Using for loop
# Finding small element
def KthMinElement(array,k):
    for i in range(k):
        min_element = float('inf')
        for num in array:
            if num < min_element:
                min_element = num
        array.remove(min_element)
    return min_element
print(KthMinElement([1,0,3,5,2],2))

# Finding large element
def KthMaxElement(array,k):
    for i in range(k):
        max_element = float('-inf')
        for num in array:
            if num > max_element:
                max_element = num
        array.remove(max_element)
    return max_element
print(KthMaxElement([1,2,3,4,5,7,6],2))
