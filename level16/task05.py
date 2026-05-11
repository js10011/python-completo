class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

def check_type(obj):
    return isinstance(obj, Animal)

# Exemplos de uso:
dog = Dog()
cat = Cat()
not_animal = "Not an animal"

print(check_type(dog))  # True
print(check_type(cat))  # True
print(check_type(not_animal))  # False