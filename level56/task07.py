import heapq

def dijkstra(graph, start, end):
    # Criar um dicionário para armazenar os menores custos para alcançar cada nó
    shortest_paths = {node: (float('inf'), []) for node in graph}
    shortest_paths[start] = (0, [start])
    
    # Criar uma fila de prioridade para visitar os nós
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Ignorar nós que já foram processados
        if current_distance > shortest_paths[current_node][0]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < shortest_paths[neighbor][0]:
                shortest_paths[neighbor] = (distance, shortest_paths[current_node][1] + [neighbor])
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths[end]

# Exemplo de grafo: dicionário, onde o chave - cidade, e o valor - dicionário de vizinhos e distâncias até eles
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Exemplo de uso da função
start_city = 'A'
end_city = 'D'
distance, path = dijkstra(graph, start_city, end_city)
print(f"O caminho mais curto de {start_city} para {end_city} custa {distance} e passa por {path}.")