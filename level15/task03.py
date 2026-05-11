class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Criação de um objeto da classe Rectangle
rect = Rectangle(5, 10)

# Cálculo da área do retângulo
print(rect.area())