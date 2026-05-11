class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

# Demonstração de operação da pilha
stack = Stack()
print("Pilha vazia:", stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)
print("Elemento no topo da pilha:", stack.peek())

print("Removendo elemento:", stack.pop())
print("Removendo elemento:", stack.pop())
print("Elemento no topo da pilha:", stack.peek())

print("Pilha vazia:", stack.is_empty())
print("Removendo elemento:", stack.pop())
print("Pilha vazia:", stack.is_empty())