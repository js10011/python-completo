# Criação de um dicionário com informações sobre uma pessoa
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Obter um valor por chave usando colchetes
name = person['name']
print(f'Name: {name}')

# Obter de forma segura um valor por chave usando o método get()
age = person.get('age')
print(f'Age: {age}')

# Usar o método setdefault() para obter um valor por chave e adicionar a chave se ela não existir
country = person.setdefault('country', 'USA')
print(f'Country: {country}')

# Exibir todo o dicionário para ver as alterações
print(person)