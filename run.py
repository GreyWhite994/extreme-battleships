from random import randint

scores = {"computer":0, "player":0}

def create_board(size):
    """Creates a board by using the size parameter. Returns board"""
    board = [["."] * size for i in range(size)]
    return board

def create_ships(ship_num, size, board):
    """Creates ships by taking ship_num, size and board parameters. Prevents duplicate ship locations
    by comparing to locations in ship_locations list. If ship_x, ship_y not in ship_locations a ship will be created and 
    the location used will be appended to ship_locations"""
    ship_locations = []
    for location in range(ship_num):
            while True:
                ship_x,ship_y = randint(0, size - 1), randint(0, size - 1)
                if ((ship_x,ship_y)) not in ship_locations:
                    board[ship_x][ship_y] = '@'
                    ship_locations.append((ship_x,ship_y))
                    break

def print_board(board, name):
    """Prints board by taking board and name parameters"""
    print(f"{name}'s Board")
    row_number = 1
    for row in board:
        print("|%s|" % ("|".join(row)))
        row_number += 1


def player_guess(computer_board, computer_guess_board, name, size):
    """Takes input from user in the form of x and y variables to guess computer ship location.
    Validates x and y so as to disallow non-integers and guesses which are off grid or repeat guesses.
    If x/y corresponds to a ship location player score is incremented and an asterisk is printed in that location.
    Else it is a miss and an X is printed to the location"""
    print(f"{name}'s turn")
    while True:
        while True:
            try:
                x = int(input("Please enter a row: \n"))
            except ValueError:
                print("Please enter a number!")
                continue
            if x >= 1 and x <= size:
                break
            else:
                print(f"You must enter a number between 1 and {size}")
        while True:
            try:
                y = int(input("Please enter a column: \n"))
            except ValueError:
                print("Please enter a number!")
                continue
            if y >= 1 and y <= size:
                break
            else:
                print(f"You must enter a number between 1 and {size}")
        if computer_board[x-1][y-1] =='X' or computer_board[x-1][y-1] =='*':
            print("You already guessed that location!")
        else:
            break
    print(f"{name} guessed {x},{y}")
    if computer_guess_board[x-1][y-1] == '@':
        print("Hit")
        computer_board[x-1][y-1] = '*'
        scores["player"] += 1
    else:
        print("Miss")
        computer_board[x-1][y-1] = 'X'

def computer_guess(player_board, size):
    print("Computer's turn")
    x = randint(0, size - 1)
    y = randint(0, size - 1)
    while True:
        if player_board[x][y] =='X' or player_board[x][y] =='*':
            x = randint(0, size - 1)
            y = randint(0, size - 1)
        else:
            break
    print(f"Computer guessed {x+1},{y+1}")
    if player_board[x][y] == '@':
        print("Hit")
        player_board[x][y] = '*'
        scores["computer"] += 1
    else:
        print("Miss")
        player_board[x][y] = 'X'

def play_game(player_board, computer_guess_board, computer_board, name, size, ship_num):
    game_over = False
    while game_over != True:
        player_guess(computer_board, computer_guess_board, name, size)
        print("-" * 35)
        computer_guess(player_board, size)
        print("-" * 35)
        print(f"After this round the scores are {name}:{scores['player']} and Computer:{scores['computer']}")
        print("-" * 35)
        print_board(computer_board, 'Computer')
        print("-" * 35)
        print_board(player_board, name)
        print("-" * 35)
        if scores["player"] == ship_num:
            print(f"{name} wins!")
            game_over = True
        elif scores["computer"] == ship_num:
            print("Computer wins!")
            game_over = True
        else:
            keep_playing = input("Enter any key to continue or n to quit:")
            if keep_playing == 'n':
                game_over = True
                new_game()
        

def new_game():
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print("Welcome to Extreme Battleships!")
    print("Top left corner is row: 1, col: 1")
    print("-" * 35)
    while True:
        name = input("What is your name: \n")
        if name.isalpha():
            break
        else:
            print("Invalid name. Please enter a name using only letters!")
    print("-" * 35)
    while True:
        try:
            size = int(input("How big would you like the game board to be(e.g if 6 is entered the board will be a 6x6 grid), minimum is 3 and the limit is 10: \n"))
        except ValueError:
            print("Please enter a number")
            continue
        if size >=3 and size <=10:
            break
        else:
            print("Number must be between 3 and 10!")
    print("-" * 35)
    while True:
        try: 
            ship_num = int(input("How many ships would you like each player to have (Minimum is 3 and the limit is 8): \n"))
        except ValueError:
            print("Please enter a number")
            continue 
        if ship_num >=3 and ship_num <=8:
            break
        else:
            print("Number must be between 3 and 8!")
    print("-" * 35)

    player_board = create_board(size)
    computer_board = create_board(size)
    computer_guess_board = create_board(size)
    create_ships(ship_num, size, player_board)
    create_ships(ship_num, size, computer_guess_board)
    print_board(computer_board, 'Computer')
    print("-" * 35)
    print_board(player_board, name)
    print("-" * 35)
    play_game(player_board, computer_guess_board, computer_board, name, size, ship_num)

new_game()