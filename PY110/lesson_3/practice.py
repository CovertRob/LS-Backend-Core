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
# def smaller_numbers_than_current(input_ints):
#     seen = set()
#     counts_of_smaller = []
#     num_of_ints_smaller = 0
#     for num in input_ints:
#         for elem in input_ints:
#             if elem < num and elem not in seen:
#                 seen.add(elem)
#                 num_of_ints_smaller += 1
#         counts_of_smaller.append(num_of_ints_smaller)
#         seen.clear()
#         num_of_ints_smaller = 0
#     print(counts_of_smaller)
#     return counts_of_smaller

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

# # This one I initially struggled with and took me about 40 minutes to re-work it a bit
# def minimum_sum(input_list):
#     if len(input_list) < 5:
#         return None
#     total = sum(input_list[0:5])
    
#     for nums in range(1, len(input_list) - 4):
#         next_five = sum(input_list[nums:nums+5])
#         if next_five < total:
#             total = next_five
#         if len(input_list) == 5:
#             return total
#     return total

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
# def closest_numbers(input):
#     sorted_input = sorted(input)
#     difference = max(sorted_input) # need to start not at 0 otherwise condition below won't work
#     pair = (0, 0)
#     for i in range(0, len(sorted_input) - 1):
#         current_difference = abs(sorted_input[i] - sorted_input[i+1])
#         if current_difference < difference:
#             difference = current_difference
#             pair = (sorted_input[i], sorted_input[i+1])
#     idx1, idx2 = input.index(pair[0]), input.index(pair[1])
#     if idx1 > idx2:
#         return (input[idx2], input[idx1])
#     return (input[idx1], input[idx2])

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

# another way to do it:
def pairs(lst):
    pair_count = 0
    seen = []
    for i in range(len(lst)):
        if lst[i] not in seen:
            seen.append(lst[i])
        else:
            seen.remove(lst[i])
            pair_count += 1
    return pair_count


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

# got chopy between translating your algorithm once you found issues with it

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

<<<<<<< HEAD
# other solution for it: from Khaled
def longest_vowel_substring(string):
    start, end = 0, 1
    longest = 0
    while True:
        current = string[start: end]
        if current[-1] in VOWELS:
            if len(current) > longest:
                longest = len(current)
            end += 1
        else:
            start = end
            end = start + 1
        if end > len(string):
            break
    return longest

=======
>>>>>>> 11dbb9c01c2587fa8bb2c27420fb651c0b74fd5b
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
    if str == sub:
        return 1
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

# print(count_substrings('babab', 'bab') == 1)
# print(count_substrings('babab', 'ba') == 2)
# print(count_substrings('babab', 'b') == 3)
# print(count_substrings('babab', 'x') == 0)
# print(count_substrings('babab', 'x') == 0)
# print(count_substrings('', 'x') == 0)
# print(count_substrings('bbbaabbbbaab', 'baab') == 2)
# print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
# print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

# Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. For example, in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.

# If a substring occurs more than once, you should count each occurrence as a separate substring.

# Problem 
#   Input - string containing digits
#   Output - integer representing even substring combinations
#   Need to figure out how many combinations of even number substrings can be made with the digits in the input string
#   Substrings need a minimum of 1 digit to count as a substring
#   Count each occurrence even if a repeat digit

# Examples - return 0 if there are no even substrings

# Data structures 
#   List - for iterating the digits in the string

# Algorithm
#   instantiate substring counter
#   iterate over input string within range index 0 to end of string (i)
#       iterate over input string within range i to end of string (j)
#           if slicce from i to j is an even substring, increment counter
#   return counter

def even_substrings(input):
    sub_counter = 0
    for i in range(0, len(input)+1):
        for j in range(i+1, len(input)+1):
            if int(input[i:j]) % 2 == 0:
                sub_counter += 1
    return sub_counter

# print(even_substrings('1432') == 6)
# print(even_substrings('3145926') == 16)
# print(even_substrings('2718281') == 16)
# print(even_substrings('13579') == 0)
# print(even_substrings('143232') == 12)

# Create a function that takes a nonempty string as an argument and returns a tuple consisting of a string and an integer. If we call the string argument s, the string component of the returned tuple t, and the integer component of the tuple k, then s, t, and k must be related to each other such that s == t * k. The values of t and k should be the shortest possible substring and the largest possible repeat count that satisfies this equation.

# You may assume that the string argument consists entirely of lowercase alphabetic letters.

# Problem
#   Input - single string, all lowercase letters
#   Output - tuple containing string and integer
#   Problem - find the shortest possible substring and the largest possible repeat count that satisfies s == t * k
#   Need to iterate until the first letter repeats itself again to find the shortest substring
#   Sub - problem: finding k repeat count
#       input: 2 strings, str and sub
#       output: integer, count of how many times sub occurs in str

