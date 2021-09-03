import random

def initPopulation(nb_individus, nb_gene, valMaxChromosome):
    population = [[0] * nb_gene for n in range(nb_individus)]
    for i in range(0, nb_individus):
        for g in range(0, nb_gene):
            population[i][g] = (random.randint(1, valMaxChromosome))
    return population

def selectIndividuals(pop, target, precision):
    return [p for p in pop if sum(p) in range(int(target*(1-precision)), int(target*(1+precision)))]

def findTarget(population, target):
    for p in population:
        if (sum(p) == target):
            return p

def printPopulation(population):
    print("Population's length : {}".format(len(population)))
    for p in population:
            print("{} - {}".format(p, sum(p, 0)))

def crossIndividuals(pop):
    newPopulation = [[0] * len(pop[0]) for n in range(len(pop))]
    for p in range(0, len(pop)):
        n = random.randrange(0, len(pop))
        newPopulation[p][0:int(len(pop[0])/2)] = pop[n][0:int(len(pop[0])/2)]
        n = random.randrange(0, len(pop))
        newPopulation[p][-int(len(pop[0])/2):] = pop[n][-int(len(pop[0])/2):]
    return newPopulation

def muteIndividuals(pop, valChromosome, nMutation):
    while(nMutation >= 0):
        individu = random.randrange(0, len(pop))
        chromosome = random.randrange(0, len(pop[0]))
        pop[individu][chromosome] = random.randint(0, valChromosome)
        nMutation -= 1
    return pop


# parameters
# paramètres à faire varier
NB_CHROMOSOME_MAX = 5
VAL_CHROMOSOME_MAX = 6
NB_INDIVIDUAL_MAX = 5
PRECISION = 90/100
NB_MUTATION = 2
TARGET = 10
# p est l'individu qui atteint l'objectif 
# si p = cible on a trouvé un individu
p = 0
# compteur de nombre de tentatives
attempts = 1

# MAIN
print("### BUILDING POPULATION")
pop = initPopulation(NB_INDIVIDUAL_MAX, NB_CHROMOSOME_MAX, VAL_CHROMOSOME_MAX)
printPopulation(pop)
p = findTarget(pop, TARGET)
while (not p) and (len(pop) > 0):
    attempts += 1
    print("### INDIVIDUALS SELECTION")
    pop = selectIndividuals(pop, TARGET, PRECISION)    
    print("### COMPARE INDIVIDUALS TO TARGET")
    p = findTarget(pop, TARGET)
    if (p or len(pop) <= 0): break
    print("### INDIVUALS CROSSING")
    pop = crossIndividuals(pop)
    print("### COMPARE INDIVIDUALS TO TARGET")
    p = findTarget(pop, TARGET)
    if (p or len(pop) <= 0): break
    print("### MUTATION")
    pop = muteIndividuals(pop, VAL_CHROMOSOME_MAX, NB_MUTATION)
    print("### COMPARE INDIVIDUALS TO TARGET")
    p = findTarget(pop, TARGET)
    if (p or len(pop) <= 0): break
    printPopulation(pop)

if (p):
    print("Individual {} validate the target : {}".format(p, TARGET))
else:
    print("Population is exhausted for target : {}".format(TARGET))
print("Attempts count : {}".format(attempts))
