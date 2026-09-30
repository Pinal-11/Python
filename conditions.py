# >   greater than
# >=  greater than or equal to
# <   less than
# <=  less than or equal to
# ==  equality check 
# !=  not eqaul to

# = is assignment operator copy the from right to left.

#----------------comparision-------------------

# x = int(input("What's X: "))
# y = int(input("What's Y: "))

# if x > y:
#     print("X is greater than Y")
# elif x < y:
#     print("X is less than Y")
# else:
#     print("X is equal to Y")

#-----------------------------------------------

# x = int(input("What's X: "))
# y = int(input("What's Y: "))

# if x > y or x < y:
#     print("X is not equal to Y")
# else:
#     print("X is equal to Y")

#-----------------------------------------------

# x = int(input("What's X: "))
# y = int(input("What's Y: "))

# if x != y:
#     print("X is not equal to Y")
# else:
#     print("X is equal to Y")

#-----------------------------------------------
#### Grade System ###

# score = int(input("Score: "))

# if score >=90 and score <=100:
#     print("Grade: A")
# elif score >=80 and score <= 89:
#     print("Grade: B")
# elif score >=70 and score < 80:
#     print("Grade: C")
# elif score >=60 and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

#----------------2nd Way --------------------

# score = int(input("Score: "))

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")


#----------------Parity Code (odd even number) --------------------

# x = int(input("What's X: "))

# if x % 2 == 0:
#     print("X is Even")
# else:
#     print("X is Odd")

#---------------Another Way ---------------

def main():
    x = int(input("What's X: "))

    if is_even(x):
        print("X is Even")
    else:
        print("X is Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

