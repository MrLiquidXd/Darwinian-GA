![logo](https://github.com/MrLiquidXd/Darwinian-GA/assets/161674051/0ed0b889-2553-43f9-8271-e38d9c89456a)

[Ссылка на PyPi](https://pypi.org/project/Darwinian/)

## Вдохновлен EasyGa ❤️ 
[ссылка на их проект](https://github.com/danielwilczak101/EasyGA?ysclid=lt6np341qo375655432)

# Darwinian GA

Эта библиотека Python реализует "Дарвиновский" Генетический Алгоритм (GA) для задач оптимизации. GA симулирует процесс естественного отбора, где наиболее приспособленные особи выбираются для воспроизводства, чтобы произвести потомство следующего поколения.

## Особенности

- **Генетическое представление**: Каждая особь в популяции представлена в виде списка генов.
- **Инициализация популяции**: Популяция инициализируется случайными особями, но возможние значения генов могут задоваться пользователем.
- **Функция приспособленности**: Пользовательская функция для оценки приспособленности особи.
- **Выбор**: Реализованы три типа методов выбора: Лучшие Родители, Турнир и Рулетка.
- **Скрещивание**: Метод для объединения генов двух родителей для создания новой особи.
- **Мутация**: Метод для внесения небольших изменений в особи для поддержания разнообразия в популяции.

## Методы

- `setup`: Инициализирует GA с необходимыми параметрами.
- `tournament_selection`: Выбирает лучшую особь из случайно выбранного подмножества популяции.
- `roulette_selection`: Выбирает особь из популяции с использованием выбора рулеткой.
- `crossover`: Объединяет гены двух особей для создания новой.
- `mutate`: Вносит небольшие изменения в особь.
- `bestparents`: Запускает GA с использованием метода выбора Лучшие Родители.
- `tournament`: Запускает GA с использованием метода выбора Турнир.
- `rulette`: Запускает GA с использованием метода выбора Рулетка.

## Использование

Для использования этого модуля вам нужно определить функцию приспособленности, которая оценивает приспособленность особи. Затем вы можете инициализировать GA с необходимыми параметрами и запустить его с использованием одного из методов выбора.


```python
from darwinian import darwinian_GA
import random

# Определите функцию приспособленности
def fitness(individual):
    return sum(individual)

# Инициализируйте GA
ga = darwinian_GA()
ga.setup(len_gen=10, pop_size=100, mutation_rate=0.1, crossover_chance=0.5, epochs=100, fitness_func=fitness)

# Запустите GA
best_individuals = ga.bestparents()
print(best_individuals[0])
```

GA будет развивать популяцию в течение указанного количества эпох и возвращать лучших особей из окончательной популяции. Вы также можете распечатать популяцию на каждой эпохе, чтобы наблюдать за прогрессом GA.

```python
ga.bestparents(print_pop=True)
```

## Кастомизация функции генерации особи rand_func

Эта функция генерирует гены индивида. По умолчанию, генерируются случайное целое число в диапазоне от 0 до 1.

Получается -> [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

Ее можно переопределить:

```python
from darwinian import darwinian_GA
import random

def fitness(individual):
    return sum(individual)

# Инициализируйте GA
ga = darwinian_GA()
ga.setup(len_gen=10, pop_size=100, mutation_rate=0.1, crossover_chance=0.5, epochs=100, fitness_func=fitness, rand_func= lambda: random.randint(0, 5))

# Запустите GA
best_individuals = ga.bestparents()
print(best_individuals[0])
```

результат будет

```python
([5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 50)
```
## Метод максимезации или минимизации:

Если вы хотите чтоб приспособленность была минимизирована:

то вы можете использовать параметр `MaxOrMin=False`

```python
best_individuals = ga.bestparents(MaxOrMin=False)
print(best_individuals[0])
```

при прошлом примере ответ будет:

```python 
([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
```
