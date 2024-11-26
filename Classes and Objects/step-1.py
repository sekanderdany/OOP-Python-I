class MyClass:
    pass


obj = MyClass()  # creating a MyClass Object
print(obj)


# this code will compile
class Employee:
    # defining the properties and assigning them none
    ID = None
    salary = None
    department = None


'''
There are two ways to assign values to properties of a class.

1. Assign values when defining the class.
2. Assign values in the main code.
'''

# ---------------------
# Initializing
# ---------------------


class Employee:
    # defining the properties and assigning values to them
    ID = 3789
    salary = 2500
    department = "Human Resources"


# cerating an object of the Employee class
Steve = Employee()

# printing properties of Steve - an object of the Employee class
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)


# ---------------------
# Assigning
# ---------------------


class Employee:
    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None


# cerating an object of the Employee class
Steve = Employee()

# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)

# ---------------------
# Creating properties outside a class
# ---------------------


class Employee:
    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None


# cerating an object of the Employee class
Steve = Employee()

# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"

# creating a new attribute for Steve
Steve.title = "Manager"

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Title:", Steve.title)
