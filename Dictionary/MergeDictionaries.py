# Given function to merge two dictionaries. If a key exists in both, sum their values.
# Input:
# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 15, 'c': 25, 'd': 40}

# Output: {'a': 10, 'b': 35, 'c': 55, 'd': 40}

def MergeDictionaries(dict1, dict2):
    merge_dict = dict1.copy()
    for key, value in dict2.items():
        merge_dict[key] = merge_dict.get(key,0) + value
    return merge_dict
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 40}

print(MergeDictionaries(dict1, dict2))