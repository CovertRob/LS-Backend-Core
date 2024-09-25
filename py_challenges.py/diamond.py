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

    1. Dictionary to hold space values with letters

Algorithm:

Code:
'''

import string

class Diamond:

    ALPHABET = list(string.ascii_uppercase)

    @classmethod
    def make_diamond(cls, letter):
        diamond = ""
        alphabet = cls._generate_letter()
        current = next(alphabet)
        spaces = 3
        while current <= letter:
            
            if current == 'A':
                diamond += "A\n"
            elif current == 'B':
                diamond += "B B\n"
            else: 
                diamond += f"{current}{' ' * spaces}{current}\n"
            spaces += 2
            current = next(alphabet) 
        return diamond

# Current issue: how do I correctly pad the beginning letters without knowing the end character length? Need to generate full characters ahead of time?

# What about a list and then use '\n'.join() ?

    @classmethod
    def _generate_letter(cls):
        for letter in cls.ALPHABET:
            yield letter

print(Diamond.make_diamond('E'))

