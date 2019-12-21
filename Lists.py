thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print(len(thislist))

thislist.append("orange")
print(thislist)

thislist.remove("banana")
print(thislist)

del thislist[0]     #The del keyword removes the specified index:
print(thislist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2   #Join two list
print(list3)

for x in list2:
  list1.append(x) #Append list2 into list1

print(list1)

"""
Questions 1

Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(?)
"""