# Access Modifiers

# Public attributes are those that can be accessed inside the class and outside the class.

# Example of Public attributes

'''

class Employee:
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.salary = salary

    def displayID(self):
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displayID()

'''

# Private attributes cannot be accessed directly from outside the class but can be accessed from inside the class.

# Example of Private attributes

'''
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property


Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
print("Salary:", Steve.__salary)  # this will cause an error

'''

# Example of Private methods

'''


class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displaySalary()
Steve.__displayID()  # this will generate an error

'''

# Accessing private attributes in the main code

# Properties and methods with the __ prefix are usually present to make sure that the user does not carelessly access them. Python allows for free hand to the user to avoid any future complications in the code. If the user believes it is absolutely necessary to access a private property or a method, they can access it using the _<ClassName> prefix for the property or method. An example of this is shown below:


class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property


Steve = Employee(3789, 2500)
print(Steve._Employee__salary)  # accessing a private property
