# Задание №1

# def fib(max_num):
#     a, b = 0, 1
#     for i in range(max_num):
#         yield a
#         a, b = b, a + b
# print(list(fib(10)))

# Задание №2

# def cycle(max_num):
#     a = '1'
#     b = '2'
#     c = '3'
#     for i in range(max_num):
#         yield a
#         yield b
#         yield c
# x = cycle(5)
# print('-'.join(x))

# Задание №3

from abc import ABC, abstractmethod
class Pizza:
    def __init__(self):
        self.size = 'Размер'
        self.cheese = 'Сыр'
        self.pepperoni = 'Колбаса'
        self.mushrooms = 'Грибы'
        self.onions = 'Лук'
        self.bacon = 'Бекон'
class PizzaBuilder:
    @abstractmethod
    def add_cheese(self) -> None: pass
    @abstractmethod
    def add_pepperoni(self) -> None: pass
    @abstractmethod
    def add_mushrooms(self) -> None: pass
    @abstractmethod
    def add_onions(self) -> None: pass
    @abstractmethod
    def add_bacon(self) -> None: pass


        





