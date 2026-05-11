class Stack:
    def __init__(self):
        self.container = []

    def push(self, item):
        self.container.append(item)

    def pop(self):
        if not self.is_empty():
            return self.container.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.container[-1]
        return None

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

# Exemplo de uso da pilha
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # Output: 3
print(stack.pop())   # Output: 3
print(stack.pop())   # Output: 2
print(stack.size())  # Output: 1
print(stack.is_empty()) # Output: False
stack.pop()
print(stack.is_empty()) # Output: True