import random
from darwinian import Darwinian_GA
import matplotlib.pyplot as plt

ga = Darwinian_GA()
points_coords = {
    0: (0, 6),
    1: (4, 2),
    2: (5, 9),
    3: (2, 5),
    4: (4, 5),
    5: (2, 1),
    6: (6, 3),
    7: (0, 0),
    8: (3, 8)
}

dlina = len(points_coords)-1

def path(*ind):
    total = 0
    individual = ind[0]
    for i in range(len(individual) - 1):
        total += ((points_coords[individual[i]][0] - points_coords[individual[i + 1]][0]) ** 2 + (points_coords[individual[i]][1] - points_coords[individual[i + 1]][1]) ** 2) ** 0.5
    for i in individual:
        if individual.count(i) > 1:
            total += 100
    if ind[1] != False:
        if individual[0] == 0: total -= 100
        if individual[dlina] == dlina: total -= 100


    return total


ga.setup(
    len_gen=dlina+1, pop_size=150, mutation_rate=0.08, crossover_chance=0.7, epochs=1000, fitness_func=path, rand_func= lambda: random.randint(0, dlina),
)

best = ga.constructor(MaxOrMin=False)[0]

print(f"кротчайший путь: {best[0]}, расстояние: {path(best[0], False)}")


plt.scatter([point[0] for point in list(points_coords.values())[:dlina]], [point[1] for point in list(points_coords.values())[:dlina]], c='b')
plt.scatter([points_coords[dlina][0]], [points_coords[dlina][1]], c='r')
plt.plot([points_coords[i][0] for i in best[0]], [points_coords[i][1] for i in best[0]])

plt.show()
