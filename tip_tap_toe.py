def draw_table(field):
    for i in range(len(field)):
        for j in range(len(field)):
            print(f'|{field[i][j]}|', end=' ')
        print()


def check_lines(field, current_player):
    count = 0
    for line in field:
        for i in line:
            if i == current_player:
                count += 1
    if count == len(line):
        return True
    else:
        return False


def get_columns(size_board):
    result = []
    for j in range(size_board):
        result.append([(i, j) for i in range(size_board)])
    return result


def check_columns(result, current_player):
    count = 0
    for col in result:
        for i in col:
            if i == current_player:
                count += 1
    if count == len(col):
        return True
    else:
        return False


def get_first_diagonal(size_board):
    result = []
    for i in range(size_board):
        result.append([(i, i) for i in range(size_board)])
        return result


def get_second_diagonal(size_board):
    result = []
    for i in range(size_board):
        result.append([(i, 2 - i) for i in range(size_board)])
        return result


def check_diagonal(result, current_player):
    count = 0
    for diagonal in result:
        for i in diagonal:
            if i == current_player:
                count += 1
    if count == len(diagonal):
        return True
    else:
        return False


def make_move(field, current_player, size_board):
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
    field[row][column] = current_player
    return field, row, column


def switch_player(current_player):
    if current_player == 'x':
        return '0'
    else:
        return 'x'


def create_board():
    while True:
        size_board = input('Введите размер поля:\n')
        if not size_board.isdecimal():
            print('Вводить можно только целые положительные числа')
            continue
        elif int(size_board) <= 1:
            print('Нужно ввести число больше 2')
            continue
        else:
            size_board = int(size_board)
            break
    return [['_' for _ in range(size_board)] for _ in range(size_board)], size_board


def main():
    print('Игра "Крестики-Нолики"')
    turn_count = 0
    field, size_board = create_board()
    while True:
        print('Кто будет первым ходить? Введите 0 или x')
        current_player = input().lower()
        if current_player.lower() not in ('0', 'x'):
            print('Нужно ввести 0 или x')
        else:
            break
    while turn_count <= 8:
        field, i, j = make_move(field, current_player, size_board)
        print('Доска выглядит так')
        draw_table(field)
        if check_lines(field, current_player) or check_columns(get_columns(size_board), current_player):
            print(f'Победил {current_player}')
            break
        elif check_diagonal(get_first_diagonal(size_board), current_player) or\
                check_diagonal(get_second_diagonal(size_board), current_player):
            print(f'Победил {current_player}')
            break
        current_player = switch_player(current_player)
        turn_count += 1
        if turn_count == 9:
            print('Ничья')


if __name__ == "__main__":
    main()
