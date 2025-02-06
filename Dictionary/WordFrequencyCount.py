# Given function is to count the number of words in an dictionary
# input - it is an interesting session and it was worth joining
# output - {'it': 2, 'is': 1, 'an': 1, 'interesting': 1, 'session': 1, 'and': 1, 'was': 1, 'worth': 1, 'joining': 1}
def WordCount(input):
    words = input.split()
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word,0) + 1
    return freq_dict
text = "it is an interesting session and it was worth joining"
print(WordCount(text))