'''
Problem: Take a string of digits and return all the possible consecutive number series of a specified length in that string

    IMOW: find all substrings of a given length in the input string

    Input: string representing a number
    Output: A list containing sublists which contain the series of integers

    Requirements:
        1. Raise ValueError if there are no series of specified length available
        2. Class Series that take an string input to the constructor

Examples / Test Cases:

Data Structures:

Algorithm:

Code:
'''

class Series:

    def __init__(self, number) -> None:
        self.number = number

    def slices(self, length):
        if length > len(self.number):
            raise ValueError
        return list(map(self._single_slice_to_int, [list(self.number[i:i + length]) for i in range(len(self.number) - length + 1)]))

    def _single_slice_to_int(self, sublist):
        return [int(item) for item in sublist]