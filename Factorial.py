# Function to calculate the factorial of a given number
# input - 5
# output - 120
def factorial(n):
    result = 1
    return 1 if (n == 0 or n == 1) else n * factorial(n-1)

print(factorial(5))
