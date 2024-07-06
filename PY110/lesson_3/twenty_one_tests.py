import twenty_one as t1
import pprint
import copy

# This module serves as the test cases used to validate the individual functions in the program

def initialize_deck_tests():
    pprint.pp(t1.initialize_deck())
    pprint.pp((len(t1.initialize_deck())) == 52)

def initialize_game_board_tests():
    pprint.pp(t1.initialize_game_board())

def display_game_board_tests():
    game_board = t1.initialize_game_board()
    card1 = ('king', 'hearts')
    card2 = ('3', 'spades')
    card3 = ('ace', 'clubs')
    game_board['dealer'].append(card1)
    game_board['dealer'].append(card2)
    game_board['dealer'].append(card3)

    game_board['player'].append(card1)
    game_board['player'].append(card2)
    game_board['player'].append(card3)

    t1.display_board(game_board) 

def shuffle_deck_tests():
    deck = t1.initialize_deck()
    test_deck = copy.deepcopy(deck)
    t1.shuffle_deck(deck)
    pprint.pp(deck)
    print(deck == test_deck)

def deal_cards_tests():
    board = t1.initialize_game_board()
    deck = t1.initialize_deck()
    t1.shuffle_deck(deck)
    t1.deal_cards(board, deck)
    # pprint.pp(deck) # used to ensure shuffle
    t1.display_board(board) # check not empty

def hit_test():
    board = t1.initialize_game_board()
    deck = t1.initialize_deck()
    t1.shuffle_deck(deck)
    t1.deal_cards(board, deck)

    t1.hit(board, deck, 'player')
    t1.display_board(board)

def check_for_bust_test():
    board = t1.initialize_game_board()
    deck = t1.initialize_deck()
    t1.shuffle_deck(deck)
    t1.deal_cards(board, deck)
    t1.display_board(board)
    t1.hit(board, deck, 'player')
    t1.hit(board, deck, 'player')
    t1.display_board(board)
    print(t1.check_for_bust(board, 'player'))

def solve_bug_4(): # use to debug stack
    board = t1.initialize_game_board()
    deck = t1.initialize_deck()
    card1 = ('ace', 'hearts')
    card2 = ('ace', 'spades')
    card3 = ('3', 'clubs')
    card4 = ('6', 'clubs')
    board['dealer'].append(card3)
    board['dealer'].append(card4)

    board['player'].append(card1)
    board['player'].append(card2)
    t1.display_board(board)
    t1.play_round(board, deck)

# solve_bug_4()
   

#initialize_deck_tests()

#initialize_game_board_tests()

#display_game_board_tests()

#shuffle_deck_tests()

# deal_cards_tests()

#hit_test()

#check_for_bust_test()

card1 = ('ace', 'hearts')
card2 = ('3', 'clubs')
card3 = ('9', 'clubs')
board = t1.initialize_game_board()
board['player'].append(card1)
board['player'].append(card2)
board['player'].append(card3)
print(t1.check_for_bust(board, 'player'))
