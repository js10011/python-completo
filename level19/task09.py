class CollectionIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.collection):
            item = self.collection[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

# Exemplos de uso:
# Para lista
ci_list = CollectionIterator([1, 2, 3, 4])
for item in ci_list:
    print(item)

# Para string
ci_string = CollectionIterator("hello")
for char in ci_string:
    print(char)