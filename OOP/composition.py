# Strong relationship

class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Engine(power)

    def show_details(self):
        print(f"{self.brand} has an engine with {self.engine.power} HP")


# en = Engine()

car = Car("Toyata", 200)

car.show_details()