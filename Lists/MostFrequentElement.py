# Given function is to find the most frequent element in a list.
# Input - [1,2,3,4,1,3,2,1]
# Ouput - 1
from collections import Counter
def MostFrequent(lst):
    return Counter(lst).most_common(1)[0][0]
print(MostFrequent([1,2,3,4,1,3,2,1]))
