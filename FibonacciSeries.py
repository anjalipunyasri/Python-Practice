# Function to calculate the fibonacci series
# Input - 4
# Output - 3
def FibonacciSeries(n):
    if n < 0:
        print("Check the input properly")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return FibonacciSeries(n-1)+FibonacciSeries(n-2)
print(FibonacciSeries(4))
