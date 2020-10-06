# Игра "Крестики-нолики"
# Каждый ход один из игроков ставит  свой знак (крестик или нолик) в одну из свободных ячеей
# Побеждает тот, кто первым составит линию из трех своих знаков (диагонали считаются)

# Инициализируем массив, в котором будет хранить информацию о ячейках
gameboard = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
# Задаем игроков и сообщаем им об этом
player_1 = 'x'
player_2 = 'o'

print('''Первый игрок играет за Х, а второй будет играть за О.
Координаты вводятся в формате: x y, где x - номер строки, а y - номер столбца.
Координаты разделены между собой пробелом. Пример ввода:0 0''')

# Распечатывание таблицы
def print_gameboard():
    print(' ', 0, 1, 2)
    i = 0
    for row in gameboard:
        print(i, end=" ")
        for column in row:
            print(column, end=" ")
        print()
        i += 1

# Ход игрока
def make_a_move(fraction):
    print()
    print(f'Сейчас ходит {fraction}') # Сообщаем о том, кто сейчас ходит
    while True: # Создаем вечный цикл из которого выходим только при верном вводе координат. Ошибки исключаем логическими операторами
        try:
            request = input('Введите координаты хода: ')
            x, y = int(request.split(' ')[0]), int(request.split(' ')[1]) # Записываем координаты в переменные
            if gameboard[x][y] == ' ': # Проверяем, не занята ли уже клетка другим символом
                gameboard[x][y] = fraction
                break
            else:
                print('Эта клетка уже занята. Попробуйте свободную')
        except: # Для всех остальных исключений
            print('Вы ввели недействительные координаты, либо ввели их не в том формате. Попробуйте еще раз')

    # Начинаем форматированный вывод таблицы после успешного хода
    print_gameboard()

# Функция проверки условия победы
def check_win(fraction):
    if (gameboard[0][0] == fraction and gameboard[0][1] == fraction and gameboard[0][2] == fraction) or\
        (gameboard[1][0] == fraction and gameboard[1][1] == fraction and gameboard[1][2] == fraction) or\
            (gameboard[2][0] == fraction and gameboard[2][1] == fraction and gameboard[2][2] == fraction) or \
            (gameboard[0][0] == fraction and gameboard[1][0] == fraction and gameboard[2][0] == fraction) or \
            (gameboard[0][1] == fraction and gameboard[1][1] == fraction and gameboard[2][1] == fraction) or \
            (gameboard[0][2] == fraction and gameboard[1][2] == fraction and gameboard[2][2] == fraction) or \
            (gameboard[0][0] == fraction and gameboard[1][1] == fraction and gameboard[2][2] == fraction) or\
            (gameboard[2][0] == fraction and gameboard[1][1] == fraction and gameboard[0][2] == fraction):
        return f'Победили {fraction}'
    elif (' ' not in gameboard[0]) and (' ' not in gameboard[1]) and (' ' not in gameboard[2]):
        return 'Ничья!'
    else:
        return ''

# Запускаем саму игру
print_gameboard()

while True:
    make_a_move(player_1)
    if len(check_win(player_1)):
        print()
        print(check_win(player_1))
        break
    make_a_move(player_2)
    if len(check_win(player_2)):
        print()
        print(check_win(player_2))
        break