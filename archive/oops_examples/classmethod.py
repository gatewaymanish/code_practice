# Class methods modify class-level attributes.

class Employee:
    company = "TechCorp"

    @classmethod
    def set_company(cls, name):
        cls.company = name

# Usage
Employee.set_company("InnovateTech")
print(Employee.company)  # Output: InnovateTech

