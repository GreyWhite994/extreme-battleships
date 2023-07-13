from random import randint

scores = {"computer":0, "player":0}


class Board:
    """Main Board class. Sets up the board and has methods to create ships, print the board and validate guesses.
    Inspiration for this code taken from 'Portfolio project 3 scope' https://youtu.be/4sqtzZQpDJE"""
    def __init__(self, size, name, ship_num, type):
        self.size=size
        self.name=name
        self.board=[[" "] * size for i in range(size)]
        self.ship_num=ship_num
        self.type=type
        self.guesses = []
        self.ship_locations = []
    
    def create_ships(self):
        """Prevents duplicate ship locations by comparing to locations in ship_locations list. 
        If ship_x, ship_y not in ship_locations a ship will be created and the location 
        used will be appended to ship_locations"""
        for location in range(self.ship_num):
            while True:
                ship_x,ship_y = randint(0, self.size - 1), randint(0, self.size - 1)
                if ((ship_x,ship_y)) not in self.ship_locations:
                    if self.type=='player':
                        self.board[ship_x][ship_y] = '@'
                        self.ship_locations.append((ship_x,ship_y))
                        break
                    else:
                        self.ship_locations.append((ship_x,ship_y))
                        break

    def print_board(self):
        """Prints the board with the appropriate name"""
        print(f"{self.name}'s Board")
        row_number = 1
        for row in self.board:
            print("|%s|" % ("|".join(row)))
            row_number += 1 

    def guess(self, x, y):
        """Takes x,y parameters, if x,y already in guesses list duplicate will be returned.
        Else guess is either a hit or miss and location appended to guesses. Board will be updated with X or * if it is a hit/miss"""
        if ((x, y)) in self.guesses:
            return "duplicate"
        else:
            self.guesses.append((x, y))
            self.board[x][y] = "X"
            if (x,y) in self.ship_locations:
                self.board[x][y] = '*'
                return 'Hit'
            else:
                return 'Miss'


def player_guess(computer_board, name, size):
    """Player inputs row,column. Must be between 1 and the board size. If the guess is not a duplicate, the guess will be printed
    and score incremented if it is a hit."""
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
        result = Board.guess(computer_board, x-1, y-1)
        if result != 'duplicate':
            break
        else:
            print("That location has already been guessed!")
    print(f"{name} guessed {x},{y}")
    if result == 'Hit':
        print("Hit")
        scores["player"] += 1
    else:
        print("Miss")


def computer_guess(player_board, size):
    """x,y are random integers between 0 and board size-1. If the guess is a duplicate a new value will be assigned to x,y.
    Else, computer score will be incremented if it is a hit"""
    print("Computer's turn")
    while True:
        x = randint(0, size - 1)
        y = randint(0, size - 1)
        result = Board.guess(player_board, x, y)
        if result != 'duplicate':
            break
    print(f"Computer guessed {x+1},{y+1}")
    if result == 'Hit':
        print("Hit")
        scores["computer"] += 1
    else:
        print("Miss")

def play_game(player_board, computer_board, name, size, ship_num):
    """Game will continue until game_over is true. The player and computer take guesses in rounds. The scores are printed after each round.
    The updated boards with X/* are printed after each round. Player can quit after each round by entering n when prompted. Game is over
    when either or both players hit all the opposing ships"""
    game_over = False
    while game_over != True:
        player_guess(computer_board, name, size)
        print("-" * 35)
        computer_guess(player_board, size)
        print("-" * 35)
        print(f"After this round the scores are {name}:{scores['player']} and Computer:{scores['computer']}")
        print("-" * 35)
        Board.print_board(computer_board)
        print("-" * 35)
        Board.print_board(player_board)
        print("-" * 35)
        if scores["player"] == ship_num and scores["computer"] == ship_num:
            print("It is a draw!")
            game_over = True
        elif scores["player"] == ship_num:
            print(f"{name} wins!")
            game_over = True
        elif scores["computer"] == ship_num:
            print("Computer wins!")
            game_over = True
        else:
            keep_playing = input("Enter any key to continue or n to quit:").lower()
            if keep_playing == 'n':
                game_over = True
                new_game()
        

def new_game():
    """Sets up a new game by resetting scores to 0. Gets input from player to get their name and preferred board size and ship number.
    Validation in place to prevent improper input. Creates instances of player_board and computer_board. Prints each board and calls the
    play_game function"""
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
            size = int(input("How big would you like the game board\n(e.g if 6 is entered the board will be a 6x6 grid), minimum is 3 and the limit is 10: \n"))
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
            ship_num = int(input("How many ships would you like each board to have\n(Minimum is 3 and the limit is 8): \n"))
        except ValueError:
            print("Please enter a number")
            continue 
        if ship_num >=3 and ship_num <=8:
            break
        else:
            print("Number must be between 3 and 8!")
    print("-" * 35)

    player_board = Board(size,name,ship_num,'player')
    computer_board = Board(size,"Computer",ship_num,'computer')
    Board.create_ships(player_board)
    Board.create_ships(computer_board)
    Board.print_board(computer_board)
    print("-" * 35)
    Board.print_board(player_board)
    print("-" * 35)
    play_game(player_board, computer_board, name, size, ship_num)

new_game()