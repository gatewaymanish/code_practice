# Multiple inheritance allows a class to inherit from multiple parent classes.

class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def roll(self):
        return "Wheels rolling"

class Car(Engine, Wheels):
    pass

# Usage
my_car = Car()
print(my_car.start())  # Output: Engine started
print(my_car.roll())   # Output: Wheels rolling