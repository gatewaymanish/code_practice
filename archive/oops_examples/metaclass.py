# Metaclasses in Python are "classes that create classes." They define how classes
# behave and allow customization of class creation.
#  How Metaclasses Work
# - Normally, classes create objects.
# - A metaclass creates classes (which are themselves objects).
# - Python uses type as the default metaclass.
#  Example: Custom Metaclass

class Meta(type):
    def __new__(cls, name, bases, class_dict):
        class_dict["custom_attribute"] = "Added by metaclass"
        return super().__new__(cls, name, bases, class_dict)

class MyClass(metaclass=Meta):
    pass

# Usage
print(MyClass.custom_attribute)  # Output: Added by metaclass


#  Modifies class attributes dynamically
#  Useful for enforcing rules or adding functionality
# Would you like more examples, such as validating attributes,
# logging, or enforcing singleton behavior? 🚀 You can also check
# out this guide for more details!
