import AI_LAB_3
import random
import numpy as np
"""
ranking = [
    ([1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0,
      1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0], 15),
    ([1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0,
      1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0], 14),
]
"""


def select(ranking):

    parent1, fitness1 = ranking[0]
    parent2, fitness2 = ranking[1]

    return parent1, parent2


def crossover(parent1, parent2, crossover_rate):
    option = [1, 0]
    prob = [crossover_rate, 1 - crossover_rate]
    check_possibility = np.random.choice(option, p=prob)
    if check_possibility == 1:
        crossover_point = random.randint(1, len(parent1) - 1)
        child = parent1[0:crossover_point] + parent2[crossover_point:]
        return child
    else:
        child = parent1
        return child


def mutate(individual, mutation_rate):
    mutant = list(individual)
    for gen in range(0, len(mutant)):
        option = [1, 0]
        prob = [mutation_rate, 1 - mutation_rate]
        check_possibility = np.random.choice(option, p=prob)
        if check_possibility == 1:
            mutant[gen] ^= 1
    return mutant


def evolve(ranking, crossover_rate, mutation_rate):
    new_population = []
    for _ in ranking:
        parent1, parent2 = select(ranking)
        child = crossover(parent1, parent2, crossover_rate)
        mutant = mutate(child, mutation_rate)
        new_population.append(mutant)

    return new_population


AI_LAB_3.POPULATION_SIZE = 100
AI_LAB_3.CROSSOVER_RATE = 1
AI_LAB_3.MUTATION_RATE = 0.05


AI_LAB_3.EVOLVE = evolve
AI_LAB_3.log()
