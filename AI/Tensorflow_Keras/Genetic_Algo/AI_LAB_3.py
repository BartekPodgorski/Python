import random

SOLUTION = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1,
            0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]


def get_initial_population(population_size):
    population = []
    for _ in range(population_size):
        population.append([random.randint(0, 1) for i in range(len(SOLUTION))])

    return population


def get_fitness(individual):
    fitness = 0
    for feature in range(len(SOLUTION)):
        if individual[feature] == SOLUTION[feature]:
            fitness += 1

    return fitness


def get_the_best_individual(population):
    the_best_fitness = 0
    the_best_individual = None
    for index, individual in enumerate(population):
        fitness = get_fitness(individual)
        if fitness > the_best_fitness:
            the_best_fitness = fitness
            the_best_individual = individual

    return the_best_individual


def rank(population):
    ranking = []
    for individual in population:
        ranking.append((list(individual), get_fitness(individual)))

    return sorted(ranking, key=lambda tup: tup[1], reverse=True)


def log():
    with open("AI_LAB_3.txt", "w") as logfile:
        population = get_initial_population(POPULATION_SIZE)
        the_best_individual = get_the_best_individual(population)
        print(the_best_individual, file=logfile)
        iteration = 0
        while the_best_individual != SOLUTION:
            iteration += 1
            print(iteration)
            population = rank(population)
            population = EVOLVE(population, CROSSOVER_RATE, MUTATION_RATE)
            the_best_individual = get_the_best_individual(population)
            print(the_best_individual, file=logfile)
