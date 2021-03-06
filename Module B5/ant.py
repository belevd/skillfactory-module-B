# Муравей находится на координатной плоскости в точке с координатами (1000, 1000)
# Он может передвигаться на 1 клетку вверх, вниз, вправо или влево
# Сумма цифр координаты клетки, на которую он наступает, не может превышать 25
# Найти количество доступных муравью клеток

counter = 0
valid_list = {999 : [1000]} # Нужно для проверки значения на валидность передвижений
limit = 25 # Задаем лимит суммы клеток

# Ищем максимальную координату по одной из осей при условии, что по второй муравей не двигаемтся
x = 1000
while sum(map(int, list(str(x)))) <= limit - 1:
    x += 1
print(x)
# Начинаем перебирать значения координат двумя циклами, сразу же проверяя их на валидность передвижения
for i in range(1000, x):
    valid_list[i] = []
    for j in range(1000, x):
        if sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= limit:
            if (j in valid_list[i - 1]) or (j - 1 in valid_list[i]):
                counter += 1
                valid_list[i].append(j)

print(counter)

