# Below code is to calculate the product of the elements except the current index.
# Input: [1,2,3,4]
# Explanation: [2*3*4, 1*3*4, 1*2*4, 1*2*3]
# Expected output: [24, 12, 8, 6]
def ProductOfElements(array):
    n = len(array)
    answer = [1] * n

    # Compute prefix product
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= array[i]

    # Compute suffix product and combine
    suffix = 1
    for j in range(n - 1, -1, -1):
        answer[j] *= suffix
        suffix *= array[j]

    return answer

array = [1, 2, 3, 4]
result = ProductOfElements(array)
print(result)
