'''
Problem: 
    Create a program that manages meetup days.
    Objects in this program will represent a meetup date. Each object takes a month number (1-12) and a year (eg 2021). The meetup object then needs to be able the exact date of the meeting in the specified month and year. The user can ask something like 2nd wednesday of May 20021 and object needs to determine that for that month will occur on 12th of May, 2021.

    Input descriptors: 'first', 'second', 'third', 'fourth', 'fifth', 'last', 'teenth' (case-insensitive)
      - teenth represents those days that end in 'teenth', which is exactly 7. Each day of the week will have exactly one date that is the 'teenth' of that day in every month.
    
    Input days: 'Monday' to 'Sunday', case-insensitive

    Requirments:
        1. Must return a date object from the datetime module

Examples / Test Cases:

    1. Can take advantage of the datetime date function

    Meetup constructor
        - (year, integer day)

    day method
        - (day of week as string, descriptor as string)

Data Structures:

    Input: strings
    Output: 

Algorithm:

    a date object 

    *In a given month and year, find the N day of the week in that month*
    Methods:
        1. find day for first to fifth - note that the fifth day of the month doesn't occur every month, return None in this case
        2. find last day
        3. find teenth day

    1. for using numbered descriptors
    - iterate through the dates of the month starting from 1
        - SET descriptor counter
        - if the current day is equal to the given day of the week AND it is the N descriptor occurrence of it: return date
        - else increment the descriptor counter

    2. for using the last day descriptor
    - iterate through the dates of the month in reverse
        - return the first match to the given day of the week

    3. for use with the teenth day descriptor
    - iterate through the dates of the month starting from the thirteenth
        - if the current day is equal to the given day of the week: return date
    
Code
'''

from datetime import date
from calendar import monthrange

class Meetup:

    ISO_WEEKDAY = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

    DESCRIPTOR_T0_NUM = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5}

    def __init__(self, year, month) -> None:
        self.year = year
        self.month = month

    def day(self, day_of_week, descriptor):
        descriptor_func = self._determine_func(descriptor)
        meeting = None
        try:
            if descriptor == 'last' or descriptor == 'teenth':
                meeting = descriptor_func(self.year, self.month, day_of_week)
            else:
                meeting = descriptor_func(self.year, self.month, day_of_week, descriptor)
        except ValueError:
            return None
        return meeting

    def _determine_func(self, descriptor):

        numbered = ['first', 'second', 'third', 'fourth', 'fifth']
        if descriptor.casefold() in numbered:
            return self._numbered_descriptor
        if descriptor.casefold() == 'last':
            return self._last_day
        return self._teenth_day

    def _numbered_descriptor(self, year, month, day_of_week, descriptor):
        counter = 0
        for i in range(1, 32):
            meeting = date(year, month, i)
            if Meetup.ISO_WEEKDAY[meeting.isoweekday()] == day_of_week:
                counter += 1
                if Meetup.DESCRIPTOR_T0_NUM[descriptor] == counter:
                    return meeting
            
    # current issue: iterating backwards causes a ValueError
    def _last_day(self, year, month, day_of_week):
        beginning, end = monthrange(year, month)
        for i in range(end, beginning, -1):
            meeting = date(year, month, i)
            if Meetup.ISO_WEEKDAY[meeting.isoweekday()] == day_of_week:
                return meeting

    def _teenth_day(self, year, month, day_of_week):
        for i in range(13, 20):
            meeting = date(year, month, i)
            if Meetup.ISO_WEEKDAY[meeting.isoweekday()] == day_of_week:
                return meeting

# LS's solution:

from datetime import date, timedelta

class Meetup:
    DAY_OF_WEEK = {
        'sunday': 6,
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
    }

    SCHEDULE_START_DAY = {
        'first': 1,
        'second': 8,
        'third': 15,
        'fourth': 22,
        'fifth': 29,
        'teenth': 13,
        'last': None,
    }

    def __init__(self, year, month):
        self.year = year
        self.month = month
        if self.month == 12:
            self.days_in_month = (date(self.year + 1, 1, 1) - timedelta(days=1)).day
        else:
            self.days_in_month = (date(self.year, self.month + 1, 1) - timedelta(days=1)).day

    def day(self, weekday, schedule):
        weekday = weekday.lower()
        schedule = schedule.lower()

        first_possible_day = self.first_day_to_search(schedule)
        last_possible_day = min(first_possible_day + 6, self.days_in_month)

        day_of_week = self.DAY_OF_WEEK[weekday]

        for day in range(first_possible_day, last_possible_day + 1):
            current_date = date(self.year, self.month, day)
            if current_date.weekday() == day_of_week:
                return current_date
        return None

    def first_day_to_search(self, schedule):
        return self.SCHEDULE_START_DAY[schedule] or (self.days_in_month - 6)


