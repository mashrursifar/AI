class Department:
    def __init__(self, name):
        self.name = name 

class University:

    def __init__(self, name):
        self.name = name
        self.department = []

    def add_department(self, department):
        self.department.append(department)

    def show_departments(self):
        return [department.name for department in self.department ]
    

un1 = University("Daffodil")
dep1 = Department("CSE")
dep2 = Department("SWE")

un1.add_department(dep1)
un1.add_department(dep2)

print(un1.show_departments())