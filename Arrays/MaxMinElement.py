# Function to find the maximum and minimum element in an array
# Approach 1 - Using Max and Min functions
def MaxMinElement(array):
    max_element = max(array)
    min_element = min(array)
    return max_element,min_element
print(MaxMinElement([1,2,3,7,4,5]))

# Approach 2 - Using for loop
def MaxMinElement(array):
    n = len(array)
    max_element = array[0]
    min_element = array[0]
    for i in range(1,n):
        if array[i] > max_element:
            max_element = array[i]
        if array[i] < min_element:
            min_element = array[i]
    return max_element,min_element
print(MaxMinElement([1,2,3,4,7,1,6,9,2]))

