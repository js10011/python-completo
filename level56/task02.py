def adjacency_matrix_to_list(matrix):
    adj_list = []
    for i in range(len(matrix)):
        neighbors = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                neighbors.append(j)
        adj_list.append(neighbors)
    return adj_list

# Exemplo de uso
matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

print(adjacency_matrix_to_list(matrix))