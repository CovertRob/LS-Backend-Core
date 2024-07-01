# lst = [14, 15, 16, 17, 18, 19, 20, 21]

#print(lst)  # [5, 6, 7, 8, 9, 10, 2, 3]

# addition of each number in the integers

# problem - each integer's digits added together is the tansformation
# input: a list
# output: digits added to eachother

# exampels / test cases

# lst = [14, 15, 16, 17, 18, 19, 20, 21]

#print(lst)  # [5, 6, 7, 8, 9, 10, 2, 3]

# algorithm:
# turn the list of integers into strings so we can access the individual integer
# use a for loop to access each element and append it to the new list
# return the new list

# string_lst = [str(element) for element in lst]

# int_list = [int(str_element[0]) + int(str_element[1]) 
#                             for str_element in string_lst]

# print(int_list)

word = 'what-a-b.e.a.utiful day!'

# crazy_letters = # your code here

# print(crazy_letters) # ['w', 'H', 'a', 'T', 'a', 'B', 'e', 'A', 'u', 'T', 'i', 'F', 'u', 'L', 'd', 'A', 'y']

# problem: we want to extract all alpahbetical chars and capitalize every other char

# input: a single string that may contain non alphabateical chars
# output: a list containing every char and with every other one capitalized

# exercises / test cases: above

# algorithm:

# first we need to filter the string for only alphabetical chars
# then we split the word based on empty string delimiter into list elements
# iterate through the lists elements and capitalize every other one
# return the string

# alpha_word = [filtered_chars for filtered_chars in word 
#                                 if filtered_chars.isalpha()]

# print(crazy_letters)

# word = 'what-a-b.e.a.utiful day!'


# extract all alphabetic characters from the string
# iterate through all characters in the new string:
    # idx in range(0, len(string), 2) -> lowercase
    # idx in range(1, len(string), 2) -> uppercase

filtered_word = ''

for char in word:
    if char.isalpha():
        filtered_word += char

filtered_chars = list(filtered_word)

# for idx in range(0, len(filtered_word), 2):
#     filtered_chars[idx] = filtered_chars[idx].lower()

# for idx in range(1, len(filtered_word), 2):
#     filtered_chars[idx] = filtered_chars[idx].upper()

# for i in range(len(filtered_chars)):
#     if i % 2 == 0:
#         filtered_chars[i] = filtered_chars[i].lower()
#     else:
#         filtered_chars[i] = filtered_chars[i].upper()
# crazy_letters = [ char.lower() if idx % 2 == 0 else char.upper() 
#                  for idx, char in enumerate(filtered_chars) ]

# # crazy_letters = # your code here



# print(crazy_letters) # ['w', 'H', 'a', 'T', 'a', 'B', 'e', 'A', 'u', 'T', 'i', 'F', 'u', 'L', 'd', 'A', 'y']

# def wordsOfLengthN(words, length):
    # Your implementation here

my_words = ['foo', 'bar', 'baz']

# print(wordsOfLengthN(my_words, 3))  # ['foo', 'bar', 'baz']
# print(wordsOfLengthN(my_words, 2))  # []

# def wordsOfLengthN(words, length):
#     # matching_length = ''
#     for element in words:
#         if len(element) == length:
#             # matching_length += element
#             return element
#     return None

# my_words = ['foo', 'bar', 'baz']
# print(wordsOfLengthN(my_words, 3))  # 'foo'
# print(wordsOfLengthN(['a', 'bb'], 2)) # 'bb'
# print(wordsOfLengthN(my_words, 2))  # None

# Problem
# Input: list of string elements, possibly various lengths
# output: a list of strings only matching the passed length
# Should not modify the original list
# need to return a list containing length matching words

# Examples
# above

# Data structure
# lists

# Algo
#   create new empty list to serve as return list
#   iterate through each string element in word arg
#       check if element matches length arg
#       if element lenght matches append to return list
#   return the new list
# print the result



# Code


word = 'Sesquipedalianism'
print(parts(word))  # ['S', 'Se', 'Ses', 'Sesq', 'Sesqu', 'Sesqui', 'Sesquip', 'Sesquipe', ...]


# start w empty list
    # Iterate thru lengths, starting with one
    # for each len, append substring to list
    # rturn list
def parts(string):
    lst = []
    # Iterate thru lengths, starting with one
    for length in range(1, len(string) + 1):
        lst.append(string[0 : length])
    return lst


word = 'Sesquipedalianism'
print(parts(word))  # ['S', 'Se', 'Ses', 'Sesq', 'Sesqu', 'Sesqui', 'Sesquip', 'Sesquipe', ...]

# ADDITONAL Practice:

# def sum_of_squares(lst):
#     # Implementation

# numbers = [1, 2, 3, 4, 5]
# print(sum_of_squares(numbers))  # => 55 (1^2 + 2^2 + 3^2 + 4^2 + 5^2)


# ####

# def longest_word(sentence):

# sample_sentence = 'This is a sample sentence with long words'
# print(longest_word(sample_sentence))  # => ['sentence']

# ###

# # Find the longest substring in alphabetical order.
# # Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
# # The input will only consist of lowercase characters and will be at least one letter long.
# # If there are multiple solutions, return the one that appears first.

# def longest(string):


# print(longest('asd') == 'as')
# print(longest('nab') == 'ab')
# print(longest('abcdeapbcdef') ==  'abcde')
# print(longest('asdfaaaabbbbcttavvfffffdf') == 'aaaabbbbctt')
# print(longest('asdfbyfgiklag') == 'fgikl')
# print(longest('z') == 'z')
# print(longest('zyba') == 'z')


# ####

# # Re-order the characters of a string, so that they are concatenated into a new string in "case-insensitively-alphabetical-order-of-appearance" order.
# # Whitespace and punctuation shall simply be removed!
# # The input is restricted to contain no numerals and only words containing the english alphabet letters.

# def alphabetized(string):


# # Tests
# print(alphabetized("The Holy Bible") == "BbeehHilloTy")
# print(alphabetized("!@$%^&*()_+=-`,") == "")
# print(alphabetized("CodeWars can't Load Today") == "aaaaCcdddeLnooorstTWy")
