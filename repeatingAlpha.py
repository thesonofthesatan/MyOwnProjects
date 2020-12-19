# Tells you the repeating term in a String

inp_1 = input("Enter a value: ")


try:
    def find_moving(STQ):
        Y = {}
        for PQ in STQ:
            if PQ in Y:
                return PQ
            else:
                Y[PQ] = 0

    print("Repeating term in the provided String is: " + find_moving(inp_1))

except:
    print("No match found!")
