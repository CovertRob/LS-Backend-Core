# Exercises from module lessons

# Practicing higher-order functions with callbacks

def for_each(callback, iterable):
    for item in iterable:
        callback(item)

# for_each(lambda number: print(number**2), [1, 2, 3, 4, 5])

# pets = ('cat', 'dog', 'fish', 'bearded dragon')
# for_each(lambda string: print(string.title()), pets)

# nested_lists = [[1, 2], [3, 4], [5, 6, 7]]
# for_each(lambda sublist: sublist.pop(), nested_lists)
# print(nested_lists)

# for_each is type generic iteration

# next one

def times(callback, count):
    for item in range(count):
        callback(item)

# times(lambda number: print(number**2), 5)

# pets = ('cat', 'dog', 'fish', 'bearded dragon')
# new_pets = []
# times(lambda index: new_pets.append(pets[index].title()),
#       len(pets))
# print(new_pets)

# times only iterates, the code that calls times provides the details of what it should do

# write a select function that mimics the built-in filter function
# Take two arguments: a callback function and iterable
# return a list of all the elements of the iterable for which the callback function returns a truthy value
# Do not include any elements for which the callback returns a falsy value

def select(callback, iterable):
    return [item for item in iterable if callback(item)]

# numbers = [1, 2, 3, 4, 5]
# colors = {'red', 'orange', 'yellow', 'green',
#           'blue', 'indigo', 'violet'}

# odd_numbers = select(lambda number: number % 2 != 0, numbers)
# print(odd_numbers)            # [1, 3, 5]

# large_numbers = select(lambda number: number >= 10, numbers)
# print(large_numbers)          # []

# small_numbers = select(lambda number: number < 10, numbers)
# print(small_numbers)          # [1, 2, 3, 4, 5]

# short_color_names = select(lambda color: len(color) <= 5, colors)
# print(short_color_names)      # ['blue', 'red', 'green']
# # The order of the colors may vary, but should include the
# # indicated colors.

# Write a reject function that mimics the select function, but rather rejects from the iterable
# only include elements for which the callback returns a falsy value

def reject(callback, iterable):
    return [item for item in iterable if not callback(item)]

# numbers = [1, 2, 3, 4, 5]
# colors = {'red', 'orange', 'yellow', 'green',
#           'blue', 'indigo', 'violet'}

# even_numbers = reject(lambda number: number % 2 != 0, numbers)
# print(even_numbers)            # [2, 4]

# small_numbers = reject(lambda number: number >= 10, numbers)
# print(small_numbers)          # [1, 2, 3, 4, 5]

# large_numbers = reject(lambda number: number < 10, numbers)
# print(large_numbers)          # []

# long_color_names = reject(lambda color: len(color) <= 5, colors)
# print(long_color_names)
# # ['yellow', 'violet', 'orange', 'indigo']
# # The order of the colors may vary, but should include the
# # indicated colors.

# Write a reduce function
# 3 arguments: 
#   a callback that takes two arguments: first is the current element of the iterable, second is the current reduction value, commonly called the accumulator and named accum.
#   an iterable
#   a starting value: initial value for the current argument in the callback

def reduce(callback, iterable, initial):
   
    for item in iterable:
        initial = callback(item, initial)
    return initial

# numbers = (1, 2, 4, 8, 16)
# total = lambda number, accum: accum + number
# print(reduce(total, numbers, 0))        # 31

# numbers = [10, 3, 5]
# product = lambda number, accum: accum * number
# print(reduce(product, numbers, 2))      # 300

# colors = ['red', 'orange', 'yellow', 'green',
#           'blue', 'indigo', 'violet']
# rainbow = lambda color, accum: accum + color[0].upper()
# print(reduce(rainbow, colors, ''))      # ROYGBIV
        

# Use the reduce function to compute the sum of the squares in a list of numbers

# square = lambda number, accum: accum + (number **2)
# print(reduce(square, numbers, 0))

# Create a generator expresion that generates teh reciprocals of the numbers from 1 to 10. A reciprocal of a number n is 1/n. Use a for loop to print each value.

# reciprocal = ((1/num) for num in range(1, 11))
# for recip in reciprocal:
#     print(recip)

# Create a generator function that generates the reciprocals of the numbers from 1 to n, where n is an argument to the function. Use a for loop to print each value.

# def reciprocal(num):
#     count = 1
#     while count <= num:
#         yield 1/count
#         count += 1
# for recip in reciprocal(10):
#     print(recip)

