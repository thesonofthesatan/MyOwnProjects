import random

fun_factor = random.randint(0, 100)


def looping(string):
    for mayur in range(fun_factor):
        r_fact = random.randint(0, 5)
        P = ["      ", "         ", "     ", "-", "--", "---"]
        S = str(P[r_fact])
        print(S + " | ")
        if r_fact == 3:
            print("       " + S)


def looping_2(string):
    Z = fun_factor
    while Z != 0:
        r_fact = random.randint(0, 5)
        P = ["      ", "         ", "     ", "-", "--", "---"]
        S = str(P[r_fact])
        Z = Z - 1
        print(S + " | ")
        if r_fact == 3:
            print("   " + S)
    return Z


print("")
looping(" ")
print("")
looping_2(" ")
