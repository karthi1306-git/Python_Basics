# Lists are used to store multiple values in a single Variable
# Lists are one among of 4 Built-in datatypes in Python to store collections of data
# Lists are ordered, Changeable and allow duplicate values

# Sample
thislist = ["Prog1", "Prog2", "Prog3", "Prog4"]
print(thislist)

# Allow Duplicate Values
thislist1 = ["Prog1", "Prog2", "Prog3", "Prog4", "Prog1"]
print(thislist1)

# Length
print(len(thislist1))
print(type(thislist1))

# List with combination of any datatypes
thislist2 = ["Prog1", 5, 4.5, 1j, "Prog1"]
print(thislist2)

# Another way of creating the list using list() constructor
thislist3 = list(("P1", "P2", "P3"))
print(thislist3)

# Accessing the items
thislist4 = ["Prog1", "Prog2", "Prog3", "Prog4", "Prog5"]
print(thislist4[1])
print(thislist4[-1])
print(thislist4[2:4])
print(thislist4[:4])
print(thislist4[3:])
print(thislist4[-4:-1])
if "Prog3" in thislist4:
    print("Yes")

# Changing the List Item
List1 = ["P1", "P2", "P3"]
List1[1] = ["P4"]
print(List1)
# Changing the range of List values
List1[1:2] = ["P10", "P10"]
print(List1)
# Changing the single value in a range
List1[0:5] = ["P20"]
print(List1)
List1.insert(1, "P21")
print(List1)
List1.append("P23")
print(List1)

# extend the list in another existing list
List2 = ["X1", "X2"]
List3 = ["X3", "X4"]
List2.extend(List3)
print(List2)

# Removing the items from the List
List4 = ["Y1", "Y2", "Y3", "Y4"]
List4.remove("Y3")
print(List4)
List4.remove("Y2")
print(List4)
# Removing the items from the List
List4.pop(1)
print(List4)
# pop() defines the removal of item from the last index
List4.pop()
print(List4)

# Remove the items by using del keyword
List5 = ["A1", "A2"]
del List5[0]
print(List5)
# It will clear the items but Lists will remain same
List5.clear()
print(List5)
# Delete the List completely
del List5
# print List5 - Encounters error since deleting in the previous


# Lopping the Lists
List_01 = ["X1", "X2", "X3", "X4"]
for x in List_01:
    print(x)

# Loop through the index numbers
for i in range(len(List_01)):
    print(List_01[i])

# With the help of While loop
i = 0
while i < len(List_01):
    print(List_01[i])
    i = i + 1

# List Comprehension - Shortest Syntax to print all the items
[print(x) for x in List_01]

# Sort the Lists - Ascending Order
List_02 = ["Zebra", "Parrot", "Bird", "Horse", "Dog"]
List_02.sort()
print(List_02)
List_03 = [45, 65, 4, 32, 11, 39, 99]
List_03.sort()
print(List_03)

# Sort the Lists - Descending Order
List_03.sort(reverse= True)
print(List_03)

# Reverse the Order from the Lists
List_03.reverse()
print(List_03)

# Copy the Lists
MyList_01 = ["Z1", "Z2", "Z3", "Z4"]
MyList_02 = MyList_01.copy()
print(MyList_02)

# Another way to make a Copy
MyList_03 = list(MyList_02)
print(MyList_03)

# Join the Lists using + Operator
MyList_04 = MyList_01 + MyList_02 + MyList_03
print(MyList_04)

# Join the Lists using extend keyword
MyList_05 = [3, 4, 5]
MyList_04.extend(MyList_05)
print(MyList_04)