# Use a generator expression to capitalize every string in a list of strings. Use a single print invocation to print all the capitalized strings as a tuple.

# strs = ['one', 'two', 'three']
# capitalized = (str.capitalize() for str in strs)
# print(tuple(capitalized))

# Create a generator function that generates the capitalized version of every string in a list of strings. Use a single print invocation to print all the capitalized strings as a tuple.

# strs = ['one', 'two', 'three']
# def capitalize(lst):
#     for str in lst:
#         yield str.capitalize()

# print(tuple(capitalize(strs)))

# Use a generator expression to capitalize the strings in a list of strings whose length is at least 5. Use a single print invocation to print all the capitalized strings as a set.

# lst = ['one', 'two', 'three']
# atleast_5 = (str.capitalize() for str in lst if len(str) >= 5)
# print(set(atleast_5))

# Create a generator function that generates the capitalized version of every string in a list of strings whose length is less than 5. Use a single print invocation to print all the capitalized strings as a set.

# lst = ['one', 'two', 'three']
# def atleast_5(lst):
#     for str in lst:
#         if len(str) < 5:
#             yield str.capitalize()

# print(set(atleast_5(lst)))

# file = open('/home/robert_feconda/launchschool/LS-Backend-Core/PY130/example.txt', 'r')
# content = file.read()
# file.close()

# print(repr(content))
# # 'Running dog\nSleeping cat\nSwimming fish\nSinging bird\n'

# file = open('/home/robert_feconda/launchschool/LS-Backend-Core/PY130/example.txt', 'r')
# content = file.readlines()
# file.close()

# print(repr(content))
# # ['Running dog\n', 'Sleeping cat\n',
# #  'Swimming fish\n', 'Singing bird\n']

# file = open('/home/robert_feconda/launchschool/LS-Backend-Core/PY130/example.txt', 'r')
# print(repr(file.readline()))   # 'Running dog\n'
# print(repr(file.readline()))   # 'Sleeping cat\n'
# print(repr(file.readline()))   # 'Swimming fish\n'
# print(repr(file.readline()))   # 'Singing bird\n'
# print(repr(file.readline()))   # ''
# print(repr(file.readline()))   # ''
# file.close()

# file = open('/home/robert_feconda/launchschool/LS-Backend-Core/PY130/example.txt', 'r')
# for line in file:
#     print(repr(line))
# 'Running dog\n'
# 'Sleeping cat\n'
# 'Swimming fish\n'
# 'Singing bird\n'

# file.close()

# Writing to a file below.
# Don't use a REPL to run this code
# file = open('output.txt', 'w')
# file.write('Hello, world!\n')

# lines = ['First line\n', 'Second line\n']
# file.writelines(lines)

# file.close()

# Practice Problems: Arguments and Parameters

# Write a function named combine that takes three positional arguments and returns a tuple containing all three. Call this function with three different values.

def combine(one, two, three):
    return (one, two, three)
# print(combine('a', 2, None))

# Define a function named multiply that accepts two positional-only arguments and returns their product. The function should not allow these parameters to be passed as keyword arguments.

def multiply(one, two, /):
    return one*two

# print(multiply(3, 2))
# print(multiply(one=3, two=2))

# Create a function named describe_pet that takes one positional argument animal_type and one keyword argument name with a default value of an empty string. The function should print a description of the pet. The function should not accept more than 1 positional argument.

def describe_pet(animal_type, *, name=''):
    if name:
        print(f"I am a {animal_type} and my name is {name}")
    else:
        print(f"I am a {animal_type}")
# Could use / to make animal_type position only
# describe_pet('Cat')
# describe_pet('Cat', name='Crackers')
# describe_pet(animal_type='Cat', name='Crackers')

# Write a function named calculate_average that any number of numeric arguments and returns their average. Make sure it returns None if no arguments are provided

def calculate_average(*args):
    if args:
        return sum(args) / len(args)
    return None

# Create a function named find_person that accepts any number of keyword arguments in which each key is someone's name and the value is their associated profession. The function should check whether any of the key/value pairs has a key of "Antonina" and then, if the key is found, print a message that shows Antonina's profession. Otherwise, it should say "Antonina not found". The function should not accept any positional arguments.

def find_person(**kwargs):
    if 'Antonina' in kwargs.keys():
        print(kwargs['Antonina'])
    else:
        print('Antonina not found')

