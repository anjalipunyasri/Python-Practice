# Below function is to count the consonants present in the given input string
# Input - "SWEETY"
# Output - 4
def CountingConsonants(string):
    vowels = ["A","E","I","O","U"]
    count = 0
    for character in string:
        if character not in vowels:
            count += 1
    print(count)
print(CountingConsonants("SWEETY"))

