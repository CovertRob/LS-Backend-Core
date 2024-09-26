'''
Problem: Given an input letter, output it in a diamond shape. It prints a diamond starting with 'A', with the supplied letter at the widest point.

    Input: single letter as string
    Output: multi-line string forming a diamond

    Requirements:
        1. The first row contains one A
        2. The lat row contains one A
        3. All rows, except the first and last, have exactly two identical letters
        4. The diamond is horizontally and vertically symmetric
        5. Has a square shape: width equals height
        6. Top half: ascending order
        7. Bottom half: descending order

Examples / Test Cases:

    1. Each line ends with a newline character
    2. Line one is centered, line 2 has one space, each space after has n + 2 spaces where n is the spaces in the line before

Data Structures:

    1. Find the max width of the diamond to be created, each line must be this long

Algorithm:

Code:
'''

import string

class Diamond:

    ALPHABET = list(string.ascii_uppercase)

    @classmethod
    def make_diamond(cls, letter):
        if letter == 'A':
            return "A\n"
        diamond = ""
        diamond_size = cls._get_diamond_size(letter)

        for char in cls.ALPHABET[:cls.ALPHABET.index(letter) + 1]:
            if char == 'A':
                diamond += 'A'.center(diamond_size)
                diamond += '\n'
            else:
                letter_pad = cls._get_diamond_size(char)
                diamond += f"{char}{(letter_pad - 2) * ' '}{char}".center(diamond_size)
                if char != letter: diamond += "\n"

        return (diamond + ''.join(reversed('\n' + diamond[:diamond.index(letter)])))

    # used to compute both max diamond size and individual letter pad size
    @staticmethod
    def _get_diamond_size(letter):
        if letter == 'A':
            return 1
        if letter == 'B':
            return 3
        return (Diamond.ALPHABET.index(letter)) * 2 + 1