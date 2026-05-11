class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Criação de um objeto da classe Car
my_car = Car("Toyota", "Camry", 2020)

# Chamada do método display_info()
my_car.display_info()