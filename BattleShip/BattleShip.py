"""
***-------------------------------------------------------------------|
Title:      BattleShip
Version:    1.0.0
Date:       21FEB2021
Author:     David Leinen (daleinen@hotmail.com)

Program randomly evovles text to match that of user entry
Run from any command line with the Python 3

***-------------------------------------------------------------------|
"""

from random import randint 

def main():
    #creating list for game board and creating grid of 5X5 
    board = [] 
    for _ in range(5):
        board.append(["O"] * 5)
        
    #putting battleship on board
    ship_row = random_row(board)
    ship_col = random_col(board)

    #printing welcome message
    print_welcome()
    print_board(board)

    #giving the player 5 turns
    for turn in range(0,5):
        
        #getting player input for row and column
        print()
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
        #subtracting one to change column/row 0 to 1
        guess_row = guess_row - 1
        guess_col = guess_col - 1
        
        #printing turn number
        print("\nTurn:", turn + 1)
        
        #correct guess
        if guess_row == ship_row and guess_col == ship_col:
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
            elif board[guess_row][guess_col] == "X":
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

def print_board(b):
    for row in b:
        print(" ".join(row))

def random_row(b):
    return randint(0, len(b) - 1)

def random_col(b):
    return randint(0, len(b[0]) - 1)

def print_welcome():
    print("\nWelcome to BattleShip v1.0\n")
    print("Let's play Battleship!")
    print("You have 5 guesses\n")

if __name__ == "__main__":
    main()