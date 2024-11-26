# Methods in a Python class

'''
In Python classes, we have three types of methods:  - instance methods
- class methods
- static methods

- Class methods: work with class variables and are accessible using the class name rather than its object. Since all class objects share the class variables, class methods are used to access and modify class variables.

** Class methods are accessed using the class name and can be accessed without creating a class object.

'''

class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables
    
    @classmethod
    def getTeamName(cls):
        return cls.teamName


print(Player.getTeamName())

'''
Static methods: are methods that are usually limited to class only and not their objects. They have no direct relation to class variables or instance variables. They are used as utility functions inside the class or when we do not want the inherited classes to modify a method definition.

** Static methods can be accessed using the class name or the object name.
'''

class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @staticmethod
    def demo():
        print("I am a static method.")


p1 = Player('lol')
p1.demo()
Player.demo()

class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)


weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))