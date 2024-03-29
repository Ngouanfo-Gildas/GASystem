import random
import math
import time
from typing import List
import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

    def distance(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    def point_aleatoire(self, m: int):
        self.x = random.randint(0, m)
        self.y = random.randint(0, m)
        return self

class Rectangle:
    """ Rectangle est un rectangle défini par 4 points"""
    def __init__(self, point1: Point,  point2: Point,  point3: Point,  point4: Point):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

    def if_rectangle(self):
        return self.point1.distance(self.point2) == self.point3.distance(self.point4) and self.point1.distance(self.point3) == self.point2.distance(self.point4)
    
    def __str__(self):
        return "["+str(self.point1)+", "+str(self.point2)+", "+str(self.point3)+", "+str(self.point4)+"]"

    def surface(self):
        return self.point1.distance(self.point2) * self.point1.distance(self.point4)
    
    def rectangle_aleatoire(self, zone_size: int, lon: int): 
        """Rectangle aléatoire de longueur lon\n"""      
        self.point1.point_aleatoire(zone_size)
        if self.point1.x + lon > zone_size and self.point1.y + lon > zone_size:
            self.point2.x = self.point1.x - lon
            self.point2.y = self.point1.y
            self.point3.x = self.point2.x
            self.point3.y = self.point1.y - lon
            self.point4.x = self.point1.x
            self.point4.y = self.point3.y
        elif self.point1.x + lon > zone_size:
            self.point2.x = self.point1.x
            self.point2.y = self.point1.y + lon
            self.point3.x = self.point1.x - lon
            self.point3.y = self.point2.y
            self.point4.x = self.point1.x
            self.point4.y = self.point1.y
        elif self.point1.y + lon > zone_size:
            self.point2.x = self.point1.x - lon
            self.point2.y = self.point1.y
            self.point3.x = self.point2.x
            self.point3.y = self.point1.y - lon
            self.point4.x = self.point1.x
            self.point4.y = self.point3.y
        else:
            self.point2.x = self.point1.x + lon
            self.point2.y = self.point1.y
            self.point3.x = self.point2.x
            self.point3.y = self.point1.y + lon
            self.point4.x = self.point1.x
            self.point4.y = self.point3.y
        return self

    def show_rectangle(self):
        x = [self.point1.x, self.point2.x, self.point3.x, self.point4.x, self.point1.x]
        y = [self.point1.y, self.point2.y, self.point3.y, self.point4.y, self.point1.y]
        plt.plot(x, y, "o--", color="black")
        plt.show()

Individu = List[Point]

Population = List[Individu]

def generate_genome(nb_nodes: int, zone_size: int) -> Individu:
    """ nb_nodes: nombre de noeuds à utiliser\n
        zone_size: la longueur de la zoe de déploiement """
    nodes: Individu = [Point() for i in range(nb_nodes)]
    genome: Individu = [Point()]*nb_nodes
    for i in range(nb_nodes):
        genome[i] = nodes[i].point_aleatoire(zone_size)
    return genome

def show_genome(rayonC: int, rayonS: int, genome: Individu):
    alpha = np.linspace(0, 2*np.pi, 200)
    for node in genome:
        cx = node.x
        cy = node.y

        xc = cx + rayonC*np.cos(alpha)
        yc = cy + rayonC*np.sin(alpha)

        xs = cx + rayonS*np.cos(alpha)
        ys = cy + rayonS*np.sin(alpha)

        plt.plot(cx, cy, "o", color="red")
        plt.plot(xc, yc, "b")
        plt.plot(xs, ys, "g")
    
    plt.grid(linestyle='-')
    plt.axis("equal")
    plt.show()

def generate_population(pop_size: int, nb_nodes: int, zone_size: int) -> Population:
    """ pop_size: taille de la population\n
        nb_nodes : lonueur d'un gène 
        zone_size: la longueur de la zoe de déploiement """
    return [generate_genome(nb_nodes, zone_size) for _ in range(pop_size)]

def calculFitness(individu: Individu):
    pass

def selection_roulatte(population: Population, fitnessPopulation: list, nombre: int) -> list:
    taille = len(population)
    selectionnes = []
    sommeFitness = sum(fitnessPopulation)
    probabilite = [fitnessPopulation[i]/sommeFitness for i in range(taille)]
    
    probabiliteCumule = [0 for i in range(taille)]
    probabiliteCumule[0] = probabilite[0]
    for i in range(taille):  
        probabiliteCumule[i] = probabiliteCumule[i] + sum([probabilite[j] for j in range(i+1)])

    for i in range(nombre):
        r = random.random()
        if r < probabiliteCumule[0]:
            selectionnes.append(population[0])
        else:
            for i in range(taille):
                if probabiliteCumule[i-1] < r  and r <= probabiliteCumule[i]:
                    selectionnes.append(population[i])
    return selectionnes

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

def crossover(genome1: Individu, genome2: Individu, probC: float):
    """ genome1, genome2: sont les deus solutions à croiser\n
        probC : la probabilité de crossover """
    offsprint1 = genome1
    offsprint2 = genome2
    nb = int(probC * len(genome1))
    pos1 = select_nb_gene(genome1, nb)
    pos2 = select_nb_gene(genome2, nb)

    pos11 = select_nb_gene(offsprint1, nb)
    pos22 = select_nb_gene(offsprint2, nb)

    for i in range(nb):
        offsprint1[pos11[i]] = genome2[pos2[i]]
        offsprint2[pos22[i]] = genome1[pos1[i]]

    print(pos1, pos2, sep="\n")
    return offsprint1, offsprint2

def mutation(genome: Individu, probM: float, zone_size: int) -> Individu:
    nb = int(probM * len(genome)) + 1
    pos = select_nb_gene(genome, nb)
    print(pos)
    for i in range(nb):
        genome[pos[i]].point_aleatoire(zone_size)
    return genome



pop     = [1,   2,  3, 4, 5,  6,  7,  8,  9]
fitness = [28, 18, 14, 9, 26, 30, 20, 50, 35]
# print(selection_roulatte(pop, fitness, 5))

p = Point()
q = Point() 
r = Point() 
s = Point()
rect = Rectangle(p, q, r, s)
# print(rect.rectangle_aleatoire(50, 1))
# rect.show_rectangle()

#population = generate_population(10, 5, 30)
genome1: Individu = generate_genome(20, 1200)
genome2: Individu = generate_genome(5, 20)
show_genome(60, 100, genome1)
# for p in genome1:
#     print(p, end=" ")
# print()
# for p in genome2:
#     print(p, end=" ")
# print()

# gen1, gen2 = crossover(genome1, genome2, 0.5)
# for p in gen1:
#     print(p, end=" ")
# print()
# for p in gen2:
#     print(p, end=" ")
# print()

# gen3 = mutation(gen1, 0.1, 20)
# for p in gen3:
#     print(p, end=" ")
# print()