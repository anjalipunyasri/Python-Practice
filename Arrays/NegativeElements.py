# Given function is to move all the negative elements to one side in the array
# Input - [-1,0,3,-2,0]
# Output - [-1,-2,3,0,0]
def NegativeElements(array):
    n = len(array)
    low = 0
    for high in range(n):
        if array[high] < 0:
            array[low], array[high] = array[high], array[low]
            low += 1
    return array
print(NegativeElements([-1,0,3,-2,0]))