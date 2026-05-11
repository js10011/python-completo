from collections import deque

def find_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    
    return []

# Exemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
goal = 'F'
print(find_shortest_path(graph, start, goal))