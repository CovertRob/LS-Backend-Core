# Factory function example

def greeter(prompt):
    def add_greet(str_input):
        return prompt + str_input
    return add_greet

# name = 'Robby'

# say_hello = greeter('howdy ')
# print(say_hello(name))

# lst = ['a', 'bb', 'ccccc', 'dd']
# new_lst = sorted(lst, key=len)
# print(new_lst)

# imperitive
# lst = ['one', 'two', 'three']
# new_lst = []
# for item in lst:
#     new_lst.append(item.title())

#   # declarative
# new_lst = map(str.title, lst)
# print(list(new_lst))

from string import ascii_uppercase

def gen_example():
    for letter in ascii_uppercase:
        yield letter

# print(next(gen_example()))

names = ['jasmin ', 'robby ', 'heather']

capitalize = lambda name1, name2, name3: name1.title() + name2.title() + name3.title()

# print(capitalize(*names))

with open('exmple.txt', 'r') as file:
    for line in file:
        print(line)

