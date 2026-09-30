# x = 1
# y = 2
# z = x + y
# print(z)  -> output is 3

#------------------------------------------------#

# x = input("What's X? ")     # 3
# y = input("What's Y? ")     # 2
# z = x + y

# print(z)    # output 32 why not 5 ?? because bydefault the input is the sting (text)

#--------------------------------------------------#


# x = input("What's X? ")     # 3
# y = input("What's Y? ")     # 2
# z = int(x) + int(y)

# print(z)    # output 5

#----------------------------------------------------#

# x = input("What's X? ")     # 3
# y = input("What's Y? ")     # 2
# print(x + y)    # output 32

#----------------------------------------#

# x = int(input("What's X? "))     # 3
# y = int(input("What's Y? "))     # 2
# print(x + y)    # output 5


#---------------------FLOAT-----------------#

# i = float(input("Enter Number for I: "))
# j = float(input("Enter Number for J: "))

# k = round(i + j)
# print(f"{k:,}")
# # print(round(i + j))

#-------------FLoat with roundup---------------

i = float(input("Enter Number for I: "))
j = float(input("Enter Number for J: "))

#k = round(i/j, 2) # this use for the how many digits yoi want after decimal point.

k = i / j
print(f"{k:.4f}") # this is also the same how many digits you want to print after decimal so add the number accordingly 