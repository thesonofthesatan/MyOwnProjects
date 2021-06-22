import random

a1 = 0
a2 = 0
a3 = 0

b1 = 0
b2 = 0
b3 = 0

c1 = 0
c2 = 0
c3 = 0

computerInput1 = ''

while a1 == 0 or a2 == 0 or a3 == 0 or b1 == 0 or b2 == 0 or b3 == 0 or c1 == 0 or c2 == 0 or c3 == 0:
    print(str(a1) + " " + str(a2) + " " + str(a3))
    print(str(b1) + " " + str(b2) + " " + str(b3))
    print(str(c1) + " " + str(c2) + " " + str(c3))
    playerInput = raw_input("Enter the location: ")
    computerInput = random.randint(1, 9)

    if a1 == 0 and playerInput == 'a1':
        a1 = 1
    elif a2 == 0 and playerInput == 'a2':
        a2 = 1
    elif a3 == 0 and playerInput == 'a3':
        a3 = 1
    elif b1 == 0 and playerInput == 'b1':
        b1 = 1
    elif b2 == 0 and playerInput == 'b2':
        b2 = 1
    elif b3 == 0 and playerInput == 'b3':
        b3 = 1
    elif c1 == 0 and playerInput == 'c1':
        c1 = 1
    elif c2 == 0 and playerInput == 'c2':
        c2 = 1
    elif c3 == 0 and playerInput == 'c3':
        c3 = 1
    else:
        print("Invalid Input. Chance = -1")

    if a1 == 0 and computerInput == 1:
        a1 = 2
        computerInput1 = 'a1'
    elif a2 == 0 and computerInput == 2:
        a2 = 2
        computerInput1 = 'a2'
    elif a3 == 0 and computerInput == 3:
        a3 = 2
        computerInput1 = 'a3'
    elif b1 == 0 and computerInput == 4:
        b1 = 2
        computerInput1 = 'b1'
    elif b2 == 0 and computerInput == 5:
        b2 = 2
        computerInput1 = 'b2'
    elif b3 == 0 and computerInput == 6:
        b3 = 2
        computerInput1 = 'b3'
    elif c1 == 0 and computerInput == 7:
        c1 = 2
        computerInput1 = 'c1'
    elif c2 == 0 and computerInput == 8:
        c2 = 2
        computerInput1 = 'c2'
    elif c3 == 0 and computerInput == 9:
        c3 = 2
        computerInput1 = 'c3'
    else:
        print("Wrong input by computer.")

    print("computer played - " + str(computerInput1))

    if a1 == a2 == a3 == 1:
        print("Player win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif b1 == b2 == b3 == 1:
        print("Player win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif c1 == c2 == c3 == 1:
        print("Player win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif a1 == b1 == c1 == 1:
        print("Player win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif a2 == b2 == c2 == 1:
        print("Player win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif a3 == b3 == c3 == 1:
        print("Player win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif a1 == b2 == c3 == 1:
        print("Player win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif c1 == b2 == a3 == 1:
        print("Player win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif a1 == a2 == a3 == 2:
        print("Computer win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif b1 == b2 == b3 == 2:
        print("Computer win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif c1 == c2 == c3 == 2:
        print("Computer win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif a1 == b1 == c1 == 2:
        print("Computer win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif a2 == b2 == c2 == 2:
        print("Computer win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif a3 == b3 == c3 == 2:
        print("Computer win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif a1 == b2 == c3 == 2:
        print("Computer win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
    elif c1 == b2 == a3 == 2:
        print("Computer win")
        print(str(a1) + " " + str(a2) + " " + str(a3))
        print(str(b1) + " " + str(b2) + " " + str(b3))
        print(str(c1) + " " + str(c2) + " " + str(c3))
        exit()
