from random import randint

def create_board(size):
    board = [["."] * size for i in range(size)]
    return board

def create_ships(ship_num, type, size, board):
    if type == "player":
        for location in range(ship_num):
            ship_x, ship_y = randint(0, size - 1), randint(0, size - 1)
            board[ship_x][ship_y] = '@'
    else:
        for location in range(ship_num):
            ship_x, ship_y = randint(0, size - 1), randint(0, size - 1)

def print_board(board, name):
    print(f"{name}'s Board")
    row_number = 1
    for row in board:
        print("|%s|" % ("|".join(row)))
        row_number += 1

player_board = create_board(6)
create_ships(3,"player", 6,player_board)
print_board(player_board, "Gray")

def make_guess(board):
    x = int(input("Please enter a row: \n"))
    y = int(input("Please enter a column: \n"))
    if board[x-1][y-1] == '@':
        print("Hit")
    else:
        print("Miss")

make_guess(player_board)