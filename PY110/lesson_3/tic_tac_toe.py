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

# Bonus features (change tracker):
# 1. join_or() - implemented in seperate file, imported as module
# 2. implemented score tracking logic into game loop
# 3. Refactored main() loop to make game state control cleaner and more modular because was getting messy from additional logic and program control
# 4. Implemented defensive AI logic. Tried iterating through the whole board using a match case implementation first but too messy. Restarted w/ referencing LS solution. Created find_at_risk_squares and defensive_move functions. Still not the most readable, perhaps refactor. 
# 5. 

import random
import os
import ttt_bonus_pedac as BF
import time

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

# Current bug - doesn't handle None object return if it is a tie

WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
    [1, 4, 7], [2, 5, 8], [3, 6, 9],
    [1, 5, 9], [3, 5, 7] 
]

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

def at_risk_squares(board):
    danger_squares = []
    for winning_combos in WINNING_LINES:
        markers_in_line = [board[square] for square in winning_combos]
        if markers_in_line.count(HUMAN_MARKER) == 2:
            for marker in winning_combos:
                if board[marker] == INITIAL_MARKER:
                    danger_squares.append(marker)#need to return the index here...bug. not empty str)
    return danger_squares

def defensive_move(danger_squares):
    # if more than one danger square doesn't really matter...just choose the first one
    return danger_squares[0]


def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    danger_squares = at_risk_squares(board)
    if danger_squares:
        board[defensive_move(danger_squares)] = COMPUTER_MARKER
    else:
        square = random.choice(empty_squares(board))
        board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board):
    for line in WINNING_LINES:
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

def check_match_win(player_count, computer_count):
    if player_count >= 3 and computer_count < 3:
        return 'Player'
    if computer_count >= 3 and player_count < 3:
        return 'Computer'
    return None

def play_rounds(board):
    while True:
        display_board(board)
        player_chooses_square(board)
        if someone_won(board) or board_full(board):
            break
        computer_chooses_square(board)
        if someone_won(board) or board_full(board):
            break

def match_state(board, player_win_count, computer_win_count):
    if someone_won(board):
            winner = detect_winner(board)
            prompt(f"{winner} won!")
            if winner == 'Player':
                player_win_count += 1
            if winner == 'Computer':
                computer_win_count += 1
            # will check if any player has majority wins and return winner if so
            # Will return None if there is not a match winner yet
            if check_match_win(player_win_count, computer_win_count) == None:
                prompt(f'Current match score - you: {player_win_count} computer: {computer_win_count}. Still no match winner!')
                return player_win_count, computer_win_count, False # continue with match flag
            else:
                prompt(f"Match winner is {check_match_win(player_win_count, computer_win_count)}")
                # Set the match won flag to true so we know which prompts to use in outer game loop
                # match_won = True
                return player_win_count, computer_win_count, True # match is over flag
    else:
        prompt("It's a tie!")

def play_match():
    player_win_count = 0
    computer_win_count = 0
    match_won = False

    while True:
        board = initialize_board()
        play_rounds(board)
        display_board(board)
        player_win_count, computer_chooses_square, match_won = match_state(board, player_win_count, computer_win_count)
        if not match_won:
            prompt("Continue with match? (y or n)")
            answer = input().lower()
            if answer[0] != 'y':
                break
        else:
            prompt("Would you like to start another match? (y or n)")
            anser = input().lower()
            if anser[0] != 'y':
                break
            else:
                player_win_count = 0
                computer_win_count = 0

def main():
    prompt("Welcome to Tic Tac Toe. Best out of 5 wins the overall match! \n initiating game...")
    time.sleep(5)
    play_match()
    # program will exit match function if match ends or player decides to end game at the end of a round/ the match
    prompt('Thanks for playing Tic Tac Toe!')

# Execution control function
if __name__ == "__main__":
    main()