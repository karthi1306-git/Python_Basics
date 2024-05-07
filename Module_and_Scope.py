# If variable is created inside the function, then the Variable will have Scope inside the function only
xc = 100


def welcome():
    xd = "Welcome"
    print(xd)


class Sample1:

    def __init__(self):
        print(xc)

    def __str__(self):
        print("Executing the Method")


S1 = Sample1()
S1.__str__()
welcome()