def repeated_substring(input):
    shortest_sub = input
    for i in range(1, len(input)):
        if input[0] == input[i]:
            shortest_sub = input[0:i]
            break
    return (shortest_sub, count_substrings(input, shortest_sub))

# refactored to account for my extra test case: I still don't like how I did this it doesn't feel like a good solution
def repeated_substring(input):
    shortest_sub = input
    for i in range(1, len(input)):
        if input[0] == input[i]:
            shortest_sub = input[0:i]
            if shortest_sub * count_substrings(input, shortest_sub) == input:
                break
    return (shortest_sub, count_substrings(input, shortest_sub))

# print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
# print(repeated_substring('xyxy') == ('xy', 2))
# print(repeated_substring('xyz') == ('xyz', 1))
# print(repeated_substring('aaaaaaaa') == ('a', 8))
# print(repeated_substring('superduper') == ('superduper', 1))
# # my solution breaks if the word contains a repeat of the first character: (my own test case)
# print(repeated_substring('expertexpert') == ('expert', 2))

# Create a function that takes a string as an argument and returns True if the string is a pangram, False if it is not.

# Pangrams are sentences that contain every letter of the alphabet at least once. For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram since it uses every letter at least once. Note that case is irrelevant.

# Problem
#   Input: string
#   Output: boolean
#   Return true if the string contains every letter of the alphabet

# Examples below

# Data structures - use a set for the alphabet

# Algorithm
#   instantiate alphabet chars as a set
#   iterate through the input string
#       try to remove value from set
#       if key error, continue
#   return true if the alphabet set is empty

def is_pangram(input):
    alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    for char in input:
        try:
            alphabet.remove(char)
        except KeyError:
            continue
    return not bool(alphabet)

# print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
# print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
# print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

# my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
# print(is_pangram(my_str) == True)

# Create a function that takes two strings as arguments and returns True if some portion of the characters in the first string can be rearranged to match the characters in the second. Otherwise, the function should return False.

# You may assume that both string arguments only contain lowercase alphabetic characters. Neither string will be empty.

# Problem
#   Input: two strings, all lowercae letters
#   Output: boolean value
#   Need to determine if every character in str2 are in str1, which would allow str1 to be re-arranged to form str2
#   Need to be careful of repeat characters being accounted for their appropriate number of times - need to remove the char each time we check it's presence

#   Examples - str1 can be longer than str 2

# data structures - use lists to get chars

# Algorithm
#   instantiate str1 as list
#   instantiate str2 as list
#   iterate through str2
#       if str2 char is in str1 -> remove str2 char from str1
#       else -> return False
#   return False

def unscramble(str1, str2):
    list_str1 = list(str1)
    list_str2 = list(str2)
    for char in list_str2:
        try:
            list_str1.remove(char)
        except ValueError:
            return False
    return True

# print(unscramble('ansucchlohlo', 'launchschool') == True)
# print(unscramble('phyarunstole', 'pythonrules') == True)
# print(unscramble('phyarunstola', 'pythonrules') == False)
# print(unscramble('boldface', 'coal') == True)

# Create a function that takes a single integer argument and returns the sum of all the multiples of 7 or 11 that are less than the argument. If a number is a multiple of both 7 and 11, count it just once.

# For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.

# If the argument is negative, return 0.

# Problem
#   Input: integer
#   Output: integer sum
#   Compute the multiples of 7 and 11 that are below the argument
#   Store the multiples in a set so that there are no repeat multiples
#   Do not inclue ceiling 

# Examples - below

# Data structures - set

# Algorithm
#   instantiate multiples as set
#   get the multiples of 7 below arg and add to set
#   get the multiples of 11 below are and add to set
#   return the sum of the set
#   

def seven_eleven(ceiling):
    multiples = set()
    seven_multiples = {num for num in range(7, ceiling, 7)}
    eleven_multiples = {num for num in range(11, ceiling, 11)}
    multiples = seven_multiples | eleven_multiples
    return sum(multiples)

#my own test case, issue with when exaxt multiple

# print(seven_eleven(10) == 7)
# print(seven_eleven(11) == 7)
# print(seven_eleven(12) == 18)
# print(seven_eleven(25) == 75)
# print(seven_eleven(100) == 1153)
# print(seven_eleven(0) == 0)
# print(seven_eleven(-100) == 0)

# Create a function that takes a string argument that consists entirely of numeric digits and computes the greatest product of four consecutive digits in the string. The argument will always have more than 4 digits.

# Problem
#   Input: string of integers greater than length 4
#   Output: integer (multiplication)
#   Find the substring of digits that results in the greatest product
#   Can deduce if there are lenght of string arg - 3 combinations available
#   need to find all the substrings of digits length 4 or greater - use comprehension and ranges

# Examples - 

# Data structures - integer and string

# Algorithm
#   find all substrings of input string length 4 or greater and store in a list
#       sub-problem
#   compute product of each substring and store in a list
#   return the maximum product

