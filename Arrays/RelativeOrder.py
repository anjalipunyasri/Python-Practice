# Function to give the relative order based on the array.
# If the array consists of 0 then it should be placed at the last.
# Input - [1,0,2,0,4]
# Output - [1,2,4,0,0]

def RelativeOrder(array):
    n = len(array)
    non_zero_index = 0
    for i in range(n):
        if array[i] != 0:
            array[i], array[non_zero_index] = array[non_zero_index], array[i]
            non_zero_index += 1

    return array
array = [1,0,2,0,4]
print(RelativeOrder(array))