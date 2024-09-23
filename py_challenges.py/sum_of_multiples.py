''' 
Problem: 
    Given a natural number and a set of one or more other numbers, fin dthe sum of all the multiples of the numbers in the set that are less than the first number.
    If a set of numbers is not given, use a default set of 3 and 5. 

    Input: integer
    Output: integer (sum)

    IMOW: Given an integer input, we need to sum up all the multiples that are less than that integer input based on the numbers in the given or default set.

    Requirements: 
        1. Provide default set for constructor
        2. Provide a sum_up_to(input) method to be called with the default set
        3. Provide a to(input) method to be called with a provided set

Examples / Test Cases:

    1. Given an input of 20 and the default set of 3 and 5, the multiples of 3 and 5 that are less than 20 are 3, 5, 6, 9, 10, 12, 15, 18 which equals 78

Data Structures:
    Input: integer
    Output: integer
    intermediary: set
                    list for the multiples

Algorithm:

    1. Utilize a generator function to produce the multiples up to the input upper limit
    2. return the sum of the multiples

Code:
'''

class SumOfMultiples:

    DEFAULT_SET = {3, 5}

    def __init__(self, *multiples):
        self.multiples = set(multiples)

    @classmethod
    def sum_up_to(cls, upper_limit, input=DEFAULT_SET):
        multiples = set()
        for value in input:
            multiples = multiples.union(cls._multiples_of_(value, upper_limit)) 
        return sum(multiples)

    @staticmethod
    def _multiples_of_(value, upper_limit):
        for multiple in range(value, upper_limit):
            if multiple % value == 0:
                yield multiple
    
    def to(self, upper_limit):
        return SumOfMultiples.sum_up_to(upper_limit, self.multiples)

# LS's solution to study:

# class SumOfMultiples:
#     def __init__(self, *multiples):
#         self.multiples = multiples if multiples else (3, 5)

#     def to(self, num):
#         return sum(x for x in range(1, num) if self._any_multiple(x))

#     @classmethod
#     def sum_up_to(cls, num):
#         return cls().to(num)

#     def _any_multiple(self, num):
#         return any(num % multiple == 0 for multiple in self.multiples)