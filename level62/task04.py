import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor(cities):
    n = len(cities)
    start_city = cities[0]
    unvisited = cities[1:]
    current_city = start_city
    route = [start_city]

    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        route.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    route.append(start_city)
    return route

# Exemplo de uso
cities = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
path = nearest_neighbor(cities)
print("Caminho do viajante comercial:", path)