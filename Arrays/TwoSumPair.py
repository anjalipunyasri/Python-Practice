# Given function is to check if the sum of the pair is equal to the target number or not.
# Input = [0,-1,2,-3,1]
# Target = -4
# Output = 0

# Approach 1 - It will generate all the possible pairs and checks with the target
def SumPair(array,target):
    n = len(array)
    for i in range(n):
        for j in range(i+1,n):
            if array[i]+array[j] == target:
                return True
    return False
input = [0,-1,2,-3,1]
print(SumPair(input,-4))
