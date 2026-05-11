class DynamicArray:
    def __init__(self):
        self.array = []
    
    def add(self, element):
        self.array.append(element)
    
    def remove(self, index):
        if 0 <= index < len(self.array):
            self.array.pop(index)
    
    def get(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")
    
    def set(self, index, element):
        if 0 <= index < len(self.array):
            self.array[index] = element
        else:
            raise IndexError("Index out of bounds")

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)


# Exemplos de uso:
arr = DynamicArray()
arr.add(1)
arr.add(2)
arr.add(3)
print(arr)  # [1, 2, 3]

arr.remove(2)
print(arr)  # [1, 2]

print(arr.get(1))  # 2

arr.set(1, 5)
print(arr)  # [1, 5]

print(len(arr))  # 2