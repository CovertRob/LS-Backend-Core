import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

# Win Counters
player_count = 0
computer_count = 0

def player_wins(player_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[player_choice]

def prompt(message):
    print(f'==> {message}')

def display_winner(player, computer):
    if player_wins(player, computer):
        prompt('You win!')
        track_winner('user')
    elif player_wins(player, computer) is not True & (player != computer):
        prompt('Computer wins!')
        track_winner('comp')
    else:
        prompt("It's a tie!")



def track_winner(user_or_comp):
    global player_count
    global computer_count
    if user_or_comp == 'user':
        player_count += 1
    if user_or_comp == 'comp':
        computer_count += 1

prompt('Welcome to RPS with bonus features. Best 3 out of 5 is grand winner.')

while True:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice.")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}, computer chose {computer_choice}')

    display_winner(choice, computer_choice)
    if (player_count >= 3) and computer_count < 3:
        prompt('User is the grand winner!')
        break
    if ((computer_count >= 3) and player_count < 3):
        prompt('Computer is the grand winner!')
        break
    prompt(f'Score tracker: user: {player_count}, computer: {computer_count}')

    # Break if the user doesn't want to play again
    prompt('Do you want to play again? (y/n)?')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt('Please enter "y" or "n".')
        answer = input().lower()
    if answer[0] == 'n':
        break
