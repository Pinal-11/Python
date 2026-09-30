# print ("Helllo, World!!!")

# ---Comments: notes to yourself in your code. and computer is ingore your comments. 
# ---Functions: Function is like an actions or a verb will let you to do something in the program 
# ---generally speaking. In any language comes with the predefine function it comes with actions and arguments 
# ---so here print is also the function. 
# ---"Helllo, World!!!" --> is the input of the some string. which is anything in any language.
# ---Function has some side effects so here the "print" function has one side effect is string apperiance in the screen.
# ---Bug - bug in the program its called mistake 
# ---Return Value --> 
# ---Variable --> Is just a container for some value inside of a computer or inside of your own program.
# ---single `=` sing is the assignment operator. and its work Right to Left


name = input("What is your name? ") # input is the function and it gives or handof the value to the name to reuse in future and the variable is store the value
# print("Hello")
# print(name) # because name is variable if i add double quots then it become the simple string.
# print("Hello," + name) # its got the answer but not look asthetic ==> Hello,name
# print("Hello, " + name) # Yeah this is i want => Hello, name
# --- + is not for the addition its for the concatination.


# --- Another way --
# print("Hello, ", name) # output: Hello,  Pinal #Ah, its comes with extra spaces
# print("Hello,",name) # output: Hello, Pinal # its right.


# --- print(*Objects, sep=' ', end="\n") --> its a print function default args.
# print("Hello, ", end="")
# print("Hello, ", end="$$&&") # hhh ugly output
# print(name)

# print("Hello,", name) # - it looks good
# print("Hello,", name, sep="555") # - Hello,555Pinal So now know how sep uses 


# ----- Now i want to use the double quots in the output

# print("Hello, "friends"") # -- It gives the invalid syntax error
# print("Hello, 'friends'") # -- Hello, 'friends'
# print('Hello, "Friendss"') # -- Hello, "Friendss"
# print("Hello, \"Friendss\"") # -- Hello, "Friendss"  --> "\" work as the escape charachter like it will ignore the next character after \ this.

#----- BEST Way -------

print(f"Hello, {name}") #-- Hello, Pinal
# Its a special function called formate.