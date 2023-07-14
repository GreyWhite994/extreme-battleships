# Extreme Battleships

Extreme Battleships is a Python terminal game, which uses the Code Institute mock terminal on Heroku.

Users can attempt to beat the computer by finding all their battleships before the computer can locate their ships. The user can set the board size and amount of ships that each player has thereby increasing or decreasing the difficulty. The game is over when either the computer or the player finds all the opposing ships. A draw is also possible if the final ship of both players is found on the same turn.

The live version of the project can be found [here](https://extreme-battleships-0e054539df86.herokuapp.com/).

## How to play

Extreme battleships is based on the classic battleships game. More can be found on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

In this game, the player enters their name and what size they would like the board to be (min(3x3), max(10x10)). They also enter how many ships they want each board to have (min(3), max(8)).

The player can see their ships on their board, denoted by @. However, the computer's ships are hidden.

The player and computer each take a guess in turn. The aim is to sink eachother's ships by guessing the correct location.

Misses are highlighted on each board with **'X'** and hits are shown as **'*'**.

The player to sink all the opposing ships first is declared the winner.

## Existing Features 

- Player input:
    - Player can enter the desired board size (min(3x3), max(10x10)).
    - Player can enter how many ships they want each board to have (min(3), max(8)).

![board_size](assets/images/board_ship.png)
<br/>
e.g 7x7 board with 5 ships.
<br/>

![custom_board](assets/images/custom_board.png)

- Random ship generation
    - Ships are randomly placed on both the player and computer board. They are invisble on computer board.

<br/>
e.g 5x5 board with 4 ships.
<br/>

![computer_board](assets/images/computer_board.png)

- Player can enter guess.

- Displays scores after each round.

![guesses](assets/images/scores.png)

- Input validation/error checking
    - Player/computer cannot make same guess twice.
    - A guess off the size of the board cannot be made.
    - Row/Column guesses must be an integer.

- Data maintained in class instances

- Player can stop the game after each round.

![quit_game](assets/images/quit_game.png)

## Future Features

- Allow player to choose ship positions.
- Allow player to choose ships of different sizes.
- Have ships larger than 1x1 square.
- Allow player to set turn/time limit if desired.

## Data Model

I used a Board class as data model. The game created two instances of this class to create the player board and the computer board. The Board class stores the board size, the number of ships, player type and name. Also, the ship locations and guesses for that board.

The class also has a number of methods to play the game. This includes a print_board method to print out current board. A create_ships method to add ships to the board. Also, a guess method to validate guesses and add them to the list of guesses already made on that board.

## Testing

- I have tested the project by doing the following:
    - Passed the code successfully by running pylint run.py and found no significant issues.
    - Given invalid inputs e.g off-grid guesses, non-integers entered for co-ordinates and guesses made more than once.
    - Tested in local terminal and Heroku terminal.
    - Entered non-alphabetical characters for input of name.
    - Tested in event of a draw would code execute properly.

e.g Below a guess made outside board size.

![guess_off_grid](assets/images/grid_size_validation.png)

e.g Non-integer inputted for a guess.

![non-integer_guess](assets/images/number_validation.png)

e.g Entering a guess that has already been made.

![repeat_guess](assets/images/already_guessed.png)

e.g Non-alphabetical input entered for name.

![name_validation](assets/images/name_validation.png)

e.g Draw

![Draw](assets/images/draw.png)

## Bugs

- Solved Bugs
    - Guesses were incorrectly showing on boards e.g Player would guess (1,3) but the board would update at (2,4). This was due
    to list index starting at 0. Thus, this was fixed by minusing 1 from the x,y variables before they were passed to the guess function.
    - If both the player and computer destroyed the last of eachother's ships on the same turn it would incorrectly state the player was the winner due to how the if statement was structured. This was solved as stated above by first checking for the draw condition.

- Remaining Bugs
    - No remaining bugs

## Validator Testing
- Used Pylint tool. No significant errors found.

## Deployment
- Deployment steps
    - Fork/clone this repository
    - Create a new Heroku app
    - Set the buildbacks to **Python** and **NodeJS** in that order
    - Link the Heroku app to the repository
    - Click Deploy

## Credits
- Code institute for the deployment terminal
- Wikipedia for Battleships game material
- Inspiration for how to structure the Board class (https://www.youtube.com/watch?v=4sqtzZQpDJE)