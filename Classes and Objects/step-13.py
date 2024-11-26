'''
Object-Based Programming

Objects represent individual entities and encapsulate data and behavior, offering a modular and organized approach to software development.

At the core of object-based programming are independent objects, each responsible for specific functionalities

- A Car object that represents the vehicle.
- An Engine object that manages propulsion.
- Multiple Wheel objects that facilitate the movement.
'''

# Define a simple object representing a car
from Car import Car
from Wheel import Wheel
from Engine import Engine


class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def display_info(self):
        print("Car: {self.color} {self.model}")

# Define a simple object representing an engine


class Engine:
    def start(self):
        print("Engine started.")

# Define a simple object representing a wheel


class Wheel:
    def rotate(self):
        print("Wheel rotating.")


# As demonstrated below, these objects possess capabilities that correspond to their specific roles or functionalities.

# Define a simple object representing a car
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def display_info(self):
        print("Car: " + self.color + " " + self.model)


# Instantiate individual objects
my_car = Car("Red", "SUV")
my_engine = Engine()
my_wheels = [Wheel() for _ in range(4)]

# Demonstrate individual object functionality
print("Demonstration of Individual Object Functionality:")
my_car.display_info()  # Output: Car: Red SUV
my_engine.start()      # Output: Engine started.
for wheel in my_wheels:
    wheel.rotate()     # Output: Wheel rotating.


# Object Collaboration

from Engine import Engine
from Wheel import Wheel

# Define a composite object representing a car chassis

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.engine = Engine()
        self.wheels = [Wheel() for _ in range(4)]

    def start(self):
        self.engine.start()

    def drive(self):
        for wheel in self.wheels:
            wheel.rotate()
