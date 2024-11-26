# Implementing Methods in a Class

'''
The self argument#
One of the major differences between functions and methods in Python is the first argument in the method definition. Conventionally, this is named self. The user can use different names as well, but self is used by almost all the developers working in Python. We will also be using this convention for ease of understanding.

This pseudo-variable provides a reference to the calling object, that is the object to which the method or property belongs to. If the user does not mention the self as the first argument, the first parameter will be treated for reference to the object.

Note: The self argument only needs to be passed in the method definition and not when the method is called.
'''


class Employee:
    # defining the initializer
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)


# initializing an object of the Employee class
Steve = Employee(3789, 2500, "Human Resources")

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Tax paid by Steve:", Steve.tax())
print("Salary per day of Steve", Steve.salaryPerDay())

#################################################
# Method overloading

'''
Overloading refers to making a method perform different operations based on the nature of its arguments.

Unlike in other programming languages, methods cannot be explicitly overloaded in Python but can be implicitly overloaded.

In order to include optional arguments, we assign default values to those arguments rather than creating a duplicate method with the same name. If the user chooses not to assign a value to the optional parameter, a default value will automatically be assigned to the variable.
'''

class Employee:
    # defining the properties and assigning them None to the
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    # method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

    def tax(self, title=None):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)


# cerating an object of the Employee class
Steve = Employee()

# Printing properties of Steve
print("Demo 1")
Steve.demo(1, 2, 3)
print("\n")

print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")

print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)


'''
Advantages of method overloading
One might wonder that we could simply create new methods to perform different jobs rather than overloading the same method. However, under the hood, overloading saves us memory in the system. Creating new methods is costlier compared to overloading a single one.

Since they are memory-efficient, overloaded methods are compiled faster compared to different methods, especially if the list of methods is long.

An obvious benefit is that the code becomes simple and clean. We don’t have to keep track of different methods.

Polymorphism is a very important concept in object-oriented programming. Method overloading plays a vital role in its implementation.
'''