# Define a function named concat_strings that takes any number of strings and returns the concatenation of all the strings. Add a keyword-only argument sep with a default value of ' ' that specifies the separator to use between the strings.

def concat_strings(*args, sep=' '):
    return sep.join(args)
# Don't need to / can't apply *, to make keyword only, you can't have positional after *args

# Create a function named register that takes exactly three arguments: username as positional-only, password as keyword-only, and age as either a positional or keyword argument.

def register(username, /, age, *, password):
    return {'username': username, 'password': password, 'age': age}

# Create a function named print_message that requires a keyword-only argument (message) and an optional keyword-only argument (level) with a default value of "INFO". The function should print out the message prefixed with the level. The function shouldn't accept any positional arguments.

def print_message(*, message, level='INFO'):
    return f"[{level}] {message}"

def greet_all(*names):
    for name in names:
        print(f"Hello, {name}.")

# names = ["Chris", "Pete", "Nick"]
# greet_all(names) # This doesn't work because *names turns the arguments into one tuple
# Hello, Chris.
# Hello, Pete.
# Hello, Nick.

# predict the output
# a, b, c = (1, 2, 3)
# print(a, b, c)

# a, _, c = (1, 2, 3)
# # 1, 2, 3

# a, b = (1, 2, 3) # will raise an error

# a, b, c, d, e = (1, 2, 3) # you get an error

# a, *rest = [1, 2, 3, 4, 5] # rest will contain 2, 3, 4, 5

# first, *middle, last = "hello"
# print(f"First: {first}, Middle: {middle}, Last: {last}")
# First: h, Middle: ['e', 'l', 'l'], Last: o

# write a single line of code that swaps a and b
# a = 1
# b = 2
# a, b = b, a
# print(a, b)

adders = []
for n in range(1, 4):
    adders.append(lambda x, n=n: n + x)

# add1, add2, add3 = adders

# print(add1(10))  # Output: 11
# print(add2(10))  # Output: 12
# print(add3(10))  # Output: 13

# What does the following code print

def make_greeting():
    greeting = "Hello"

    def greet_func(name, greet=None):
        if not greet:
            return f"{greeting} {name}!"

        return f"{greet} {name}!"

    return greet_func

# greet_person = make_greeting()
# print(greet_person("John", "Goodbye"))
# print(greet_person("Jane"))
# Goodbye John!
# Hello Jane!

# What does the following program print

def make_counter():
    def counter_func():
        counter = 0
        counter += 1
        return counter

    return counter_func

# increment_counter = make_counter()
# print(increment_counter()) # 1
# print(increment_counter()) # 1

# increment_counter = make_counter()
# print(increment_counter()) # 1
# print(increment_counter()) # 1
# Closure plays no part in this execution

# What will this code print
from functools import partial

def greet(name, greeting):
    return f"{greeting}, {name}!"

# say_hello_to = partial(greet, greeting="Hello")
# print(say_hello_to(name="Alice"))  # What will this print?
# Hello, Alice!
# the functools module creates a new version of the greet function with the greeting argument pre-filled

# Write a function named later that takes two arguments: a function, func, and an argument for that function, argument. The return value should be a new function that calls func with argument as its argument. Here's an example of how it might be used:

def later(func, argument):
    def inner():
        return func(argument)
    return inner

def printer(message):
    print(message)

# print_warning = later(printer, "The system is shutting down!")
# print_warning()  # The system is shutting down!

# Write a function named later2 that takes two arguments: a function, func, and an argument for that function, first_arg. The return value should be a new function that takes an argument, second_arg. The new function should call the func with the arguments provided by first_arg and second_arg. Here's an example of how it might be used:

def later2(func, first_arg):
    def inner(second_arg):
        return func(first_arg, second_arg)
    return inner

def notify(message, when):
    print(f"{message} in {when} minutes!")

# shutdown_warning = later2(notify, "The system is shutting down")
# shutdown_warning(30) # The system is shutting down in 30 minutes!

def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")

    return wrapper

# decorated_hello = my_decorator(say_hello)
# decorated_hello()
# Before the function call
# Hello!
# After the function call

@my_decorator
def say_hello():
    print("Hello!")

# say_hello()

from dataclasses import dataclass
from pprint import pprint
@dataclass
class Square:
    width: float

    @property
    def area(self):
        return self.width**2
    
# pprint(Square.__dict__)

