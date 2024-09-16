'''
Write a program to determine whether a triangle is equilateral, isosceles, or scalene

An equilateral triangle has all three sides the same length
An isosceles triangle has exactly two sides of the same length
A scalene triangle has all sides of different lengths

Triangle: all sides of length > 0, sum of the lengths of any 2 sides must be greater than the length of the third side

Problem: Given an input of 3 integers to define triangle side lengths, we need to determine if the triangle is equilaterial, isosceles, or scalene
    Input: 3 integers
    Output: a 'kind' property that outputs a string classifying the triangle based on the integers inputs
    Requirements: float length sides, ValueError if wrong input, no negative inputs, satisfy length input requirement for any 2 sides

Examples/Test cases:
 - (3, 4, 4) is isosceles: two of the sides have to be equal
 - Must be able to satisfy float lengths for the sides
Data Structures:
    - integers
    - strings
    - 

Algorithm:

    Constructor:
    1. Save the three side lengths
    2. Check whether any sid elength is less than or equal to 0, if so raise an exception
    3. Use comparisons to determine whether the sum of any two side lengths is less than or equal to the length of the third side. If so, raise an exception.

    kind:
    1. Compare the values representing the three side lengths
    2. If all three side lengths are equal return 'equilateral'
    3. If the triangle is not equilateral, but any two side lengths are equal to one another, return 'isosceles'.
    4. If none of the side lengths are equal to one another, return 'scalene'.

'''

class Triangle:

    def __init__(self, s1, s2, s3) -> None:
         self.sides = (s1, s2, s3)

    @property
    def sides(self):
         return self._sides
    
    @sides.setter
    def sides(self, lengths):
         # validate input here
         s1, s2, s3 = lengths
         if not all(side > 0 for side in lengths):
              raise ValueError
         if s1 + s2 <= s3:
              raise ValueError
         if s2 + s3 <= s1:
              raise ValueError
         if s1 + s3 <= s2:
              raise ValueError
         self._sides = (s1, s2, s3)
    
    @property
    def kind(self):
        if len(set(self.sides)) == 1:
            return "equilateral"
        elif len(set(self.sides)) == 2:
            return "isosceles"
        else:
            return "scalene"