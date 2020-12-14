try:
    inp_1 = int(input("How many numbers you want to add to the list: "))
    numbers = []

    while inp_1 != 0:
        inp_2 = int(input("Enter number: "))
        numbers.append(inp_2)
        inp_1 = inp_1 - 1
    print("\nThe numbers you added are: " + str(numbers))

    print("\nFor add +, for multiply *")
    operator = input("Enter what operator you want to add: ")

    if operator == "+":
        print("Answer for addition: " + str(sum(numbers)))

    elif operator == "*":
        def multiply():
            result = 1
            for x in numbers:
                result = result * x
            return result

        print("Multiplication answer: " + str(multiply()))

except ValueError:
    print("Entered value is wrong!")
