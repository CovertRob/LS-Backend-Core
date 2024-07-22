# This file contains all the practice problems done for PY110 material
# Consists of primarily advanced collections manipulation.

import sys

sys.set_int_max_str_digits(50_000)

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
# print(parts(word))  # ['S', 'Se', 'Ses', 'Sesq', 'Sesqu', 'Sesqui', 'Sesquip', 'Sesquipe', ...]


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
# print(parts(word))  # ['S', 'Se', 'Ses', 'Sesq', 'Sesqu', 'Sesqui', 'Sesquip', 'Sesquipe', ...]

# ADDITONAL Practice:

def sum_of_squares(lst):
    pass

# numbers = [1, 2, 3, 4, 5]
# print(sum_of_squares(numbers))  # => 55 (1^2 + 2^2 + 3^2 + 4^2 + 5^2)


# ####

def longest_word(sentence):
    pass
# sample_sentence = 'This is a sample sentence with long words'
# print(longest_word(sample_sentence))  # => ['sentence']

# ###

# Find the longest substring in alphabetical order.
# Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
# The input will only consist of lowercase characters and will be at least one letter long.
# If there are multiple solutions, return the one that appears first.

def longest(string):
    pass

# print(longest('asd') == 'as')
# print(longest('nab') == 'ab')
# print(longest('abcdeapbcdef') ==  'abcde')
# print(longest('asdfaaaabbbbcttavvfffffdf') == 'aaaabbbbctt')
# print(longest('asdfbyfgiklag') == 'fgikl')
# print(longest('z') == 'z')
# print(longest('zyba') == 'z')


# ####

# Re-order the characters of a string, so that they are concatenated into a new string in "case-insensitively-alphabetical-order-of-appearance" order.
# Whitespace and punctuation shall simply be removed!
# The input is restricted to contain no numerals and only words containing the english alphabet letters.

def alphabetized(string):
    pass

# # Tests
# print(alphabetized("The Holy Bible") == "BbeehHilloTy")
# print(alphabetized("!@$%^&*()_+=-`,") == "")
# print(alphabetized("CodeWars can't Load Today") == "aaaaCcdddeLnooorstTWy")

####

# Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values and its values become keys.

# problem - need to take an input of one dictionary. Both it's values and keys are unique, meaning they do not match. Need to invert it aka swap the keys and values.
# inputs: a dictionary
# outptu: an inverted dictionary
# questions: I assume that all the values are also hashable and can be keys? (verify this).
# Do we want to mutate or return a new dictionary?

# Examples / test cases below

# data structures : dictionary, key/value pairs

# algorithm - 

#   create a new dictionary that will be the one to return
#   iterate through the dictionary's items
#       access the tuple elements using element notation
#       append the elements to the new dictionary in opposite order
#   return the new dictionary

def invert_dict(input_dict):
    #inverted = {}
    inverted = {pairs[1]: pairs[0] for pairs in input_dict.items()}
    
    # for pairs in input_dict.items():
    #     inverted[pairs[1]] = pairs[0]
    print(inverted)
    return inverted

# LS:
def invert_dict(my_dict):
    return {value: key for key, value in my_dict.items()}

# print(invert_dict({
#           'apple': 'fruit',
#           'broccoli': 'vegetable',
#           'salmon': 'fish',
#       }) == {
#           'fruit': 'apple',
#           'vegetable': 'broccoli',
#           'fish': 'salmon',
#       })  # True

# Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs for the specified keys.

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}


def keep_keys(input_dict, keys):
    return {key: value for key, value in input_dict.items()
                        if key in keys}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
#print(keep_keys(input_dict, keys) == expected_dict) # True

# LS
def keep_keys(my_dict, key_list):
    return {key: my_dict[key]
            for key in key_list
            if key in my_dict}
# This is safer because it avoids potential KeyValue errors if the key is not in the list being checked

# Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.

def remove_vowels(input):
    vowels = 'aeiouAEIOU'
    new_list = []
    append_string = ''
    for word in input:
        for char in word:
            if char not in vowels:
                append_string += char
        new_list.append(append_string)
        append_string = ''
    print(new_list)
    return new_list

# All of these examples should print True
# original = ['abcdefghijklmnopqrstuvwxyz']
# expected = ['bcdfghjklmnpqrstvwxyz']
# print(remove_vowels(original) == expected)        # True

# original = ['green', 'YELLOW', 'black', 'white']
# expected = ['grn', 'YLLW', 'blck', 'wht']
# print(remove_vowels(original) == expected)        # True

# original = ['ABC', 'AEIOU', 'XYZ']
# expected = ['BC', '', 'XYZ']
# print(remove_vowels(original) == expected)        # True

# Write a function that takes a string as an argument and returns a list that contains every word from the string, with each word followed by a space and the word's length. If the argument is an empty string or if no argument is passed, the function should return an empty list.

# You may assume that every pair of words in the string will be separated by a single space.

def word_lengths(input=[]):
    try:
        split_word = input.split()
    except AttributeError:
        return []
    return [f"{word} {str(len(word))}" for word in split_word]


# All of these examples should print True
# words = 'cow sheep chicken'
# expected_result = ['cow 3', 'sheep 5', 'chicken 7']
# print(word_lengths(words) == expected_result)        # True

# words = 'baseball hot dogs and apple pie'
# expected_result = ['baseball 8', 'hot 3', 'dogs 4',
#                    'and 3', 'apple 5', 'pie 3']
# print(word_lengths(words) == expected_result)        # True

# words = "It ain't easy, is it?"
# expected_result = ['It 2', "ain't 5", 'easy, 5',
#                    'is 2', 'it? 3']
# print(word_lengths(words) == expected_result)        # True

# big_word = 'Supercalifragilisticexpialidocious'
# print(word_lengths(big_word) == [f'{big_word} 34'])  # True

# print(word_lengths('') == [])                        # True
# print(word_lengths() == [])                          # True

# Given two lists of integers of the same length, return a new list where each element is the product of the corresponding elements from the two lists.

def multiply_items(list_a, list_b):
    return [list_a[i] * list_b[i] for i in range(len(list_a))]
# or using zip:
def multiply_items(list1, list2):
    return [num1 * num2 for num1, num2 in zip(list1, list2)]

# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

# Write a function that takes a list of numbers and returns the sum of the sums of each leading subsequence in that list. Examine the examples to see what we mean. You may assume that the list always contains at least one number.

