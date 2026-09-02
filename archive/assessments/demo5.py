# create a class with name employee with variable age, name and salary
# create 3 objects


class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary





e1 = Employee('Manoj', 25, 50000)
e2 = Employee('David', 30, 30000)
e3 = Employee('Rashi', 22, 40000)


l1 = [e1, e2, e3]
# sorted by age in manner e3, e1, e2
for i in range(len(l1)-1):
    for j in range(len(l1)-i-1):
        if l1[j].salary > l1[j+1].salary:
            l1[j], l1[j+1] = l1[j+1], l1[j]



# 2nd method using sorted() builtin function
res = sorted(l1, key=lambda x:x.age)
print('result ', res)
[print(x.name) for x in res]

