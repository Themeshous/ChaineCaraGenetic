import random
import string

# Fonction objective
def fitness(chromosome, target):
    fitness = 0
    for i in range(len(chromosome)):
        if chromosome[i] != target[i]:
            fitness += 1
    return fitness

# Génération initiale de la population
def generate_population(size, length):
    population = []
    for i in range(size):
        chromosome = ''.join(random.choices(string.printable, k=length))
        population.append(chromosome)
    return population

# Sélection des individus pour la reproduction
def selection(population, fitnesses):
    new_population = []
    for i in range(len(population)):
        parent1 = random.choices(population, weights=fitnesses)[0]
        parent2 = random.choices(population, weights=fitnesses)[0]
        new_population.append(parent1)
    return new_population

#Croisement
def crossover(parent1, parent2):
    child = ""
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child += parent1[i]
        else:
            child += parent2[i]
    return child

# Mutation
def mutation(chromosome, probability):
    chromosome = list(chromosome)
    for i in range(len(chromosome)):
        if random.random() < probability:
            chromosome[i] = random.choice(string.printable)
    return "".join(chromosome)

# Boucle principale de l'algorithme génétique
def genetic_algorithm(population_size, mutation_probability, max_iterations, target):
    population = generate_population(population_size, len(target))
    for i in range(max_iterations):
        fitnesses = [fitness(chromosome, target) for chromosome in population]
        population = selection(population, fitnesses)
        new_population = []
        for i in range(int(population_size/2)):
            #i+1
            parent1 = population[i]
            parent2 = population[i+1] if i+1 < len(population) else population[0]
            child = crossover(parent1, parent2)
            child = mutation(child, mutation_probability)
            new_population.append(child)
        population = new_population
    best_chromosome = min(population, key=lambda x: fitness(x, target))
    best_fitness = fitness(best_chromosome, target)
    return best_chromosome, best_fitness

# Appeler l'algorithme génétique
population_size = 100
mutation_probability = 0.01
max_iterations = 1000
target = "Bonjour tout le monde"
best_chromosome, best_fitness = genetic_algorithm(population_size, mutation_probability, max_iterations, target)
print(best_chromosome, best_fitness)