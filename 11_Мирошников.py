# Задание №1
# class Soda():
#     def __init__(self, taste = ""):
#         self.taste = taste
#     def type_taste(self):
#         if self.taste:
#             print(f"Газировка с {self.taste} вкусом") 
#         else:
#             print("У вас обычная газировка")
# soda1 = Soda("апельсін")
# soda2 = Soda()
# soda1.type_taste()
# soda2.type_taste()

# Задание №2
# class Square:
#     def __init__(self, side):
#         self.side = side
    
#     def perimetr(self):
#         return self.side * 4
    
#     def __add__(self, other):
#         return self.perimetr() + other.perimetr()
#     def __sub__(self, other):
#         return self.perimetr() - other.perimetr()
#     def __mul__(self, other):
#         return self.perimetr() * other.perimetr()
#     def __truediv__(self, other):
#         return self.perimetr() / other.perimetr()

# square1 = Square(10)
# square2 = Square(20)
# print("Действие addition:", square1 + square2)
# print("Действие subtraction:", square1 - square2)
# print("Действие multiplication:", square1 * square2)
# print("Действие division:", square1 / square2)

# Задание №3

# class Car:
#     def __init__(self, color, type, year):
#         self.color = color
#         self.type = type
#         self.year = year
#     def start_engine(self):
#         print("Двигатель заведен")
#     def stop_engine(self):
#         print("Двигатель заглушен")
# car1 = Car("черный", "седан", "2020")
# car1.start_engine()
# car1.stop_engine()
# print(car1.color, car1.type, car1.year)

# Задание №4

# import math
# class Sphere:
#     def __init__(self, r = 1, x = 0, y = 0, z = 0):
#         self.r, self.x, self.y, self.z = r, x, y, z
#     def get_volume(self):
#         volume = (4 / 3) * math.pi * self.r ** 3
#         return volume
#     def get_square(self):
#          square = 4 * math.pi * self.r ** 2
#          return square
#     def get_radius(self):
#         return self.r
#     def get_center(self):
#         return (self.x, self.y, self.y)
#     def get_center(self, r):
#         self.r = r
#     def set_center(self, x, y, z):
#         self.x, self.y, self.z = x, y, z
#     def is_point_inside(self, x, y, z):
#         if math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2) <= self.r:
#             return True
#         else:
#             return False

# Задание № 5

# class SuperStr(str):
#     def is_repeatance(self, s):
#         # так и не понял что этот метод должен делать
#     def is_palindrome(self):
#         s = self.lower()
#         return s == s[::-1]
