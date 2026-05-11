class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self._model_ = model

    def get_model(self):
        return self._model_

    def set_model(self, model):
        self._model_ = model

# Criação do objeto da classe Car
car = Car("Toyota", "Camry")

# Configurar novos valores para os atributos
car.brand = "Honda"
car.set_model("Civic")

# Exibir os valores dos atributos na tela
print(f"Brand: {car.brand}")
print(f"Model: {car.get_model()}")