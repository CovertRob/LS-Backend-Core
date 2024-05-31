# How can you determine whether a given string ends 
# with an exclamation mark (!)? Write some code that prints True or False 
# depending on whether the string ends with an exclamation mark.

# def ends_with_exclamation(word):
#     return word.endswith('!')

# print(ends_with_exclamation('Hello!'))

# write two ways to prepend famous words to the front of a string

famous_words = "seven years ago..."

test = "are cool"

def prepend_one(word, famous):
    return famous + word

# or

print("{} {}".format(famous_words, test))

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
