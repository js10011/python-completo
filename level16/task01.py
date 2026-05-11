class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

# Exemplo de uso
car = Car("Toyota", "Corolla", "Petrol")
print(f"Brand: {car.brand}, Model: {car.model}, Fuel Type: {car.fuel_type}")