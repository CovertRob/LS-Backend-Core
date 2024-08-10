# Practice exercises contained in the OO with Python book
'''
How do we create a class and an object in Python?

Write a program that defines a class and creates two objects from that class. The class should have at least one instance variable that gets initialized by the initializer.

What class you create doesn't matter, provided it satisfies the above requirements.
'''

#. We create a class and an object in Python by using an instantation construtor

class Motorcycle():

    def __init__(self, engine):
        self.engine = engine
        type_name = self.__class__.__name__
        print(f"This is a {engine} size {type_name}")

# supermini = Motorcycle('112')
# big_bike = Motorcycle('250')

# Given an instance of a Foo object, show two ways to print I am a Foo object without hardcoding the word Foo.

# you can use an F string and use foo.__class__.__name__ or do type(self).__name__

class Foo:
    pass

# foo = Foo()
# print(f'I am a {type(foo).__name__} object')
# print(f'I am a {foo.__class__.__name__} object')

# Example of using property decorators:
# Added in print statements to visualize what is happening:

class GoodDog:

    def __init__(self, name, age):
        self.name = name
        print("Init in action")
        self.age = age

    def speak(self):
        return f'{self.name} says arf!'

    @property
    def name(self):
        print('NAME GETTER IN ACTION')
        return self._name

    @name.setter
    def name(self, name):
        print('NAME SETTER IN ACTION')
        if not isinstance(name, str):
            raise TypeError('Name must be a string')

        self._name = name
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError('Age must be an integer')

        if age < 0:
            raise ValueError("Age can't be negative")

        self._age = age

# sparky = GoodDog('Sparky', 5)
# print(sparky.name)          # Sparky
# print(sparky.age)           # 5
# sparky.name = 'Fireplug'

# print(sparky.name)          # Fireplug
# sparky.age = 6

# # print(sparky._name)
# # print(sparky.name)

# print(sparky.age)           # 6

# sparky.name = 42  # TypeError: Name must be a string

# sparky.age = -1   # ValueError: Age can't be negative

# Create a Car class with the listed requirements

class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self.speed = 0
    
    @classmethod
    def gas_mileage(cls, gallons, miles):
        mileage = miles / gallons
        print(f'{mileage} miles per gallon')

    def engine_start(self):
        print('The engine is on!')

    def engine_off(self):
        self.speed = 0
        print("Let's park this baby")
        print("The engine is off")

    def speed_up(self, number):
        self.speed += number

    def brake(self, number):
        self.speed -= number
    
    def get_speed(self):
        print(f'Your speed is {self.speed} mph')

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, paint):
        self._color = paint

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year
    
    def spray_paint(self, paint):
        self.color = paint
        print(f'Your {paint} paint job looks great!')


# lumina = Car('chevy lumina', 1997, 'white')
# lumina.engine_start() # The engine is on!
# lumina.get_speed()    # Your speed is 0 mph.
# lumina.speed_up(20)   # You accelerated 20 mph.
# lumina.get_speed()    # Your speed is 20 mph.
# lumina.speed_up(30)   # You accelerated 30 mph.
# lumina.get_speed()    # Your speed is 50 mph.
# lumina.brake(15)      # You decelerated 15 mph.
# lumina.get_speed()    # Your speed is 35 mph.
# lumina.brake(30)      # You decelerated 30 mph.
# lumina.get_speed()    # Your speed is 5 mph.
# lumina.engine_off()   # Let's park this baby!
#                       # The engine is off
# lumina.get_speed()    # Your speed is 0 mph.
    
# print(f'My car is {lumina.color}.')
# # My car is white.

# print(f"My car's model is a {lumina.model}.")
# # My car's model is a chevy lumina.

# print(f"My car's year is {lumina.year}.")
# # My car's year is 1997.

# lumina.color = 'brown'
# print(f'My car is now {lumina.color}.')
# # My car is now brown.

# lumina.year = 2023
# AttributeError: property 'year' of 'Car' object
# has no setter

# lumina.spray_paint('pink')
# print(lumina.color)

#Car.gas_mileage(13, 351)

class Person:

    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name)

    @property
    def name(self):
        first_name = self._first_name.title()
        last_name = self._last_name.title()
        return f'{first_name} {last_name}'

    @name.setter
    def name(self, name):
        first_name, last_name = name
        self._set_name(first_name, last_name)

    @classmethod
    def _validate(cls, name):
        if not name.isalpha():
            raise ValueError('Name must be alphabetic.')

    def _set_name(self, first_name, last_name):
        Person._validate(first_name)
        Person._validate(last_name)
        self._first_name = first_name
        self._last_name = last_name

# Possibly make turn engine on instance method a static method because it doesn't technically modify the object state

# Magic method exercises

# 1. Create a Car class that makes the following code work as indicated:

class Car:

    def __init__(self, make, year, color) -> None:
        self._make = make
        self._year = year
        self._color = color

    def __str__(self) -> str:
        return f"{self._color.title()} {self._year} {self._make}"
        
    def __repr__(self) -> str:
        return f"Car({repr(self._make)}, {repr(self._year)}, {repr(self._color.title())})"

# vwbuzz = Car('ID.Buzz', 2024, 'red')
# print(vwbuzz)        # Red 2024 ID.Buzz
# print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

import math

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        dot_product = ((self.x * other.x) +
                        (self.y * other.y))
        return dot_product

    def __abs__(self):
        sum_of_squares = ((self.x ** 2) +
                          (self.y ** 2))
        return math.sqrt(sum_of_squares)

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

