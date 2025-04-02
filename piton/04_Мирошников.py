# import math

# print(math.pi)
import math

# a = int(input("Введите значение а"))
# b = int(input("Введите значение b"))
# y = (a**2 / 3) + ((a**2 + 4) / b) + (((a**2 + 4)**(0.5)) / 4) + ((((a**2 + 4)**3)**(0.5)) / 4)
# print("y = ", y)

# x = int(input("Введите значение х"))
# y = math.cos(x) + math.sin(x)
# print(y)

# x = int(input("Введите значение х"))
# y = (math.cos(x**2) ** 2 + math.sin(2 * x - 1) ** 2) ** (1 / 3)
# print(y)

# x = int(input("Введите значение х"))
# y = 5 * x + 3 * x**2 * (1 + math.sin(x) ** 2)
# print(y)

# i = int(input("Введите годовую процентную ставку"))
# s = int(input("Введите сумму займа"))
# n = int(input("Введите количество месяцев, на которые взят кредит"))
# p = i / 12 / 100
# m = (s * p * (1 + p) ** n) / ((1 + p) ** n - 1)
# a = m * n
# b = a - s
# print("Размер ежемесячной выплаты:", round(m, 2), "Полная выплата банку:", round(a, 2), "Переплата:", round(b, 2))

# R1 = int(input("Введите радиус планеты 1"))
# V1 = int(input("Введите орбитальную планеты 1"))
# R2 = int(input("Введите радиус планеты 2"))
# V2 = int(input("Введите орбитальную планеты 2"))
# L1 = (2 * R1 * math.pi) / V1
# L2 = (2 * R2 * math.pi) / V2
# print("Длина года на планете 1 равна", L1, "Длина года на планете 2 равна", L2)
# print ("На планете 1 год длинне") if L1 > L2 else print("На планете 2 год длинне")

import random
# a = int(input("Введите количество попыток бросков"))
# b = random.randint(0, 1)
# print (("Орел")) if b > 0 else print(("Решка"))

# n = int(input("Введите количество по пыток бросков"))
# print(*["Орёл" if random.randint(0,1) else "Решка" for i in range(n)],sep="\n")

# n = int(input("Введите количество бросков"))
# print (*[random.randint (1, 6) for i in range(n)], sep="\n")

import string
# dlin_par = int(input("Укажите длину пароля"))
# bol_buk = string.ascii_uppercase 
# mal_buk = string.ascii_lowercase
# combo = bol_buk + mal_buk
# par1 = random.sample(combo, dlin_par)
# par = "".join(par1)
# print(par)

# numbers = [random.randint(1, 49) for i in range(7)]
# print(*sorted(numbers))


# print(*[random.randint(0, 255) for i in range(4)], sep=".")

# generate_ip = [random.randint(0, 255) for i in range(4)]
# print(* generate_ip, sep= ".")

# bol_buk = string.ascii_uppercase
# ran_buk = random.sample(bol_buk, 2)
# r_l_b = "".join(ran_buk)
# r_p_b = "".join(ran_buk)
# l = r_l_b + str(random.randint(0, 99))
# p = str(random.randint(0, 99)) + r_p_b
# print(l,p, sep="_")

