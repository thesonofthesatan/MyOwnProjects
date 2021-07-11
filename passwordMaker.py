# GUI remaining to be made

from Tkinter import *
root = Tk()

passwordInput = raw_input("Enter the password hint (with a space within each letter): ")
passwordHint = raw_input("Enter password (with a space within each letter): ")


class passwordMaker:
    def __init__(self):
        pass

    breakPasswordInput = passwordInput.split()
    print breakPasswordInput
    for characters in breakPasswordInput:
        if characters == 'a' and 'A':
            print("b")
        elif characters == 'b' and 'B':
            print("c")
        elif characters == 'c' and 'C':
            print("@")
        elif characters == 'd' and 'D':
            print("&")
        elif characters == 'e' and 'E':
            print("#")
        elif characters == 'f' and 'F':
            print("t")
        elif characters == 'g' and 'G':
            print("f")
        elif characters == 'h' and 'H':
            print("E")
        elif characters == 'i' and 'I':
            print("1")
        elif characters == 'j' and 'J':
            print("i")
        elif characters == 'k' and 'K':
            print(")")
        elif characters == 'l' and 'L':
            print(">")
        elif characters == 'm' and 'M':
            print("w")
        elif characters == 'n' and 'N':
            print("<")
        elif characters == 'o' and 'O':
            print("0")
        elif characters == 'p' and 'P':
            print("9")
        elif characters == 'q' and 'Q':
            print("/")
        elif characters == 'r' and 'R':
            print("v")
        elif characters == 's' and 'S':
            print("$")
        elif characters == 't' and 'T':
            print("l")
        elif characters == 'u' and 'U':
            print("[")
        elif characters == 'v' and 'V':
            print("!")
        elif characters == 'w' and 'W':
            print("-")
        elif characters == 'x' and 'X':
            print("%")
        elif characters == 'y' and 'Y':
            print("4")
        elif characters == 'z' and 'Z':
            print("#")
        else:
            print("Unrecognized Input")


class passwordDecoder:

    def __init__(self):
        pass

    breakPasswordHint = passwordHint.split()
    print breakPasswordHint
    for characters in breakPasswordHint:
        if characters == 'b' and 'B':
            print("a")
        elif characters == 'c' and 'C':
            print("b")
        elif characters == '@':
            print("c")
        elif characters == '&':
            print("d")
        elif characters == '#':
            print("e")
        elif characters == 't' and 'T':
            print("f")
        elif characters == 'f' and 'F':
            print("g")
        elif characters == 'e' and 'E':
            print("h")
        elif characters == '1':
            print("i")
        elif characters == 'i' and 'I':
            print("j")
        elif characters == ')':
            print("k")
        elif characters == '>':
            print("l")
        elif characters == 'w' and 'W':
            print("m")
        elif characters == '<':
            print("n")
        elif characters == '0':
            print("0")
        elif characters == '9':
            print("p")
        elif characters == '/':
            print("q")
        elif characters == 'v' and 'V':
            print("r")
        elif characters == '$':
            print("s")
        elif characters == 'l' and 'L':
            print("t")
        elif characters == '[':
            print("u")
        elif characters == '!':
            print("v")
        elif characters == '-':
            print("w")
        elif characters == '%':
            print("x")
        elif characters == '4':
            print("y")
        elif characters == '#':
            print("Z")
        else:
            print("Unrecognized Input")


passwordMaker()
passwordDecoder()

myLabel = Label(root, text=passwordHint)
myLabel.pack()
root.mainloop()
