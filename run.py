from random import randint

def create_board(size):
    board = [["."] * size for i in range(size)]
    return board

def print_board(board):
    row_number = 1
    for row in board:
        print("|%s|" % ("|".join(row)))
        row_number += 1