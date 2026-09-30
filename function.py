# Now we are going to write our own function.

name = input("Enter you name: ")
hello()
print(name)

#-----------------------

def hello():
  print("Hello")

name = input("Enter you name: ")
hello()
print(name)

#-----------------------

def hello(to):
  print(f"Hello, {to}")

name = input("Enter you name: ")
hello(name)
# print(name)

# ----------------

def hello(to="World"):
  print(f"Hello, {to}")

hello() # default arg will use here if we not going to pass it on the function then.
name = input("Enter you name: ")
hello(name) # it will use the passed value.
# print(name)

#-------------------

def main():
    namea = input("Enter you name: ")
    hello()

def hello():
    print(namea)
    print(f"Hello, {namea}")

main ()

#-------------------------

def main():
  hello()
  name = input("Enter you name: ")
  hello(name)

def hello(to="World"):
  print(f"Hello, {to}")

main ()

-------------------------

def main():
    x = int(input("What's X: "))
    print("X square: ", square(x))

main()

-------------------------

def main():
    x = int(input("What's X: "))
    print(f"X square: {square(x)}")     # two way to print the same thing
    x = x+1
    print("X Sqaure:", square(x))

def square(n):
    #return n * n
    #return n ** 2
    return pow(n, 2)
main()
