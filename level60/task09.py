import random
import numpy as np

# Parâmetros do algoritmo genético
POPULATION_SIZE = 100
NUM_GENERATIONS = 500
TOURNAMENT_SIZE = 5
MUTATION_RATE = 0.01

# Exemplo de função de aptidão (maximização da função)
def fitness_function(individual):
    return sum(individual)

# Inicialização da população
def initialize_population(pop_size, chromosome_length):
    population = []
    for _ in range(pop_size):
        individual = np.random.randint(2, size=chromosome_length)
        population.append(individual)
    return population

# Seleção por torneio
def tournament_selection(population, fitnesses):
    selected = random.sample(list(zip(population, fitnesses)), TOURNAMENT_SIZE)
    selected.sort(key=lambda x: x[1], reverse=True)
    return selected[0][0]

# Crossover de ponto único
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

# Mutação
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
    return individual

# Ciclo principal do algoritmo genético
def genetic_algorithm():
    chromosome_length = 10
    population = initialize_population(POPULATION_SIZE, chromosome_length)

    for generation in range(NUM_GENERATIONS):
        fitnesses = [fitness_function(ind) for ind in population]
        new_population = []

        for _ in range(POPULATION_SIZE // 2):
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))

        population = new_population

    # Solução ótima
    best_individual = max(population, key=fitness_function)
    return best_individual, fitness_function(best_individual)

# Chamada do algoritmo
best_individual, best_fitness = genetic_algorithm()
print("Melhor indivíduo:", best_individual)
print("Função de aptidão:", best_fitness)