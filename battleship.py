import sys
from random import randint

ai_board = []
player_board = []

#Try using input given by user. If user input produces error, default to 5 turns
try:
    gamelimit = int (sys.argv[1])
except:
    gamelimit = 5

#If user input is less than 0 or more than 25, set it to 10
if (gamelimit < 0 or gamelimit > 25):
    gamelimit = 10

#If user input is less than 3, then default board size to 5
board_size = int(sys.argv[2])
if (board_size < 3):
    board_size = 5

#Create game board
for x in range(board_size):
    ai_board.append(["~"] * board_size)
    player_board.append(["~"] * board_size)

def print_ai_board(ai_board):
    print("OPFOR Board")
    for row in ai_board:
        print(" ".join(row))

def print_player_board(player_board):
    print("\nYour Board")
    for row in player_board:
        print(" ".join(row))

print ("Let's play Battleship!")

def random_row(ai_board):
    return randint(0, len(ai_board) - 1)

def random_col(ai_board):
    return randint(0, len(ai_board) - 1)     

def player_row(player_board):
    x = input("Enter the row your ship is located on: ")
    return (int(x) - 1)
def player_col(player_board):
    y = input("Enter the column your ship is located on: ")
    return (int(y) - 1)

#place AI ship on board
ai_ship_row = random_row(ai_board)
ai_ship_col = random_col(ai_board)
ai_attack_row = 0
ai_attack_col = 0

player_ship_row = player_row(player_board)
player_ship_col = player_col(player_board)
player_board[player_ship_row][player_ship_col] = "A"

print(ai_ship_row + 1)
print(ai_ship_col + 1)
print()
print_ai_board(ai_board)
print_player_board(player_board)

#start game
for turn in range(gamelimit):
    guess_row = int(input("Guess Row:")) - 1
    guess_col = int(input("Guess Col:")) - 1

    if guess_row == ai_ship_row and guess_col == ai_ship_col:
        print ("Congratulations! You sunk the enemy battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Oops, that's not even in the ocean.")
        elif(ai_board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            ai_board[guess_row][guess_col] = "X"
        if turn == gamelimit:
            print ("Game Over")
            break
        #random number generator strikes back!
        #make loop for checking if shot at prev spot
        y = random_row(player_board)
        x = random_col(player_board)
        print("%d %d" % (x,y))
        if (x == player_ship_col and y == player_ship_row):
            print("Curses! You have been struck by OPFOR! Pull back!")
            print("Game Over!")
            break
        player_board[x - 1][y - 1] = "X"
    #Print turn number 
    print ("Turn %s" %(turn +1))

    print_ai_board(ai_board)
    print_player_board(player_board)