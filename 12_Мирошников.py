# Задание №1

# class product:
#     def __init__(self, name, store, price):
#         self.name = name
#         self.store = store
#         self.price = price
# class Hub:
#     def __init__(self):
#         self.producrs =  []
#     def add_products(self, product):
#         self.producrs.append(product)
# pruduct_1 = product('phone', 'Apple', 3000)
# product_2 = product('notebook', 'Asus', 4000)
# hub_1 = Hub()
# hub_1.add_products(pruduct_1)
# hub_1.add_products(product_2)
# print(pruduct_1.price)

# Задание №2

# class BeeElef:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def fly(self):
#         if self.a < self.b:
#             return True
#         else:
#             return False
#     def trumpet(self):
#         if self.b <= self.a:
#             return "tu-tu-doo-doo"
#         else:
#             return "wzzzz"
#     def eat(self, meal, value):
#         if meal == "nectar":
#             self.a += value
#             self.b -= value
#         elif meal == "grass":
#             self.a -= value
#             self.b += value
#         if self.a > 100:
#             self.a = 100
#         elif self.a < 0:
#             self.a = 0
#         if self.b > 100:
#             self.b = 100
#         elif self.b < 0:
#             self.b = 0
#     def all(self):
#         return (self.a, self.b)
# c = BeeElef(20, 30)
# c.eat("nectar", 50)
# print(c.fly())
# print(c.trumpet())
# print(c.all())

# Задание №3

class Bus:
    def __init__(self, speed, max_place, max_speed, list_name, free_place, dict_place):
        self.speed = speed
        self.max_place = 30
        self.max_speed = 60
        self.list_name = []
        self.free_place = self.max_place - len(self.list_name)
        self.dict_place = {}
        # for i in range(0, self.max_place):
        #     key = self.list_name[i]
        #     value = self.max_place[i]
        #     self.dict_place[key] = value
    def add_pass(self, pass_1):
        self.pass_1 = pass_1
        if len(self.list_name) + self.pass_1 <= self.max_place:
            return len(self.list_name) + self.pass_1
        else:
            return "Свободных мест нет"
    def sub_pass(self, pass_2):
        self.pass_2 = pass_2
        if len(self.list_name) - self.pass_2 >= 0:
            return len(self.list_name) - self.pass_2
        else:
            return "Все пассажиры вышли"
    def add_speed(self, speed_1):
        self.speed_1 = speed_1
        if self.speed + self.speed_1 <= self.max_speed:
            return self.speed + self.speed_1
        else:
            return "Максимальная скорость 60"
    def sub_speed(self, speed_2):
        self.speed_2 = speed_2
        if self.speed - self.speed_2 > 0:
            return self.speed - self.speed_2
        else:
            return "Вы остановились"
    def add_pass1(self, pass_3):
        self.pass_3 = pass_3
        if self.pass_3 in self.list_name:
            return "Пассажир уже в автобусе"
        else:
            self.list_name += self.pass_3
    def sub_pass1(self, pass_4):
        self.pass_4 = pass_4
        if self.pass_4 in self.list_name:
            self.list_name -= self.pass_4
        else:
            return "Такого пассажира нет в автобусе"
x = Bus(50, 30, 60, [], 10, {})
print(x.add_speed(50))
# Вроде работает, но есть сомнения. Особенно со словарем







    