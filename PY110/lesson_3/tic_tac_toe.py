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
# 4. Implemented defensive AI logic. Tried iterating through the whole board using a match case implementation first but too messy. Restarted w/ referencing LS solution. Created find_find_almost_winning_combos and defensive_move functions. Still not the most readable, perhaps refactor in future.
# 5. Implement offensive AI logic. Refactor at_risk_squares to find_almost_winning_combos and add arg so it can find both computer and player patterns to use in both defensive and offensive logics. Refactor computer_choose_square to implement modified functions.
# 6. Refactor to check offensive move first, just flip if statements
# 7. Computer turn refinements - offense, choose 5 first (this basically makes the game impossible to win if you go computer first lol), and turn choices - solved bug getting stuck in player_choose_square loop when board was fille due to lack of empty check
# 8. Refactored the input handling for continuing match and rounds. Discovered bug 3.

# Bug 3 (unsolved) - on player first turn, when player wins, computer still marks square and updates board to show it before the game is ended claiming player as winner

import random
import os
import ttt_bonus_pedac as BF
import time

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
CHOOSE_TURN = None

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
    # Had to add check because getting stuck in loop when doing computer turn first when it reaches a full board
    if len(empty_squares(board)) == 0:
            return
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        # Implementation of join_or bonus feature 
        prompt(f"Choose a square ({BF.join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break # break if it is a valid square
        prompt("Sorry, that's not a valid choice")
        
    
    board[int(square)] = HUMAN_MARKER

def find_almost_winning_combos(board, marker):
    danger_squares = []
    for winning_combos in WINNING_LINES:
        markers_in_line = [board[square] for square in winning_combos]
        if markers_in_line.count(marker) == 2:
            for marker in winning_combos:
                if board[marker] == INITIAL_MARKER:
                    danger_squares.append(marker)#need to return the index here...bug. not empty str)
    return danger_squares

def offensive_move(attack_squares):
    return attack_squares[0]

def defensive_move(danger_squares):
    # if more than one danger square doesn't really matter...just choose the first one
    return danger_squares[0]


def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    
    danger_squares = find_almost_winning_combos(board, HUMAN_MARKER)
    winning_squares = find_almost_winning_combos(board, COMPUTER_MARKER)
    if winning_squares:
        board[offensive_move(winning_squares)] = COMPUTER_MARKER
    elif danger_squares:
        board[defensive_move(danger_squares)] = COMPUTER_MARKER   
    elif board[5] == INITIAL_MARKER:
        board[5] = COMPUTER_MARKER # fixed bug...= not ==...30 minutes later
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

def choose_player():
    while True:
        choice = input()
        if choice.lower() == 'person' or choice.lower() == 'computer' or choice == '':
            global CHOOSE_TURN 
            CHOOSE_TURN = choice
            break
        else:
            prompt("That's not a valid choice. Please try again.")

# refactored to include match for player choosing who goes first
def play_rounds(board):
    while True:
        display_board(board)
        match CHOOSE_TURN:
            case 'player':
                player_chooses_square(board)
                computer_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break
            case 'computer':
                computer_chooses_square(board)
                display_board(board)
                player_chooses_square(board) # current bug, does not end the game
                if someone_won(board) or board_full(board):
                    break
            case _:
                player_chooses_square(board)
                computer_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break
        # if len(empty_squares(board)) == 0:
        #     break


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
        return player_win_count, computer_win_count, False # added line to fix bug throwing not able to unpack none in main game loop

# generic input() checker...besides at the beginning of the game, the only time we ask for text input is in the shape of a 'y' or 'n'
def check_user_input(input):
    if (input.lower() == 'y' or input.lower() == 'n') and len(input) == 1:
        return True
    return False

def play_match():
    player_win_count = 0
    computer_win_count = 0
    match_won = False

    while True:
        board = initialize_board()
        play_rounds(board)
        display_board(board)
        player_win_count, computer_win_count, match_won = match_state (board, player_win_count, computer_win_count)
        if not match_won:
            prompt("Continue with match? (y or n)")
            answer = input().lower()
            while not check_user_input(answer):
                prompt("Not a valid choice. Please choose 'n' or 'y'.")
                answer = input().lower()
            if answer[0] == 'n': # refactored to just test for 'n' instead of ! 'y' to make it more readable since we do the check above in the while loop
                break
        else:
            prompt("Would you like to start another match? (y or n)")
            anser = input().lower()
            while not check_user_input(anser):
                prompt("Not a valid choice. Please choose 'n' or 'y'.")
                answer = input().lower()
            if anser[0] == 'n':
                break
            else:
                player_win_count = 0
                computer_win_count = 0

def main():
    prompt("Welcome to Tic Tac Toe. Best out of 5 wins the overall match! \n")
    prompt("Would you like the computer or you to go first? \n Please enter person or computer (hit enter for default - person)")
    choose_player()
    print("initiating game...")
    time.sleep(5)
    play_match()
    # program will exit match function if match ends or player decides to end game at the end of a round/ the match
    prompt('Thanks for playing Tic Tac Toe!')

# Execution control function
if __name__ == "__main__":
    main()