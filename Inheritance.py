# Sample Parent Class
class Employee:
    def __init__(self, Band, Rating):
        self.Band = Band
        self.Rating = Rating

    def display_sal(self):
        if self.Band == "A" and self.Rating == "1":
            print("10 to 15LPA")
        elif self.Band == "B" and self.Rating == "1":
            print("8 to 10LPA")
        else:
            print("5 LPA")


E1 = Employee("A", "1")
E1.display_sal()


# Creating the Base Class to inherit from the above Super Class
class LeaveBalance(Employee):
    pass


# Creating the object ref for Child Class that inherits from the Super Class
L1 = LeaveBalance("A", "1")
L1.display_sal()


class A:
    a = 5
    b = 6

    def MethodA(self):
        print("Parent Class Method is executed")

objA = A()
objA.MethodA()

class B(A):

    def MethodB(self):
        print("Child Class Method is Executed")
        print(A.a)
        print(A.b)
        print(super().a)
        print(super().b)
        super().MethodA()

objB = B()
objB.MethodB()
objB.MethodA()
