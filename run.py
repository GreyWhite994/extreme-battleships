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


def player_guess(computer_board, computer_guess_board, name):
    print(f"{name}'s Guess!")
    x = int(input("Please enter a row: \n"))
    y = int(input("Please enter a column: \n"))
    print(f"{name} guessed {x},{y}")
    if computer_guess_board[x-1][y-1] == '@':
        print("Hit")
        computer_board[x-1][y-1] = '*'
        scores["player"] += 1
    else:
        print("Miss")
        computer_board[x-1][y-1] = 'X'

def computer_guess(player_board, size):
    print("Computer's Turn")
    x = randint(0, size - 1)
    y = randint(0, size - 1)
    print(f"Computer guessed {x+1},{y+1}")
    if player_board[x-1][y-1] == '@':
        print("Hit")
        player_board[x-1][y-1] = '*'
        scores["computer"] += 1
    else:
        print("Miss")
        player_board[x-1][y-1] = 'X'

def play_game(player_board, computer_guess_board, computer_board, name, size, ship_num):
    game_over = False
    while game_over != True:
        player_guess(computer_board, computer_guess_board, name)
        print_board(computer_board, 'Computer')
        computer_guess(player_board, size)
        print_board(player_board, name)
        print(f"After this round the scores are {name}:{scores['player']} and Computer:{scores['computer']}")
        if scores["player"] == ship_num:
            print(f"{name} wins!")
            game_over = True
        elif scores["computer"] == ship_num:
            print("Computer wins!")
            game_over = True
 

def new_game():
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print("Welcome to Extreme Battleships!")
    name = input("What is your name: \n")
    print("-" * 35)
    while True:
        try:
            size = int(input("How big would you like the game board to be(e.g if 6 is entered the board will be a 6x6 grid), minimum is 3 and the limit is 10: \n"))
        except ValueError:
            print("Please enter a number")
            continue
        if size >=3 and size <=10:
            break
    while True:
        try: 
            ship_num = int(input("How many ships would you like each player to have (Minimum is 3 and the limit is 8): \n"))
        except ValueError:
            print("Please enter a number")
            continue 
        if ship_num >=3 and ship_num <=8:
            break
    print("-" * 35)

    player_board = create_board(size)
    computer_board = create_board(size)
    computer_guess_board = create_board(size)
    create_ships(ship_num, 'player', size, player_board)
    create_ships(ship_num, 'guess_board', size, computer_guess_board)
    print_board(computer_board, 'Computer')
    print("-" * 35)
    print_board(player_board, name)
    play_game(player_board, computer_guess_board, computer_board, name, size, ship_num)

new_game()