def sum_of_sums(input_list):
    final_sum = 0
    for i in range(len(input_list)):
        final_sum += sum(input_list[:i+1])
    print(final_sum)
    return final_sum

# print(sum_of_sums([3, 5, 2]) == 21)               # True
# # (3) + (3 + 5) + (3 + 5 + 2) --> 21

# print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

# print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# # (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

# print(sum_of_sums([4]) == 4)                      # True

# Write a function that takes one argument, a positive integer, and returns the sum of its digits.
def sum_digits(input_int):
    sum_all = 0
    for char in str(input_int):
        sum_all += int(char)
    return sum_all

# print(sum_digits(23) == 5)              # True
# print(sum_digits(496) == 19)            # True
# print(sum_digits(123456789) == 45)      # True

# Write a function that takes a string as an argument and returns that string with a staggered capitalization scheme. Every other character, starting from the first, should be capitalized and should be followed by a lowercase or non-alphabetic character. Non-alphabetic characters should not be changed, but should be counted as characters for determining when to switch between upper and lower case.

def staggered_case(input_str):
    iter_string = ''
    for index, char in enumerate(input_str):
        if char.isalpha and index % 2 == 0:
            iter_string += char.upper()
        else:
            iter_string += char.lower()
    print(iter_string)
    return iter_string

# string = 'I Love Launch School!'
# result = "I LoVe lAuNcH ScHoOl!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_CaPs"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

# Modify the function from the previous exercise so it ignores non-alphabetic characters when determining whether it should uppercase or lowercase each letter. The non-alphabetic characters should still be included in the return value; they just don't count when toggling the desired case.

def staggered_case(input_str):
    iter_string = ''
    upper = True
    for char in input_str:
        if char.isalpha():
            iter_string += char.upper() if upper else char.lower()
            upper = not upper
        else:
            iter_string += char
    print(iter_string)
    return iter_string

# string = 'I Love Launch School!'
# result = "I lOvE lAuNcH sChOoL!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_cApS"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

# Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the initial occurrence. Return the refined sequence.

def unique_sequence(input):
    return [elem for index, elem in enumerate(input) 
                if input[index] != input[index-1]]

# original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
# expected = [1, 2, 6, 5, 3, 4]
# print(unique_sequence(original) == expected)      # True

# Write a function that rotates a list by moving the first element to the end of the list. Do not modify the original list; return a new list instead.

# If the input is an empty list, return an empty list.
# If the input is not a list, return None.
# Review the test cases below, then implement the solution accordingly.

# All of these examples should print True

def rotate_list(input_list):
    if type(input_list) != list:
        return None
    return input_list[1:] + input_list[0:1]

# print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
# print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
# print(rotate_list(['a']) == ['a'])
# print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
# print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
# print(rotate_list([]) == [])

# # return `None` if the argument is not a list
# print(rotate_list(None) == None)
# print(rotate_list(1) == None)

# # the input list is not mutated
# lst = [1, 2, 3, 4]
# print(rotate_list(lst) == [2, 3, 4, 1])
# print(lst == [1, 2, 3, 4])

# Write a function that rotates the last count digits of a number. To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.

# problem: from the end of the number, flip the provided last digits and append it back to the whole number 
# input: an integer and the amount of digits to rotate/flip
# output: an integer that's been modified based on the digits argument
# questions - do we have to allow floats? Seems not from test cases
# can we always assume an input will be an integer, not None or other data types?

# see test cases below

# data structures - will need to use strings to manipulate the individual digits, possibly a list to split up all the indivdual digits while flipping the digits

# algorithm

# code

def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_part = number_str[:-count]
    second_part = number_str[-count:]
    result_str = first_part + rotate_string(second_part)

    return int(result_str)

def rotate_string(string):
    return string[1:] + string[0]

# print(rotate_rightmost_digits(735291, 2) == 735219)  # True
# print(rotate_rightmost_digits(735291, 3) == 735912)  # True
# print(rotate_rightmost_digits(735291, 1) == 735291)  # True
# print(rotate_rightmost_digits(735291, 4) == 732915)  # True
# print(rotate_rightmost_digits(735291, 5) == 752913)  # True
# print(rotate_rightmost_digits(735291, 6) == 352917)  # True
# print(rotate_rightmost_digits(1200, 3) == 1002)      # True

# Take the number 735291 and rotate it by one digit to the left, getting 352917. Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. Keep the first two digits fixed in place and rotate again to get 321759. Keep the first three digits fixed in place and rotate again to get 321597. Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. The resulting number is called the maximum rotation of the original number.

# Write a function that takes an integer as an argument and returns the maximum rotation of that integer. You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

# problem - need to do a max rotation on an integer. max rotation is defined as the length of the integer - 2, since a rotation can only be done on 2 or more numbers. 

# examples / test cases: see below, especially note the '0' and integer case

# data structures - integers, not negative numbers

# algorithm
#   use the rotate_rightmost_digits function to assist
#   iterate through the length of the integer
#       This function wants us to start rotating from the left most digit which is (-len) 

def max_rotation(input):
    num_length = len(str(input))
    rotated_int = input
    while num_length > 1:
        rotated_int = rotate_rightmost_digits(rotated_int, num_length)
        num_length -= 1
    return rotated_int

#LS's solution:
# need to remember can use ranges backwards with step counts like that
def max_rotation(number):
    number_digits = len(str(number))
    for count in range(number_digits, 1, -1):
        number = rotate_rightmost_digits(number, count)

    return number

# print(max_rotation(735291) == 321579)          # True
# print(max_rotation(3) == 3)                    # True
# print(max_rotation(35) == 53)                  # True
# print(max_rotation(8703529146) == 7321609845)  # True

# # Note that the final sequence here is `015`. The leading
# # zero gets dropped, though, since we're working with
# # an integer.
# print(max_rotation(105) == 15)                 # True

def minilang(program):
    stack = []
    register = 0

    for token in program.split():
        match token:
            case "ADD":
                register += stack.pop()
            case "DIV":
                register //= stack.pop()
            case "MULT":
                register *= stack.pop()
            case "REMAINDER":
                register %= stack.pop()
            case "SUB":
                register -= stack.pop()
            case "PUSH":
                stack.append(register)
            case "POP":
                register = stack.pop()
            case "PRINT":
                print(register)
            case _:
                register = int(token)

    return register

