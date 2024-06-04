# How can you determine whether a given string ends 
# with an exclamation mark (!)? Write some code that prints True or False 
# depending on whether the string ends with an exclamation mark.

# def ends_with_exclamation(word):
#     return word.endswith('!')

# print(ends_with_exclamation('Hello!'))

# write two ways to prepend famous words to the front of a string

# famous_words = "seven years ago..."

# test = "are cool"

# def prepend_one(word, famous):
#     return famous + word

# # or

# print("{} {}".format(famous_words, test))

# munsters_description = "the Munsters are CREEPY and Spooky."
# # => 'The munsters are creepy and spooky.'

# numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

# # two ways to reverse list without mutating original
# new_list = list(numbers.__reversed__())
# print(new_list)
# print(numbers[::-1])

# var = 10

# def function1():
#     var = 20
#     print(var)
#     # will print 20

# function1()

# try:
#     print(var) # will print 10
# except NameError:
#     print("Error occurred")

# def function2():
#     var += 5
#     print(var)

# try:
#     function2()
# except UnboundLocalError: # will print error ocurred
#     print("Error occurred")

# def function3():
#     global var
#     var += 5
#     print(var) # will print 15

# function3()
# print(var) # will print 15
