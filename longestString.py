# This small program calculates the longest string in the given set of string
# And provides it's length and name.

numberOfString = int(input("How many Strings: "))
num1 = 0
lengths = []
ourString = []
extArray = []
valueOfLongestString = ""
print("\n")


def longestString(numberOne, stringCount):
    while numberOne != stringCount:
        givenString = input("Enter String here: ")
        ourString.append(givenString)
        lengthOfString = len(givenString)
        lengths.append(lengthOfString)
        numberOne = numberOne + 1
    maxLength = max(lengths)

    for ele in ourString:
        if len(ele) == maxLength:
            print("\nMax Length: " + str(maxLength) + " and the work is: " + ele)


longestString(num1, numberOfString)