def substring_product(input):
    product = 1 # start at 1 so no multiply by 0
    for digits in input:
        product *= int(digits)
    return product

def greatest_product(input):
    sub_digits = [input[i:i+4] for i in range(0, len(input)) if len(input[i:i+4]) == 4]
    products = [substring_product(sub) for sub in sub_digits]
    return max(products)

# print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
# print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
# print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
# print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

# Create a function that returns the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. You may assume that the input string contains only alphanumeric characters

# Problem
#   Input - lowercase letters and numbers as a string, no spaces
#   Output - integer
#   Need to determine which alphanumeric characters occur more than once in the input string
#   Need to treat string as case-insensitive when comparing

# Examples - see that if ther are no repeats return 0

# Data structure - sets and lists

# Algorithm
#   instantiate copy of input str in lowercase and as a list
#   instantiate list comprehension, iterate through str list, append if it's count in the list in greater than 1 to find repeat characters
#   return the size of the set of the repeat chars to get rid of duplicate repeats

def distinct_multiples(input_str):
    str_as_list = list(input_str.lower())
    repeat_chars = [char for char in str_as_list if str_as_list.count(char) > 1]
    return len(set(repeat_chars))

# print(distinct_multiples('xyz') == 0)               # (none)
# print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
# print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
# print(distinct_multiples('unununium') == 2)         # u, n
# print(distinct_multiples('multiplicity') == 3)      # l, t, i
# print(distinct_multiples('7657') == 1)              # 7
# print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
# print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

# Create a function that takes a list of integers as an argument. The function should determine the minimum integer value that can be appended to the list so the sum of all the elements equal the closest prime number that is greater than the current sum of the numbers. For example, the numbers in [1, 2, 3] sum to 6. The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to sum to 7.

# Notes:

# The list will always contain at least 2 integers.
# All values in the list must be positive (> 0).
# There may be multiple occurrences of the various numbers in the list.

# Problem
#   Input: list of integers
#   Output: integer
#   Need to determine the sum of the input list of integers
#   Need to determine the closest prime number to that sum
#   Need to determine the difference between that sum and that prime number to find number to append 
#   Prime number = number has multiples that are only 1 and itself
#       problem - prime number generator
#       sub-problem - determine a numbers factors

# Examples - 

# Data structures - lists

# Algorithm
#   instantiate sum of the input list and calculate it
#   instantiate closest prime number greater than the sum of the list
#   calculate the difference between the greater first prime and the sum of the list
#   return the difference

# Algorithm
#   instantiate prime counter, starting input integer
#   while true
#       increment the prime counter
#       if current value of prime counter only has 2 factors -> break

# Algorithm
#   instantiate range from 2 to input // 2
#       if the input mod range value is 0
#           return false
#   return true

