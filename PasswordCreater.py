#A program which creates Passwords and keeps it for you
import random

input1 = (input("Enter a word which will be converted to your password: ")) #Asking a word
input1 = input1.lower() #Lowering the cases

# Took help from geekforgeeks

def reverseWordNewWord(NewWord): 
 
   words = NewWord.split(" ") 
     
   newWords = [word[::-1] for word in words] 

   newNewWord = " ".join(newWords) 
 
   return newNewWord

#replace this segment = (input1.replace("from this", "two this")) 
input1 = (input1.replace("s", "$")) 
input1 = (input1.replace("a", "@"))
input1 = (input1.replace("h", "#"))
input1 = (input1.replace("i", "!"))
input1 = (input1.replace("r", "&"))
input1 = (input1.replace("p", "9"))
input1 = (input1.replace("b", "6")) 
input1 = (input1.replace("l", "1"))
input1 = (input1.replace("o", "0"))
    
NewWord = input1

print("")
 
print("New Password = ", reverseWordNewWord(NewWord), random.randrange(10, 1000, 7)) #From, to, difference between numbers

typeis = reverseWordNewWord(NewWord), random.randrange(10, 1000, 7) #To be continude

"""
Part 2 will be a program where the user has the has the option to save the password with a certain tag. Example, $t@&173 for Facebook
"""