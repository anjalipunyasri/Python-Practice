# Function to swap the two numbers
# Approach 1
a = 1
b = 2
a,b = b,a
print(a)
print(b)

# Approach 1 - Using function
def Swapping(a,b):
    a,b = b,a
    return a,b
print(Swapping(1,2))

# # Approach 2
temp = a
a = b
b = temp
print(a)
print(b)

# Approach 2 - Using function
def Swapping(a,b):
    temp = a
    a = b
    b = temp
    return a,b
print(Swapping(1,2))