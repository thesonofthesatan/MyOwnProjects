#Makeing a program which takes in two ints and does calculations. 
#These calculations includes - Addition, Subtraction, Multiplication and Division.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

num3 = (num1 * num2)
num4 = (num1 + num2)
num5 = (num1 - num2)
num6 = (num1 / num2)

print("\nChose which output you need")
print("1 for multiply")
print("2 for addition")
print("3 for subtraction")
print("4 for division")
print("")

inp1 = int(input("Enter here: "))
print("")

if(inp1 == 1):
    print("Answer = ", num3)

elif(inp1 == 2): 
    print("Answer = ", num4)
    
elif(inp1 == 3): 
    print("Answer = ", num5)

elif(inp1 == 4): 
    print("Answer = ", num6)
    
else:
    print("Wrong Option")
