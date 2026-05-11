def check_subclass(class1, class2):
    return issubclass(class1, class2)

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass

# Verificação
print(check_subclass(Car, Vehicle))  # Deve retornar True
print(check_subclass(Bicycle, Vehicle))  # Deve retornar True