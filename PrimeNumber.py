# Function to check if the given number is prime or not
# input - 4
# Output - Prime number
def PrimeNumber(n):
    if n == 0 and n == 1:
        print("Not a prime number",n)
    elif n > 1:
        for i in range(2,n):
            if n % i == 0:
                print(n, "Not a prime Number")
                break
        else:
            print(n, "is a Prime Number")
    else:
        print(n,"is not a prime number")

PrimeNumber(7)