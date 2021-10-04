from GASystem import Point, Individu, Population, show_genome
import random, copy
from math import sqrt

# ------------------------------------------------------------------
def positions_potentielles(largeur_zone: int, rs):
    potentials_positions = []
    k = 2*rs*sqrt(sqrt(3)/2)
    j = rs
    while j<largeur_zone:
        i = rs
        while i<largeur_zone:
            potentials_positions.append(Point(i, j))
            i += k
        j += k
    return potentials_positions

# -------------------------------------------------------------------
# Générer un schéma de placement aléatoire
def generate_solution(pos_potentiel: Individu, nb_nodes: int):
    individu = []
    n = len(pos_potentiel)
    for i in range(nb_nodes):
        k = random.randint(0, n-1)
        if k not in individu:
            individu.append(pos_potentiel[k])
    return individu

# -------------------------------------------------------------------
# Générer un ensemble d'individus (population)
def generate_population(pos_potentiel: Individu, pop_size: int, nb_nodes: int) -> Population:
    """ pop_size: taille de la population\n
        nb_nodes : lonueur d'un gène 
        zone_size: la longueur de la zoe de déploiement """
    return [generate_solution(pos_potentiel, nb_nodes) for _ in range(pop_size)]

# -------------------------------------------------------------------
# Générer une liste d'événements
def generate_events(nb_events: int, zone_size: int) -> Individu:
    """ nb_nodes: nombre d'événements'\n
        zone_size: la longueur de la zone de déploiement """
    nodes: Individu = [Point() for i in range(nb_events)]
    events: Individu = [Point()]*nb_events
    for i in range(nb_events):
        events[i] = nodes[i].point_aleatoire(zone_size)
    return events

# -------------------------------------------------------------------
def select_nb_gene(genome: Individu, nb: int) -> list:
    """ Retourne les positions des gènes de génome\n
        sélectionnées aléatoirement. \n
        nb: est le nombre de ces gènes. """
    n = len(genome)
    positions = []
    while len(positions)<nb:
        p = random.randint(0, n-1)
        if p not in positions:
            positions.append(p)
    return positions

# -------------------------------------------------------------------
# Croiser deux solutions pour fournir deux nouvelles solutions
def crossover(genome1: Individu, genome2: Individu, probC: float):
    """ genome1, genome2: sont les deus solutions à croiser\n
        probC : la probabilité de crossover """
    offsprint1 = copy.deepcopy(genome1)
    offsprint2 = copy.deepcopy(genome2)
    nb = int(probC * len(genome1))

    pos1 = select_nb_gene(genome1, nb)
    pos2 = select_nb_gene(genome2, nb)

    pos11 = select_nb_gene(offsprint1, nb)
    pos22 = select_nb_gene(offsprint2, nb)

    for i in range(nb):
        offsprint1[pos11[i]] = genome2[pos2[i]]
        offsprint2[pos22[i]] = genome1[pos1[i]]

    return offsprint1, offsprint2

# -------------------------------------------------------------------
# Muter une solution pour produire une nouvelle solution
def mutation(individu: Individu, pm: float):
    n = len(individu)
    nb = int(pm*n)
    for i in range(nb):
        i1 = random.randint(0, n-1)
        i2 = random.randint(0, n-1)
        individu[i1], individu[i2] = individu[i2], individu[i1]
    return individu

# ------------------------------------------------------
# Calculer la liste des événements couverts
def event_couvert(solution: Individu, events: Individu, Rs):
    """Rs = rayon de coverture"""
    eventCover = []
    for p in solution:
        for e in events:
            if e.distance(p) < Rs :
                if e not in eventCover:
                    eventCover.append(e)
    return eventCover

# --------------------------------
# Calculer la liste des voisins d'un noeud
def list_voisins(solution: Individu, node: Point, Rc):
    """Rc = rayon de communication"""
    voisin = []
    for q in solution :
        if node.distance(q) < Rc :
            voisin.append(q)
    return voisin

# --------------------------------
# Construction des clusters
def list_clusters(solution:Individu, Rc):
    clusters = []
    for p in solution:
        cluster = []
        Vp = list_voisins(solution, p, Rc)
        for q in Vp:
            if q not in cluster:
                cluster.append(q)
            Vq = list_voisins(solution, q, Rc)
            for r in Vq:
                if r not in cluster:
                    cluster.append(r)
            solution.remove(q)
        clusters.append(cluster)
    return clusters

# --------------------------------
# Evaluation d'une solution
def fitness_sol(solution, events, Rs):
    fitness = 0
    event_size = len(events)
    evt_cv = event_couvert(solution, events, Rs)
    fitness = len(evt_cv)/event_size*100
    return fitness

def fitnessFunction(population, events, Rs):
    fitnessValues = []
    for solution in population:
        fitness_val = fitness_sol(solution, events, Rs)
        fitnessValues.append([solution, fitness_val])
    return fitnessValues

# --------------------------------
def unique(liste):
    set_list = []
    for elt in liste:
        if elt not in set_list:
            set_list.append(elt)
    return set_list

# --------------------------------
def selection_rang(fitnessValues):
    select = copy.deepcopy(fitnessValues)
    nwlists = unique(select)
    nwlist = sorted(nwlists, key=lambda x: x[1], reverse = True)
    if len(nwlist) < 2:
        x = nwlist[0][0]
    else:
        x = nwlist[1][0]
    return nwlist[0][0], x


ZONE_SIZE = 100
Rs = 6
NB_NODES  = 20
NB_EVENTS = 8
events_list   = generate_events(NB_EVENTS, ZONE_SIZE)
def main():
    pop_size      = 100
    pc            = 0.65
    pm            = 0.05
    nb_generation = 50
    pos_potentiel = positions_potentielles(ZONE_SIZE, Rs)
    population    = generate_population(pos_potentiel, pop_size, NB_NODES)
    i  = 0  
    cond2 = 0
    while cond2 < 90 and i < nb_generation:
        nvlle_gen     = []
        fitnessValues = fitnessFunction(population, events_list, Rs)
        for j in range(35):
            s1, s2 = selection_rang(fitnessValues)
            o1, o2    = crossover(s1, s2, pc)
            o11 = mutation(o1, pm)
            o22 = mutation(o2, pm)
            nvlle_gen.append(o11)
            nvlle_gen.append(o22)
        population = copy.deepcopy(nvlle_gen)
        cond2 = fitness_sol(population[0], events_list, Rs)
        print(cond2)
        i = i+1
    return population[0]


best_solution = main()
"""for k in best_solution:
    print(k)"""
show_genome(10, 6, best_solution, events_list)
