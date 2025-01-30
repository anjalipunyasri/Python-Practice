# Given function is to sort the array using Dutch National Flag Algorithm
# Input - [2, 1, 0, 2, 0, 1]
# Output - [0, 0, 1, 1, 2, 2]
def SortingArray(array):
    n = len(array)
    low, mid, high = 0,0,len(array)-1
    while mid <= high:
        if array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
        elif array[mid] == 1:
            mid += 1
        else:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
    return array

array = [2,1,0,2,0,1]
print(SortingArray(array))

