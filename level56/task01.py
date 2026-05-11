def has_edge(matrix, vertex1, vertex2):
    if vertex1 < 0 or vertex2 < 0 or vertex1 >= len(matrix) or vertex2 >= len(matrix[0]):
        return False
    return matrix[vertex1][vertex2] == 1


# Exemplo de uso:
adj_matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

print(has_edge(adj_matrix, 0, 1))  # True
print(has_edge(adj_matrix, 0, 2))  # False