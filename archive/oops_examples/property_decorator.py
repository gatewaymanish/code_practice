# Property decorators allow computed attributes without explicit method calls.

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

# Usage
temp = Temperature(25)
print(temp.fahrenheit)  # Output: 77.0