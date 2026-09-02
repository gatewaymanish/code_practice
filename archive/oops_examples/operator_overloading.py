# Operator overloading allows custom behavior for operators like +

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # Output: Vector(6, 8)


## more example
class Number:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __str__(self):
        return f"Number({self.value})"

# Usage
n1 = Number(3)
n2 = Number(4)
print(n1 * n2)  # Output: Number(12)

##
class CustomList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

# Usage
my_list = CustomList([10, 20, 30])
print(my_list[1])  # Output: 20