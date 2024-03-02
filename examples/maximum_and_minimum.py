# импорт библиотек
from darwinian import Darwinian_GA
import random

# Во первых мы создадим экземпляр maxGA
maxGA = Darwinian_GA()

# Функция приспособленности
def fitness(individual):
    return sum(individual)

# инициализируем 
maxGA.setup(10, 10, 0.01, 0.8, 100, fitness, lambda: random.randint(0, 1))

# запускаем
max_individual = maxGA.constructor(MaxOrMin=True)
min_individual = maxGA.constructor(MaxOrMin=False)

print(max_individual[0])
print(min_individual[0])

# >>> ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10)
# >>> ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
