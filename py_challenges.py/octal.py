'''
Problem: Given an octal (base 8) input string, produce a decimal output

    Input: String represnting a integer
    Output: integer in base 10 (decimal)

    Requirements:
        1. Treat invalid input as octal 0
        2. Valid octal numbers are 0-7 inclusive

    Questions: 
        1. What does octal 0 actually mean?: invalid inputs will produce an integer value of 0

Examples / Test Cases:
    1. We are converting from base-8 to base-10 so the outputs are always going to be less than the input

    Format:
    233 # decimal
    2*10^2 + 3*10^1 + 3*10^0
    2*100  + 3*10   + 3*1 = 233
    Follow same format but where the 10's are 8's for base-8 notation

    We can see that 233 in base 10 is equal to 155 in base 8

    We are actually performing a transformation on the numbers here

    Use the following:
    1. map function
    2. lambda
    3. unpack string

    - 130 examples
    - 1*10^2 + 3*10^1 + 0 = 130
    - 1*8^2  + 3*8^1 + 0 = 64 + 24 = 88
    - 8*8^1 + 8*8^0 = 72
    - 8*10^1 + 8*10^0 = 88

Data Structures:
    Input: string
    Output: integer
    intermediary: strings

Algorithm:
    1. We are starting off with a number in base-8 so we first need to produce the number value in base-8


Code:

1. Forced myself to utilize map with a callback
'''

class Octal:

    def __init__(self, num):
        self.num = num

    def to_decimal(self):
        invalid = ['8', '9']
        for digit in self.num:
            if digit in invalid or not digit.isdigit():
                return 0
        converted_places = []
        places_and_values = [(int(place), int(digit)) for place, digit in enumerate(self.num[::-1])]
        converted_places = map(self._raise_value_to_power_of_8, places_and_values)
        return sum(converted_places)


    def _raise_value_to_power_of_8(self, pair):
        place, digit = pair
        return digit * (8 ** place)


