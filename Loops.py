"""
A for loop is used for iterating over a sequence (that is
either a list, a tuple, a dictionary, a set, or a string).

"""

fruits = ["apple", "banana", "cherry"] #Print each fruit in a fruit list:
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

for x in range(5, 10):
  print(x)

for x in range(2, 30, 3): #Increment the sequence with 3 (default is 1):
  print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

"""
Loop through the items in the fruits list.


fruits = ["apple", "banana", "cherry"]
 for x in fruits:
  print(x)

"""