num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

print("\nEnter 1 for add\nEnter 2 for subtract\nEnter 3 for multiply\nEnter 4 for divide")
num3 = input("\nEnter what you want to do with these numbers: ")


def to_do_with_numbers(num4):  # Can use float for decimal value too
    if num4 == "1" or num4 == "+":
        num5 = int(num1) + int(num2)
        return num5
    elif num4 == "2" or num4 == "-":
        num5 = int(num1) - int(num2)
        return num5
    elif num4 == "3" or num4 == "*":
        num5 = int(num1) * int(num2)
        return num5
    elif num4 == "4" or num4 == "/":
        num5 = int(num1) / int(num2)
        return num5
    else:
        print("Wrong input!")


print("\nAnswer: " + str(to_do_with_numbers(num3)))
