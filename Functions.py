# A function is a block of code which runs only when it is called
# In Python, A function is defined by a Keyword def
# From the Function perspective, Parameter is a variable while defining in the function
# From the Function perspective, Arguments is a value which passing while calling the function
def my_function():
    print("Strings,Lists,Loops")


# Call the Function
my_function()


# Function with Arguments/Parameters
def my_function1(fname, lname):
    print("First Name is " + fname)
    print("Last Name is " + lname)


# call the function with arguments
my_function1("Karthik", "Selvam")


# Arbitrary Arguments - If you dont know any number of arguments - Put * before to the Parameters
def fn_Login(*params):
    print("First index Value is " + params[2])


fn_Login("P1", "P2", "P3")


# Keyword Arguments - Can send the arguments with the Key = value syntax
def fn_Login1(URL, uname, pwd):
    print("URL is " + URL)
    print("U_Name is " + uname)
    print("Password is " + pwd)


fn_Login1(uname="Karthik", pwd="Test", URL="https://kc.com")


# Passing List as an arguments to a function
def fn_List01(objList):
    for x in objList:
        print(x)


fruits = ["Berry", "Apple", "Grape", "Pine"]
fn_List01(fruits)


# Return function - To let a function to return a value
def fn_cal(var):
    final = var + 5
    return final


print(fn_cal(5))

x=5
def f(*x):
    return sum(x)
    print(x)



