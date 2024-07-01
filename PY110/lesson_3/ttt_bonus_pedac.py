# File contains the PEDAC's & pseudocode for tic tac toe bonus features

## Improved "join"

### Problem

# - Write a function that modifies the string join() method by being smarter and providing the functionality to use a custom delimiter and custom grammatic word such as 'or' and 'and' for the last element of the list being joined
# - Input:
# - Output:

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
    converted_to_strings = [str(str_nums) for str_nums in input_list]
    joined_string = ''
    if len(converted_to_strings) == 0:
        return joined_string
    if len(converted_to_strings) == 1:
        joined_string += converted_to_strings[0]
        return joined_string
    if len(converted_to_strings) == 2:
        joined_string = f"{converted_to_strings[0]} {last_word} {converted_to_strings[1]}"
        return joined_string
    for index, string in enumerate(converted_to_strings):
        if index != len(converted_to_strings) - 1:
            joined_string += (string + delim)
        else:
            joined_string = f"{joined_string}{last_word} {string}"
        
    return joined_string

print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"'