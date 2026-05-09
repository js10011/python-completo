# Perfil do gato

# Escreva uma função create_cat_profile(name: str, age: int, **kwargs: str) -> None, que aceita o nome e a idade do gato como parâmetros obrigatórios,
# bem como um número arbitrário de parâmetros nomeados (por exemplo, raça, cor, etc.).
# A função deve exibir o perfil do gato, incluindo todos os parâmetros passados.

# Escreva seu código aqui

# para criar ou aceitar pares chave=valor
def create_cat_profile(name: str, age: int, **kwargs: str) -> None:
    print(f"Nome: {name}, Idade: {age}")
    for chave, valor in kwargs.items():
        print(f"{chave}:{valor}")
    
create_cat_profile("Murzick", 3, raça="Siamês", cor="Preto")
create_cat_profile("Barsik", 5, país="China", hobby="Caçar ratos")