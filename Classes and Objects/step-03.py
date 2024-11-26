# Class and Instance Variables

'''
Class variables:
The class variables are shared by all instances or objects of the classes. A change in the class variable will change the value of that property in all the objects of the class.

Instance variables:
The instance variables are unique to each instance or object of the class. A change in the instance variable will change the value of the property in that specific object only.

!! class variables are defined outside the initializer and instance variables are defined inside the initializer.

'''


# Defining class variables and instance variables

class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables


p1 = Player('Mark')
p2 = Player('Steve')

print("\n!!Defining class variables and instance variables!!\n")
print("Name:", p1.name)
print("Team Name:", p1.teamName)
print("Name:", p2.name)
print("Team Name:", p2.teamName)


# Wrong use of class variables


'''
It is imperative to use class variables properly since they are shared by all the class objects and can be modified using any one of them. Below is an example of wrongful use of class variables:
'''


class Player:
    formerTeams = []  # class variables
    teamName = 'Liverpool'

    def __init__(self, name):
        self.name = name  # creating instance variables


p1 = Player('Mark')
p2 = Player('Steve')

p1 = Player('Mark')
p1.formerTeams.append('Barcelona')  # wrong use of class variable
p2 = Player('Steve')
p2.formerTeams.append('Chelsea')  # wrong use of class variable

print("\n!!! wrong use of class variable!!!\n")
print("Name:", p1.name)
print("Team Name:", p1.teamName)
print(p1.formerTeams)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
print(p2.formerTeams)


'''
In the example above, while the instance variable name is unique for each and every object of the Player class, the class variable, formerTeams, can be accessed by any object of the class and is updated throughout. We are storing all players currently playing for the same team, but each player in the team may have played for different former teams. To avoid this issue, the correct implementation of the example above will be the following:
'''


class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables
        self.formerTeams = []


p1 = Player('Mark')
p1.formerTeams.append('Barcelona')
p2 = Player('Steve')
p2.formerTeams.append('Chelsea')

print("\n!!Using class variables smartly\n")
print("Name:", p1.name)
print("Team Name:", p1.teamName)
print(p1.formerTeams)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
print(p2.formerTeams)