def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Exemplo de chamada de função
print_person_info(name="John", age=30, city="New York", profession="Engineer")