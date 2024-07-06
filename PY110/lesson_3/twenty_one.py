# Twenty One game program. Dumbed down version of blackjack.

# Notes
# 1. Implementation detail - did not use any constants to determine who's turn it was because in 21 and blackjack, the player always goes first. No need to have flexibility to alternate beginning turns.
# 2. Felt encapsulating add up aces in it's own function was not worth it so keopt the logic in the generic add up hand function.
# 3. While doing PEDAC, found that the stay logic is easily placed in one line in the game loop so no need for seperate function.
# 4. Had to resist the urge to just extrapolate and turn the cards into their own class. Feel like would have been easier to understand but holding off until PY20 for now.
# 5. Tried very hard to have functions only do one thing and keep logical parts of the program encapsulated. Ex. Not displaying the new board after updating it with a new card in the same function
# 5. Changed check_bust to return the hand value instead of boolean so don't need redundant add up hand function

import random
import time
import os

# Bug Tracker:
# 1. Current issue with tracking ace values is the value between hits...the determine bust function re-calculates the ace values each pass through on the hand - need to use some logic with the ace indexes if they are from the initial dealing or not *SOLVED
# 2. Edge case - dealt two ace's off the start, the 2nd needs to be worth 1 - *SOLVED
# 3. Having issue where off the rip it says player is winner off rip - *SOLVED
# 4. With two aces off initial deal, hit stay and then it just shuffled the cards again... *SOLVED - bad syntax
# 5. Dealt ace and a 3, hit a 9, did not bust - *SOLVED - wasn't checking ace index correctly


def prompt(text):
    print(f"==> {text}")

def create_card_for_display(card): # needs to return a string card, card argument is a tuple (face value, suite)
    spades = '\u2660'
    hearts = '\u2665'
    diamonds = '\u2666'
    clubs = '\u2663'
    suite_to_print = ''
    face_value_to_print = ''

    royals = ['jack', 'queen', 'king', 'ace']
    # using this becaue full words in the cards messes up spacing, so just use first letter capitalized if it is a royal card since they are all unique first letters
    if card[0] in royals:
        face_value_to_print = card[0][0].upper()
    else:
        face_value_to_print = card[0]
    # using this case statement to set the correct unicode to be chosen
    match card[1]:
        case 'hearts':
            suite_to_print = hearts
        case 'diamonds':
            suite_to_print = diamonds
        case 'clubs':
            suite_to_print = clubs
        case 'spades':
            suite_to_print = spades
    cli_card = f""" ___________
                    |     {face_value_to_print}    |
                    |          |
                    |     {suite_to_print}    |
                    |          |
                    |__________|
                    """
    return cli_card

def display_board(board, all=False): # still need to implement not displaying all
    os.system('clear')
    dealer, player = board.values()
    if dealer == [] and player == []:
        prompt('The board is currently empty')
        return
    dealer_hand = '' # use empty string to avoid list brackets when printing them below
    if all is True: # used with all flag to display all cards at end of match
        for card in dealer:
            dealer_hand += (create_card_for_display(card))
        prompt(f"Dealer's hand: {dealer_hand}")
    if all is False:
        for index, card in enumerate(dealer):
            if index == 1: # This is the 2nd card, aka the card that is suppose to be face down in the dealers hand
                dealer_hand += '''


                    unknown card


                    '''
            else:
                dealer_hand += (create_card_for_display(card))
        prompt(f"Dealer's hand: {dealer_hand}")
    player_hand = ''
    for card in player:
        player_hand += (create_card_for_display(card))
    prompt(f"Player's hand: {player_hand}")

def initialize_game_board():
    return {
        'dealer': [],
        'player': [],
    }

def update_game_board_with_card(board, card, dealer_or_player):
    # for adding to data structure not displaying
    # handles one card at a time
    board[dealer_or_player].append(card)

def initialize_deck():
    # need to use list instead of string because of representing two digit values
    valid_face_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    valid_suites = ['hearts', 'diamonds', 'clubs', 'spades']
    return [(face, suite) for face in valid_face_values
                            for suite in valid_suites]

def shuffle_deck(deck):
    prompt('Shuffling cards now...')
    time.sleep(2)
    random.shuffle(deck)

