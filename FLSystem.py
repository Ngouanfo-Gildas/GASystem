import numpy as np
import matplotlib.pyplot as plt
from random import randint

def print_circle(zoneI: int, rayonC: int, rayonS: int, nombre: int):
    alpha = np.linspace(0, 2*np.pi, 200)

    for i in range(nombre+1):
        cx = randint(1, zoneI-5)
        cy = randint(1, zoneI-5)
        xc = cx + rayonC*np.cos(alpha)
        yc = cy + rayonC*np.sin(alpha)
        xs = cx + rayonS*np.cos(alpha)
        ys = cy + rayonS*np.sin(alpha)
        plt.plot(cx, cy, "+")
        plt.plot(xc, yc, "b")
        plt.plot(xs, ys, "g")
    
    plt.grid(linestyle='-')
    plt.axis("equal")
    
    plt.show()

print_circle(1000, 60, 100, 15)


