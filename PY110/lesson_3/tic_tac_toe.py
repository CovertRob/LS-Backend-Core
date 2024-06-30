# Problem

# Tic Tac Toe is a 2-player gam eplayed on a 3x3 grid called the board. 
# Each player takes a turn and marks a square on the board. The first player
# to get 3 squares in a row -- horizontally, vertically, or diagonally -- wins. 
# If all 9 squares are filled and neither player has 3 in a row, the game
# ends in a tie. 

# Flow chart:
# 1. Display the initial empty 3x3 board
# 2. Ask the user to mark a square
# 3. Computer marks a square
# 4. Display the updated board stae
# 5. If it's a winning board, display the winner
# 6. If the board is full, display tie
# 7. If neither play won and board is not full, go to step 2
# 8. Play again?
# 9 If yes, go to 1
# 10. Goodbye

# Outer loop between steps 1 and 9
# Inner loop between steps 2 an 7
import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

def display_board(board):
    os.system('clear')
    
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')


def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    print(f'==> {message}')

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({', '.join(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break # break if it is a valid square
        prompt("Sorry, that's not a valid choice")
        
    
    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return False

def main():
    board = initialize_board()
    display_board(board)
    while True:
        player_chooses_square(board)
        computer_chooses_square(board)
        display_board(board)
        if someone_won(board) or board_full(board):
            break

# Execution control function
if __name__ == "__main__":
    main()