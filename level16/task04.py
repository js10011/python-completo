class Animal:
    def make_sound(self):
        return "Uuuuuuu!"

class Dog(Animal):
    def make_sound(self):
        return super().make_sound() + " Au-au!"

class Cat(Animal):
    def make_sound(self):
        return super().make_sound() + " Miau-miau!"

# Exemplos de uso:
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Uuuuuuu! Au-au!
print(cat.make_sound())  # Uuuuuuu! Miau-miau!