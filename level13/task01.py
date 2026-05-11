# Criação de vários objetos de diferentes tipos
int_obj = 42
str_obj = "hello"
list_obj = [1, 2, 3]
tuple_obj = (4, 5, 6)
set_obj = {7, 8, 9}
dict_obj = {'a': 1, 'b': 2}

# Determinação e exibição de identificadores únicos de objetos usando id()
print("Identificadores Únicos:")
print(f"id(int_obj): {id(int_obj)}")
print(f"id(str_obj): {id(str_obj)}")
print(f"id(list_obj): {id(list_obj)}")
print(f"id(tuple_obj): {id(tuple_obj)}")
print(f"id(set_obj): {id(set_obj)}")
print(f"id(dict_obj): {id(dict_obj)}")

# Exibição de valores de hash de objetos que podem ser hashados usando hash()
print("\nValores de Hash:")
print(f"hash(int_obj): {hash(int_obj)}")
print(f"hash(str_obj): {hash(str_obj)}")
print(f"hash(tuple_obj): {hash(tuple_obj)}")

# Exibição de lista de atributos e métodos do objeto usando dir()
print("\nAtributos e Métodos:")
print(f"dir(int_obj): {dir(int_obj)}")
print(f"dir(str_obj): {dir(str_obj)}")
print(f"dir(list_obj): {dir(list_obj)}")
print(f"dir(tuple_obj): {dir(tuple_obj)}")
print(f"dir(set_obj): {dir(set_obj)}")
print(f"dir(dict_obj): {dir(dict_obj)}")