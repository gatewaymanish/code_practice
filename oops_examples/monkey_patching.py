# Monkey patching in Python refers to modifying or extending the behavior of
# classes or modules at runtime without altering their original source code.
# This technique is often used for testing, debugging, or adding functionality
# to third-party libraries.
# Example: Monkey Patching a Class Method

class Animal:
    def speak(self):
        return "I make a sound"

# Monkey patching the method
def new_speak(self):
    return "Woof! Woof!"

Animal.speak = new_speak  # Replacing the original method

# Usage
dog = Animal()
print(dog.speak())  # Output: Woof! Woof!


# Dynamically modifies the behavior of speak()
# Useful for testing without modifying the original class
# Example: Monkey Patching a Module Function


import time

# Original function
print(time.sleep)  # Output: <built-in function sleep>

# Monkey patching
def fast_sleep(seconds):
    print(f"Skipping actual sleep for {seconds} seconds")

time.sleep = fast_sleep  # Replacing the function

# Usage
time.sleep(3)  # Output: Skipping actual sleep for 3 seconds

# Overrides built-in functions dynamically
# Useful for speeding up tests by bypassing delays
#  Considerations
# - Use with caution: Can lead to unexpected behavior if misused.
# - Avoid in production: Best for testing or debugging.
# - Prefer subclassing or decorators for structured modifications.
