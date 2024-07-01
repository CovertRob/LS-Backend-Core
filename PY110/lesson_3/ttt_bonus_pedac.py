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

# Keep score bonus feature

# Need to keep score of computer and player wins, first to win majority
# of 5 matches (3/5) wins the match. 

# Implemented in the main game loop