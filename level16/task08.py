class BaseA:
    def action(self):
        print("Action from BaseA")
        
class BaseB:
    def action(self):
        print("Action from BaseB")

class Derived(BaseA, BaseB):
    def action(self):
        super().action()
        print("Action from Derived")

d = Derived()
d.action()