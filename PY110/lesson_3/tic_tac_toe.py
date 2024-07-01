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
import ttt_bonus_pedac as BF

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

def display_board(board):
    os.system('clear')

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
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
        # Implementation of join_or bonus feature 
        prompt(f"Choose a square ({BF.join_or(valid_choices)}):")
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

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
        [1, 5, 9], [3, 5, 7] # diagonals
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                    and board[sq2] == COMPUTER_MARKER
                    and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
    return None

def someone_won(board):
    return bool(detect_winner(board))

def main():
    while True:
        board = initialize_board()
        
        while True:
            display_board(board)
            player_chooses_square(board)
            if someone_won(board) or board_full(board):
                break
            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break
        display_board(board)
        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
        else:
            prompt("It's a tie!")
        prompt("Play again? (y or n)")
        answer = input().lower()

        if answer[0] != 'y':
            break
    prompt('Thanks for playing Tic Tac Toe!')

# Execution control function
if __name__ == "__main__":
    main()