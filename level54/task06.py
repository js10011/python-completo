class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False

    def search(self, key):
        return self.get(key) is not None

def demo():
    ht = HashTable(10)
    ht.insert("key1", "value1")
    ht.insert("key2", "value2")
    ht.insert("key3", "value3")
    
    print("Get key1:", ht.get("key1"))  # Output: value1
    print("Get key2:", ht.get("key2"))  # Output: value2
    print("Get key4:", ht.get("key4"))  # Output: None

    print("Exists key1:", ht.search("key1"))  # Output: True
    print("Exists key4:", ht.search("key4"))  # Output: False

    print("Delete key1:", ht.delete("key1"))  # Output: True
    print("Get key1 after delete:", ht.get("key1"))  # Output: None

    ht.insert("key1", "value1_new")
    print("Get key1 after reinsert:", ht.get("key1"))  # Output: value1_new

demo()