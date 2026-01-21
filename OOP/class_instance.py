class Employee:

    company_name = "MS LTD."

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"EMP name : {self.name} \nSalary : {self.salary}")

    @classmethod
    def change_company_name(cls, name): # Class method use for common class. We use it for common name for objects. Like class variables.
        cls.company_name = name

ob1 = Employee("Sifar", 50000)

Employee.change_company_name("XYZ Company")
ob1.display_info()
print(ob1.company_name)