# minilang('PRINT')
# # 0

# minilang('5 PUSH 3 MULT PRINT')
# # 15

# minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# # 5
# # 3
# # 8

# minilang('5 PUSH POP PRINT')
# # 5

# minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # 5
# # 10
# # 4
# # 7

# minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# # 6

# minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# # 12

# minilang('-3 PUSH 5 SUB PRINT')
# # 8

# minilang('6 PUSH')
# # (nothing is printed)

# Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

# You may assume that the string does not contain any punctuation.

def word_to_digit(input):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    split_input = [str(numbers.index(word)) if word in numbers else word 
                    for idx, word in enumerate(input.split())]
    
    return ' '.join(split_input)

# message = 'Please call me at five five five one two three four'
# print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

# A prime number is a positive number that is evenly divisible only by itself and 1. Thus, 23 is prime since its only divisors are 1 and 23. However, 24 is not prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24. Note that the number 1 is not prime.

# Write a function that takes a positive integer as an argument and returns true if the number is prime, false if it is not prime.

# You may not use any of Python's add-on packages to solve this problem. Your task is to programmatically determine whether a number is prime without relying on functions that already do that for you.

def is_prime(input):
    if input == 1:
        return False
    for i in range(2, input):
        if input % i == 0:
            return False
    return True

import math
# LS, fastest solution:
def is_prime(number):
    if number == 1:
        return False

    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False

    return True

# print(is_prime(1) == False)              # True
# print(is_prime(2) == True)               # True
# print(is_prime(3) == True)               # True
# print(is_prime(4) == False)              # True
# print(is_prime(5) == True)               # True
# print(is_prime(6) == False)              # True
# print(is_prime(7) == True)               # True
# print(is_prime(8) == False)              # True
# print(is_prime(9) == False)              # True
# print(is_prime(10) == False)             # True
# print(is_prime(23) == True)              # True
# print(is_prime(24) == False)             # True
# print(is_prime(997) == True)             # True
# print(is_prime(998) == False)            # True
# print(is_prime(3_297_061) == True)       # True
# print(is_prime(23_297_061) == False)     # True

# The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. The first two Fibonacci numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:

# F(1) = 1
# F(2) = 1
# F(n) = F(n - 1) + F(n - 2)    (where n > 2)



# def fibonacci(nth):
#     if nth <= 2:
#         return 1
#     previous, current = 1, 1
#     for _ in range(3, nth + 1):
#         previous, current = current, previous + current
#     return current

# print(fibonacci(1) == 1)                  # True
# print(fibonacci(2) == 1)                  # True
# print(fibonacci(3) == 2)                  # True
# print(fibonacci(4) == 3)                  # True
# print(fibonacci(5) == 5)                  # True
# print(fibonacci(6) == 8)                  # True
# print(fibonacci(12) == 144)               # True
# print(fibonacci(20) == 6765)              # True
# print(fibonacci(50) == 12586269025)       # True
# print(fibonacci(75) == 2111485077978050)  # True

# Do a recursive implementation of fibonacci:

# again, fibonacci is defined as the sum of the previous two fib numbers, starting with 1 and 1

# def fibonacci(nth):
#     if nth <= 2:
#         return 1
    
#     return fibonacci(nth - 1) + fibonacci(nth - 2)

# print(fibonacci(1) == 1)         # True
# print(fibonacci(2) == 1)         # True
# print(fibonacci(3) == 2)         # True
# print(fibonacci(4) == 3)         # True
# print(fibonacci(5) == 5)         # True
# print(fibonacci(6) == 8)         # True
# print(fibonacci(12) == 144)      # True
# print(fibonacci(20) == 6765)     # True

# Implementation with memoization below

