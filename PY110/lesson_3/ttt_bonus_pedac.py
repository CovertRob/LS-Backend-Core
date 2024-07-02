# File contains the PEDAC's & pseudocode for tic tac toe bonus features

## Improved "join"

### Problem

# - Write a function that modifies the string join() method by being smarter and providing the functionality to use a custom delimiter and custom grammatic word such as 'or' and 'and' for the last element of the list being joined
# - Input:
# - Output:
#  Questions and possible edge cases

### Examples / Test Cases

# print(join_or([1, 2, 3]))               # => "1, 2, or 3"
# print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
# print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
# print(join_or([]))                      # => ""
# print(join_or([5]))                     # => "5"
# print(join_or([1, 2]))                  # => "1 or 2"'

### Data Structures

### Algorithm

### Code

def join_or(input_list, delim=', ', last_word = 'or'):
    # Convert the integer elements to strings
    converted_to_strings = [str(str_nums) for str_nums in input_list]
    joined_string = ''
    # None value check
    for element in input_list:
        if element == None:
            return joined_string
    # Alphabetical and ascii check
    if not [element.isalpha() for element in converted_to_strings] or not delim.isascii() or not last_word.isalpha():
        return joined_string
    # Empty list check
    if len(converted_to_strings) == 0:
        return joined_string
    # If input is only 1 element
    if len(converted_to_strings) == 1:
        joined_string += converted_to_strings[0]
        return joined_string
    # If input is only 2 elements follows own syntax formatting
    if len(converted_to_strings) == 2:
        joined_string = f"{converted_to_strings[0]} {last_word} {converted_to_strings[1]}"
        return joined_string
    # Formatting for len 3 and greater lists
    for index, string in enumerate(converted_to_strings):
        if index != len(converted_to_strings) - 1:
            joined_string += (string + delim)
        else:
            joined_string = f"{joined_string}{last_word} {string}"
        
    return joined_string

# Defensive Computer

# Problem
# The computer currently picks a square at random. That's not very interesting. Let's make the computer defensive-minded so that, when an immediate threat exists, it will try to defend the 3rd square. An immediate threat occurs when the human player has 2 squares in a row with the 3rd square unoccupied. If there's no immediate threat, the computer can pick a random square.
# Input: the current TTT board
# Output: The move the computer is going to make (an open square on the TTT board)
# Edge cases: player has more than one two in a row positions

# Examples / Test Cases
# 1. If player has 2 squares in a row vertically, horizontally, or diaganolly the computer will block the third square
# 2. Empty TTT board, computer chooses random
# 3. Player does not have any in a row squares, computer chooses randomly

# Data structures
# The TTT board is represented by a dictionary with each key representing squares on the board
# Will need to use a modified version of the empty_squares() function to get a list of all the currently filled spaces
# Will need a function that finds about to win patterns on the board from that list (sub problem)
    # input: the current TTT board (dictionary)
    # output: a list of corresponding at risk squares (at risk square defined by being the third square needed to win) otherwise None

    # examples / test cases: board with 1 & 2 filled, outputs 3, board with 1 and 5, outputs 9

    # Data structure: lists representing corresponding squares

    # Algorithm:
        # define function find_at_risk_square(board)
            # retrieve the current board positions showing which ones are filled and which ones are empty
            # initializie the squares at risk to be returned
            # Iterate through the board positions
                # If the current board positions is filled by the player
                    # check winnings combos from that spot - checking the following or preceding row spot, the following or preceeding column spot, and the following or preceeding diaganol
                    # If there are two in a row in any of the matching winning patterns, add them to the at risk squares list
            # return the list of at risk squares, otherwise return None

    # Algorithm v2
    #   pass in the winning lines constant and the board
    #   for each winning line
    #       iterate through the elements in that line and check how many of them are player markers
    #   If there are at least 2 markers in that line, and if the 3rd square is available, return that square as the at risk square

# Algorithm
    # check if there are any at risk squares
    # if there are, perform a defensive move by choosing the at risk square
    # otherwise, perform a random square move

