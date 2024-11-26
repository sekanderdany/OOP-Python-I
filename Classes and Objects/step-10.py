'''
Information hiding refers to the concept of hiding the inner workings of a class and simply providing an interface through which the outside world can interact with the class without knowing what’s going on inside.

A real life example#
Let’s apply this to a real-world scenario. Take the doctor-patient model. In the case of an illness, the patient consults the doctor, after which he or she is prescribed an appropriate medicine.

The patient only knows the process of going to the doctor. The logic and reasoning behind the doctor’s prescription are unknown to the patient. A patient will not understand the medical details the doctor uses to reach his/her decision on the treatment.

This is a classic example of the patient class interacting with the doctor class without knowing the inner workings of the doctor class.


# Components of data hiding
  - Encapsulation
  - Abstraction

  Encapsulation: in OOP refers to binding data and the methods to manipulate that data together in a single unit, that is, class. 
  
  A class can be thought of as a capsule having methods and properties inside it. When encapsulating classes, a good convention is to declare all variables of a class private. This will restrict direct access by the code outside that class.
  
  When encapsulating classes, a good convention is to declare all variables of a class private. This will restrict direct access by the code outside that class. One has to implement public methods to let the outside world communicate with this class. These methods are called getters and setters. We can also implement other custom methods.

  Advantages of encapsulation
    - Classes make the code easy to change and maintain.
    - Properties to be hidden can be specified easily.
    - We decide which outside classes or functions can access the class properties.
  # Getters and Setters

  Get and set
  In order to allow controlled access to properties from outside the class, getter and setter methods are used.

  A getter method allows reading a property’s value.

  A setter method allows modifying a property’s value.
'''
# '''
class User:
    def __init__(self, username=None):  # defining initializer
        self.__username = username

    def setUsername(self, x):
        self.__username = x

    def getUsername(self):
        return (self.__username)


Steve = User('steve1')
print('Before setting:', Steve.getUsername())
Steve.setUsername('steve2')
print('After setting:', Steve.getUsername())

# '''

'''
# Understanding Encapsulation Using Examples

Encapsulation refers to the concept of binding data and the methods operating on that data in a single unit, which is also called a class.

The goal is to prevent this bound data from any unwanted access by the code outside this class. Let’s understand this by using an example of a very basic User class.

Consider that we are up for designing an application and are working on modeling the log in part of that application. We know that a user needs a username and a password to log into the application.

An elementary User class will be modeled as:

- Having a property userName
- Having a property password
- A method named login() to grant access

Whenever a new user comes, a new object can be created by passing the userName and password to the constructor of this class.
'''
# A bad example
'''

class User:
    def __init__(self, userName=None, password=None):
        self.userName = userName
        self.password = password

    def login(self, userName, password):
        if ((self.userName.lower() == userName.lower())
                and (self.password == password)):
            print("Access Granted!")
        else:
            print("Invalid Credentials!")


Steve = User("Steve", "12345")
Steve.login("steve", "12345")
Steve.login("steve", "6789")
Steve.password = "6789"
Steve.login("steve", "6789")

'''
# In the above coding example, we can observe that anyone can access, change, or print the password and userName fields directly from the main code. This is dangerous in the case of this User class because there is no encapsulation of the credentials of a user, which means anyone can access their account by manipulating the stored data. So, the above code does not follow good coding practices.

# A good example


class User:
    def __init__(self, userName=None, password=None):
        self.__userName = userName
        self.__password = password

    def login(self, userName, password):
        if ((self.__userName.lower() == userName.lower())
                and (self.__password == password)):
            print(
                "Access Granted against username:",
                self.__userName.lower(),
                "and password:",
                self.__password)
        else:
            print("Invalid Credentials!")


# created a new User object and stored the password and username
Steve = User("Steve", "12345")
Steve.login("steve", "12345")  # Grants access because credentials are valid

# does not grant access since the credentails are invalid
Steve.login("steve", "6789")
Steve.__password  # compilation error will occur due to this line