memo = {}
def fibonacci(nth):
    if nth <= 2:
        return 1
    elif nth in memo:
        return memo[nth]
    else:
        memo[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
        return memo[nth]

# print(fibonacci(1) == 1)         # True
# print(fibonacci(2) == 1)         # True
# print(fibonacci(3) == 2)         # True
# print(fibonacci(4) == 3)         # True
# print(fibonacci(5) == 5)         # True
# print(fibonacci(6) == 8)         # True
# print(fibonacci(12) == 144)      # True
# print(fibonacci(20) == 6765)     # True

# Write a function that calculates and returns the index of the first Fibonacci number that has the number of digits specified by the argument. The first Fibonacci number has an index of 1. You may assume that the argument is always an integer greater than or equal to 2.

def find_fibonacci_index_by_length(input):
    fib_count = 2
    current_len = 0
    while current_len < input:
        current_len = len(str(fibonacci(fib_count)))
        if current_len < input:
            fib_count += 1
    print(fib_count)
    return fib_count

# LS's solution w/ iteration:
import sys

def find_fibonacci_index_by_length(length):
    sys.set_int_max_str_digits(50_000)
    first = 1
    second = 1
    count = 2

    while len(str(second)) < length:
        first, second = second, first + second
        count += 1

    return count

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
# print(find_fibonacci_index_by_length(2) == 7)
# print(find_fibonacci_index_by_length(3) == 12)
# print(find_fibonacci_index_by_length(10) == 45)
# print(find_fibonacci_index_by_length(16) == 74)
# print(find_fibonacci_index_by_length(100) == 476)
# print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
#print(find_fibonacci_index_by_length(10000) == 47847)

# Write a function that takes a string and returns a dictionary containing the following three properties:

# the percentage of characters in the string that are lowercase letters
# the percentage of characters that are uppercase letters
# the percentage of characters that are neither
# All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

# You may assume that the string will always contain at least one character.

# problem: need to determine the percentages of types of characters in a string: lowercase, uppercase, and neither which would include punctuation and other non-alphabetical ascii characters. 
#   input: a string that contains at least one character, so no empty strings or lists of strings etc. Can include whitespace
#   outptut: a dictionary object that has the 3 requested keys/value pairs
#               format is float values
#               Needs to be expresssed in float as a percentage
#   questions: Is there any order to the requested output of the values in the dictionary? - lowercase, uppercase, then neither percentages in that order
#               Intertationalize it or just english ascii characters? - seems to be onlyh english
# Data structures - strings - for the input
#                 - dictionaries - for the output
#                 - list - to assist in storing and calculating percentage when iterating through the string

# examples and test cases below

# algorithm

# create dictionary object to hold values with default parameters of 0
# iterate through the string character by character
#   check if char is alpha and upper - if it is increment counter
#   check if char is alpha and lower - if it is increment counter
#   if neither of the above, increment the neither counter
# calculate the counts based on length of string and append to the respective dictionary element

# code

def letter_percentages(ip_str):
    percs = {'lowercase': 0,
            'uppercase': 0,
            'neither': 0}
    for char in ip_str:
        if char.isalpha():
            if char.isupper():
                percs['uppercase'] += 1
            if char.islower():
                percs['lowercase'] += 1
        else:
            percs['neither'] += 1
    for key in percs:
        percs[key] = format((percs[key] / len(ip_str)) * 100, ".2f")
    return percs

# LS's solution:

def percentage(count, total_count):
    return f'{(count / total_count) * 100:.2f}'

def letter_percentages(string):
    total_chars = len(string)
    lowercase_count = 0
    uppercase_count = 0
    neither_count = 0

    for char in string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        else:
            neither_count += 1

    return {
        'lowercase': percentage(lowercase_count, total_chars),
        'uppercase': percentage(uppercase_count, total_chars),
        'neither':   percentage(neither_count, total_chars),
    }
        
# expected_result = {
#     'lowercase': "50.00",
#     'uppercase': "10.00",
#     'neither': "40.00",
# }
# print(letter_percentages('abCdef 123') == expected_result)

# expected_result = {
#     'lowercase': "37.50",
#     'uppercase': "37.50",
#     'neither': "25.00",
# }
# print(letter_percentages('AbCd +Ef') == expected_result)

# expected_result = {
#     'lowercase': "0.00",
#     'uppercase': "0.00",
#     'neither': "100.00",
# }
# print(letter_percentages('123') == expected_result)

# A triangle is classified as follows:

# Equilateral: All three sides have the same length.
# Isosceles: Two sides have the same length, while the third is different.
# Scalene: All three sides have different lengths.
# To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

# Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

# def triangle(a, b, c):
#     values = [a, b, c]
#     perimeter = a + b + c
#     shortest = min(values)
#     longest = max(values)
#     middle = perimeter - longest - shortest

#     if (0 in values) or (middle + shortest) < longest:
#         return 'invalid'
#     if a == b == c:
#         return 'equilateral'
#     elif a == b or b ==c or c == a:
#         return 'isosceles'
#     else:
#         return 'scalene'

# print(triangle(3, 3, 3) == "equilateral")  # True
# print(triangle(3, 3, 1.5) == "isosceles")  # True
# print(triangle(3, 4, 5) == "scalene")      # True
# print(triangle(0, 3, 3) == "invalid")      # True
# print(triangle(3, 1, 1) == "invalid")      # True

# A triangle is classified as follows:

# Right: One angle is a right angle (exactly 90 degrees).
# Acute: All three angles are less than 90 degrees.
# Obtuse: One angle is greater than 90 degrees.
# To be a valid triangle, the sum of the angles must be exactly 180 degrees, and every angle must be greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

# Write a function that takes the three angles of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'right', 'acute', 'obtuse', or 'invalid'.

# You may assume that all angles have integer values, so you do not have to worry about floating point errors. You may also assume that the arguments are in degrees.


# input: integers that represent the triangle angles in degrees
# output: a string representing the triangles classsification
# use // floor division to maintain integers

# test cases - must handle inputs of 0

# data structures - 

# algorithm - 
#   find smallest angle
#   find largest angle
#   find middle angle based on previous two
#   determine if any input angles are 0, if so return invalid
#   determine if angles all add up to exactly 180, if not return invalid 
#   **if all angles are equal - (acute and equilateral) - can get rid of since can be caught in else statement**
#   if the smallest + middle is equal to the biggest - right 
#   if largest greater than 90 - obtuse
#   else acute
def triangle(a, b, c):
    smallest = min(a, b, c)
    biggest = max(a, b, c)
    middle = 180 - biggest - smallest
    if 0 in (a, b, c) or (a + b + c) != 180:
        return 'invalid'
    elif smallest + middle == biggest:
        return 'right'
    elif biggest > 90:
        return 'obtuse'
    else:
        return 'acute'
    

# print(triangle(60, 70, 50) == "acute")      # True
# print(triangle(30, 90, 60) == "right")      # True
# print(triangle(120, 50, 10) == "obtuse")    # True
# print(triangle(0, 90, 90) == "invalid")     # True
# print(triangle(50, 50, 50) == "invalid")    # True

# Some people believe that Fridays that fall on the 13th day of the month are unlucky days. Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year. You may assume that the year is greater than 1752, which is when the United Kingdom adopted the modern Gregorian Calendar. You may also assume that the same calendar will remain in use for the foreseeable future.

# Problem
#   - Determine how many friday the 13th's there are in a given year
#   - Assume year is greater than 1752 (input)
#   - Number of Friday 13th's will depend on if it's a leap year or not
#   - Gregorian calendar cycle is 400 years or 146, 097 days - 303 are regular years and 97 are leap years of 366 days. 
#   - Every year that is exactly divisible by 4 is a leap year, except for years that are exactly divisible by 100. Ex - years 1700, 1800, 1900 not leap years but 2000 is. Centurial years are leap years unless they are divisible by 400, in which case they are leap years. 
#   - Using the datetime module does all the work for us
#   - The month days are as follows: 
#       - 1: 31
#       - 2: 28 (29 in leap years)
#       - 3: 31
#       - 4: 30
#       - 5: 31
#       - 6: 30
#       - 7: 31
#       - 8: 31
#       - 9: 30
#       - 10: 31
#       - 11: 30
#       - 12: 31

#       - Every week is 7 days - M-F.
# Examples - see test cases below

# Data structures - use the date time date object to determine 13th's 

# Algorithm
#   loop through each month of the year
#       check if that months 13th is a friday, if it is increment counter
#   return 13th counter

import datetime as dt 

def determine_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        return False
    if year % 4 == 0:
        return True
    return False

def friday_the_13ths(year):
    counter = 0
    for months in range(1, 13):
        f13 = dt.date(year, months, 13)
        if f13.weekday() == 4:
            counter += 1
    return counter
    

# print(friday_the_13ths(1986) == 1)      # True
# print(friday_the_13ths(2015) == 3)      # True
# print(friday_the_13ths(2017) == 2)      # True

# A featured number (something unique to this exercise) is an odd number that is a multiple of 7, with all of its digits occurring exactly once each. For example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

# Write a function that takes an integer as an argument and returns the next featured number greater than the integer. Issue an error message if there is no next featured number.

# NOTE: The largest possible featured number is 9876543201.

# Problem
#   - Featured number - odd number that is a multiple of 7 (% 7 = 0) and all digits occur exactly once each. 
#   - Need to determine the next featured number after the given input integer

# Examples / Test cases
#   - 49 is a featured number
#   - 98 is not a featured number - not odd
#   - 97 is not - not a multiple of 7
#   - 133 is not - the digit 3 appears twice

# Data structures
#   - Use a list containing numbers 0 - 9 since those are all the unique numbers

# Algorithm
#   starting from the input integer, find the next multiple of 7
#       sub-problem - find multiple of a number
#   if it is odd and if all numbers only occur once - return as featured number
#       sub-problem - determining if all numbers only occur once
#   else, continue to next multiple of 7

def next_multiple_of_7(input):
    current_factor = input // 7
    next_multiple = (7 * (current_factor + 1))
    return next_multiple

def repeat_digits(input):
    valid_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for digit in str(input):
        try:
            valid_digits.remove(int(digit))
        except ValueError:
            return True
    return False

def is_featured(starting_int):
    max = 9876543201
    multiple = starting_int
    while True:
        next_multiple = next_multiple_of_7(multiple)
        #print(next_multiple)
        if next_multiple > max:
           return "There is no possible number that fulfills those requirements."
        if next_multiple % 2 == 1 and not repeat_digits(next_multiple):
            return next_multiple
        multiple = next_multiple

# LS's solution has their multiple function only go to the next odd multiple which speeds it up

# print(is_featured(12) == 21)                  # True
# print(is_featured(20) == 21)                  # True
# print(is_featured(21) == 35)                  # True
# print(is_featured(997) == 1029)               # True
# print(is_featured(1029) == 1043)              # True
# print(is_featured(999999) == 1023547)         # True
# print(is_featured(999999987) == 1023456987)   # True
# print(is_featured(9876543186) == 9876543201)  # True
# print(is_featured(9876543200) == 9876543201)  # True

# error = ("There is no possible number that fulfills those requirements.")
# print(is_featured(9876543201) == error)       # True

# Write a function that computes the difference between the square of the sum of the first count positive integers and the sum of the squares of the first count positive integers.

# Problem
#   - (sum of first count positive integers)**2 - (squares of first count positive integers and their sum)
# test cases below

# data structures
#   - 

#Algorithm
#   - Create list with first n integers

def sum_square_difference(input):
    nums = [nums for nums in range(1,input+1)]
    square_of_sums = (sum(nums)**2)
    sum_of_squares = 0
    for num in nums:
        sum_of_squares += num**2
    return square_of_sums - sum_of_squares

# print(sum_square_difference(3) == 22)          # True
# # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

# print(sum_square_difference(10) == 2640)       # True
# print(sum_square_difference(1) == 0)           # True
# print(sum_square_difference(100) == 25164150)  # True

# Write a function that takes a list as an argument and sorts that list using the bubble sort algorithm described above. The sorting should be done "in-place" -- that is, the function should mutate the list. You may assume that the list contains at least two elements.

def bubble_sort(input_list):
    
    while True:
        swapped = False
        swaps = 0
        for i in range(1, len(input_list)):
            print(i)
            if input_list[i-1] > input_list[i]:
                input_list[i-1], input_list[i] = input_list[i], input_list[i-1]
                swapped = True
                swaps += 1
        if not swapped or swaps == len(input_list) - 1:
            break
            
    print(input_list)

# lst1 = [5, 3]
# bubble_sort(lst1)
# print(lst1 == [3, 5])                   # True

# lst2 = [6, 2, 7, 1, 4]
# bubble_sort(lst2)
# print(lst2 == [1, 2, 4, 6, 7])          # True

# lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#         'Kim', 'Bonnie']
# bubble_sort(lst3)

# expected = ["Alice", "Bonnie", "Kim", "Pete",
#             "Rachel", "Sue", "Tyler"]
# print(lst3 == expected)                 # True

# Our countdown to launch isn't behaving as expected. Why? Change the code so that our program successfully counts down from 10 to 1 before launching.


# counter = 10

def decrease(counter):
    return counter - 1

# for _ in range(10):
#     print(counter)   
#     counter = decrease(counter)

# print('LAUNCH!')

# You have a function that is supposed to reverse a string passed as an argument. However, it's not producing the expected output. Explain the bug, and provide a solution.

def reverse_string(string):
    return string[::-1] # modified to be the solution

#print(reverse_string("hello") == "olleh")

# Bug here is that we are reassigning to the string argument and strings are immmutable in python so that re-assignment creates a new object each time the for loop executes. This results in appending the backwards string to the original string. Solution: use a slice to reverse the string. 

# You want to multiply all elements of a list by 2. However, the function is not returning the expected result. Explain the bug, and provide a solution.

def multiply_list(lst):
    for idx, item in enumerate(lst):
        lst[idx] = item * 2

    return lst

#print(multiply_list([1, 2, 3]) == [2, 4, 6])

# When accessing each item, it is not performing re-assignment inside of the list, it is creating a new object because integers are immutable. You need to use the enumerate function to access the index for the list and perform re-assignment on that index with the mutated item value. 

# Fix and explain why not working:

def get_key_value(my_dict, key):
    try:
        return my_dict[key]
    except KeyError:
        return None

#print(get_key_value({"a": 1}, "b"))

# or :
def get_key_value(my_dict, key):
    return my_dict.get(key, None)

# It is returning a KeyError because in the if statement accessing a key that does not exist in the dictionary results in a KeyError. We need to use a try except block if we keep the same syntax.


# Fix code:

def append_to_list(value, lst=[]):
    lst.append(value)
    print(lst)
    return lst

# print(append_to_list(1) == [1])
# print(append_to_list(2) == [2])
# print(append_to_list(2) == [2])

def sum_(numbers, factor):
    return factor * sum(numbers)

# numbers = [1, 2, 3, 4]
# print(sum_(numbers, 2) == 20)

# We are overwriting the sum function. So we are making a recursive call in the return line without meaning to. 


import copy

original = [[1], [2], [3]]
copied = copy.copy(original)

original[0][0] = 99

# print(copied[0] == [1])

# shallow copies do not copy nested objects in a list. Need to perform a deep copy

data_set = {1, 2, 3, 4, 5}

# for item in data_set:
#     if item % 2 == 0:
#         data_set.remove(item)

# sets are unchangeable, meaning you can't change their items, but you can remove and add new ones. Also, continuing to iterate over it while removing an element causes a runtime error because they are unordered so now the order has changed.
#common solution is to use a comprehension:
data_set = {item for item in data_set if item % 2 != 0}

# How can we preserve the order of the original list?
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
seen = set()
# for item in data:
#     if item not in seen:
#         seen.add(item)
#         unique_data.append(item)
# print(unique_data == [4, 2, 1, 3]) # now guranteed

# Problem
#   Given a 3x3 matrix represented by nested lists, create the transposition of that matrix.
#   Transpose - exchanging of the rows and columns of the original matrix
#   Do not modify the original matrix and do not use any external libraries. 
#   Input: a nested list containing the 3x3 matrix with integer values
#   Output: a new nested list containing the transposed 3x3 matrix with integer values

# Examples / Test cases
#   Below

# Data Structures - nested lists, remember bracket notation matrix[row][column]
#   An outer list and three sub-lists that each contain three elements

# Algorithm

# instantiate new 3x3 matrix
# iterate through the rows
# append each row number's elements to it's corresponding column index - ex row 1 element 2 will become row 2 element 1 (2nd item in that column)
# return new matrix

def transpose(matrix):
    t_mat = [[], [], []]
    for rows in matrix:
        for idx2, elem in enumerate(rows):
            t_mat[idx2].append(elem)
    return t_mat



# matrix = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# new_matrix = transpose(matrix)

# print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
# print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

# Modify the above transpopse function to make it work for any MxN matrix
# Just have to append the number of new rows by checking the length of matrix[0]

def transpose(matrix):
    t_mat = []
    for _ in range(0,len(matrix[0])):
        t_mat.append([])
    print(t_mat)
    for rows in matrix:
        for idx2, elem in enumerate(rows):
            t_mat[idx2].append(elem)
    return t_mat

# All of these examples should print True
# print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
# print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
# print(transpose([[1]]) == [[1]])

# matrix_3_by_5 = [
#     [1, 2, 3, 4, 5],
#     [4, 3, 2, 1, 0],
#     [3, 7, 8, 6, 2],
# ]
# expected_result = [
#     [1, 4, 3],
#     [2, 3, 7],
#     [3, 2, 8],
#     [4, 1, 6],
#     [5, 0, 2],
# ]

# print(transpose(matrix_3_by_5) == expected_result)

# Write a function that takes an arbitrary MxN matrix, rotates it 90 degrees and returns the result as a new matrix. Do not mutate the original matrix.

# Examples:

# matrix = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]
# 3  4  1
# 9  7  5
# 6  2  8

# 3  4  1
# 9  7  5

# 9  3
# 7  4
# 5  1

# rotating a matrix is very similar to rotating one, just have to reverse the elements after the transposition. Trying to iterate through and append the elements backwards is very hard and confusing index wise
# def rotate90(matrix):
#     t_mat = []
#     for _ in range(0,len(matrix[0])):
#         t_mat.append([])
#     for rows in matrix:
#         for idx2, elem in enumerate(rows):
#             t_mat[idx2].append(elem)
#     for row in t_mat:
#         row.reverse()
#     return t_mat    

# Other solutions from LS students:
# The matrix: list is a function annotation, a subtle way of annotating to 3rd party programs that this is supposed to return a list
def rotate90(matrix: list):
    lst = ([list(row) for row in zip(*reversed(matrix))])
    print(lst)
    return lst

# def get_sub(matrix, index):
#     return [sub[index] for sub in reversed(matrix)]
# def rotate90(matrix):
#     return [get_sub(matrix, i) for i in range(len(matrix[0]))]

# matrix1 = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# matrix2 = [
#     [3, 7, 4, 2],
#     [5, 1, 0, 8],
# ]

# new_matrix1 = rotate90(matrix1)
# new_matrix2 = rotate90(matrix2)
# new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# # These examples should all print True
# print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
# print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
# print(new_matrix3 == matrix2)

# Create a function that takes a list of numbers as an argument. For each number, determine how many numbers in the list are smaller than it, and place the answer in a list. Return the resulting list.

# When counting numbers, only count unique values. That is, if a number occurs multiple times in the list, it should only be counted once.


# problem:
# input: list of numbers
# for eah number, how many numbers in the list are smalled than it and place that answer in a list
# output: values of count smaller than each number 
# only use unique values when counting numbers that are smaller, still include repeat number for determing count

# examples below

# data structures - use lists and a set to determine unique values

# algorithm:

#   create seen() set
#   create count list to be returned
#   create current int
#   create number of ints smaller
#   iterate through the input list starting with index 0
#       iterate through the list again starting with index 0
#           if current number is less than current int, append to seen() set
#           increment the number of ints smaller
#       append the count to the respective list index
#       reset the seen set
#   return the list
#       

# completed in 15 minutes
def smaller_numbers_than_current(input_ints):
    seen = set()
    counts_of_smaller = []
    num_of_ints_smaller = 0
    for num in input_ints:
        for elem in input_ints:
            if elem < num and elem not in seen:
                seen.add(elem)
                num_of_ints_smaller += 1
        counts_of_smaller.append(num_of_ints_smaller)
        seen.clear()
        num_of_ints_smaller = 0
    print(counts_of_smaller)
    return counts_of_smaller

# refactor with comprehensions?

# print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
# print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
# print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
# print(smaller_numbers_than_current([1]) == [0])

# my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
# result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
# print(smaller_numbers_than_current(my_list) == result)

# Create a function that takes a list of integers as an argument. The function should return the minimum sum of 5 consecutive numbers in the list. If the list contains fewer than 5 elements, the function should return None.

# Problem
#   Input: a list of integers
#   Output: a single integer that is the minimum sum of 5 consecutive integers
#   Need to figure out what the smallest consecutive 5 sum of integers is
#   The numbers can be positive or negative
#   Return none if the function contains less than 5 elements
#   The number of 5 sum checks we need to do 
#   List sum does not wrap between front and end
#   The number of times we need to check sums is length of the list - 5, inclusive.
#   Example: For a list of length 6, 6 - 5 is 1, so we need to do 2 sums because there are two sets of 5 consecutive integers

# examples below

# data structures - lists

# algorithm
#   if the len of the input list is less than 5, return None
#   while true:  
#       iterate through the list of integers starting with index 0
#           get the sum of 5 integers from current index
#       if the len of input list is equal to 5, return the sum
#       if the len of (input list) - current index = 1
#           return the sum
#       

# This one I initially struggled with and took me about 40 minutes to re-work it a bit
def minimum_sum(input_list):
    if len(input_list) < 5:
        return None
    total = sum(input_list[0:5])
    
    for nums in range(1, len(input_list) - 4):
        next_five = sum(input_list[nums:nums+5])
        if next_five < total:
            total = next_five
        if len(input_list) == 5:
            return total
    return total

# print(minimum_sum([1, 2, 3, 4]) is None)
# print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
# print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
# print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
# print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

# Create a function that takes a string argument and returns a copy of the string with every second character in every third word converted to uppercase. Other characters should remain the same.

# Problem
#   Input: a string, consisting of characters and spaces
#   Output: copy of string, every 2nd char in every 3rd word uppercase
#   Need to iterate over the string and access the appropriate letters inthe appropriate words in the string. Do not mutate the original variable.
#   Do not capitalize if it is a single letter word like 'a' 


# Examples - we see no internatinal characters or numbers

# Data structures - use lists

# Algorithm
#   create split of string at the white spaces
#   use range function to get every 3rd word
#   append the uppercase word back to the split string
#   joint the string back together

# struggled with this one too, about an hour
def to_weird_case(input):
    split_str = input.split()
    for i in range(2, len(split_str), 3):
        current_word = split_str[i]
        if len(split_str[i]) == 1:
            continue
        upper_word = [char.upper() if idx % 2 == 1 else char for idx, char in enumerate(current_word)]
        weird_word = ''.join(upper_word)
        split_str[i] = weird_word
    return ' '.join(split_str)

# original = 'Lorem Ipsum is simply dummy text of the printing world'
# expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
# print(to_weird_case(original) == expected)

# original = 'It is a long established fact that a reader will be distracted'
# expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
# print(to_weird_case(original) == expected)

# print(to_weird_case('aaA bB c') == 'aaA bB c')

# original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
# expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
# print(to_weird_case(original) == expected)

# Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. If there are multiple pairs that are equally close, return the pair that occurs first in the list.

# Problem
#   Input: list of integers, whole numbers
#   output: tuple containing an integer pair
#   Iterate through the list of integers and figure out which two integers are closest in value
#   Need to get rid of negative values

# Examples - list is positive numbers

# data structures - use lists to contain integers

# algorithm:

#   use built in sort() method and sort list from smallest to largest integer
#   instantiate difference variable
#   iterate through the list of integers from index 0 to len - 1
#       get difference between current integer index and next integer index
#       if current index difference is less than stored difference, 
#           update stored difference with current index difference

# Add the pair as a key and the difference as the value
# return the pair whose index came first

# Find the difference for every pair

# This one was hard, took me a couple of hours to get everything together
def closest_numbers(input):
    sorted_input = sorted(input)
    difference = max(sorted_input) # need to start not at 0 otherwise condition below won't work
    pair = (0, 0)
    for i in range(0, len(sorted_input) - 1):
        current_difference = abs(sorted_input[i] - sorted_input[i+1])
        if current_difference < difference:
            difference = current_difference
            pair = (sorted_input[i], sorted_input[i+1])
    idx1, idx2 = input.index(pair[0]), input.index(pair[1])
    if idx1 > idx2:
        return (input[idx2], input[idx1])
    return (input[idx1], input[idx2])

# def closest_numbers(input):
#     sorted_input = sorted(input)
#     differences = {(sorted_input[num], sorted_input[num+1]): abs(sorted_input[num] - sorted_input[num+1]) for num in range(0, len(input) -1, 2)}
#     print(differences)
#     index_list = []
#     for num1, num2 in differences.keys():
#         index_list.append(num1)
#         index_list.append(num2)
#     lowest_index_elem = input[min(input.index(elem) for elem in index_list)]
#     item_to_return = ()
#     for pair in differences.keys():
#         if lowest_index_elem in list(pair):
#             item_to_return = pair
#     item1, item2 = item_to_return
#     index1 = input.index(item1)
#     index2 = input.index(item2)
#     corrected_order = ()
    

    # don't need to find difference of every combo because sorted differences will automatically be less

# bug - logic doesn't work on returning the first if multple are the same because I sort it in descending order

# print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
# print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
# print(closest_numbers([12, 22, 7, 17]) == (12, 7))

# Create a function that takes a string argument and returns the character that occurs most often in the string. If there are multiple characters with the same greatest frequency, return the one that appears first in the string. When counting characters, consider uppercase and lowercase versions to be the same.

# Problem 
#   Figure out which character occurs most in the string. If multiple charactesr with the same greates frequency, return the one that appears first in the string. 
#   Upper and lower case are the same in this problem.
# Input: A string
# Output: a single letter string

# Examples / Test Cases - No international characters or numbers, includes punctuation

# Data structures - list, perhaps a dictionary to store values

# Algorithm
#   Split the string into a list containing all individual characters
#   sort the list of strings so that it is in lexagraphical order
#   create a copy of the sorted list as a set to remove repeat elements
#   use a dictionary comprehension with the unique set to iterate through the list and count each amount of characters
#   Get the values that occur the most
#   If multiple values have same greatest occurrence, get and compare index of each char and return the value of the one that has the least index

def most_common_char(str_input):
    lowercased = str_input.lower()
    split_str = list(lowercased)
    split_str.sort()
    unique_chars = set(split_str)
    num_chars = {chars: split_str.count(chars) for chars in unique_chars}
    # find the greatest values in the dictionary and its corresponding char
    max_value = max(num_chars.values())
    greatest_values = [char for char, count in num_chars.items() if count == max_value]
    # if there is only one greatest occurency, return it
    if len(greatest_values) == 1:
        return greatest_values[0]
    index = []
    # return the letter that occurs first in the lowercased string
    for greatest_char in greatest_values:
        index.append(lowercased.index(greatest_char))
    return lowercased[min(index)]

# print(most_common_char('Hello World') == 'l')
# print(most_common_char('Mississippi') == 'i')
# print(most_common_char('Happy birthday!') == 'h')
# print(most_common_char('aaaaaAAAA') == 'a')

# my_str = 'Peter Piper picked a peck of pickled peppers.'
# print(most_common_char(my_str) == 'p')

# my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
# print(most_common_char(my_str) == 'e')

# Create a function that takes a string argument and returns a dict object in which the keys represent the lowercase letters in the string, and the values represent how often the corresponding letter occurs in the string.

# Problem: 
#   Input: a string consisting of chars, punctuation, and spaces
#   Output: a dict object, with keys the chars and valuees their occurrence value

# Examples : below

# data structures - list for string operations, set to get unique chars

# algorithm:
#   if inptu is empty or is not all alphabateical : return empty dict
#   create list object containing input string lowercased
#   create copy of list as a set to remove duplicate chars
#   iterate through each element in the set and remove it if it is not alphabetical
#   use dict comprehension to create dict object with keys as the unique values from the set and values the count of those chars from the list object containing the original string

# Got these types of problems down to a science now, did it in about 15 minutes
def count_letters(input_str):
    if len(input_str) == 0:
        return {}
    str_as_list = list(input_str)
    unique_chars_as_set = set(str_as_list)
    char_occurrences = {unique_chars: str_as_list.count(unique_chars) for unique_chars in unique_chars_as_set if unique_chars.isalpha() and unique_chars.islower()}
    return char_occurrences

# expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
# print(count_letters('woebegone') == expected)

# expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
#             'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
# print(count_letters('lowercase/uppercase') == expected)

# expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
# print(count_letters('W. E. B. Du Bois') == expected)

# print(count_letters('x') == {'x': 1})
# print(count_letters('') == {})
# print(count_letters('!!!') == {})

# Create a function that takes a list of integers as an argument and returns the number of identical pairs of integers in that list. For instance, the number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

# If the list is empty or contains exactly one value, return 0.

# If a certain number occurs more than twice, count each complete pair once. For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2. The first list contains two complete pairs while the second has an extra 2 that isn't part of the other two pairs.

#Problem
# Input: list of integers
# Output: an integer
# Need to find how many identical pairs of integers there are in the list.
# Pairs must be an even number if a number repeats. See example above with 5 of the same number, that is only 2 pairs
# If empty or one value return 0

# Examples - Should return 0 if there are no pairs to match. Ex [23]

# Data structures - list for iteration, 
#   Set won't work here for the seen ones because can't add duplicates to a set

# Algorithm
#   define function name pairs
#       instantiate pair counter
#       instantiate copy of list sorted in ascending order
#       iterate from i starting at index 0 to lenth of list - 1 (2nd to last element) with step 2 to account for pairs
#           iterate from j for range i + 1 to len of list (last element)
#           if element at index i equals element at index j -> increment the pair counter
#       return pair counter

# after over an hour I came up with a new idea: did it in about 10 minutes:

#   count how many times each number appears in the list
#   divide that number by floor division 2 and that is how many pairs there are of that number
#   add up for each number and return

def pairs(input):
    set_copy = set(input)
    numbers = {num: 0 for num in set_copy}
    for num in numbers.keys():
        numbers[num] = input.count(num) // 2
    return sum(numbers.values())


# print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
# print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
# print(pairs([]) == 0)
# print(pairs([23]) == 0)
# print(pairs([997, 997]) == 1)
# print(pairs([32, 32, 32]) == 1)
# print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

# Create a function that takes a non-empty string as an argument. The string consists entirely of lowercase alphabetic characters. The function should return the length of the longest vowel substring. The vowels of interest are "a", "e", "i", "o", and "u".

#Problem
#   Find the longest vowel substring in the input string
#   Input: string, all lowercase letters
#   Output: integer representing length of longest vowel substring
#   Can't take the string out of order here

# Examples - below

# Data structures - iterate through the string using index notation

# Algorithm
#   instantiate vowel counter list to hold count of each substring
#   instantiate valid vowel characters as a set
#   instantiate current char
#   iterate through the string for char in input
#       store first char as current char
#       if char is in vowel set
#           increment vowel counter
#       if char is not in vowel set
#           append the current value of vowel counter to list
#           reset the vowel counter to 0
#       
#    return the maximum of the vowel counter list

def longest_vowel_substring(input):
    vowel_counts = []
    vowel_counter = 0
    valid_vowels = 'aeiou'
    for char in input:
        if char in valid_vowels:
            vowel_counter += 1
        if char not in valid_vowels:
            vowel_counts.append(vowel_counter)
            vowel_counter = 0
    vowel_counts.append(vowel_counter)
    return max(vowel_counts)

# print(longest_vowel_substring('cwm') == 0)
# print(longest_vowel_substring('many') == 1)
# print(longest_vowel_substring('launchschoolstudents') == 2)
# print(longest_vowel_substring('eau') == 3)
# print(longest_vowel_substring('beauteous') == 3)
# print(longest_vowel_substring('sequoia') == 4)
# print(longest_vowel_substring('miaoued') == 5)

# Create a function that takes two string arguments and returns the number of times that the second string occurs in the first string. Note that overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.

# You may assume that the second argument is never an empty string.

# Problem
#   Input: two strings
#   Output: integer
#   Determine number of occurrences of 2nd input string in first input string
#   Overlapping substrings do not count, must be entirely seperate index

#   Examples - note that babab and bab is 1 substring, return 0 if string 1 is empty or there are no substrings

# data structures
#   string
#   list ?

# Algorithm
#   if substring 2 not in substring 1
#       return 0
#   instantiate substring counter starting with 1
#   instantiate first index occurrence with str.find(str2)
#   instantiate new str1 with slice [first index occurrence + len(str2):]
#   while true:
#       if str 2 is in new str1:
#           again set new str1 equal to slice [str.find(str2) + len(str2):]
#           increment substring counter
#       else break
#   return substring counter

def count_substrings(str, sub):
    if sub not in str:
        return 0
    sub_counter = 1
    first_index = str.find(sub)
    slice_str = str[first_index + len(sub):]
    while True:
        if sub in slice_str:
            slice_str = slice_str[slice_str.find(sub) + len(sub):]
            sub_counter += 1
        else:
            break
    return sub_counter

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)