def dfs(graph, visited, node):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, visited, neighbor)


def is_connected(graph):
    if not graph:
        return False

    visited = set()
    start_node = list(graph.keys())[0]
    dfs(graph, visited, start_node)

    # Check if all nodes were visited
    return len(visited) == len(graph)


# Exemplo de uso:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
print(is_connected(graph))  # Output: True