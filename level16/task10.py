class M:
    def action(self):
        print("Class M action")

class N(M):
    def action(self):
        print("Class N action")
        super().action()

class O(M):
    def action(self):
        print("Class O action")
        super().action()

n = N()
n.action()