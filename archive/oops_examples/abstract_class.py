# enforce method implementation in subclasses.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())  # Output: Woof! Meow!