# Problem
#   Inputs: list of strings
#   Outputs: new list of strings that are the input list but sorted
#   Explicit:
#       Sort: based on highest number of adjacent consontants a string contains
#       Tie in consontants string are to retain original order
#       Next to eac other means in same word or if there is a space between two
#       consonants in adjacent words
#   Implicit:
#       Must ignore vowel characters when sorting
#       Must count number of adjacent consonants in each string to compare them #       against each other
#       Strings may contain multiple words
#       vowels: a, e, i, o u, 
#       single consonants in string do not affect sort order in comparison to strings with no consonants. ONLY adjacent consonants affect sort order
#   Questions:
#       Does case matter when comparing consonants?
#       Does this sort function need to be internationalized?
#       Do strings always contain multiple words? Single? Empty?
#       Can strings contain no adjacent consonants?
#       Clarify space between two consonants in adjaent words?
#       Sort in ascending or descending order?
#       


# Examples / Test Cases

# below

# sorted in descending order, w most consonants first
# all the strings inputs are lowercase
# there are no international unicode characters
# input list always contains at least 2 strings, can be single word
# space is a whitespace character
# strings can contain no consonants - use tie criteria

# Data Structures
# Need to use a list here to store the sorted strings in
# possibly a dictionary to store number of consonants 

# Algorithm
# 1. Loop through input list and determine number of adjacent consonants in
#   in each string
#   a. Given a string, return a count of the highest number of adjacent
#       consonants anywhere in that string.
#       Input: string
#       Output: integer representing highest count of adj-con.
#       Need to remove any spaces from input string
#       Don't want to update the count if the temp string contains only
#           one consonant
# 2. Append strings to new list in sorted order based on adjacent consonants
# 3. Return sorted list of strings

#   Algorithm for sub-problem counting consonants:
#   - Remove spaces from input string
#   - Initialize a "maximum consonants count" to zero
#   - Initialize an "adjacent consonants string" to empty string
#   - For each "letter" in the "input string":
#       - If the "letter" is a consonant:
#           - Concatenate it to the adjacent consonants string.
#       - If the "letter" is a vowel:
#           - If the "adjacent consonants string" has a length greater than 1:
#               - Set "maximum consonants count" to the length of the
#                   "adjacent consonants string"
#           - Reset the "adjacent consonants string" to empty string
#   - Return the "maximum consonants count"



# Code

def count_max_adjacent_consonants(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    no_space_string = input_string.replace(' ', '')
    max_consonants_count = 0
    adjacent_consonants_string = ''

    for char in no_space_string:
        if char not in vowels:
            adjacent_consonants_string += char
            if len(adjacent_consonants_string) > max_consonants_count:
                if len(adjacent_consonants_string) > 1:
                    max_consonants_count = len(adjacent_consonants_string)
        else:
            if len(adjacent_consonants_string) > 1:
                max_consonants_count = len(adjacent_consonants_string)
            adjacent_consonants_string = ''
    return max_consonants_count


def sort_by_consonant_count(input_list):
    input_list.sort(key = count_max_adjacent_consonants, reverse=True)
    return input_list
# count consonants test cases (sub problem)
# print(count_max_adjacent_consonants('dddaa'))       # 3
# print(count_max_adjacent_consonants('ccaa'))        # 2
# print(count_max_adjacent_consonants('baa'))         # 0
# print(count_max_adjacent_consonants('aa'))          # 0
# print(count_max_adjacent_consonants('rstafgdjecc')) # 4

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

