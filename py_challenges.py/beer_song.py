'''
Problem: Given a range of verses or verse number, generate the respective verse of the 99 Bottles of Beer song.
    Input: integer, either 1 integer or two integers providing a range (inclusive)
    Output: the verse/s

    Requirements: 
        1. Create a BeerSong class with:
            - verse() class method: one argument, a number
            - verses() class method: two arguments, first argument should be greater than the second because the beer song is descending
            - lyrics() class method which produces the entire song
        2. The entire lyrics have 100 verses
        3. return a string
        4. Handle bottle and bottles
        5. Handle take one and take it for 1 bottle

    Questions:

Examples / Test Cases:
    1. Each output verse ends with a \n character
    2. When outputting multiple verses, there is a \n character between them

Data Structures:
    Input: integer/s
    Output: string
    intermediary: string and lists for manipulation purposes

Algorithm:

    1. verse
        - use regex to match X positions in BEER_VERSE verse format
        - replace X's in first line with input integer
        - replace X in second line and replace with minus 1 of input integer
        - set 'bottles' to singular if it is 1 bottle, plural otherwise

    2. verses

    3. lyrics

    SET plural beers on the wall string constant for first part of verse
    SET singular beer on the wall string constant for first part of verse
    SET

    *Use regex to replace plural or singular beer?*


Code:
'''

# import re as re
# from copy import copy

# class BeerSong:

#     BEER_VERSE = "99 bottles of beer on the wall, 99 bottles of beer.\nTake one down and pass it around, 98 bottles of beer on the wall.\n"

#     BEER_ZERO_VERSE = "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n"

#     BEER_ONE_VERSE = "1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n"

#     DEFAULT_VERSE = "X bottles of beer on the wall, X bottles of beer.\nTake one down and pass it around, X bottles of beer on the wall.\n"

#     @classmethod
#     def verse(cls, beers_verse):
#         if beers_verse == 99:
#             return cls.BEER_VERSE
#         if beers_verse == 0:
#             return cls.BEER_ZERO_VERSE
#         if beers_verse == 1:
#             return cls.BEER_ONE_VERSE
#         number_spots = re.finditer(r'(X)', cls.DEFAULT_VERSE, flags=re.M)
#         corrected_verse = copy(cls.DEFAULT_VERSE)
        
#         for i in range(3):
#             match = next(number_spots)
#             if i == 2:
#                 corrected_verse = corrected_verse[:match.start()] + f"{beers_verse - 1}" + cls.DEFAULT_VERSE[match.end():]
#             elif i == 1:
#                 corrected_verse = corrected_verse[:match.start()+1] + str(beers_verse) + corrected_verse[match.end():]
#             else:    
#                 corrected_verse = corrected_verse[:match.start()] + str(beers_verse) + corrected_verse[match.end():]
#         return corrected_verse
    
# # current issues: indexes don't match correctly with single digit beers - change back to X generic constant to solve?

#     @classmethod
#     def verses(cls, start_verse, end_verse):
#         generated_lines = '\n'.join([cls.verse(num_verse) for num_verse in range(start_verse, end_verse-1, -1)])
        
#         return generated_lines


#     @classmethod
#     def lyrics(cls):
#         pass

class BeerSong:
    @classmethod
    def verse(cls, number):
        if number > 1:
            return f"{number} bottles of beer on the wall, {number} bottles of beer.\n" \
                   f"Take one down and pass it around, {number - 1} bottle{'s' if number - 1 > 1 else ''} of beer on the wall.\n"
        elif number == 1:
            return "1 bottle of beer on the wall, 1 bottle of beer.\n" \
                   "Take it down and pass it around, no more bottles of beer on the wall.\n"
        else:
            return "No more bottles of beer on the wall, no more bottles of beer.\n" \
                   "Go to the store and buy some more, 99 bottles of beer on the wall.\n"

    @classmethod
    def verses(cls, start, end):
        return '\n'.join(BeerSong.verse(i) for i in range(start, end - 1, -1))

    @staticmethod
    def lyrics():
        return BeerSong.verses(99, 0)

# LS's solution:

# class Verse:
#     def __init__(self, bottles):
#         self.bottles = bottles

#     def single_verse(self):
#         if self.bottles == 0:
#             return self._zero_bottle_verse()
#         elif self.bottles == 1:
#             return self._single_bottle_verse()
#         elif self.bottles == 2:
#             return self._two_bottle_verse()
#         else:
#             return self._default_verse()

#     def _default_verse(self):
#         return (
#             f"{self.bottles} bottles of beer on the wall, {self.bottles}"
#             f" bottles of beer.\nTake one down and pass it around, "
#             f"{self.bottles - 1} bottles of beer on the wall.\n"
#         )

#     def _two_bottle_verse(self):
#         return (
#             "2 bottles of beer on the wall, 2 bottles of beer.\n"
#             "Take one down and pass it around, 1 bottle of beer "
#             "on the wall.\n"
#         )

#     def _single_bottle_verse(self):
#         return (
#             "1 bottle of beer on the wall, 1 bottle of beer.\n"
#             "Take it down and pass it around, no more bottles of beer "
#             "on the wall.\n"
#         )

#     def _zero_bottle_verse(self):
#         return (
#             "No more bottles of beer on the wall, no more bottles "
#             "of beer.\nGo to the store and buy some more, 99 bottles "
#             "of beer on the wall.\n"
#         )

# class BeerSong:
#     @classmethod
#     def verse(cls, number):
#         return Verse(number).single_verse()

#     @classmethod
#     def verses(cls, start, stop):
#         result = []
#         current_verse = start
#         while current_verse >= stop:
#             result.append(cls.verse(current_verse))
#             current_verse -= 1
#         return "\n".join(result)

#     @classmethod
#     def lyrics(cls):
#         return cls.verses(99, 0)