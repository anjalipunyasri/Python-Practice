# Append the variables in the list
# input - ['A','B']
# Output - ['A','B','C']
input_list = ['A','B']
input_list.append('C')
print(input_list)

# Append the variables in the Dictionary
# input - {'a':1,'b':2}
# output - {'a':1,'b':2,'c':3}
input_dict = {'a':1,'b':2}
input_dict['c'] = 3
print(input_dict)

# Comprehension
# List
    # input - range(1,10)
    # output - [1,2,3,4,5,6,7,8,9]
list_comp = [i for i in range(1,10)]
print(list_comp)

# Dictionary
    # input - Square the key into the value
    # output - {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
dict_comp = {i: i*i for i in range(1,10)}
print(dict_comp)

# Tuple
tuple_comp = (i for i in range(1,10))
print(tuple_comp)

