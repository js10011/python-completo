class A:
    def method(self):
        print("A")
        # Sem chamada para super() porque A é a classe mais alta na hierarquia

class B(A):
    def method(self):
        print("B")
        super().method()

class C(A):
    def method(self):
        print("C")
        super().method()

class D(B, C):
    def method(self):
        print("D")
        super().method()

d = D()
d.method()