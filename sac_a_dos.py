import random
import copy

POIDS = 50

objets = [
    {
        "poids": 0.05,
        "valeur": 1500
    },
    {
        "poids": 2,
        "valeur": 25000
    },
    {
        "poids": 12,
        "valeur": 2000
    },
    {
        "poids": 35,
        "valeur": 40000
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
        "poids": 3,
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

def unique(liste):
    set_list = []
    for elt in liste:
        if elt not in set_list:
            set_list.append(elt)
    return set_list

def selection_rang(population, fitnessValues):
    select = copy.deepcopy(fitnessValues)
    nwlist = sorted(select, key=lambda x: x[2], reverse = True)   
    return population[nwlist[0][0]], population[nwlist[1][0]]

def final_selection(population, fitnessValues):
    select = copy.deepcopy(fitnessValues)
    nwlist = [ elt for elt in select if elt[2] <= POIDS]
    nwlist = unique(sorted(nwlist, key=lambda x: x[1], reverse = True))
    return str(population[nwlist[0][0]])+" - POIDS  = "+str(nwlist[0][2])+" VALEUR = "+str(nwlist[0][1])

def print_solution(individu, objets):
    solution = "\n"
    n = len(individu)
    for id in range(n):
        if individu[id] == 1:
            solution += str(objets[id])+"\n"
    print(solution)

def main():
    pop_size      = 200
    pc            = 0.75
    pm            = 0.2
    nb_generation = 100
    population    = initPopulation(pop_size, nombre_objets)
    i  = 0  
    while i < nb_generation:
        nvlle_gen     = []
        fitnessValues = fitnessFunction(population, objets)
        for j in range(20):
            s1, s2 = selection_rang(population, fitnessValues)
            o1, o2    = crossover(s1, s2, pc)
            o11 = mutation(o1, pm)
            o22 = mutation(o2, pm)
            nvlle_gen.append(o11)
            nvlle_gen.append(o22)
        population = copy.deepcopy(nvlle_gen)
        i = i+1
    return final_selection(population, fitnessValues)

solution = main()
print(solution)

def initPopulationC(nb_individus, nb_gene):
    """ nb_individus: Nombre de solution à générer \n
        nb_gene : Nombre de gènes par individu \n
    """
    population = []
    for cp in range(nb_individus):
        individu = [1]
        while len(individu)<nb_gene:
            val = random.randint(2, nb_gene)
            if val not in individu:
                individu.append(val)
        population.append(individu)
    return population
