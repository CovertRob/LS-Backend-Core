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

import re as re
from copy import copy

class BeerSong:

    BEER_VERSE = "99 bottles of beer on the wall, 99 bottles of beer.\nTake one down and pass it around, 98 bottles of beer on the wall.\n"

    BEER_ZERO_VERSE = "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n"

    BEER_ONE_VERSE = "1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n"

    @classmethod
    def verse(cls, beers_verse):
        if beers_verse == 99:
            return cls.BEER_VERSE
        if beers_verse == 0:
            return cls.BEER_ZERO_VERSE
        if beers_verse == 1:
            return cls.BEER_ONE_VERSE
        number_spots = re.finditer(r'(\d\d)', cls.BEER_VERSE, flags=re.M)
        corrected_verse = copy(cls.BEER_VERSE)
        for i in range(3):
            match = next(number_spots)
            if i == 2:
                corrected_verse = corrected_verse[:match.start()] + str(beers_verse-1) + corrected_verse[match.end():]
            else:    
                corrected_verse = corrected_verse[:match.start()] + str(beers_verse) + corrected_verse[match.end():]
        return corrected_verse
    
# current issues: indexes don't match correctly with single digit beers - change back to X generic constant to solve?

    @classmethod
    def verses(cls, start_verse, end_verse):
        generated_lines = '\n'.join([cls.verse(num_verse) for num_verse in range(start_verse, end_verse-1, -1)])
        
        return generated_lines


    @classmethod
    def lyrics(cls):
        pass

print(BeerSong.verses(15, 11))