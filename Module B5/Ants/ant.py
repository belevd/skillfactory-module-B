#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 08:01:37 2020

@author: ilya
"""

# Движение в минус от стартовых координат можно не рассмаривать, т.к.
# сразу будут "предельные значения", соответственно муравей может двигаться
# только в плюс по обеим координатам.
# Посещенная муравьём площадь будет представлять собой равнобедренный
# треугольник с равными сторонами расположенными на осях X и Y.
# -> Задача сводится к нахождения длины сторон по осям и вычёркиванию
# клеток не удовлетворяющих условию внутри треугольника


# Стартовые координаты.

x = 1000
y = 1000


# Ключ - номер точки по координате X
# Значение - список точек по координате Y

dict = {999: [1000]}


# Сумма длины списков с координатами

summ = 0


# Проверка на допустимость координат

def check_sum(x, y):
    x_sum = sum(map(int, str(x)))
    y_sum = sum(map(int, str(y)))
    if x_sum + y_sum <= 25:
        return True
    else:
        return False


# Заполнение словаря координатами по оси X

while check_sum(x, y):
    if check_sum(x, y):
        dict[x] = []
        x += 1

print(dict)

# Максимальное значение координат        

x_y_max_length = len(dict) - 1 + 1000
counter = 0

print(x_y_max_length)

# Заполнение возможных точек по оси Y для осей X и прибавление
# количества точек к результату
for i in range(1000, x_y_max_length):
    for j in range(1000, x_y_max_length):
        if sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= 25:
            if j in dict[i - 1] or j - 1 in dict[i]:
                counter += 1
                dict[i].append(j)

#
# for key, value in dict.items():
#     for i in range(x_y_max_length):
#         if check_sum(key, i):
#             value.append(i+y)
#     summ += len(value)


print(counter)