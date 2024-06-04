# How can you determine whether a given string ends 
# with an exclamation mark (!)? Write some code that prints True or False 
# depending on whether the string ends with an exclamation mark.

# def ends_with_exclamation(word):
#     return word.endswith('!')

# print(ends_with_exclamation('Hello!'))

# write two ways to prepend famous words to the front of a string

# famous_words = "seven years ago..."
# famous_words = "seven years ago..."

# test = "are cool"
# test = "are cool"

# def prepend_one(word, famous):
#     return famous + word
# def prepend_one(word, famous):
#     return famous + word

# # or

# print("{} {}".format(famous_words, test))
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

# print (munsters_description.capitalize())

# letter swap
# munsters_description = "The Munsters are creepy and spooky."

# print(munsters_description.swapcase())

# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."
# word = 'Dino'
# print(word in str1)
# print('Dino' in str2)

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

# flintstones.append("Dino")
# flintstones.extend(['Dino', 'Hoppy'])

# advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

# print(advice[:advice.rfind('house')])
# # or
# print(advice.split("house")[0])

# advice = "Few things in life are as important as house training your pet dinosaur."

# print(advice.replace('important', 'urgent'))