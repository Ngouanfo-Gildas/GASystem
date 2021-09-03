import random
import copy

POIDS = 15

objets = [
    {
        "poids": 12,
        "valeur": 2000
    },
    {
        "poids": 2,
        "valeur": 100000
    },
    {
        "poids": 2,
        "valeur": 2000
    },
    {
        "poids": 1,
        "valeur": 2000
    },
    {
        "poids": 4,
        "valeur": 10000
    }
]

nombre_objets = len(objets)

# Fonction d'initialisation de la population
def initPopulation(nb_individus, nb_gene):
    """ nb_individus: Nombre de solution à générer \n
        nb_gene : Nombre de gènes par individu \n
    """
    population = [[0] * nb_gene for n in range(nb_individus)]
    for i in range(0, nb_individus):
        for g in range(0, nb_gene):
            population[i][g] = (random.randint(0, 1))
    return population

def crossover(ind1, ind2, pc):
    """ ind1, ind2 : sont deux individus \n
        pc : la probabilité de crossover 
    """
    ofs1 = copy.deepcopy(ind1)
    ofs2 = copy.deepcopy(ind2)
    nb = int(pc * len(ind1))
    offsp1 = ind1[:nb] + ofs2[nb:]
    offsp2 = ind2[:nb] + ofs1[nb:]
    return offsp1, offsp1

def reversebit(b):
    return 0 if b==1 else 1

def mutation(individu, pm):
    tail_ind = len(individu)
    nb = int(pm * tail_ind)
    for i in range(nb):
        va = random.randint(0, tail_ind-1)
        individu[va] = reversebit(individu[va])
    return individu

def fitnessFunction(population, objets):
    pop_size = len(population)
    nombre_objets = len(objets)
    fitnessValues = []
    for individu in population:
        valeur = 0
        poids = 0
        for gene in range(nombre_objets):
            valeur += individu[gene]*objets[gene]['valeur']
            poids  += individu[gene]*objets[gene]['poids']
        fitnessValues.append([population.index(individu), valeur, poids])
    return fitnessValues

def selection_rang(population, fitnessValues, nbre):
    taille = len(population)
    select = copy.deepcopy(fitnessValues)
    nwlist = sorted(select, key=lambda x: x[2], reverse = True)   
    return population[nwlist[0][0]], population[nwlist[1][0]]


def main():
    pop_size      = 10
    pc            = 0.7
    pm            = 0.1
    nb_generation = 5
    population    = initPopulation(pop_size, nombre_objets)
    i  = 0
    while i < nb_generation:
        nvlle_gen     = []
        fitnessValues = fitnessFunction(population, objets)
        print(i)
        for j in range(6):
            s1, s2 = selection_rang(population, fitnessValues, 2)
            o1, o2    = crossover(s1, s2, pc)
            o11 = mutation(o1, pm)
            o22 = mutation(o2, pm)
            nvlle_gen.append(o11)
            nvlle_gen.append(o22)
        population = copy.deepcopy(nvlle_gen)
        i = i+1
    return s1

print(main())