def deal_cards(board, deck): # only to be used at beginning of game when hands are empty
    prompt('Now dealing cards...')
    time.sleep(2)
    # only 4 cards, so not making it confusing with a loop
    board['dealer'].append(deck.pop(0))
    board['dealer'].append(deck.pop(0))
    board['player'].append(deck.pop(0))
    board['player'].append(deck.pop(0))

def hit(board, deck, player_or_dealer):
    card_to_add = deck.pop(0)
    update_game_board_with_card(board, card_to_add, player_or_dealer)

def player_action(board, deck):
    if check_for_bust(board, 'player') == 21: # add check in for if player is dealt 21 off the start
        return
    while True:
        if check_for_bust(board, 'player') > 21:
            break # must check here to prevent player from continuing to be allowed to hit after a bust
        hit_or_stay = ''
        prompt('Do you want to hit or stay? (h or s)')
        while True:        
            hit_or_stay = input().lower()
            if hit_or_stay in ['h', 's']:
                break
            prompt("That's not a valid input. Please enter 'h' or 's' for hit or stay")
        if hit_or_stay == 'h':
            hit(board, deck, 'player')
            display_board(board)
        else:
            break # if chose to stay
        
def dealer_action(board, deck):
    while check_for_bust(board, 'dealer') < 17:
        prompt('Dealing going...')
        time.sleep(1)
        hit(board, deck, 'dealer')
        display_board(board, True)
        time.sleep(1)

def check_for_bust(board, player_or_winner): # thing here, could make it check only a hand and not both at the same time...we'll see when we get to implementation
    # Did generic implementation so not repeating code
    value_counter = 0
    ace_indexes = []
    for index, cards in enumerate(board[player_or_winner]):
        if cards[0] == 'ace':
            ace_indexes.append(index)
    if not ace_indexes: # logic if there are no aces in the hand
        for cards in board[player_or_winner]:
            if cards[0] in ['jack', 'queen', 'king']:
                value_counter += 10
            else: 
                value_counter += int(cards[0])
    else: # logic if there ARE aces in the hand
        for index, cards in enumerate(board[player_or_winner]): # first adds up the value without the aces using the indexes list made above
            if index not in ace_indexes and (cards[0] in ['jack', 'queen', 'king']):
                value_counter += 10
            elif index not in ace_indexes: 
                value_counter += int(cards[0])
            else:
                pass
        for aces in ace_indexes: # after determinng value without aces, adds on appropriate ace value for the number of aces present based on if it will make the hand bust or not
            if ace_indexes == [0, 1]:
                value_counter += 12 # add this in to cover edge case of dealt two Aces
            elif aces in range(2): # check if ace is part of the first two cards dealt b/c that means it's automatically worth 11
                value_counter += 11 
            elif (value_counter + 11 <= 21):
                value_counter += 11
            else:
                value_counter += 1
    return value_counter

def check_for_winner(board): # need to use check bust here too to check if winner is because of a bust
    player = check_for_bust(board, 'player')
    dealer = check_for_bust(board, 'dealer')
    if player > 21: # check player first because they can bust without the dealer turn going
        return 'dealer'
    if dealer > 21:
        return 'player'
    if player > dealer:
        return 'player'
    if dealer > player:
        return 'dealer'
    display_board(board, True)
    return "nobody! It's a tie!"
    
    

def play_round(board, deck):
    player_action(board, deck)
    if check_for_bust(board, 'player') > 21: # got rid of bust check since can put same logic in check winner function
        return
    display_board(board, True)
    dealer_action(board, deck)
    
    # don't need to check again here becaues function will just return anyways
    # in the pay_21 loop the final check with check_for_winner() will check if the dealer busted and display the appropriate winner

def play_21():
    while True:
        deck = initialize_deck()
        board = initialize_game_board()
        shuffle_deck(deck) # mutates the original object
        deal_cards(board, deck)
        display_board(board)
        play_round(board, deck)
        
        prompt(f"The winner is {check_for_winner(board)}")
        play_again = (input('==> Do you want to play another round? (y or n)')).lower()
        while True:
            if play_again in ('n', 'y'):
                break
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
    time.sleep(2)
    play_21()
    prompt('Thanks for playing! Gambling hotline if you need it: 1-800-GAMBLER')

if __name__ == "__main__":
    main()

