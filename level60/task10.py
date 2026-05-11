import random

# Condição do problema
weights = [2, 3, 4, 5, 9]
values = [3, 4, 8, 8, 10]
capacity = 20
population_size = 10
generations = 100
mutation_rate = 0.1
tournament_size = 3

# Geração da população inicial
def generate_individual(length):
    return [random.randint(0, 1) for _ in range(length)]

def generate_population(size, length):
    return [generate_individual(length) for _ in range(size)]

# Função de aptidão
def fitness(individual):
    total_weight = sum(individual[i] * weights[i] for i in range(len(individual)))
    total_value = sum(individual[i] * values[i] for i in range(len(individual)))
    if total_weight > capacity:
        return 0  # Excesso de peso na mochila
    return total_value

# Seleção por torneio
def tournament_selection(population):
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=fitness, reverse=True)
    return tournament[0]

# Crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutação
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]

# Loop principal do algoritmo genético
def genetic_algorithm():
    population = generate_population(population_size, len(weights))
    for generation in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population[:population_size]
        best_individual = max(population, key=fitness)
        print(f"Geração {generation}: Melhor indivíduo = {best_individual}, Aptidão = {fitness(best_individual)}")
    return best_individual

best_solution = genetic_algorithm()
print("Melhor solução encontrada:", best_solution)
print("Valor total:", fitness(best_solution))