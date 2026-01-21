# bstraction is an object-oriented programming principle that focuses on exposing only essential behavior 
# while hiding implementation details. In Python, abstraction is primarily implemented using abstract base classes (ABCs).
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape): 

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.1416 * self.radius

shapes = [Rectangle(10, 5), Circle(7)]

for shape in shapes:
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
    
