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

def increment_score(type):
    if type == 'Player':
        player_score += 1
    else:
        computer_score +=1
    print(player_score)

def make_guess(board, type):
    x = int(input("Please enter a row: \n"))
    y = int(input("Please enter a column: \n"))
    if board[x-1][y-1] == '@':
        print("Hit")
        increment_score(type)
    else:
        print("Miss")

def new_game():
    player_score = 0
    computer_score = 0
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

new_game()