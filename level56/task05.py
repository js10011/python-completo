from collections import deque

def is_connected(graph):
    if not graph:
        return True  # Um grafo vazio é considerado conexo

    visited = set()
    queue = deque([list(graph.keys())[0]])  # Comece com qualquer nó, por exemplo, o primeiro

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return len(visited) == len(graph)

# Exemplo de uso:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}
print(is_connected(graph))  # True