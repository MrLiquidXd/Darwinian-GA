# задача о рюкзаке

# импорт библиотек
from darwinian import Darwinian_GA
import random
backpack = Darwinian_GA() # объект, который будет выполнять задачу

# словарь, где ключ - название предмета, а значение - пара (вес, цена)
items = {
    "телефон": (5, 100), 
    "ноутбук": (20, 200),
    "контейнер": (10, 50),
    "конфеты": (10, 30),
    "монеты": (2, 1),
    "ручка": (3, 5),
    "кострюля": (8, 50),
    "бутылка воды": (2, 20),
    "еда": (2, 10),
    "зонт": (10, 150),
    "ложки/вилки": (1, 5),
    "спальный мешок": (10, 200),
    "спички": (1, 3),
    "ничто": (0, 0) # нет ничего, вес и цена равны 0
}

max_weight = 40 # максимальный вес рюкзака

def backpack_func(*individual):
    """
    функция приспособленности, которая считает цену
    для данной комбинации предметов в рюкзаке
    """
    total_weight = 0
    total_price = 0
    unique_items = set() # набор уникальных предметов в рюкзаке
    for item in individual[0]:
        if item != "ничто":
            if item in unique_items:
                return -100 # если предмет повторяется, то цена равна -100
            unique_items.add(item)
        total_weight += items[item][0] # суммируем вес
        total_price += items[item][1] # суммируем цену
    if total_weight > max_weight:
        return 0 # если вес превышает максимальный, то цена равна 0
    else:
        return total_price-total_weight # иначе возвращаем общую цену

backpack.setup(
    len_gen=len(items), # количество предметов в гене
    pop_size=100, # размер популяции
    mutation_rate=0.1, # вероятность мутации
    crossover_chance=0.5, # вероятность кроссовера
    epochs=1000, # количество итераций
    fitness_func=backpack_func, # функция приспособленности
    rand_func=lambda: random.choice(list(items.keys())), # функция для рандома
    ) # настройка объекта для выполнения задачи

best = backpack.constructor()[0] # лучшая комбинация из поколения
filtered = [gen for gen in best[0] if gen != "ничто"] # отфильтрованный список без "ничего"

print(filtered) # печатаем отфильтрованный список
