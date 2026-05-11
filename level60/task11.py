from collections import deque

def bfs(residual_graph, source, sink, parent):
    visited = [False] * len(residual_graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for ind, val in enumerate(residual_graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                if ind == sink:
                    return True
    return False

def edmonds_karp(capacity_matrix, source, sink):
    residual_graph = [row[:] for row in capacity_matrix]
    parent = [-1] * len(residual_graph)
    max_flow = 0

    while bfs(residual_graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

    return max_flow

# Exemplo de uso
capacity_matrix = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]
source = 0
sink = 5

print("Fluxo máximo: ", edmonds_karp(capacity_matrix, source, sink))