class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age
        return False

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return False

# Exemplos de utilização
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 30)

print(person1 == person2)  # False
print(person1 == person3)  # True
print(person1 < person2)   # False
print(person2 < person1)   # True