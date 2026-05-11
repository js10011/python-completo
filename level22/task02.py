import yaml

film_info = {
    "título": "Matrix",
    "diretor": "Lana e Lilly Wachowski",
    "ano de lançamento": 1999
}

yaml_str = yaml.dump(film_info, default_flow_style=False)

deserialized_data = yaml.load(yaml_str, Loader=yaml.SafeLoader)

print("String serializada no formato YAML:")
print(yaml_str)

print("Objeto dicionário desserializado:")
print(deserialized_data)