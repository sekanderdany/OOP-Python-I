'''
Challenge 2: Implement the Complete Student Class

Problem statement
Implement the complete Student class by completing the tasks below

Task
Implement the following properties as private:

 - name
 - rollNumber

Include the following methods to get and set the private properties above:

- getName()
- setName()
- getRollNumber()
- setRollNumber()

Implement this class according to the rules of encapsulation.

Input
Checking all the properties and methods

Output
Expecting perfectly defined fields and getter/setters
'''


class Student:
    __name = None
    __rollNumber = None

    def setName(self, name=None):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber=None):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber


Obj1 = Student()

Obj1.setName('Dany')
Obj1.setRollNumber(54)

print("Name:", Obj1.getName())
print("Roll Number:", Obj1.getRollNumber())