def determine_if_prime(input_int):
    for i in range(2, (input_int // 2) + 1):     
        if input_int % i == 0:
            return False
    return True

def get_next_prime(input_int):
    prime_count = input_int
    while True:
        prime_count += 1
        if determine_if_prime(prime_count):
            break
    return prime_count

def nearest_prime_sum(input_lst):
    sum_of_lst = sum(input_lst)
    next_prime = get_next_prime(sum_of_lst)
    return next_prime - sum_of_lst


# print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
# print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
# print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
# print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# # Nearest prime to 163 is 167
# print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

'''
Create a function that takes an list of integers as an argument. Determine and return the index N for which all numbers with an index less than N sum to the same value as the numbers with an index greater than N. If there is no index that would make this happen, return -1.

If you are given a list with multiple answers, return the index with the smallest value.

The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the numbers to the right of the last element is 0.

Problem
    need to determine two indexes from the input list of integers
    the index N for which all numbers less than that index must sum to the same value as the numbers with an index greater than need

Examples - the index N is not included in the computations of the sums on either side 

Data structures 
    Input: list of integers
    Output: single integers
    intermediary - 
        iterate over the list
        use a list to store sums

Algorithm
    instantiate minimum sum variable = -1
    instantiate a list to hold our sums - used in the case of multiple answers
    iterate through the input list of integers using a range
        take a slice of the of the input list from starting index to current index
        take a slice of the input list from current index to end index
        append the sum of both to our sum list of their sums are equal
    if the list of sums is not empty, find the minimum sum and set it equal to the minimum sum variable
    return the minimum sum variable 

'''
def equal_sum_index(input_lst):
    min_sum = -1
    lst_of_sums = []
    for i in range(0, len(input_lst)+1):
        slice_1 = input_lst[0:i]
        slice_2 = input_lst[i+1:len(input_lst)+1]
        if sum(slice_1) == sum(slice_2):
            lst_of_sums.append(i)
    if len(lst_of_sums) >= 1:
        min_sum = min(lst_of_sums)
    return min_sum

# print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
# print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
# print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
# print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# # The following test case could return 0 or 3. Since we're
# # supposed to return the smallest correct index, the correct
# # return value is 0.
# print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

'''
Create a function that takes an list of integers as an argument and returns the integer that appears an odd number of times. There will always be exactly one such integer in the input list.


Problem:
    Find and return the integer in the input ist that appears an odd number of times
    There is always going to be a single integer that meets these reqirements

Examples - in the case of a single input, return the input
    The odd number of times could be once while the other elements repeat twice
    The inputs can include negative numbers and 0

Data Structures -
    Input: list of integers
    Output: single integer
    Intermediary: 
        iteration through list

Algorithm
    SET unique_nums as set of input list
    iterate through set elements
        if the count of the current num in the input list is odd, return set element as the odd integer

'''

def odd_fellow(input_lst):
    unique_nums = set(input_lst)
    for elem in unique_nums:
        if input_lst.count(elem) % 2 == 1:
            return elem


# print(odd_fellow([4]) == 4)
# print(odd_fellow([7, 99, 7, 51, 99]) == 51)
# print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
# print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
# print(odd_fellow([0, 0, 0]) == 0)

'''
Create a function that takes a list of numbers, all of which are the same except one. Find and return the number in the list that differs from all the rest.

The list will always contain at least 3 numbers, and there will always be exactly one number that is different.

Problem
    We are given a list of numbers and all of them are the same except for one. Need to find the number that is different and return it.
    Guranteed to be at least 3 numbers in total, only one will ever be different.
    Input: list of integers and floats
    Output: single integer or float

Examples - see that the input can include floats and 0

Data structures - 
    Input: list
    Output: float or integer
    Intermediary - lists and sets

Algorithm
    SET input list as a set
    iterate through set
        if the count of the current set element in input list is > 1, continue, else return the current element
'''
def what_is_different(input_lst):
    unique_nums = set(input_lst)
    for num in unique_nums:
        if input_lst.count(num) == 1:
            return num

# print(what_is_different([0, 1, 0]) == 1)
# print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
# print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
# print(what_is_different([3, 4, 4, 4]) == 3)
# print(what_is_different([4, 4, 4, 3]) == 3)

# Study guide repeated problems below
'''
Problem 1 repeat

Create a function that takes a list of numbers as an argument. For each number, determine how many numbers in the list are smaller than it, and place the answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs multiple times in the list, it should only be counted once.

Problem
    Given a list of integers, determine for each number in that list how many numbers in the list are less than it and place those answer in a list
    The index of the output answer should match the index of the element being counted
    Only count unique values

Examples
    If all numbers are the same, return 0 for each index. Case is not inclusive
    IF there is only 1 element, return 0 as there are none to be less than it
    The output list length will always match the input list length

Data structures 
    Input: list
    Output: list
    Intermediary:
        lists and sets (use for getting rid of repeat values)

Algorithm
    SET unique_values as a set of the list
    SET count_less_than list as empty list
    SET less_than_counter equal to 0
    iterate through the input list of elements
        iterate through the set elements
            if element in set is less than current list element, increment less_than_counter
        append less_than_counter to the count_less_than list
        SET less_than_counter back to 0

'''
# Completed in 12 minutes, much better than last time

def smaller_numbers_than_current(input_lst):
    if len(input_lst) == 0:
        return [0]
    unique_values = set(input_lst)
    count_less_than = []
    less_than_counter = 0
    for num  in input_lst:
        for elem in unique_values:
            if elem < num:
                less_than_counter += 1
        count_less_than.append(less_than_counter)
        less_than_counter = 0
    return count_less_than
    

# print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
# print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
# print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
# print(smaller_numbers_than_current([1]) == [0])

# my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
# result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
# print(smaller_numbers_than_current(my_list) == result)

'''
Create a function that takes a list of integers as an argument. The function should return the minimum sum of 5 consecutive numbers in the list. If the list contains fewer than 5 elements, the function should return None.

Problem
    Input: list of integers
    Output: integer or None
    We need to find the 5 consecutive integer sum that is the minimum in the input list
    If there are less than 5 elements in the input list, return None

Examples
    There can be negative numbers included in the input list and 0
    The output can be a negative sum

Data structures 
    Input: list
    Output: singed integer
    Intermediary:
        lists
        range objects
        slices

Algorithm
    if the input list length is less than 5, return None
    SET current_min_sum equal to sum of input list
    iterate through the input list with range object
        take slice of 5 elements and sum them up
        if the sum of the slice is less than the current value of current_min_sum, re-assign current_min_sum to this slice's value
    return current_min_sum
'''

# Got it in 17 minutes, much better than first time and cleaner

def minimum_sum(input_lst):
    if len(input_lst) < 5:
        return None
    current_min_sum = abs(sum(input_lst))
    for i in range(0, len(input_lst)-4):
        print(input_lst[i:i+5])
        slice_sum = sum(input_lst[i:i+5])
        if slice_sum < current_min_sum:
            current_min_sum = slice_sum
    print(current_min_sum)
    return current_min_sum


# print(minimum_sum([1, 2, 3, 4]) is None)
# print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
# print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
# print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
# print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

'''
Create a function that takes a string argument and returns a copy of the string with every second character in every third word converted to uppercase. Other characters should remain the same.

Problem:
    Given a string argument, we need to return a copy of the string with every 2nd character in every third word converted to uppercase
    Leave all other characters the same
    Input: Single string 
    Output: single string
    Sub-problem:
        return a copy of a word with every 2nd charcter capitalized, every other character to remain the same

Examples - if the word is a single character, leave it alone because it doesn't meet the 2nd character requirement

Data structures
    Input: string
    Output: string
    intermediary: 
        list to hold the separated words
        range objects to iterate over the words

Algorithm:
    SET words_separated as a list with the input string split at white spaces
    SET index counter equal to 1
    SET weird_word equal to empty string
    iterate over the split list using enumerate
        if the current index - 1 equals index counter (meaning it's a third index)
            turn the word to weird case and augment assign the word to the weird word string
            set index ounter to 1
        else augment assign the normal case word to the weird_word string and increment index counter

Algorithm:
    Input: single word as a string
    Output: single string with case changed
        SET converted_str to empty string
        iterate through input_str with enumerate
            if the current index % 2 == 1, uppercase the letter and append it to the return string
            else, append the letter unchanged
        return converted_str

'''
def second_to_upper(word):
    converted_str = ''
    for idx, char in enumerate(word):
        if idx % 2 == 1:
            converted_str += char.upper()
        else:
            converted_str += char
    return converted_str

def to_weird_case(input_str):
    words_separated = input_str.split()
    index_counter = 1 # because 0, 1, 2
    weird_word = ''
    for idx, word in enumerate(words_separated):
        if index_counter == 3:
            weird_word += f" {second_to_upper(word)}"
            index_counter = 1
        else:
            weird_word += f" {word}"
            index_counter += 1
    #print(weird_word)
    return weird_word.strip()

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

'''
Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. If there are multiple pairs that are equally close, return the pair that occurs first in the list.

Problem
    Need to find and return the pair of numbers that are closest together in value given a list of integers
    If there are multiple pairs that are equally close together in value, you should return the pair that occurs first
    Need to check each pair combination in the list
    Input: list of integers
    Output: tuple consisting of integer pair in the order they appear in the list
    Use absolute value

Examples - below

Data structures:
    Input: list with integers
    Output: tuple with integers
    Intermediary: 
        range object
        lists
        tuple

Algorithm:
    SET current_min_difference = differencce of first two elements
    SET current_tuple equal to empty tuple
    iterate over the list with range object i to the length of the list
        iterate over the list with range object j from i+1 to the length of the list
            if the abs difference between i index value and j index value is less than current_min_difference value
                set current_min_difference value
                set current_tuple equal to tuple(i, j)
    return current_tuple pair
'''
def closest_numbers(input_lst):
    current_min_difference = abs(input_lst[0] - input_lst[1])
    current_tuple = ()
    for i in range(0, len(input_lst)):
        for j in range(i+1, len(input_lst)):
            difference = abs(input_lst[i] - input_lst[j])
            if difference < current_min_difference:
                current_min_difference = difference
                current_tuple = (input_lst[i], input_lst[j])
    print(current_tuple)
    return current_tuple
            

# print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
# print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
# print(closest_numbers([12, 22, 7, 17]) == (12, 7))

# Back to advanced exercises
''' 
Write a function that takes two sorted lists as arguments and returns a new list that contains all the elements from both input lists in ascending sorted order. You may assume that the lists contain either all integer values or all string values.

You may not provide any solution that requires you to sort the result list. You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.

Problem
    Input: two lists, either all integer or all string values
    Output: a sorted list of those values
    We need to return a new list with all elements from both lists sorted in ascending order
    We are not allowed to sort the result list, instead we need to build the result list one element at a time in the sorted order
    Do not mutate the input lists
    sub-problem:
        find the smallest value between two lists that is greater than a given value N

Examples - The input can include empty lists

Data structures:
    Input: two lists
    Output: one list
    Intermediary:
        lists

Algorithm:
    define function with parameters current_smallest, lst1, lst2
        SET new lst equal to lst1 + lst2
        iterate over the combined list
            if the current element is less than current

*Must pick one element at a time*
Algorithm:
    SET new empty list to be return list
    SET current_smallest equal to 0
    iterate with range object i for length of both input lists
        find the next smallest value that is not in the return list
        append next smallest value to the return list
    return the return list

Jacked this up because didn't read that the two lists are already sorted to begin with
LS's solution below:

'''
def merge(list1, list2):
    copy1 = list1[:]
    copy2 = list2[:]
    result = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            result.append(copy1.pop(0))
        else:
            result.append(copy2.pop(0))

    return result + copy1 + copy2

# All of these examples should print True
# print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
# print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
# print(merge([], [1, 4, 5]) == [1, 4, 5])
# print(merge([1, 4, 5], []) == [1, 4, 5])

# names1 = ['Alice', 'Kim', 'Pete', 'Sue']
# names2 = ['Bonnie', 'Rachel', 'Tyler']
# names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
#                   'Rachel', 'Sue', 'Tyler']
# print(merge(names1, names2) == names_expected)

'''
Problem:
    Sort a list using the merge sort algorithm.
    Input: list of either integer or string values
    Output: sorted list of the same values

Examples - 
[9, 2, 7, 6, 8, 5, 0, 1] -->              # initial list
[[9, 2, 7, 6], [8, 5, 0, 1]] -->          # divide into two lists
[[[9, 2], [7, 6]], [[8, 5], [0, 1]]] -->  # divide each sub-list in two
# repeat until each sub-list contains only 1 value
[[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]]

Data structures:
    The algorithm uses recursion
    lists

Algorithm:
    What is our base case? - when each sublist has 1 element

    split the list into two sublists until each sublist has 1 element
    call merge on the sublists
    return the merged lists
'''

def merge_sort(input_lst):
    if len(input_lst) == 1:
        return input_lst
    
    sub_list1 = input_lst[:len(input_lst) // 2]
    sub_list2 = input_lst[len(input_lst) // 2:]

    sub_list1 = merge_sort(sub_list1)
    sub_list2 = merge_sort(sub_list2)

    return merge(sub_list1, sub_list2)

# All of these examples should print True
# print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
# print(merge_sort([5, 3]) == [3, 5])
# print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
# print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

# original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#             'Kim', 'Bonnie']
# expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
#             'Sue', 'Tyler']
# print(merge_sort(original) == expected)

# original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
#             43, 5, 25, 35, 18, 46]
# expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
#             35, 37, 43, 46, 51, 54]
# print(merge_sort(original) == expected)


'''
Implement the binary search algorithm.

Problem:
    The input list that you are searching for a value in is already sorted.
    Find and return the matching value provided in the input arguments.

Examples:
    two arguments for the function: the list and the value to search for
    inputs can be strings or integers, not both

Data Structure:
    lists

Algorithm:
    SET the starting value to the value in the middle of the list
    if this value is equal to the search value, return it
    SET empty list
    if the middle value is greater than the search value, discard the lower half
    if the middle value is less than the search value, discard the upper half
    perform recursive call

'''

def binary_search(lst, search_item):
    high = len(lst) - 1
    low = 0

    while low <= high:
        mid = (high + low) // 2
       
        if lst[mid] == search_item:
            return mid
        elif lst[mid] < search_item:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# All of these examples should print True
# businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
#               'Donuts R Us', 'Eat a Lot', 'Good Food',
#               'Pasta Place', 'Pizzeria', 'Tiki Lounge',
#               'Zooper']
# print(binary_search(businesses, 'Pizzeria') == 7)
# print(binary_search(businesses, 'Apple Store') == 0)

# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

# names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
#          'Tyler']
# print(binary_search(names, 'Peter') == -1)
# print(binary_search(names, 'Tyler') == 6)

from fractions import Fraction

def egyptian(target_value):
    denominators = []
    unit_denominator = 1
    while target_value != 0:
        unit_fraction = Fraction(1, unit_denominator)
        if unit_fraction <= target_value:
            target_value -= unit_fraction
            denominators.append(unit_denominator)

        unit_denominator += 1

    return denominators

def unegyptian(denominators):
    return sum([Fraction(1, d) for d in denominators])

from fractions import Fraction

# # Using the egyptian function
# # Your results may differ for these first 3 examples
# print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
# print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
# print(egyptian(Fraction(3, 1)))
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# # Using the unegyptian function
# # All of these examples should print True
# print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
# print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
# print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
# print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
# print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
# print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
# print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
# print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))

# Easy 4 problems
'''
Write a function that takes a list of integers between 0 and 19 and returns a list of those integers sorted based on the English word for each number:
'''

def get_number_word(num):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    return numbers[num]

def alphabetic_number_sort(lst):
    return sorted(lst, key=get_number_word)

# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#               10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
#                    7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

# print(alphabetic_number_sort(input_list) == expected_result)
# # Prints True

#Transform two lists into frozen sets and find their common elements.

def intersection(lst1, lst2):
    return frozenset(lst1) & frozenset(lst2)

# list1 = [2, 4, 6, 8]
# list2 = [1, 3, 5, 7, 8]
# expected_result = frozenset({8})
# print(intersection(list1, list2) == expected_result) # True

'''
Given a dictionary, return its keys sorted by the values associated with each key.
'''

def get_value(item):
    return item[1]

def order_by_value(input_dict):
    sorted_items = sorted(input_dict.items(), key=get_value)
    return [keys[0] for keys in sorted_items]

# my_dict = {'p': 8, 'q': 2, 'r': 6}
# keys = ['q', 'r', 'p']
# print(order_by_value(my_dict) == keys)  # True

''' 
From two list arguments, determine the elements that are unique to the first list. The return value should be a set.
''' 
def unique_from_first(list1, list2):
    return set(list1) - set(list2)

# list1 = [3, 6, 9, 12]
# list2 = [6, 12, 15, 18]
# print(unique_from_first(list1, list2) == {9, 3})

'''
Write a function that takes a string argument and returns a list of substrings of that string. Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.
'''

def leading_substrings(str):
    return [str[:i] for i in range(1, len(str)+1)]

#All of these examples should print True
# print(leading_substrings('abc') == ['a', 'ab', 'abc'])
# print(leading_substrings('a') == ['a'])
# print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

'''
Write a function that returns a list of all substrings of a string. Order the returned list by where in the string the substring begins. This means that all substrings that start at index position 0 should come first, then all substrings that start at index position 1, and so on. Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous exercise:
'''
def substrings(str):
    return [ sub for idx, char in enumerate(str) 
                    for sub in leading_substrings(str[idx:]) ]

# expected_result = [
#     "a", "ab", "abc", "abcd", "abcde",
#     "b", "bc", "bcd", "bcde",
#     "c", "cd", "cde",
#     "d", "de",
#     "e",
# ]

# print(substrings('abcde') == expected_result)  # True

''' 

Write a function that returns a list of all palindromic substrings of a string. That is, each substring must consist of a sequence of characters that reads the same forward and backward. The substrings in the returned list should be sorted by their order of appearance in the input string. Duplicate substrings should be included multiple times.

You may (and should) use the substrings function you wrote in the previous exercise.

For the purpose of this exercise, you should consider all characters and pay attention to case; that is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not. In addition, assume that single characters are not palindromes.
'''

def palindromes(str):
    subs = substrings(str)
    return [sub for sub in subs if sub == sub[::-1] and len(sub) != 1]

# print(palindromes('abcd') == [])                  # True
# print(palindromes('madam') == ['madam', 'ada'])   # True

# print(palindromes('hello-madam-did-madam-goodbye') ==
#                   [
#                       'll', '-madam-', '-madam-did-madam-',
#                       'madam', 'madam-did-madam', 'ada',
#                       'adam-did-mada', 'dam-did-mad',
#                       'am-did-ma', 'm-did-m', '-did-',
#                       'did', '-madam-', 'madam', 'ada', 'oo',
#                   ])    # True

# print(palindromes('knitting cassettes') ==
#                   [
#                       'nittin', 'itti', 'tt', 'ss',
#                       'settes', 'ette', 'tt',
#                   ])    # True

''' 

Write a function that takes two arguments, an inventory item ID and a list of transactions, and returns a list containing only the transactions for the specified inventory item.

'''
def transactions_for(id, lst):
    return [dict for dict in lst if dict['id'] == id]

# transactions = [
#     {"id": 101, "movement": 'in',  "quantity":  5},
#     {"id": 105, "movement": 'in',  "quantity": 10},
#     {"id": 102, "movement": 'out', "quantity": 17},
#     {"id": 101, "movement": 'in',  "quantity": 12},
#     {"id": 103, "movement": 'out', "quantity": 20},
#     {"id": 102, "movement": 'out', "quantity": 15},
#     {"id": 105, "movement": 'in',  "quantity": 25},
#     {"id": 101, "movement": 'out', "quantity": 18},
#     {"id": 102, "movement": 'in',  "quantity": 22},
#     {"id": 103, "movement": 'out', "quantity": 15},
# ]

# print(transactions_for(101, transactions) ==
#       [
#           {"id": 101, "movement": "in",  "quantity":  5},
#           {"id": 101, "movement": "in",  "quantity": 12},
#           {"id": 101, "movement": "out", "quantity": 18},
#       ]) # True

''' 
The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). Your function should work with any integer input.

You may not use Python's datetime module.

''' 

MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def format_time(hours, minutes):
    return f"{hours:02d}:{minutes:02d}"

# Note that with the modulus operator, -3 % 1440 is 1437, with negative numbers it takes away from the 2nd number: what is the least positive integer to subtract from -3 to make 1440 divisible by -3?

def time_of_day(delta_minutes):
    delta_minutes = delta_minutes % MINUTES_PER_DAY # normalize the time to be within minutes in a day
    print(delta_minutes)
    hours = delta_minutes // MINUTES_PER_HOUR
    minutes = delta_minutes % MINUTES_PER_HOUR
    return format_time(hours, minutes)

# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True



''' 
As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, and return the number of minutes before and after midnight, respectively. Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.

Problem:
    We are given a string input in the format 00:00 which represents how many hours and minutes
    Need to convert the string format to total minutes and determine it's respective value either after or before midnight

Examples - both 00:00 and 24:00 should return 0

Data structures - integers and strings

Algorithm:
    SET hours by taking slice of input string
    SET minutes by taking slice of input string
    SET total minutes by multiplying hours by 60 minutes and adding minutes to it
    return the total minutes either from or to 0 or 1440
    
'''

def after_midnight(input):
    hours = int(input[:2])
    minutes = int(input[3:])
    if hours + minutes == 0 or hours == 24:
        return 0
    total_minutes = (hours * 60) + minutes
    return total_minutes

def before_midnight(input):
    hours = int(input[:2])
    minutes = int(input[3:])
    if hours + minutes == 0 or hours == 24:
        return 0
    total_minutes = (hours * 60) + minutes
    return 1440 - total_minutes

# LS's solution:
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def after_midnight(time_str):
    hours, minutes = [int(unit) for unit in time_str.split(":")]
    return ((hours * MINUTES_PER_HOUR) + minutes) % MINUTES_PER_DAY

def before_midnight(time_str):
    delta_minutes = MINUTES_PER_DAY - after_midnight(time_str)
    if delta_minutes == MINUTES_PER_DAY:
        delta_minutes = 0
    return delta_minutes

# print(after_midnight("00:00") == 0)     # True
# print(before_midnight("00:00") == 0)    # True
# print(after_midnight("12:34") == 754)   # True
# print(before_midnight("12:34") == 686)  # True
# print(after_midnight("24:00") == 0)     # True
# print(before_midnight("24:00") == 0)    # True
''' 
Write a function that takes a string, doubles every character in the string, then returns the result as a new string.
'''
def repeater(str):
    return ''.join([char * 2 for char in str])

# print(repeater('Hello') == "HHeelllloo")              # True
# print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
# print(repeater('') == "")                             # True

'''

Write a function that takes a string, doubles every consonant in the string, and returns the result as a new string. The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.

'''
VOWELS = 'aeiou'
def string_checker(str):
    if str not in VOWELS and str.isalpha():
        return True
    return False
    
def double_consonants(str):
    return ''.join([char * 2 if string_checker(char) else char for char in str])

# All of these examples should print True
# print(double_consonants('String') == "SSttrrinngg")
# print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
# print(double_consonants('July 4th') == "JJullyy 4tthh")
# print(double_consonants('') == "")

def reverse_number(number):
    return int(str(number)[::-1])

# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True
''' 
Write a function that takes a string argument consisting of a first name, a space, and a last name. The function should return a new string consisting of the last name, a comma, a space, and the first name.
'''
def swap_name(str):
    split_str = str.split()
    return f"{split_str[1]}, {split_str[0]}"

#print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

''' 
Create a function that takes two integers as arguments. The first argument is a count, and the second is the starting number of a sequence that your function will create. The function should return a list containing the same number of elements as the count argument. The value of each element should be a multiple of the starting number.

You may assume that count will always be an integer greater than or equal to 0. The starting number can be any integer. If the count is 0, the function should return an empty list.

Algorithm:

''' 

def sequence(count, start):
    if count == 0:
        return []
    multiples = [start*i for i in range(1, count+1)]
    return multiples

# print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
# print(sequence(4, -7) == [-7, -14, -21, -28])     # True
# print(sequence(3, 0) == [0, 0, 0])                # True
# print(sequence(0, 1000000) == [])                 # True

''' 
Write a function that takes a list as an argument and reverses its elements, in place. That is, mutate the list passed into the function. The returned object should be the same object used as the argument.

You may not use the list.reverse method nor may you use a slice ([::-1]).
'''

def reverse_list(lst):
    
    for idx in range(len(lst)//2):
        lst[idx], lst[-(idx + 1)] = lst[-(idx+1)], lst[idx]
    return lst

# list1 = [1, 2, 3, 4]
# result = reverse_list(list1)
# print(result == [4, 3, 2, 1])               # True
# print(list1 is result)                      # True

# list2 = ["a", "b", "c", "d", "e"]
# result2 = reverse_list(list2)
# print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
# print(list2 is result2)                     # True

# list3 = ["abc"]
# result3 = reverse_list(list3)
# print(result3 == ['abc'])                   # True
# print(list3 is result3)                     # True

# list4 = []
# result4 = reverse_list(list4)
# print(result4 == [])                        # True
# print(list4 is result4)                     # True

''' 
Write a function that takes a string as an argument and returns True if all parentheses in the string are properly balanced, False otherwise. To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

'''

# LS's solution: If the string is balanced, the parens value will be 0

def is_balanced(s):
    parens = 0
    for char in s:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
        if parens < 0:
            return False
    return parens == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True