import twenty_one as t1
import pprint

# This module serves as the test cases used to validate the individual functions in the program

# Test Cases for initialize deck:
def initialize_deck_tests():
    pprint.pp(t1.initialize_deck())
    pprint.pp((len(t1.initialize_deck())) == 52)

def initialize_game_board_tests():
    pprint.pp(t1.initialize_game_board())

initialize_game_board_tests()