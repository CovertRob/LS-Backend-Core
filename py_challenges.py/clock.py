'''
1. addition and subtraction operations are done in minutes
2. at method first arg is hours second arg is minutes
3. Do not mutate with arithmetic operations -- create a new Clock object
4. Clock is treated in 24hr format
'''


class Clock:

    def __init__(self, time = '00:00') -> None:
        self.time = time

    @classmethod
    def at(cls, hours='00', minutes='00'):
        return Clock(f"{hours:02}:{minutes:02}")

    def __str__(self) -> str:
        return self.time

    def __add__(self, other):
        hours_in_minutes = int(self.time[:2]) * 60
        minutes = int(self.time[3:])
        new_total_minutes = (minutes + hours_in_minutes) + other
        total_hours, total_minutes = divmod(new_total_minutes, 60)

        hour_hand = divmod(total_hours, 24)
        return Clock.at(hour_hand[1], total_minutes)


    def __sub__(self, other):
        hours_in_minutes = int(self.time[:2]) * 60
        minutes = int(self.time[3:])
        new_total_minutes = (minutes + hours_in_minutes) - other
        total_hours, total_minutes = divmod(new_total_minutes, 60)

        hour_hand = divmod(total_hours, 24)
        return Clock.at(hour_hand[1], total_minutes)

    def __eq__(self, other) -> bool:
        return self.time == other.time
    
