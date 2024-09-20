'''
Problem: Write some code that converts modern decimal numbers into their Roman number equivalents.

    Input: integer
    Output: string (numeral)

Numerals: 
    I - 1
    V - 5
    X - 10
    L - 50
    C - 100
    D - 500
    M - 1000

Requirements: 
    1. No need to convert numbers larger than 3000
    2. Written by expressing each digit separately starting with left most digit and skipping any digit with a value of zero
    3. Create class whose constructor takes integer value and has instance method to_roman()


Examples/Test Cases:

- 1000 = M
- 900 = CM
- 90 = XC
- 1990 = MCMXC
- 2008 = MMVIII

Data Structures:
    - Dict: to store the numeral value pairs
    - string: for the output numeral
    - integer: for the input number
Algorithm:

SET class constant containing numeral/value pairs

- SET input integer to a string
- split string into place value eg thousands place = 1000, hundreds place = 100 etc
    - place these values into a dictionary with value of index number
- SET numeral string to return
- Iterate over place values list and concatenate to string respective numeral representation

Code:
'''


class RomanNumeral:
    def __init__(self, number):
        self.number = number

    ROMAN_NUMERALS = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    def to_roman(self):
        roman_version = ""
        to_convert = self.number

        for key, value in self.ROMAN_NUMERALS.items():
            multiplier, remainder = divmod(to_convert, value)
            # print(multiplier, remainder)
            if multiplier > 0:
                roman_version += key * multiplier
            to_convert = remainder

        return roman_version
    
# class RomanNumeral:

#     NUMERALS = {
#         1: 'I',
#         5: 'V',
#         10: 'X',
#         50: 'L',
#         100: 'C',
#         500: 'D',
#         1000: 'M',
#     }

#     def __init__(self, num) -> None:
#         self.number = num

#     def to_roman(self):
#         pass

#     def _place_to_numeral(self, place_tuple):
#         if int(place_tuple[0]) == 0 and 1 <= int(place_tuple[1]) < 5:
#             return 'I' * int(place_tuple[1])
#         elif int(place_tuple[0]) == 0 and 5 <= int(place_tuple[1]) < 10:
#                 return 'V'
#         elif int(place_tuple[0]) == 1 and 1 <= int(place_tuple[1]) < 5:
#              return 'X'
#         elif int(place_tuple[0]) == 1 and 5 <= int(place_tuple[1]) <= 9:
#              return 'L'
#         elif int(place_tuple[0]) == 2 and  1 <= int(place_tuple[1]) < 5:
#              return 'C'
#         elif int(place_tuple[0]) == 2 and 5 <= int(place_tuple[1]) <= 9:
#              return 'D'
#         elif int(place_tuple[0]) == 3:
#              return 'M' * int(place_tuple[1])
#         return 'NA'
            
        


#     def _count_places(self):
#         place_counts = {}
#         for place, integer in enumerate(str(self.number)[::-1]):
#             place_counts[place] = integer
#         return place_counts