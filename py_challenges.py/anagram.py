'''
Problem:
    Write a program that takes a word and a list of possible anagrams and selects the correct sub-list that contains the anagrams of the word.
    
    Anagram: a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once

    Inputs: 
        1. anagram constructor takes string input for orignal word
        2. match method takes list of strings 
    Output:
        1. sub-list containing all string or empty sub-list if no matches

    Questions:
        1. Use all original letters once? (same length)
        2. capitalization match?

Examples/Test Cases:
    Requirements:
        1. If no match, return empty list
        2. anagrams are NOT case-sensitive
        3. Must return all matching anagrams
        4. anagrams are all equal length
        5. Only single string matching not phrases
        6. The same string is not a match

Data Structures:

    Input: strings and lists
    Output: strings and lists
    intermediary: 
        1. list for iteration

Algorithm:

    SET anagrams equal to empty list
    SET anagram_ordered equal to local ordered copy of object string
    iterate through Anagram instance string and each element in the input list given via argument to match
        compare sorted element to sorted object string
        IF equal, append original element to anagrams list
    return anagrams list

Code:
'''

class Anagram:

    def __init__(self, name) -> None:
        self.object_name = name

    def match(self, strs_to_compare):
        anagrams = []
        local_sorted_object_name = sorted(self.object_name.lower())
        for element in strs_to_compare:
            # compare unsorted to check for same string match
            if element.lower() == self.object_name.lower():
                continue
            if sorted(element.lower()) == local_sorted_object_name:
                anagrams.append(element) # unsorted original
        return anagrams