# v1 = Vector(5, 12)
# v2 = Vector(13, -4)
# print(v1 - v2) # Vector(-8, 16)
# print(v1 * v2) # 17
# print(abs(v1)) # 13.0

# 3. Challenge: create the class to make the below work as shown:

class Candidate:

    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        self.votes += other
        return self

class Election:

    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        max_votes = 0
        vote_count = 0
        winner = None

        for candidate in candidates:
            vote_count += candidate.votes
            if candidate.votes > max_votes:
                max_votes = candidate.votes
                winner = candidate.name

        for candidate in candidates:
            name = candidate.name
            votes = candidate.votes
            print(f'{name}: {votes} votes')

        percent = 100 * (max_votes / vote_count)
        print()
        return f'{winner} won: {percent}% of votes'
        

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

# election = Election(candidates)
# print(election.results())

# Inheritance exercises

"""
First Class	Second Class
Car	Engine : has a
Teacher	Student : has a
Flag	Color : has a
Apple	Orange : neither
Ship	Vessel : is a
Structure	Home : can be both
Shape	Circle : is a
"""

# Write the code needed to make the following code work as shown:

class Vehicle:
    number_of_vehicles = 0

    def __init__(self):
        Vehicle.number_of_vehicles += 1 # cannot use self here otherwise it'll create a new number_of_vehicles var in each instance and never increment it because self of the subclasses don't have this

    @classmethod
    def vehicles(cls):
        return Vehicle.number_of_vehicles
    
class TurnSignalsMixin:

    def signal_left(self):
        print('Signalling left')

    def signal_right(self):
        print('Signalling right')

    def signal_off(self):
        print('Signal is now off')

class Car(TurnSignalsMixin, Vehicle):

    def __init__(self):
        super().__init__()

class Truck(TurnSignalsMixin, Vehicle):

    def __init__(self):
        super().__init__()

class Boat(Vehicle):

    def __init__(self):
        super().__init__()

# print(Car.vehicles())     # 0
# car1 = Car()
# print(Car.vehicles())     # 1
# car2 = Car()
# car3 = Car()
# car4 = Car()
# print(Car.vehicles())     # 4
# truck1 = Truck()
# truck2 = Truck()
# print(Truck.vehicles())   # 6
# boat1 = Boat()
# boat2 = Boat()
# print(Boat.vehicles())    # 8

# car1.signal_left()       # Signalling left
# truck1.signal_right()    # Signalling right
# car1.signal_off()        # Signal is now off
# truck1.signal_off()      # Signal is now off
# boat1.signal_left()
# AttributeError: 'Boat' object has no attribute
# 'signal_left'

# print(Car.mro())
# print(Truck.mro())
# print(Boat.mro())
# print(Vehicle.mro())

class Vehicle:
    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg


class Car(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def family_drive(self):
        print('Taking the family for a drive')

class Truck(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def hookup_trailer(self):
        print('Hooking up trailer')

# car = Car(12.5, 25.4)
# truck = Truck(150.0, 6.25)

# print(car.max_range_in_miles())         # 317.5
# print(truck.max_range_in_miles())       # 937.5

# car.family_drive()     # Taking the family for a drive
# truck.hookup_trailer() # Hooking up trailer

# try:
#     truck.family_drive()
# except AttributeError:
#     print('No family_drive method for Truck')
# # No family_drive method for Truck

# try:
#     car.hookup_trailer()
# except AttributeError:
#     print('No hookup_trailer method for Car')
# # No hookup_trailer method for Car

class Cat:
    def __init__(self) -> None:
        pass

# whiskers = Cat()
# ginger = Cat()
# paws = Cat()

# print(whiskers == ginger)

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.sound())

    def sound(self):
        return f'{self.name} says '

class Cow(Animal):
    def sound(self):
        return super().sound() + 'moooooooooooo!'

# daisy = Cow('Daisy')
# daisy.speak()

# Create the Person class to make the below code work

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    @name.setter
    def name(self, name):
        parts = name.split()
        self.first_name = parts[0]
        if len(parts) > 1:
            self.last_name = parts[1]
        else:
            self.last_name = ''

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name


# bob = Person('bob')
# print(bob.name)           # bob
# bob.name = 'Robert'
# print(bob.name)           # Robert

# modify the Person class to facilitate the below methods

# bob = Person('Robert')
# print(bob.name)             # Robert
# print(bob.first_name)       # Robert
# print(repr(bob.last_name))  # ''
# bob.last_name = 'Smith'
# print(bob.name)             # Robert Smith

# 3. Add a new setter property for name that takes either a first name or full name, and knows how to set the first_name and last_name properties appropriately. Use the following code to test your code:

# bob = Person('Robert')
# print(bob.name)             # Robert
# print(bob.first_name)       # Robert
# print(repr(bob.last_name))  # ''
# bob.last_name = 'Smith'
# print(bob.name)             # Robert Smith

# bob.name = 'Prince'
# print(bob.first_name)       # Prince
# print(repr(bob.last_name))  # ''

# bob.name = 'John Adams'
# print(bob.first_name)       # John
# print(bob.last_name)        # Adams

# Without adding any code to the Person class, we want to compare bob and rob to see whether they both have the same name. How can we make this comparison?

bob = Person('Robert Smith')
rob = Person('Robert Smith')
print(bob.name == rob.name)

# What does the below print?

bob = Person('Robert Smith')
print(f"The person's name is: {bob}")

# memory address

# If we override __str__ in the class, the above will print the name correctly since print calls str on all of the objects inside of it