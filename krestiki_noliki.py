board = [[" "] * 3 for i in range(3)]

def greet():
    print("--------------------")
    print(" Крестики - нолики")
    print("--------------------")
    print(" Формат ввода: x y")
    print(" x - номер строки")
    print(" y - номер столбца")



def console():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(board[i])
        print(f"{i} {row_info}")




def hod():
    while True:
        coordinates = input(" Ваш ход: ").split()

        if len(coordinates) != 2:
            print(" Введите 2 координаты! ")
            continue

        x,y = coordinates

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue

        x,y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if board [x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(board[i][j])
        if symbols == ["X", "X", "X"]:
            print(" Выиграл X !!!")
            return True
        if symbols == ["0", "0", "0"]:
            print(" Выиграл 0 !!!")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(board[j][i])
        if symbols == ["X", "X", "X"]:
            print(" Выиграл X !!!")
            return True
        if symbols == ["0", "0", "0"]:
            print(" Выиграл 0 !!!")
            return True

    symbols = []
    for i in range(3):
        symbols.append(board[i][i])
    if symbols == ["X", "X", "X"]:
        print(" Выиграл X !!!")
        return True
    if symbols == ["0", "0", "0"]:
        print(" Выиграл 0 !!!")
        return True

    symbols = []
    for i in range(3):
        symbols.append(board[i][2-i])
    if symbols == ["X", "X", "X"]:
        print(" Выиграл X !!!")
        return True
    if symbols == ["0", "0", "0"]:
        print(" Выиграл 0 !!!")
        return True
    return False
greet()
counter = 0
while True:
    counter += 1

    console()

    if counter % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")


    x, y = hod()

    if counter % 2 == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "0"

    if check_win():
        break

    if counter == 9:
        print( " Ничья")
        break

