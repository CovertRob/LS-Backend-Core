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