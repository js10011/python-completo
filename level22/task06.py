import pickle

class MyClass:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(filepath, 'r')
        self.data = self.file.read()
    
    def __getstate__(self):
        state = self.__dict__.copy()
        # Remove o atributo file do estado para prevenir a serialização
        del state['file']
        return state
    
    def __setstate__(self, state):
        self.__dict__.update(state)
        # Reabre o arquivo na desserialização
        self.file = open(self.filepath, 'r')
        self.data = self.file.read()
    
    def __del__(self):
        self.file.close()

# Exemplo de uso:
obj = MyClass('example.txt')
serialized_obj = pickle.dumps(obj)
deserialized_obj = pickle.loads(serialized_obj)
print(deserialized_obj.data)