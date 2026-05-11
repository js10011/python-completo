class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, value):
        current = self.head
        if current and current.value == value:
            self.head = current.next
            return
        prev = None
        while current and current.value != value:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')

# Teste a LinkedList
sll = LinkedList()
sll.add(1)
sll.add(2)
sll.add(3)
sll.print_list()

sll.remove(2)
sll.print_list()

print(sll.find(3))  # Saídas: True
print(sll.find(2))  # Saídas: False