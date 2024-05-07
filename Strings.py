# SingleLine
a = "Python Installed"
print(a)

# MultiLine
b = """Python Installed in,
 CHN machine"""
print(b)

# Strings letters are stored in as "Arrays"
c = "Python"
print(c[0])

# Looping through a String
d = "PyCharm"
for x in d:
    print(x)

# String length
e = "PyCharm"
print(len(e))

# Check String
txt = "Python can be executed in PyCharm"
print("Python" in txt)

# Check String with if statement
txt = "Python can be executed in PyCharm"
if "Python" in txt:
    print("Yes, 'Python' is present")

# Check String with if not statement
txt = "Python can be executed in PyCharm"
if "Java" not in txt:
    print("Yes, 'Java' is not present")


# =================================================================
# Slicing the String with the indexes
x = "Python is Popular Programming Language"
print(x[10:17])
print(x[:6])
print(x[18:])

# Modify the Strings
x = "Python is Popular Programming Language"
print(x.upper())
print(x.lower())
# Remove whitespace in the strings
xy = " Hello World "
print(xy.strip())
# Replace the String
print(xy.replace("World", "India"))
# Split the String
print(xy.split(","))

# Concatenate the Strings
a = "Hello"
b = "India"
print(a+b)
print(a+" "+b)

# String Format
a = 6
txt = "My age is {}"
print(txt.format(a))

# Escape Characters
txt = "Python is \"one\" of the programming language"
print(txt)
print(txt.capitalize())
txt1 = "Python"
print(txt1.count("Pyt"))






