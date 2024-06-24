# Function that can multiply elements in a list by an arbitrary number.

def multiply(input_list, num):
    for index in range(len(input_list)):
        input_list[index] *= num
    return input_list

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]

fruits = ("apple", "banana", "cherry", "date", "banana")

# Count the number of occurrences of banana in the tuple

def count_matches(input_tup, match):
    num_matches = 0
    for word in input_tup:
        if word == match:
            num_matches += 1
    return num_matches

# print(count_matches(fruits, "banana"))
# or use built in count method for tuples


# numbers = {1, 2, 3, 4, 5, 5, 4, 3}
# print(len(numbers)) # -> 5

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# obtain all unique values from both sets
# print(a | b) # or a.union(b)

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
# for index, name in enumerate(names):
#     name_positions[name] = index
# print(name_positions)

# prints out a dictionary w/ indexes

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

# calculate the total age from above dict

def calc_total_value(dict):
    total_value = 0
    for value in dict.values():
        total_value += value
    return total_value

# print(calc_total_value(ages))

# or use sum(ages.values())

# determine minimum ages from above dict

# print(min(ages.values()))

statement = "The Flintstones Rock"

# print dict that contains frequency of each character, case sensitive

def char_frequency(input_string):
    freq_dict = {}
    input_string = input_string.replace(' ', '')
    for char in input_string:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

# print(char_frequency(statement))

dictionary = {'a': 'ant', 'b': 'bear'}
# print(dictionary.popitem())
#print(dictionary.pop())
# popitem can only remove last key-value pair in dict
# pop can remove any item from dict if you specify key


# print(list.pop())

dict = {'x': 1}

# print('x' in dict)
# print('x' in dict.keys())
# print(dict.get('x'))

my_dict = {}
#my_dict.append('fruit', 'apple')

def less_than(upper_limit):
    numbers = []

    for candidate in range(1, upper_limit):
        numbers.append(candidate)

    return numbers

# print(less_than(1))
test = list(range(1, 1))
print(test)
