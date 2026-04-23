# A singleton class in Python ensures that only one instance of the class exists
# throughout the program. This is useful for managing shared resources like database
# connections, logging, or configuration setting

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Usage Example
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True


## second way by using decorator
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Singleton:
    pass

# Usage Example
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # Output: True