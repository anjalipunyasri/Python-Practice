# Below function is to count the vowels present in the given input string
# Input - "SWEETY"
# Output - 2
def CountingVowels(string):
    vowelsString = ["A","E","I","O","U"]
    count = 0
    for character in string:
        if character in vowelsString:
            count += 1
    print(count)
print(CountingVowels("SWEETY"))
