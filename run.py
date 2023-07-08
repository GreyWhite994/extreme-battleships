from random import randint

scores = {"computer":0, "player":0}

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
            board[ship_x][ship_y] = '@'

def print_board(board, name):
    print(f"{name}'s Board")
    row_number = 1
    for row in board:
        print("|%s|" % ("|".join(row)))
        row_number += 1


def make_guess(board, type):
    x = int(input("Please enter a row: \n"))
    y = int(input("Please enter a column: \n"))
    if board[x-1][y-1] == '@':
        print("Hit")
        board[x-1][y-1] = '*'
        if type == 'player':
            scores["player"] += 1
            print(scores['player'])
    else:
        print("Miss")
        board[x-1][y-1] = 'X'

def play_game(player_board, computer_board):
    turns = 10
    while turns != 0:
        make_guess(computer_board, 'player')
        print_board(computer_board, 'Computer')
        turns -= 1
 

def new_game():
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print("Welcome to Extreme Battleships")
    name = input("What is your name: \n")
    print("-" * 35)
    size = int(input("How big would you like the game board to be: \n"))
    ship_num = int(input("How many ships would you like each player to have: \n"))
    print("-" * 35)

    player_board = create_board(size)
    computer_board = create_board(size)
    create_ships(ship_num, 'player', size, player_board)
    create_ships(ship_num, 'computer', size, computer_board)
    print_board(computer_board, 'Computer')
    print("-" * 35)
    print_board(player_board, name)
    play_game(player_board, computer_board)

new_game()