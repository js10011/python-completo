import pickle

class CustomSerializable:
    def __init__(self, name, age, password, hidden_info):
        self.name = name
        self.age = age
        self.password = password
        self.hidden_info = hidden_info

    def __reduce__(self):
        return self._serialize, (self.name, self.age)

    @staticmethod
    def _serialize(name, age):
        return CustomSerializable(name, age, None, None)

# Criação do objeto
obj = CustomSerializable("John Doe", 30, "supersecret", "hidden")

# Serialização
serialized_obj = pickle.dumps(obj)

# Desserialização
deserialized_obj = pickle.loads(serialized_obj)

# Verificação
print(f"Name: {deserialized_obj.name}, Age: {deserialized_obj.age}")
print(f"Password: {deserialized_obj.password}, Hidden Info: {deserialized_obj.hidden_info}")