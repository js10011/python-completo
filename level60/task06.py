INF = float('inf')
def create_key(visited, current):
    return (tuple(visited), current)

def visit(graph, visited, current, dp):
    n = len(graph)
    key = create_key(visited, current)

    # Se todas as cidades foram visitadas, voltamos para a cidade inicial
    if len(visited) == n:
        return graph[current][0]

    # Se o resultado já foi calculado, retorne-o
    if key in dp:
        return dp[key]

    min_cost = INF

    # Tentamos visitar todas as cidades possíveis
    for city in range(n):
        if city not in visited:
            new_visited = visited + [city]
            new_cost = graph[current][city] + visit(graph, new_visited, city, dp)
            min_cost = min(min_cost, new_cost)

    dp[key] = min_cost
    return min_cost

def tsp(graph):
    n = len(graph)
    dp = {}
    result = visit(graph, [0], 0, dp)
    return result

# Exemplos de uso
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print(tsp(graph))  # Resultado esperado: 80