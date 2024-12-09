# Below function is to count the occurance given input string
# Input - "SWEETY"
# occurance check = "S
# Output - 1
def CountingOccuranceString(string):
    occurance_check = "S"
    count = 0
    for letter in string:
        if letter == occurance_check:
            count += 1
    print(count)
print(CountingOccuranceString("SWEETY"))

