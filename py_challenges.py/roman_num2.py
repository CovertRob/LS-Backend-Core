'''
Problem:
    Write a program that converts decimal numbers into their roman number equivalents

    Input: integer into RomanNumeral constructor
    Output: string representing the input number

    Requirements:
    1. No need to convert numbers larger than 3000


Examples / Test Cases:
    Letters:
    I - 1
    V - 5
    X - 10
    L - 50
    C - 100
    D - 500
    M - 1000

    Example:
    1990 is MCMXC
    - 1000 = M
    - 900 = CM
    - 90 = XC

Data Structures:

Algorithm:

*Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero.

*If it is one less than the next level we subtract*

iterate through each number place in the input number
    - find how many times each place digit roman numeral equivalent divides into the number
    - append the divided amount times the roman numeral character to the final roman numeral
    - 

v2
split input digit into individual places padded with 0's
1000, 900, 90


Code:
'''

class RomanNumeral:

    NUMERALS = {1: 'I', 
                4: 'IV', 
                5: 'V', 
                9: 'IX', 
                10: 'X', 
                40: 'XL', 
                50: 'L', 
                90: 'XC', 
                100: 'C', 
                400: 'CD', 
                500: 'D', 
                900: 'CM', 
                1000: 'M'}

    def __init__(self, num) -> None:
        self.number = num

# both my versions don't work because we have to use the remainder to get the one's place correct in the end
    def to_roman(self):
        sub_nums = (int(num) for num in self._get_sub_numbers(self.number))
        roman_num = ''
        current_number = next(sub_nums)
        for key, value in reversed(self.NUMERALS.items()):
            multiplier, remainder = divmod(current_number, key)
            if multiplier > 0:
                roman_num += value * multiplier
                try:
                    current_number = next(sub_nums)
                except StopIteration:
                    if remainder > 0:
                        roman_num += self.NUMERALS[1] * remainder
                    break
        
        return roman_num

    def _get_sub_numbers(self, number):
        str_as_num = str(number)
        sub_numbers = []
        for i in range(len(str_as_num)-1):
            zero_pad, remainder = divmod(int(str_as_num[i:]), 10)
            if zero_pad == 0:
                sub_numbers.append(remainder)
                break
            sub_numbers.append(str_as_num[i] + ('0' * len(str(zero_pad))))
        return sub_numbers

test = RomanNumeral(93)
print(test.to_roman())
    # def to_roman(self):
    #     sub_nums = (int(num) for num in self._get_sub_numbers(self.number))

    #     roman_num = ''
    #     value = next(sub_nums)
    #     for roman_value in reversed(self.NUMERALS.keys()):
    #         amount_pad = value // roman_value
    #         if amount_pad != 0:
    #             roman_num += self.NUMERALS[roman_value] * (amount_pad)
    #             try:
    #                 value = next(sub_nums)
    #             except StopIteration:
    #                 break

    #     return roman_num
