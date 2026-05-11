# Função auxiliar para DFS
from collections import defaultdict, deque

# Criar lista de adjacências
graph = defaultdict(list)

# Rastreador de nós visitados
visited = set()
temp_marks = set()
stack = list()

def dfs(node):
    if node in temp_marks:
        raise ValueError("Graph is not a Directed Acyclic Graph (DAG)")

    if node not in visited:
        temp_marks.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        temp_marks.remove(node)
        visited.add(node)
        stack.append(node)

def topological_sort(tasks):
    for dest, src in tasks:
        graph[src].append(dest)

    # Realizar DFS em cada nó
    all_nodes = {node for edge in tasks for node in edge}
    for node in all_nodes:
        if node not in visited:
            dfs(node)

    return stack[::-1]

# Exemplo de uso:
tasks = [('a', 'b'), ('b', 'c'), ('c', 'd')]
print(topological_sort(tasks))  # Output: ['d', 'c', 'b', 'a']