#list(map(lambda number: 2 * number, [1, 2, 3]))
#print(list(map(lambda number: 2 * number, [1, 2, 3])))

# PY130 exercises

# Create a list where each number from the original list is squared using the map method

# lst = [2, 4, 6]
# print(list(map(lambda x: x*x, lst)))

# Obtain only the even numbers from a list using the filter function

# lst = [2, 3, 7, 8]
# print(list(filter(lambda x: x % 2 == 0, lst)))

# Calculate the product of all numbers in a list using the reduce function
from functools import reduce

# product = reduce(lambda x, y: x*y, lst)
# print(product)

# Use map to create a list of lengths of each string in the original list

# lst = ['one', 'five', 'eight', 'seventeen']

# print(list(map(len, lst)))

# Remove all none values from a list using the filter method

# lst = [1, 2, None, 3, None]

# print(list(filter(None, lst)))

# Use reduce to concatenate a list of strings into a single string

#lst = ['one', 'five', 'eight', 'seventeen']

#print(reduce(lambda x, y: x + y, lst))

# Use nested generator expressions to create a flat list of numbers from a list of lists

# nested_lists = [[1, 2, 3], [4, 5], [6]]

# flat_list = (num for sublist in nested_lists for num in sublist)

# for number in flat_list:
#     print(number)

# Use a generator expression to yield each character of a string in reverse order

# str = 'Robby'

# reversed = (char for char in str[::-1])
# print(next(reversed))

# # LS's:

# string = "Hello"

# reverse_generator = (string[i] for i in range(len(string) - 1, -1, -1))

# for char in reverse_generator:
#     print(char)

# Create a generator function that yields numbers from 1 to 5

def numbers():
    for i in range(1, 6):
        yield i

# for num in numbers():
#     print(num)

# Create a generator function that yields user input strings until the word "stop" is entered.

def go_until_stop():
    while True:
        s = input("Enter a string: ")
        if s == "stop":
            break
        yield s
# for user_input in go_until_stop():
#     print(user_input)

# Create a function greet that takes three arguments: a name, a greeting, and a punctuation mark, with the punctuation defaulting to a period

def greet(name, greeting, punct='.'):
    return f"{greeting}, {name}{punct}"

# print(greet("Antonina", "Hello")) # Hello, Antonina.
# print(greet("Pete", "Good morning", "!")) # Good Morning, Pete!

# Create a function create_user that takes a username and required keyword-only arguments for email and age

def create_user(username, *, email, age):
    return {"username": username, "email": email, "age": age}

# print(create_user("Srdjan", email="srdjan@example.com", age=39))
# # {"username": "Srdjan", "email": "srdjan@example.com", "age": 39}
# print(create_user("Srdjan", "srdjan@example.com", age=39))
# # Raises an exception

# Write a function build_profile that takes a first name and a last name, and any number of keyword arguments to add to a user's profile.

def build_profile(first, last, **kwargs):
    
    return {'first_name': first, 'last_name': last} | kwargs

# print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {{'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}}

# or

def build_profile(first_name, last_name, **user_info):
    profile = {"first_name": first_name, "last_name": last_name}
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Create a function concatenate that takes any number of strings and concatenates them into a single string with a space in between.

def concatenate(*strs):
    return ' '.join(strs)

# print(concatenate("Launch", "School", "is", "great")) # Launch School is great
# print(concatenate("I", "am", "working", "on", "the", "PY130", "course")) # I am working on the PY130 course

# Write a function display_info that takes a positional-only parameter data, and keyword-only parameters reverse and uppercase.

def display_info(parameter_data, /, *, reverse=False, uppercase=False):
    if reverse and uppercase:
        return parameter_data[::-1].upper()
    if reverse:
        return parameter_data[::-1]
    if uppercase:
        return parameter_data.upper()

# print(display_info("Launch", reverse=True)) # hcnuaL
# print(display_info("School", uppercase=True)) # SCHOOL
# print(display_info("cat", uppercase=True, reverse=True)) # TAC

# Given a list with four elements, unpack these elements into four separate variables.

# lst = [10, 20, 30, 40]

# one, two, three, four = lst

# print(one)

# Unpack values from a tuple of four elements, but only keep the first and last values.

# data = (100, 200, 300, 400)

# one, *_, last = data

# Unpack the first two elements from a list and store the remaining elements in another list.

# numbers = [1, 2, 3, 4, 5, 6]

# first, second, *others = numbers

