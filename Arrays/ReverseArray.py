# Approach 1 - Using slicing
def ReverseArray(array):
    array = array[::-1]
    return array
array = [1,2,3,4,5]
print(ReverseArray(array))

# Approach 2 - Using reverse function
def ReverseArray(array):
    array.reverse()
    return array
array = [1,2,3,4,5]
print(ReverseArray(array))

# Approach 3 - Using reversed function
def ReverseArray(array):
    array = list(reversed(array))
    return array
array = [1,2,3,4,5]
print(ReverseArray(array))

# Approach 4 - Using for Loop
def ReverseArray(array):
    n = len(array)
    reversed_array = [0] * n
    for i in range(n):
        reversed_array[i] = array[n-i-1]
    return reversed_array
print(ReverseArray([1,2,3,4,5]))

# Approach 5 - Using Swapping
def ReverseArray(array):
    n = len(array)
    # reversed_array = [0] * n
    for i in range(n//2):
        array[i], array[n-i-1] = array[n-i-1], array[i]
    return array
print(ReverseArray([1,2,3,4,5]))



