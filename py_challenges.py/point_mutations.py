''' 
Problem: Given two DNA strand inputs, calculate the hamming distance between the two strands.
    - Hamming distance: calculated by counting the number of differences between two homologous DNA strands
    - Only applies to sequences of equal length: if unequal length, calculate the Hamming distance over the shorter length

    Input: two strings representing DNA strands, can be any length including 0
    Output: Integer value representing hammming distance

    Requirements: 
        1. Handle empty string inputs
        2. handle differing length inputs by using shorter of the two
        3. Must be one to one aka point mutations differences
        4. We don't have to validate strand inputs

Examples/Test Cases:
    1. Create a DNA class
        - create a hamming_distance method: is an instance method
    2. DNA class constructor takes one input string of DNA
    3. hamming_distance method takes one string argument to compare the calling DNA strand against
    4. Strands to be compared are taken from the beginning of the two strands if one is longer

Data Structures:
    1. string
    2. integer
    3. maybe dict to store points

Algorithm:
    - GET length of strand 1
    - GET length of strand 2
    - if strand1 or strand2 is longer than the other, concatenate the longer to the same length of the shorter starting from index 0
    - SET hamming_distance counter to 0
    - iterate through both strand strings
        - if one of the points do NOT match, increment hamming_distance counter
    - return hamming_distance counter

Code:
'''

from copy import copy

class DNA:

    def __init__(self, strand) -> None:
        self.strand = strand

    
    def hamming_distance(self, strand2):
        return sum([1 for pair in zip(self.strand, strand2) if not pair[0] == pair[1]])

