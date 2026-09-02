def func(a, b=[]):
    return b.append(a)


def func1(a, b=[]):
    b.append(a)
    return b


print(func(2))
print(func(3))
print(func1(2))
print(func1(3))


def func():
    try:
        return 7
    finally:
        return 8

print(func())