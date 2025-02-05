# Given function is to sort the dictionary without using the inbuilt functions.
# Input:
# data = [
#     {"name":"abc", "age": 20},
#     {"name":"def", "age": 30},
#     {"name":"ghi", "age": 10}
# ]
# Output:
# [{'name': 'ghi', 'age': 10}, {'name': 'abc', 'age': 20}, {'name': 'def', 'age': 30}]

def BubbleSort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]
    return data
data = [
    {"name":"abc", "age": 20},
    {"name":"def", "age": 30},
    {"name":"ghi", "age": 10}
]
print(BubbleSort(data,"age"))

# Using in built sorted function
data = [
    {"name":"abc", "age": 20},
    {"name":"def", "age": 30},
    {"name":"ghi", "age": 10}
]
sorted_data = sorted(data,key = lambda x: x["age"])
print(sorted_data)