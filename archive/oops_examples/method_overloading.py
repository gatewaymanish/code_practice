# Allows calling the same method with different numbers of arguments

class MathOperations:
    def add(self, a, b, c=None):
        """Overloaded method using default arguments."""
        if c is not None:
            return a + b + c
        return a + b

# Usage
math = MathOperations()
print(math.add(5, 10))      # Output: 15
print(math.add(5, 10, 20))  # Output: 35

## using *args for variable length arguements
class MathOperations:
    def add(self, *args):
        """Overloaded method using variable-length arguments."""
        return sum(args)

# Usage
math = MathOperations()
print(math.add(5, 10))      # Output: 15
print(math.add(5, 10, 20))  # Output: 35
print(math.add(1, 2, 3, 4)) # Output: 10

## using multiple dispatch  (multipledispatch library)
from multipledispatch import dispatch

class MathOperations:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c

# Usage
math = MathOperations()
print(math.add(5, 10))      # Output: 15
print(math.add(5, 10, 20))  # Output: 35