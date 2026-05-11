class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = new_node

    def get(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None


ht = HashTable(10)
ht.insert('apple', 1)
ht.insert('banana', 2)
ht.insert('grape', 3)
ht.insert('apple', 4)

print(ht.get('apple'))   # Output: 4
print(ht.get('banana'))  # Output: 2
print(ht.get('grape'))   # Output: 3
print(ht.get('pear'))    # Output: None