'''
Problem: Compute the scrabble score for a given word

    Letter values:
        1: A, E, I, O, U, L, N, R, S, T
        2: D, G
        3: B, C, M, P
        4: F, H, V, W, Y
        5: K
        8: J, X
        10: Q, Z
    
    How to score: sum the values of all the tiles used in each word

    Input: a string
    Output: integer score

    Requirements:
        1. Scrabble class with constructor that handles string inputs
        2. Handle \t\n etc. characters and None
        3. Create score() method
        4. Scores are case-insensitive
    
    Need to iterate through the input string, get how many times each character occurs, and then sum up all of their values into a total word score based on character count

Examples / Test Cases:
    1. Empty strings, line characters, and None produce an integer count of 0 for score()

Data Structures:
    Input: string (to get a score other than 0)
    Output: integer
    Intermediary: 
        1. dictionay to store character counts
        2. dictionary to store character values


Algorithm:

    1. GET dictionary whose keys are the characters in the input string and values are count occurence of the character in the string
    2. Iterate over character occurence dictionary keys and append matching character score * how many times it appears to a word_sum to calculate the scrabble score

Code:
'''

class Scrabble:

    LETTER_VALUES = {
        'a': 1,'e': 1,'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 'r': 1, 
        's': 1, 't': 1,'d': 2,'g': 2,'b': 3,'c': 3,'m': 3,'p': 3,'f': 4,
        'h': 4,'v': 4, 'w': 4, 'y': 4, 'k': 5,'j': 8,'x': 8, 'q': 10,
        'z': 10,
    }

    def __init__(self, word) -> None:
        self.word = word

    @classmethod
    def calculate_score(cls, input_str):
        local_scrabble = Scrabble(input_str)
        return local_scrabble.score()

    def score(self):
        char_occurrences = self._count_character_occurences(self.word)
        scrabble_score = 0
        for char in char_occurrences:
            scrabble_score += char_occurrences[char] * self.LETTER_VALUES[char]
        return scrabble_score

    def _count_character_occurences(self, input):
        char_counts = {}
        if input is None or not input.isalpha():
            return char_counts
        local_lower = input.lower()
        for char in local_lower:
            char_counts[char] = local_lower.count(char)
        return char_counts