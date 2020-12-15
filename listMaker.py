try:
    inp_1 = int(input("Enter number of entries: "))

    A = []
    Q = 0
    while Q != inp_1:
        inp_2 = input("Enter name(s): ")
        A.append(inp_2)
        Q = Q + 1

    print("")
    for nme in A:
        print("  " + nme)

    sing = input("\nFor write enter w, for alter a: ")

    if sing == "w":
        names = open("names.txt", "w")
        S = 0
        n = 0
        while S != inp_1:
            names.write("\n " + A[n])
            S = S + 1
            n = n + 1
        names.close()

    elif sing == "a":
        names = open("names.txt", "a")
        S = 0
        n = 0
        while S != inp_1:
            names.write("\n " + A[n])
            S = S + 1
            n = n + 1
        names.close()

except ValueError:
    print("Wrong something!")
