'''
Problem: Write a program that can tell whether a number is perfect, abundant, or deficient

    Classification is based on a comparision between the number and the sum of its positive divisors: the numbers that can be evenly divided into the target number with no remainder, excluding the number itself.

    Aliquot sum: the sum of the positive divisors excluding the target number
        1. Perfect: sum equals the original number
        2. Abundant: sum is greater than the original number
        3. Deficient: sum less than the original number

    Requirements:
        1. Divisors to sum must evenly divide with no remainder
        2. Do not include the number itself as a divisor
        3. Create PerfectNumber class with no constructor and classify method that takes integer input
        4. Raise ValueError if input is not a positive integer

    Input: integer
    Output: perfect, abundant, or deficient string value

    Rules
        1. When finding divisors, any number greater than half the target number won't divide evenly with no remainder: use floor division
        2. How can I use a lambda in this? A callback?
            - use filter to computer divisors

Examples / Test Cases:

    1. 6 is perfect because divisors are 1, 2, 3: 1 + 2 + 3 = 6
    2. Prime numbers are always deficient
    2. 1 is always a divisor

Data Structures:
    1. input: integer
    2. output: string
    3. intermediary: integer

Algorithm:

    1. SET list equal to all positive divisors for target number
    2. return classification based on divisor list sum

Code:

Used:
    1. generator
    2. lambda
    3. filter function
'''

class PerfectNumber:

    def __init__(self) -> None:
        pass

    @classmethod
    def classify(cls, natural_number):
        try:
            even_divisors = cls._get_even_divisors(natural_number)
            divisor_sum = sum(even_divisors)
            if divisor_sum == natural_number:
                return 'perfect'
            if divisor_sum > natural_number:
                return 'abundant'
            return 'deficient'
        except ValueError as e:
            raise

    @staticmethod
    def _get_even_divisors(input):
        if not input > 0:
            raise ValueError("Input must be a positive integer")
        possible_even_divisors = (num for num in range(1, (input//2)+1))
        even_divisors = filter(lambda divisor: input % divisor == 0, possible_even_divisors)
        return list(even_divisors)