# Function to calculate the max of the number in the given list
# Input - ['1','8','2','3','6','2']
# Output - 8
# Approach 1
def maximumNumberList():
    list = ['1','8','2','3','6','2']
    maxlist = max(list)
    print(maxlist)
print(maximumNumberList())

# Input - ['6','2','1','7','3']
# Output - 7
# Approach 2
input_list = ['6','2','1','7','3']
maxlist = input_list[0]
for input in input_list:
    if maxlist < input:
        maxlist = input
print(maxlist)

