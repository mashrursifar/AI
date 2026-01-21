class Laptop:
    
    def __init__(self, brand):
        self.brand = brand
        

class Student:
    def __init__(self,name, laptop_obj):
        self.name = name 
        self.laptop_v = laptop_obj

    def show_laptop_info(self):
        print(f"{self.name} has a laptop named {self.laptop_v.brand}")


lp1 = Laptop("Legion")
std = Student("Sifar", lp1)

std.show_laptop_info()