# Criamos um dicionário com informações sobre uma pessoa
person = {
    'name': 'Alexey',
    'age': 30,
    'address': {
        'city': 'Moscou',
        'street': 'Tverskaya',
        'house': 10
    },
    'contact_info': {
        'email': 'alexey@example.com',
        'phone': '+7 123 456 7890'
    }
}

# Alteramos valores no nível superior
person['name'] = 'Alexandre'
person['age'] = 31

# Alteramos valores no dicionário aninhado
person['address']['city'] = 'São Petersburgo'
person['address']['street'] = 'Perspectiva Nevsky'

# Alteramos valores em um nível de aninhamento mais profundo
person['contact_info']['email'] = 'alexandre@example.com'

# Adicionamos um novo elemento ao dicionário aninhado
person['address']['apartment'] = 5

# Excluímos um elemento do dicionário aninhado
del person['contact_info']['phone']

# Excluímos um elemento do nível superior
del person['age']

# Exibimos o resultado
print(person)