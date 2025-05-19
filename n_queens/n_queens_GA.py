import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

N = 8
POPULATION_SIZE = 150  #aumentei de 100 para 150
MUTATION_RATE = 0.1   #aumentei de 0.05 para 0.1
MAX_GENERATIONS = 1000
VISUALIZE_EVERY = 50
MAX_FITNESS = (N * (N - 1)) // 2

def create_individual():
    genes = [random.randint(0, N - 1) for _ in range(N)]
    fitness = evaluate_fitness(genes)
    return (genes, fitness)

def evaluate_fitness(genes):
    non_attacking = 0
    for i in range(len(genes)):
        for j in range(i + 1, len(genes)):
            if genes[i] != genes[j] and abs(genes[i] - genes[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking

def create_population():
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    population.sort(key=lambda x: x[1], reverse=True)
    return population

def select_parent(population):
    candidates = random.sample(population, 5)
    candidates.sort(key=lambda x: x[1], reverse=True)
    return candidates[0]

def crossover(parent1, parent2):
    crossover_point = random.randint(0, N - 1)
    child_genes = parent1[0][:crossover_point] + parent2[0][crossover_point:]
    return (child_genes, evaluate_fitness(child_genes))

def mutate(individual):
    genes = individual[0][:]
    if random.random() < MUTATION_RATE:
        i = random.randint(0, N - 1)
        genes[i] = random.randint(0, N - 1)
    return (genes, evaluate_fitness(genes))

def evolve_population(population):
    new_generation = population[:10]
    while len(new_generation) < POPULATION_SIZE:
        parent1 = select_parent(population)
        parent2 = select_parent(population)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_generation.append(child)
    new_generation.sort(key=lambda x: x[1], reverse=True)
    return new_generation

def plot_board(genes, generation, fitness):
    plt.figure(figsize=(6, 6))
    plt.title(f'Geração {generation} - Fitness: {fitness}')
    plt.xticks(range(N))
    plt.yticks(range(N))
    plt.grid(True)
    plt.gca().invert_yaxis()

    for x in range(N):
        for y in range(N):
            color = 'white' if (x + y) % 2 == 0 else 'gray'
            plt.gca().add_patch(patches.Rectangle((x, y), 1, 1, color=color))

    for col, row in enumerate(genes):
        plt.text(col + 0.5, row + 0.5, '♛', fontsize=24,
                 ha='center', va='center', color='red')

    plt.xlim(0, N)
    plt.ylim(0, N)
    plt.gca().set_aspect('equal')
    plt.show()

def run_genetic_algorithm(max_generations, population_size, mutation_rate):
    population = create_population()

    for generation in range(1, max_generations + 1):
        best_individual = population[0]

        if best_individual[1] >= MAX_FITNESS:
            print("Solução encontrada na geração:", generation)
            plot_board(best_individual[0], generation=generation, fitness=best_individual[1])
            return "Solução encontrada na geração: " + str(generation)

        if generation % VISUALIZE_EVERY == 0:
            print("Geração", generation, "Melhor fitness:", best_individual[1])
            plot_board(best_individual[0], generation, best_individual[1])

        population = evolve_population(population)

    print("Não foi encontrada uma solução perfeita")
    plot_board(population[0][0], max_generations, population[0][1])
    return "Solução não encontrada"

run_genetic_algorithm(MAX_GENERATIONS, POPULATION_SIZE, MUTATION_RATE)
