# Function to calculate the minimum in the given list
# Input - ['2','6','7','9','3']
# Output - 2
# Approach 1
def MinNumList():
    list = ['2','6','7','9','3']
    min_list = min(list)
    print(min_list)
print(MinNumList())

# Input - ['2','6','7','9','3']
# Output - 2
# Approach 2
input_list = ['2','6','7','9','3']
min_list = input_list[0]
for input in input_list:
    if min_list > input:
        min_list = input
print(min_list)