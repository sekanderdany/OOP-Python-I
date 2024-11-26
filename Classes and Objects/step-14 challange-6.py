'''
Challenge: Enhancing Car Functionality

Enhancement requirements for the Car class
Enhance the functionality of the Car class as follows:

Task 1: Modify the start method to check if the engine is already running and display a message accordingly.

Task 2: Introduce a turn_off method to deactivate the car. This method should check if the engine is running and display a message if the engine is already off.

Task 3: Modify the drive method to verify the engine’s status before allowing the car to move. If the engine is not started, the drive method should display a message indicating that the engine needs to be started first.
'''

from Engine import Engine
from Wheel import Wheel

# Define a composite object representing a car chassis


class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.engine = Engine()
        self.wheels = [Wheel() for _ in range(4)]
        self.is_engine_started = False  # adding a flag

    def start(self):
        if not self.is_engine_started:
            self.engine.start()
            self.is_engine_started = True
        else:
            print("The engine is already running.")

# New method to deactivate the car

    def turn_off(self):
        if self.is_engine_started:
            print("Turning off the car.")
            self.is_engine_started = False
        else:
            print("The engine is already off.")

    def drive(self):
        if self.is_engine_started:
            print("Driving the car...")
            for wheel in self.wheels:
                wheel.rotate()
        else:
            print("Cannot drive the car. Start the engine first.")


# Create an instance of Car
my_car = Car("Red", "SUV")

# Start the car's engine
my_car.start()

# Drive the car
my_car.drive()

my_car.turn_off()

my_car.drive()

my_car.start()

my_car.drive()
