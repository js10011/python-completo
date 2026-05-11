import heapq

def dijkstra(adj_list, start):
    # Inicialização
    n = len(adj_list)
    dist = {i: float('inf') for i in adj_list}
    dist[start] = 0
    priority_queue = [(0, start)]

    # Ciclo principal
    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)
        
        # Se a distância atual for maior que a registrada, continuar
        if current_dist > dist[current_vertex]:
            continue

        # Atualizando distâncias para os vizinhos
        for neighbor, weight in adj_list[current_vertex]:
            distance = current_dist + weight
            
            # Se encontrado caminho mais curto, atualizar e colocar na fila
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return dist

# Exemplo de uso:
adj_list = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
start = 0
print(dijkstra(adj_list, start))