# print(others)

# Given a nested tuple data = ((1, 2), (3, 4), (5, 6)), write a code to unpack this tuple into individual variables a, b, c, d, e, f.

# data = ((1, 2), (3, 4), (5, 6))

# (a, b), (c, d), (e, f) = data

# print(a, b, c, d, e, f)

# Write a program that prints the longest sentence in a string based on the number of words. Sentences may end with periods (.), exclamation points (!), or question marks (?). You should treat any sequence of characters that are not spaces or sentence-ending characters as a word. Thus, -- should count as a word. Log the longest sentence and its word count. Pay attention to the expected output, and be sure you preserve the punctuation from the end of the sentence. Note that this problem is about manipulating and processing strings. As such, every detail about the string matters (e.g., case, punctuation, tabs, spaces, etc.).

import re

def longest_sentence(text):
    sentences = re.findall(r'\w.*?[.!?]', text)

    longest = max(sentences, key=lambda s: len(s.split()))

    print(longest + "\n")
    print(f"The longest sentence has {len(longest.split())} words.\n")

long_text = (
    'Four score and seven years ago our fathers brought forth on this '
    'continent a new nation, conceived in liberty, and dedicated to the '
    'proposition that all men are created equal. Now we are engaged in a '
    'great civil war, testing whether that nation, or any nation so '
    'conceived and so dedicated, can long endure. We are met on a great '
    'battlefield of that war. We have come to dedicate a portion of that '
    'field, as a final resting place for those who here gave their lives '
    'that that nation might live. It is altogether fitting and proper that '
    'we should do this.'
)

longer_text = long_text + (
    'But, in a larger sense, we can not dedicate, we can not consecrate, '
    'we can not hallow this ground. The brave men, living and dead, who '
    'struggled here, have consecrated it, far above our poor power to add '
    'or detract. The world will little note, nor long remember what we say '
    'here but it can never forget what they did here. It is for us the '
    'living, rather, to be dedicated here to the unfinished work which '
    'they who fought here have thus far so nobly advanced. It is rather '
    'for us to be here dedicated to the great task remaining before us -- '
    'that from these honored dead we take increased devotion to that '
    'cause for which they gave the last full measure of devotion -- that '
    'we here highly resolve that these dead shall not have died in vain '
    '-- that this nation, under God, shall have a new birth of freedom -- '
    'and that government of the people, by the people, for the people, '
    'shall not perish from the earth.'
)

def sentence_split(string):
    ENDS, LAST_LETTER = (".", "!", "?"), -1
    words = string.split()
    terminal_word_indices = []
    print(words)
    for word_index in range(len(words)):
        if words[word_index][LAST_LETTER] in ENDS:
            terminal_word_indices.append(word_index)

    for sentence_index in range(len(terminal_word_indices)):
        if sentence_index == 0:
            initial_index = 0
        else:
            initial_index = 1 + terminal_word_indices[sentence_index - 1]
        final_index = 1 + terminal_word_indices[sentence_index]

        yield words[initial_index:final_index]

def longest_sentence(text):
    result = max((sentence for sentence in sentence_split(text)), key=len)

    print(" ".join(result))
    print("")
    print(f"The longest sentence has {len(result)} words.")
    print("")

###############################################################################

# Texts and tests omitted for brevity

# longest_sentence(long_text)
# Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.
#
# The longest sentence has 30 words.

# longest_sentence(longer_text)
# # It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
# #
# # The longest sentence has 86 words.

# longest_sentence("Where do you think you're going? What's up, Doc?")
# # Where do you think you're going?
# #
# # The longest sentence has 6 words.

# longest_sentence("To be or not to be! Is that the question?")
# # To be or not to be!
# #
# # The longest sentence has 6 words.

def greet(name, /, greeting):
    print(f"{greeting}, {name}!")

# print(greet('Robby', 'yup'))

def greet(name, *names, me):
    print(name, names, me)

nums = [1, 2, 3, 4, 5]

a, *b, c = 'Hello'

from time import perf_counter
from functools import lru_cache

def time_runs(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        return_value = func(*args, **kwargs)
        print(f"The function ran in {perf_counter()-start} seconds")
        return return_value

    return wrapper

@time_runs
@lru_cache
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True

# The first function call
# is_prime(73729261)
# The function ran in 2.1655370840016985 seconds

# The second function call
# is_prime(73729261)
# The function ran in 8.330098353326321e-07 seconds

