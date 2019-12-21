def my_function():
  print("Hello from a function")

my_function()



def myfunc():
  global x          # Global
  x = "fantastic"

myfunc()

print("Python is " + x)


def my_function(fname):     # With Arg
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

def my_function(food):      #Passing List Arg
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x):         #Return Statement
  return 5 * x

print(my_function(3))