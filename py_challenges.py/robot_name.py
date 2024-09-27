'''
Problem:
    Write a program that manages robot factory settings. It needs to generate a random name when the robot is first booted up and also when it is reset to factory settings. Names cannot be repeated.

    Input: no input to Robot constructor
    Output: no direct output except to name instance variable

    Requirements:
        1. Robot class that takes no constructor arguments
            - instance variable name
            - property to generate the name properly
            - reset() method to reset the name
        2. Name generator must be able to handle name collisions with the random generator.
        3. No repeat names allowed
        4. Different robots must have different names even though they are different object instances
        5. Name must follow format: char, char, num, num, num
        6. random generator name seed uses a seed with 4 digits

    Notes on Random:
        1. Given the same seed, the generator will reproduce the same value

    Questions:
        1. Does reset need to also re-set the seed value?


Examples / Test Cases:

    1. Studying test case 'different_name_when_chosen_name_is_taken' shows that the name generator must be able to handle a repeat of the same seed for the random module and still generate a different name

    2. The regex pattern allows repeat letters and digits

Data Structures:
    Input: nothing
    Output: string
    intermediary: list to store used names

Algorithm:
    If the generator reproduces an already used name, we need to reset the state of the random generator to a new seed

    Class Structure:
        1. Set a class counter that maintains a list of all Robots and their names for collision purposes
        2. name will have a getter and setter property: the setter will perform the name generation and check for collisions
    
    name setter
        1. generate two random letters
        2. generate 3 ranodm digits between 0 and 9
        3. concatenate the letters and digits to form the robot name
        4. Check for collision, if there is, reset the generator with a new seed and re-do name generation
        5. If no collision, assign it to the name variable and add it to the class name container

    reset
        1. use the name setter to set the name to a new name

Code:
'''
import random
import string

class Robot:

    ALPHABET = string.ascii_uppercase
    NAME_HISTORY = []

    def __init__(self) -> None:
        self.name = self._generate_name()

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        while True:
            if name in Robot.NAME_HISTORY:
                random.seed()
                name = self._generate_name()
            else:
                self._name = name
                Robot.NAME_HISTORY.append(name)
                break

    def reset(self):
        Robot.NAME_HISTORY.remove(self.name)
        self.name = self._generate_name()


    def _generate_name(self):
        rand_letters = ''.join([random.choice(Robot.ALPHABET) for i in range(2)])
        rand_nums = ''.join([str(random.randint(0, 9)) for i in range(3)])
        return rand_letters + rand_nums
