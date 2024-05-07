#Lists, Tuples, Sets, Dictionaries

#Tuples - Immutable(Can't change the Chars in Tuples)
Corp_Companies = ("TechM", "CTS1", "TCS3", 123, 123.456)
print(Corp_Companies[1])

#Adding two tuples
Corp_Companies2 = Corp_Companies + ("Athena", "YBM")
print(Corp_Companies2)

#Slicing Tuples
print(Corp_Companies2[0:2])
print(Corp_Companies2[2:4])

#Length of Tuples
print(len(Corp_Companies2))

#Sort of Tuples
a = (9, 4, 6, 3)
print(sorted(a))

#Nesting Tuples(Complex Data Structues)
final = a + Corp_Companies2
print(final)

#_____________________________________________________________________________________________
#Sets
#Sets are mutable, Unordered & Create with {} & doesn't allow duplicate values
Travels={"SKB","YBM","Vetri","KPN"}
print(Travels)
Travels1=[1, 2, 3]
Travels3=set(Travels1)
print(Travels3)

#Dictionaries
#Dictionaries are denoted with Curly braces
#Keys: Immutable & Unique
#Values: immutable, mutable & duplicates
#Each Key and value pair separated by comma

Akey1 = {"KNP": 1234, "YBM": 1456}
print(Akey1.get("YBM"))
print(Akey1.keys())
print(Akey1.values())


AA=((11,12),[21,22])
print(AA[0][1])

