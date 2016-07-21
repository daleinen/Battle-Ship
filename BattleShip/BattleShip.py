#Battleship 1.0
#dleinen 09SEP15
#Python2

from random import randint 

#************************* functions *************************
#function to print board formated correctly
def print_board(board):
    for row in board:
        print(" ".join(row))

#function getting random numbers for battleship
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

#************************* end of functions *************************

#creating list for game board and creating grid of 5X5 
board = [] 
for x in range(5):
    board.append(["O"] * 5)
    
#putting battleship on board
ship_row = random_row(board)
ship_col = random_col(board)

#printing welcome message
print("\nLet's play Battleship!")
print("You have 5 guesses\n")
print_board(board)

#giving the player 5 turns
for turn in range(0,5):
    
    #getting player input for row and column
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))
    #subtracting one to change collumn/row 0 to 1
    guess_row = guess_row - 1
    guess_col = guess_col - 1
    
    #printing turn number
    print("\nTurn:"), turn + 1
    
    #correct guess
    if (guess_row == ship_row and guess_col == ship_col):
        board[ship_row][ship_col] = "B"
        print_board(board)
        print("\nCongratulations! You sunk my battleship!")
        break
    #incorrect guesses
    else:
        #off the board
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        #same guess    
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        #place a guess for miss
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        #game over at 4 turns
        if turn == 4:
            board[ship_row][ship_col] = "B"
            print_board(board)
            print("\nGame Over\n")
            break
        #printing board after turn with X    
    print_board(board)