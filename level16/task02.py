class Animal:
    def speak(self):
        return "Rrrr!"

class Dog(Animal):
    def speak(self):
        return super().speak() + " Au-au!"

# Exemplo de uso:
dog = Dog()
print(dog.speak())  # Saída: Rrrr! Au-au!