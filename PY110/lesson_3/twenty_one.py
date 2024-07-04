# Twenty One game program. Dumbed down version of blackjack.

# README: 
# 1. Implementation detail - did not use any constants to determien who's turn it was because in 21 and blackjack, the player always goes first. No need to have flexibility to alternate beginning turns.
# 2. Felt encapsulating add up aces in it's own function was not worth it so keopt the logic in the generic add up hand function.
# 3. While doing PEDAC, found that the stay logic is easily placed in one line in the game loop so no need for seperate function.
# 4. Had to resist the urge to just extrapolate and turn the cards into their own class. Feel like would have been easier to understand but holding off until PY20 for now.

# Bug Tracker:

def prompt(input):
    print(f"==> {input}")

def create_card_for_display():
    pass

def display_board(board, all=False):
    pass

def initialize_game_board():
    return {
        'dealer': [],
        'player': [],
    }

def add_up_hand(hand):
    pass

def update_game_board_with_cards(board, cards, dealer_or_player):
    pass

def initialize_deck():
    # need to use list instead of string because of representing two digit values
    valid_face_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    valid_suites = ['hearts', 'diamonds', 'clubs', 'spade']
    return [[face, suite] for face in valid_face_values
                            for suite in valid_suites]

def shuffle_deck(deck):
    pass

def deal_cards(board, deck):
    pass

def hit(board, deck, player_or_dealer):
    pass

def player_action(board, deck):
    pass

def dealer_action(board, deck):
    pass

def check_for_bust(board): # thing here, could make it check only a hand and not both at the same time...we'll see when we get to implementation
    pass

def check_for_winner(board):
    pass

def play_round(board, deck):
    pass

def play_21():
    while True:
        deck = initialize_deck()
        board = initialize_game_board()
        shuffle_deck(deck) # mutates the original object
        prompt('Now dealing cards...')
        deal_cards(board, deck)
        display_board(board)
        play_round(board, deck)
        prompt(f"The winner is {check_for_winner(board)}")
        play_again = (input(prompt('Do you want to play another round? (y or n)'))).lower()
        while True:
            if play_again == 'n' or 'y':
                break
            else:
                prompt('That is not a valid input. Please enter y or n')
            play_again = input().lower()
        if play_again == 'n':
            break
        

def main():
    prompt('''Welcome to the game 21. \n 
    This is basically a basic version of blackjack, but here are some rules to help you out. \n
    You, the player, are playing against the dealer. You are initially dealt 2 cards. The dealer also has 2 cards but you can only see one of them.\n 
    You, the player, always goes first. All cards are worth their face value except for Royals, which are each worth 10, and Aces,\n 
    which are worth 1 or 11 depending on if they will make the player bust (lose).\n 
    After the initial deal, you can choose to hit (deal another card) or stay. If you hit and go over 21, the game is over and the dealer wins.\n
    If you get to 21 you win. If you choose to stay below 21, the dealer then goes and hits until his hand has a value of at least 17.\n
    If they do not make it to 21, the highest value hand wins.\n
    That's the game! May the odds be ever in your favor.''')
    play_21()
    prompt('Thanks for playing! Gambling hotline if you need it: 1-800-GAMBLER')

if __name__ == "__main__":
    main()

