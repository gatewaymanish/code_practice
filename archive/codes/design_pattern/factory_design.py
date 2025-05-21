# The Factory Pattern is a creation design pattern that provides an interface for creating
# objects but allows subclasses to alter the type of objects that are created. It helps
# decouple object creation from the main logic, making the code more flexible and maintainable.
# Key Benefits of Factory Pattern
# - Encapsulation: Hides object creation logic from the client.
# - Decoupling: Reduces dependencies between classes.
# - Scalability: Easily extendable to support new object types.


from abc import ABC, abstractmethod


# Step 1: Define an abstract class (interface)
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Step 2: Create concrete classes
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Step 3: Create the Factory class
class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            return None


# Usage
animal = AnimalFactory.get_animal("dog")
if animal:
    print(animal.speak())  # Output: Woof!


## another way
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass

class Car(Vehicle):
    def create(self):
        return "Car created"

class Bike(Vehicle):
    def create(self):
        return "Bike created"

class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError("Invalid vehicle type")

vehicle = VehicleFactory.get_vehicle("car")
print(vehicle.create())  # Output: Car created