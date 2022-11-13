def draw_table(field: list) -> None:
    """
    функция рисует поле
    :param field: поле 
    :return:
    """
    for i in range(len(field)):
        for j in range(len(field)):
            print(f'|{field[i][j]}|', end=' ')
        print()


def check_lines(field: list, current_player: str) -> bool:
    """
    функция проверяет выигрыш по строкам
    :param field: поле
    :param current_player: игрок (X или 0)
    :return:
    """
    count = 0
    for line in field:
        for i in line:
            if i == current_player:
                count += 1
    if count == len(line):
        return True
    else:
        return False


def get_columns(size_board: int) -> list:
    """
    Функция высчитывает индексы ячеек по столбцам
    :param size_board: размер поля
    :return: список кортежей
    """
    result = []
    for j in range(size_board):
        result.append([(i, j) for i in range(size_board)])
    return result


def check_columns(result: list, current_player: str) -> bool:
    """
    Функция проверяет выигрыш по столбцам
    :param result: список кортежей с индексами ячеек по столбцам
    :param current_player: игрок (X или 0)
    :return:
    """
    count = 0
    for col in result:
        for i in col:
            if i == current_player:
                count += 1
    if count == len(col):
        return True
    else:
        return False


def get_first_diagonal(size_board: int) -> list:
    """
    Функция высчитывает индексы ячеек главной диагонали
    :param size_board: размер поля
    :return: список кортежей
    """
    result = []
    for i in range(size_board):
        result.append([(i, i) for i in range(size_board)])
        return result


def get_second_diagonal(size_board: int) -> list:
    """
    Функция высчитывает индексы ячеек побочной диагонали
    :param size_board: размер поля
    :return: список кортежей
    """
    result = []
    for i in range(size_board):
        result.append([(i, 2 - i) for i in range(size_board)])
        return result


def check_diagonal(result: list, current_player: str) -> bool:
    """
    функция проверяет выигрыш по диагоналям
    :param result: список кортежей с индексами ячеек
    :param current_player: игрок (X или 0)
    :return:
    """
    count = 0
    for diagonal in result:
        for i in diagonal:
            if i == current_player:
                count += 1
    if count == len(diagonal):
        return True
    else:
        return False


def make_move(field: list, current_player: str, size_board: int) -> tuple:
    """
    функция запрашивает координаты хода
    :param field: поле
    :param current_player: игрок (X или 0)
    :param size_board: размер поля
    :return: индекс ячейки
    """
    print(f'Куда ставим {current_player}?')
    while True:
        row, column = input(f'Введите две цифры от 0 до {size_board - 1} через пробел\n').strip().split()
        try:
            row, column = int(row), int(column)
        except ValueError:
            print(f'Можно вводить только цифры от 0 до {size_board - 1} включительно')
            continue
        if row not in range(size_board) or column not in range(size_board):
            print(f'Ход можно сделать только в ячейки с номерами от 0 до {size_board - 1} включительно')
        elif field[row][column] != '_':
            print('Ячейка занята, попробуйте другую')
        else:
            break
    return row, column


def switch_player(current_player: str) -> str:
    """
    функция меняет игрока
    :param current_player: игрок (X или 0)
    :return:
    """
    if current_player == 'x':
        return '0'
    else:
        return 'x'


def get_size_board() -> int:
    """
    функция запрашивает размер поля
    :return: размер поля
    """
    while True:
        try:
            size_board = int(input('Введите размер поля:\n'))
        except ValueError:
            print('Нужно ввести число')
            continue
        if size_board > 2:
            break
        print('Нужно ввести одно целое число больше 2')
    return size_board


def create_board():
    """
    функция инициализирует поле
    :return: двумерный список индексов ячеек, размер поля
    """
    size_board = get_size_board()
    return [['_'] * size_board for _ in range(size_board)], size_board
# [['_'] * size_board] * size_board


def get_player() -> str:
    """
    функция запрашивает очередность игроков
    :return: первый игрок (X или 0)
    """
    while True:
        print('Кто будет первым ходить? Введите 0 или x')
        current_player = input().lower()
        if current_player.lower() not in ('0', 'x'):
            print('Нужно ввести 0 или x')
        else:
            break
    return current_player


def is_win(field: list, current_player: str, size_board: int) -> bool:
    """
    функция проверяет, есть ли в игре победитель
    :param field: поле
    :param current_player: игрок (X или 0)
    :param size_board: размер поля
    :return:
    """
    if check_lines(field, current_player) or\
            check_columns(get_columns(size_board), current_player) or \
            check_diagonal(get_first_diagonal(size_board), current_player) or \
            check_diagonal(get_second_diagonal(size_board), current_player):
        return True
    return False


def game(field: list, size_board: int, player: str):
    """
    функция определяет процесс игры
    :param field: поле
    :param size_board: размер поля
    :param player: игрок (X или 0)
    :return: игрок-победитель или None
    """
    turn_count = 0
    current_player = player
    while turn_count < size_board * size_board:
        i, j = make_move(field, current_player, size_board)
        field[i][j] = current_player
        print('Доска выглядит так')
        draw_table(field)
        if is_win(field, current_player, size_board):
            print(f'Победил {current_player}')
            return current_player
        current_player = switch_player(current_player)
        turn_count += 1
    print('Ничья')
    return None


def main():
    print('Игра "Крестики-Нолики"')
    field, size_board = create_board()
    player = get_player()
    game(field, size_board, player)
    
    
if __name__ == "__main__":
    main()
    