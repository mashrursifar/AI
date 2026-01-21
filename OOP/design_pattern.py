#Singleton
# Singleton is used when exactly one object is needed to coordinate actions across the system.

# Some resources or services should not have multiple instances because that would:
# 1. Waste resources
# 2. Cause inconsistent behavior
# 3. Lead to data conflicts
# 4. Singleton solves this by centralizing control.
# Common use cases: Database Connection Manager, Configuration / Settings Manager, Logging System

class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance

ob1 = Singleton()
ob2 = Singleton()

print(ob1 is ob2)

# Factory Design Pattern
# The Factory Design Pattern is a creational design pattern that provides an interface for creating objects while 
# allowing subclasses or separate factory classes to decide which concrete class to instantiate.
# In essence, object creation is encapsulated, so client code is decoupled from specific implementations.

class Car:
    def driver(self):
        return "Driving a car"

class Bike:
    def driver(self):
        return "Riding a bike"

class VehicleFactory:
    @staticmethod
    def get_vehicle(type):
        if type == "car":
            return Car()
        elif type == "bike":
            return Bike()
        else:
            return ValueError("Unknown Type")

vechile = VehicleFactory.get_vehicle("bike")
print(vechile.driver())


# Builder Design Pattern
# Build step by step not at a time. Like building a 5 storey buldiding at first it needs to build ground floor first then 1st, 2nd so on...

class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def __str__(self): #dunder) method used to define the human-readable string representation of an object.
        return f"Coumpter with {self.cpu} CPU, {self.ram} RAM, {self.storage} Storage"
        
class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self
    
    def set_storage(self, storage):
        self.storage = storage
        return self

    def build(self):
        return Computer(self.cpu, self.ram, self.storage)

builder = ComputerBuilder()

computer = builder.set_cpu("Ryzen 7").set_ram("16 GB").set_storage("1 TB").build()

print(computer)


