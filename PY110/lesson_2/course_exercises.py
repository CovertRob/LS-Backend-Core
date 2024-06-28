lst = [10, 9, -6, 11, 7, -16, 50, 8]

# Sort the list fist in ascending numeric order, then descending, do not mutate the list

# print(sorted(lst))
# print(sorted(lst, reverse=True))

# mutate the list

# Use sort method

# compare by string

# print(sorted(lst, key=str))

# sort dict

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def get_published_year(book):
    return int(book['published'])

# This works here because it calls the function on the
# the dictionaries when comparing
# sorted_books = sorted(books, key=get_published_year)
# print(sorted_books)

# This does not work:

# print(sorted(books, key=(int(books['published']))))

dict1 = {
    "numbers":     [41, 42],
    "coordinates": (43, 44),
    "details":     {"age": 45, "weight": 46},
    "items":       {47, 48},
    "records":     frozenset([49, 50]),
}

valid_set = {1, 2, (3, 4), frozenset([5, 6])}
# print(valid_set)    # {1, 2, (3, 4), frozenset([5, 6])}

# This will raise a TypeError since lists are not hashable and can't
# be elements of a set.
# invalid_set = {1, 2, [3, 4]}

test = frozenset([1, 2])
# print(test)

lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]

lst3 = [['abc'], ['def'], {'third': ['ghi']}]

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}

lst1[2][1][3]
lst2[1]['third'][0]
lst3[2]['third'][0][0]
dict1['b'][1]
list(dict2['3rd'].keys())[0]

# Change the value 3 to 4
lst1 = [1, [2, 3], 4]

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]

dict1 = {'first': [1, 2, [3]]}

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}

# lst1[1][1] = 4
# print(lst1)

# lst2[2] = 4
# print(lst2)

# dict1['first'][2][0] = 4
# print(dict1)

# dict2['a']['a'][2] = 4
# print(dict2)

# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }

# for name in munsters.keys():
#     print(f'{name} is a {munsters[name]["age"]}-year-old {munsters[name]["gender"]}')

# Need to use items to iterate both values and keys
# for name, info in munsters.items():
#     print(f"{name} is a {info['age']}-year-old {info['gender']}.")

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

males = [member['age'] for member in munsters.values()
                        if member['gender'] == 'male']
#print(sum(males))

# Return a new list with the same structure but with the values in each
# sublist orderd in ascending order. Use comprehension
# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# newlst = [sorted(elements) for elements in lst]
# print(newlst)

# Given following data structure, write code that defines a dictionary
# where the key is the first item in each sublist and the value is the 2nd

# lst = [
#     ['a', 1],
#     ['b', 'two'],
#     ['sea', {'c': 3}],
#     ['D', ['a', 'b', 'c']]
# ]

# newdict = {lstelements[0]:lstelements[1] for lstelements in lst}
#print(newdict)


# Sort the list so that the sub lists are ordered based on the sum of the 
# odd numbers that they contain. Dont mutate orignal list
# lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

# def sum_odd(sublist):
#     odd_numbers = [num for num in sublist if num % 2 != 0]
#     return sum(odd_numbers)
# sorted_list = sorted(lst, key=sum_odd)
# print(sorted_list)

# Return a new list identical in structure but with each number
# incremented by 1. Don't modify oriignal list.
# lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# new_list = [{key: value + 1 for key, value in dictionary.items()}
#                             for dictionary in lst]
# print(new_list)

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# return new list identical in structure but containing only
# numbers that are a multiple of 3


def divisible_by_3(sublist):
    return [num for num in sublist if num % 3 == 0]

# new_list = [divisible_by_3(sublist) for sublist in lst]
# print(new_list)
# or, possibly refactoring too much
# new_list = [[num for num in sublist if num % 3 == 0] 
#                     for sublist in lst]
# print(new_list)

# Return a list that contains the colors of the fruits and the sizes
# of the vegetables. Sizes should be uppercase, colors capitalized


dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def pick_item(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    else:
        return item['size'].upper()
# result = [pick_item(item) for item in dict1.values()]

# print(result)

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# Return a list that contains only dict's where all numbers are even

def list_is_even(input):
    return all([num % 2 == 0 for num in input])

def all_even(dictionary):
    lists_are_even = [list_is_even(list_value)
                        for list_value in dictionary.values()]
    return all(lists_are_even)

result = [dictionary for dictionary in lst 
                        if all_even(dictionary)]

# print(result)
# create a uuid with given parameters
import random

def create_uuid():
    hex_chars = '0123456789abcdef'
    sections = [8, 4, 4, 4, 12]
    uuid = []

    for section in sections:
        chars = [random.choice(hex_chars) for _ in range(section)]
        uuid.append(''.join(chars))

    return '-'.join(uuid)

#print(create_uuid())

# Create a list of every vowel (a, e, i, o, u) that appears in
# the contained strings, then print it

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# my solution: issue is when there is more than 1 vowel in the word
def check_vowel(input_string):
    vowels = 'aeiou'
    string_vowels = [chars for chars in input_string 
                                            if chars in vowels]
    return string_vowels

def list_of_vowels(input_dict):
    vowels_list = [check_vowel(elements)
                        for lists in input_dict.values()
                        for elements in lists]
    return vowels_list

# LS solution: much more concise...abs

vowels = 'aeiou'

chars = [char for key in dict1
                for word in dict1[key]
                for char in word if char in vowels]
#print(chars)
    
DATA = [
    {'one': '1', 'two': 2},
    [{'four': 5, 'three': 6}, 'three'],
    'three',
    {'2': 'two', '3': 'three'}
]

# print(DATA[1][0].get('three'))

todo_lists = [
    {
        "id": 1,
        "list_name": 'Groceries',
        "todos": [
            {"id": 1, "name": 'Bread', "completed": False},
            {"id": 2, "name": 'Milk', "completed": False},
            {"id": 3, "name": 'Apple Juice', "completed": False}
        ]
    }
]

todo_lists[0]["todos"][2].update({"name": 'Orange Juice'})
# print(todo_lists)

def even_values(lst):
    evens = []

    for value in lst:
        if value % 2 == 0:
            evens.append(value)
        lst.pop(0)

    return evens

print(even_values([1, 3, 4, 2, 4, 6, 5, 7, 9, 10, 12]))