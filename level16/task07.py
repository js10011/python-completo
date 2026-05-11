class Base1:
    def describe(self):
        print("This is Base1")

class Base2:
    def describe(self):
        print("This is Base2")

class Combined(Base1, Base2):
    pass

obj = Combined()
obj.describe()