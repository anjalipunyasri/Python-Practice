# Given function is to find the second largest element in the list.
# Approach 1 - Using bubble sort
# Input - ['2','1','3']
# Output - 2
def SecondLargest(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[i] > list[j+1]:
                list[i], list[j+1] = list[j+1],list[i]
    return list[1]
print(SecondLargest(['2','1','3']))

# Approach 2 - Using if else condition
def SecondLargest(list):
    first, second = float('-inf'), float('-inf')
    for num in list:
        if num > first:
            second, first = first, num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None
print(SecondLargest([2,1,3]))
