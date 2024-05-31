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

# or

# print("{} {}".format(famous_words, test))

# lower case all except the first char.
# munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

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