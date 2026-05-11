class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        return f"{self.brand} {self.model} está dirigindo."

class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def ride(self):
        return f"{self.brand} {self.model} está andando."

# Exemplos de uso das classes:
car = Car("Toyota", "Corolla")
print(car.drive())  # Output: Toyota Corolla está dirigindo.

motorcycle = Motorcycle("Yamaha", "R1")
print(motorcycle.ride())  # Output: Yamaha R1 está andando.