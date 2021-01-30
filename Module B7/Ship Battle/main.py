from random import randint


# Исключения

class GameExceptions(Exception):
    pass


class DotExceptions(GameExceptions):
    pass


class DotCompareError(DotExceptions):
    def __str__(self):
        return 'Точка сравнивается с другим объектом! (не точкой)'


class DotWithNegativeCoordinatesError(DotExceptions):
    def __str__(self):
        return 'Точка имеет отрицательные координаты!'


class DotSubError(DotExceptions):
    def __str__(self):
        return 'При совершении операции точка получает отрицательные координаты!'


class ShipExceptions(GameExceptions):
    pass


class ShipIsOutOfBoardError(ShipExceptions):
    def __str__(self):
        return 'Неверное размещение корабля: координаты выходят за границы поля!'


class ShipCrossOtherError(ShipExceptions):
    def __str__(self):
        return 'Неверное размещение корабля: пересечение с другим кораблем или его соседними координатами!'


class BoardException(GameExceptions):
    pass


class BoardMissError(BoardException):
    def __str__(self):
        return 'Выстрел мимо игрового поля!'


class BoardUsedCoordinateError(BoardException):
    def __str__(self):
        return 'В эту клетку уже стреляли!'


# Класс точки
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Dot):
            raise DotCompareError
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

    def __add__(self, other):
        if self.x + other.x < 0 or self.y + other.y < 0:
            raise DotSubError
        return Dot(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if self.x < other.x or self.y < other.y:
            raise DotSubError
        return Dot(self.x - other.x, self.y - other.y)

    @property
    def negative(self):
        if self.x < 0 or self.y < 0:
            return True
        return False


# Класс корабля
class Ship:
    def __init__(self, bow, length, orientation):
        if bow.negative:
            raise DotWithNegativeCoordinatesError
        self.bow = bow
        self.length = length
        self.orientation = orientation
        self.lives = length
        self.dots = self.ship_dots()

    def hitted(self, shot):
        return shot in self.dots

    def hit(self):
        self.lives -= 1

    def ship_dots(self):
        ship_dots = []
        add_dot = None
        if self.orientation == 1:
            add_dot = Dot(1, 0)
        elif self.orientation == 0:
            add_dot = Dot(0, 1)
        cur_dot = self.bow
        for _ in range(self.length):
            ship_dots.append(cur_dot)
            cur_dot += add_dot
        return ship_dots


# Класс доски
class Board:
    def __init__(self, size=6, hidden=False):
        self.size = size
        self.hidden = hidden

        self.killed_ships = 0
        self.ships = []

        self.field = [['O'] * self.size for _ in range(self.size)]
        self.filled_dots = []

    def __str__(self):
        res = '  |'
        for i in range(self.size):
            res += f" {i + 1} |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hidden:
            res = res.replace("■", "O")
        return res

    def check_out(self, d):
        return not ((0 <= d.x <= self.size - 1) and (0 <= d.y <= self.size - 1))

    def ship_outline(self, ship, show=False):
        neighbours = [Dot(-1, -1), Dot(-1, 0), Dot(-1, 1),
                      Dot(0, -1), Dot(0, 1),
                      Dot(1, -1), Dot(1, 0), Dot(1, 1)]
        for dot in ship.dots:
            for neighbour in neighbours:
                try:
                    cur = dot + neighbour
                    if not (self.check_out(cur)) and cur not in self.filled_dots:
                        if show:
                            self.field[cur.x][cur.y] = "."
                        self.filled_dots.append(cur)
                except DotSubError:
                    pass

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.check_out(dot):
                raise ShipIsOutOfBoardError
            elif dot in self.filled_dots:
                raise ShipCrossOtherError

        for dot in ship.dots:
            self.field[dot.x][dot.y] = "■"
            self.filled_dots.append(dot)

        self.ships.append(ship)
        self.ship_outline(ship)

    def make_shot(self, dot):
        if dot.negative:
            raise DotWithNegativeCoordinatesError
        elif self.check_out(dot):
            raise BoardMissError
        elif dot in self.filled_dots:
            raise BoardUsedCoordinateError

        self.filled_dots.append(dot)

        for ship in self.ships:
            if dot in ship.dots:
                ship.hit()
                self.field[dot.x][dot.y] = "X"
                if ship.lives == 0:
                    self.killed_ships += 1
                    self.ship_outline(ship, show=True)
                    print('Корабль уничтожен!')
                    return True
                else:
                    print('Попадение!')
                    return True

        self.field[dot.x][dot.y] = "."
        print('Мимо!')
        return False

    def game_start(self):
        self.filled_dots = []


# Общий класс игрока
class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def shot(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.shot()
                repeat = self.enemy.make_shot(target)
                return repeat
            except BoardException as e:
                print(e)


# Класс компьютерного противника
class AI(Player):
    def shot(self):
        while True:
            dot = Dot(randint(0, 5), randint(0, 5))
            if dot not in self.enemy.filled_dots:
                print(f"Ход компьютера: {dot.x + 1} {dot.y + 1}")
                return dot


# Класс пользователя
class User(Player):
    def shot(self):
        while True:
            user_shot = self.choose_dot(input("Введите координаты выстрела: "))
            if isinstance(user_shot, Dot):
                return user_shot

    def bow(self, ship_length):
        while True:
            user_bow = self.choose_dot(input(f"Укажите координату носа корабля длинной {ship_length}: "))
            if isinstance(user_bow, Dot):
                return user_bow

    @staticmethod
    def choose_dot(user_str):
        try:
            coord = user_str.split()
            x, y = int(coord[0]), int(coord[1])
            dot = Dot(x - 1, y - 1)
            if dot.negative:
                print('Вы ввели точку с отрицательными координатами!')
                return
            return dot
        except IndexError:
            print('Введите две координаты!')
        except ValueError:
            print('Координаты должны быть числами!')

    @staticmethod
    def choose_orientation():
        while True:
            try:
                orientation = int(input("Введите ориентацию корабля (1 - вертикальная, 0 - горизонтальная): "))
                if not (orientation == 1 or orientation == 0):
                    print('Нужно ввести число 1 или 0!')
                    continue
                return orientation
            except ValueError:
                print('Нужно ввести число 1 или 0!')


# Класс игры
class Game:
    def __init__(self, size=6):
        self.size = size
        self.ships_length = [3, 2, 2, 1, 1, 1, 1]
        self.greet()
        player_board = self.fill_board()
        ai_board = self.random_board()
        ai_board.hidden = True

        self.ai = AI(ai_board, player_board)
        self.player = User(player_board, ai_board)

    def try_board(self):
        board = Board(size=self.size, hidden=True)
        attempts = 0
        for ship_length in self.ships_length:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size - 1), randint(0, self.size - 1)), ship_length, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except ShipIsOutOfBoardError:
                    pass
                except ShipCrossOtherError:
                    pass
        board.game_start()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def fill_board(self):
        print('Расставляем корабли')
        b = Board()
        player = User(b,b)
        board = Board(size=self.size)
        for ship_length in self.ships_length:
            while True:
                bow = player.bow(ship_length)
                orientation = player.choose_orientation()
                ship = Ship(bow, ship_length, orientation)
                try:
                    board.add_ship(ship)
                    break
                except ShipIsOutOfBoardError as e:
                    print(e)
                    pass
                except ShipCrossOtherError as e:
                    print(e)
                    pass
            print(board)
        print('Доска успешно заполнена кораблями! Можно начинать!')
        board.game_start()
        return board

    @staticmethod
    def greet():
        print("--------------------")
        print("  Приветствуем вас  ")
        print("      в игре        ")
        print("     морской бой    ")
        print("--------------------")
        print(" формат ввода: x y  ")
        print("  x - номер строки  ")
        print("  y - номер столбца ")

    def loop(self):
        num = 0
        while True:
            print("-" * 20)
            print("Доска пользователя:")
            print(self.player.board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.ai.board)
            print("-" * 20)
            if num % 2 == 0:
                print("Ходит пользователь")
                repeat = self.player.move()
            else:
                print("Ходит компьютер")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.killed_ships == len(self.ships_length):
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.player.board.killed_ships == len(self.ships_length):
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.loop()


g = Game()
g.start()
