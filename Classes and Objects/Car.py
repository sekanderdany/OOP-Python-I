# Define a simple object representing a car
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def display_info(self):
        print("Car: " + self.color + " " + self.model)


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


'''
