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

