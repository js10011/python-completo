def make_filter(threshold):
    def filter_func(value):
        return value > threshold
    return filter_func

# Criamos várias funções de filtro com diferentes valores de limite
filter_10 = make_filter(10)
filter_20 = make_filter(20)
filter_30 = make_filter(30)

# Lista de dados para filtrar
data = [5, 15, 25, 35, 45]

# Filtramos os dados e exibimos os resultados
print(list(filter(filter_10, data)))  # Deve exibir [15, 25, 35, 45]
print(list(filter(filter_20, data)))  # Deve exibir [25, 35, 45]
print(list(filter(filter_30, data)))  # Deve exibir [35, 45]