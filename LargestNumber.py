# Function to get the largest number
# input - 5,10,3
# Output = 10 is the largest number
def LargestNumber(a,b,c):
    if a > b and a > c:
        print(a, "is the largest number")
    elif b > a and b > c:
        print(b, "is the largest number")
    elif c > a and c > b:
        print(c, "is the largest number")
LargestNumber(5,10,3)