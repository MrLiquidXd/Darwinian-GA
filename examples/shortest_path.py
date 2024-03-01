import random
from darwinian import darwinian_GA
import matplotlib.pyplot as plt

ga = darwinian_GA()
points_coords = {
    0: (0, 6),
    1: (4, 2),
    2: (5, 9),
    3: (1, 3),
    4: (4, 8),
    5: (2, 1),
    6: (6, 3),
}

# plt.scatter([point[0] for point in list(points_coords.values())[:6]], [point[1] for point in list(points_coords.values())[:6]], c='b')
# plt.scatter([points_coords[6][0]], [points_coords[6][1]], c='r')
# plt.show()

def path(individual):
    total = 0
    for i in range(len(individual) - 1):
        total += ((points_coords[individual[i]][0] - points_coords[individual[i + 1]][0]) ** 2 + (points_coords[individual[i]][1] - points_coords[individual[i + 1]][1]) ** 2) ** 0.5
    for i in individual:
        if individual.count(i) > 1:
            total += 100
    return total

ga.setup(
    len_gen=7, pop_size=100, mutation_rate=0.1, crossover_chance=0.5, epochs=1000, fitness_func=path, rand_func= lambda: random.randint(0, 6),
)

best = ga.bestparents(False)[0]

print(f"кротчайший путь: {", ".join(map(str, best[0]))}, расстояние: {best[1]}")

# draw path
plt.scatter([point[0] for point in list(points_coords.values())[:6]], [point[1] for point in list(points_coords.values())[:6]], c='b')
plt.scatter([points_coords[6][0]], [points_coords[6][1]], c='r')
plt.plot([points_coords[i][0] for i in best[0]], [points_coords[i][1] for i in best[0]])
plt.show()