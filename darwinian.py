import random

class Darwinian_GA():
    def __init__(self) -> None:
        """
        Привет, используй .setup()! 
        """

    def setup(self, len_gen: int, pop_size: int, mutation_rate: float, crossover_chance: float, epochs: int, fitness_func: callable, rand_func = lambda: random.randint(0, 1)) -> None:
        """
        Загрузка!
        len_gen - длина индивида! [0, 1, 1, 0, 1... n раз]
        pop_size - размер популяции(количество индивидов)
        mutation_rate - вероятность мутации, желательно от 0 до 0.5
        epochs - количество эпох - это ясно
        fitness_func - функция приспособленности начинается с def fitness(individual):
        rand_func - случайное значение может быть функцией rand_func = lambda: random.randint(0, 1)
        """
        self.len_gen = len_gen # длина индивида
        self.pop_size = pop_size # размер популяции
        self.mutation_rate = mutation_rate # вероятность мутации
        self.crossover_chance = crossover_chance # вероятность кроссовера
        self.epochs = epochs # количество эпох
        self.population = [] # популяция
        self.fitness = fitness_func # функция приспособленности
        self.rand_func = rand_func # случайное значение может быть функцией
        new_individual = [] # новый индивид
        
        # Инициализируем популяцию
        
        for i in range(pop_size):
            new_individual = []
            for j in range(len_gen):
                new_individual.append(self.rand_func())
            
            self.population.append(new_individual)

    # __selection_utils__
    
    def tournament_selection(self, tournament_size) -> list:
        '''
        Выбираем двух родителей с помощью турнирного отбора
        '''
        # Случайным образом выбираем особей для турнира
        tournament = random.sample(self.population, tournament_size)
        # Определяем лучшую особь в турнире
        best_individual = max(tournament, key=self.fitness)
        return best_individual

    def roulette_selection(self) -> list:
        '''
        Выбираем двух родителей с помощью рулетки
        '''
        # Случайным образом выбираем особей для рулетки
        fitness_sum = sum(map(self.fitness, self.population))
        roulette = [self.fitness(individual) / fitness_sum for individual in self.population] if fitness_sum != 0 else [1 / len(self.population) for _ in range(len(self.population))]
        return random.choices(self.population, weights=roulette, k=1)[0]

    def crossover(self, individual_1, individual_2) -> list:
        '''
        Кроссовер
        '''
        # Случайным образом выбираем особей для кроссовера
        new_individual = []
        for i in range(len(individual_1)):
            if random.random() < self.crossover_chance:
                new_individual.append(individual_1[i])
            else:
                new_individual.append(individual_2[i])
        return new_individual

    def mutate(self, individual) -> list:
        '''
        Мутация
        '''
        # Случайным образом выбираем особей для мутации
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = self.rand_func()
        return individual
    
    # __selection_constructor__
    
    def constructor(self, selection_method: str = "bestparents", MaxOrMin: bool = True, how_much: int = 5, print_pop: bool = False, **kwargs) -> list:
        """
        Аргументы:
            selection_method (str, optional): _description_. Defaults to "bestparents".
            MaxOrMin (bool, optional): _description_. Defaults to True.
            how_much (int, optional): _description_. Defaults to 5.
            print_pop (bool, optional): _description_. Defaults to False.

        Ща покажу как этим пользоваться:
        1) bestparents - выбираем двух лучших родителей
        2) tournament - выбираем двух родителей с помощью турнирного отбора
        3) roulette - выбираем двух родителей с помощью рулетки
        
        При турнирном отборе можно задать параметр tournament_size, по умолчанию равен 2
        """
        for i in range(self.epochs):
            l = list(zip(self.population, map(self.fitness, self.population)))
            best = sorted(l, key=lambda x: x[1], reverse=MaxOrMin)[:how_much]
            if print_pop: print(best)
            self.population = list()
            self.population.append(best[0][0])
            if random.randint(0, 1) > 1: self.population.append(best[how_much-1][0])
            for i in range(self.pop_size-2):
                
                match selection_method:
                    case "bestparents":
                        # Выбираем двух лучших родителей
                        self.population.append(self.crossover(best[0][0], best[1][0]))
                    case "tournament":
                        # Выбираем двух родителей с помощью турнирного отбора
                        tournament_size = kwargs["tournament_size"] if "tournament_size" in kwargs else 2
                        parent1 = self.tournament_selection(tournament_size)
                        parent2 = self.tournament_selection(tournament_size)
                        # Создаем новую особь с помощью кроссовера
                        self.population.append(self.crossover(parent1, parent2))
                    case "roulette":
                        # Выбираем двух родителей с помощью рулетки
                        parent1 = self.roulette_selection()
                        parent2 = self.roulette_selection()
                        # Создаем новую особь с помощью кроссовера
                        self.population.append(self.crossover(parent1, parent2))
                    case _:
                        raise ValueError("Я твоя не понимать!")
            for i in self.population:
                i = self.mutate(i)
        l = list(zip(self.population, map(self.fitness, self.population)))
        best = sorted(l, key=lambda x: x[1], reverse=MaxOrMin)[:how_much]
        return best
    
