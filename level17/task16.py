dependency_graph = dict()
visited = set()
temp_marked = set()
result = list()

def dfs(package):
    if package in temp_marked:
        raise ValueError("Cycle detected!")
    if package not in visited:
        temp_marked.add(package)
        for dep in dependency_graph.get(package, []):
            dfs(dep)
        temp_marked.remove(package)
        visited.add(package)
        result.append(package)

def topological_sort(packages):
    dependency_graph.update({ pkg: deps for pkg, deps in packages})
    for package in dependency_graph:
        if package not in visited:
            dfs(package)
    return result

# Exemplo de uso:
packages = [
    ('a', ['b', 'c']),
    ('b', ['c', 'd']),
    ('c', ['d']),
    ('d', [])
]

print(topological_sort(packages))
# Output: ['d', 'c', 'b', 'a']