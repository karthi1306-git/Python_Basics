# Simple Class Creation and accessing the Class Properties
class MyClass1:
    x = 101


objMy = MyClass1()
print(objMy.x)


# A class with the Init function(Kind of Constructor) to execute as soon as the Object of Class is instantiated
class Company:
    # It is kind of Constructor - This block will be executed as soon the object of Class is instantiated
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print("Company Name is: " + name)
        print("Year Started: " + year)

    # Creating the Method inside the class
    def welcome(self):
        print("Hello " + self.name + "! Welcome to Association")


C1 = Company("TECH-M", "1991")
C1.welcome()


# Creating the Class with the __str__ function
class Department:
    # Self Parameter is a reference to the current instance of the class
    # Used to access variables belongs to the Class
    def __init__(self, Dept, Head):
        self.Dept = Dept
        self.Head = Head

    def __str__(self):
        return "Department is "+self.Dept


objDep = Department('BME', 'SK')
print(objDep)
print(objDep.Head)
