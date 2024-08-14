# Find the class
# Update the following code so that instead of printing values, each statement prints the name of the class to which it belongs

# Comments show expected output
# print("Hello".__class__)                # <class 'str'>
# print((5).__class__)                      # <class 'int'>
# print(([1, 2, 3]).__class__)              # <class 'list'>

# print(type("Hello"))                # <class 'str'>
# print(type(5))                      # <class 'int'>
# print(type([1, 2, 3]))              # <class 'list'>

# Create the class
# create an empty class named Cat

import copy


class Cat:

    def __init__(self) -> None:
        print('I am a cat!')

# Create the object
# using code from above, create an instance of Cat and assign it to a variable named kitty
#kitty = Cat()

# Hello, Sophie (Part 1)

# Using code from above, add a parameter to init that provides a name for the Cat object. Use an instance variable to print a greeting with the provided name.

class Cat:

    def __init__(self, name) -> None:
        self._name = name
        print(f"Hello, my name is {self._name}")

#kitty = Cat('Sohpie')

# Part 2
# Move the greeting from init method to an instance method named greet that prints a greeting when invoked. Make sure you write some code that invokes the method

class Cat:

    def __init__(self, name) -> None:
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def greet(self):
        print(f"Hello! My name is {self.name}")

# kitty = Cat('Sophie')
# kitty.greet()

# Privacy
# Modify the instance variable so it indicates it is intended for internal use -> already did this

# Modify the code to use a getter with name instead of accessing the instance variable

# Add a setter method named name

# kitty.name = 'Luna'
# kitty.greet()

# Default Person
# Create a class named Person.

# When you instantiate a Person object, you should pass in one argument that contains the person's name.

# If no arguments are given, the Person object should be instantiated with a name of "John Doe".

class Person:

    def __init__(self, name="John Doe") -> None:
        self.name = name

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 1:
            self._name = new_name

person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
# print(person1.name)    # John Doe
# print(person2.name)    # Pepe Le Pew
        
# Generic Greeting Part 1
# Create a class named Cat for which calling Cat.generic_greeting prints Hello! I'm a cat!

class Cat:

    @classmethod
    def generic_greeting(cls):
        print('Hello! I am a cat!')

# Cat.generic_greeting()
# kitty = Cat()
# # also works:
# type(kitty).generic_greeting()

# Hello, Chloe
# Using the following code, add an instance method named rename that renames kitty when invoked

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def rename(self, new_name):
        self.name = new_name

# Comments show expected output
# kitty = Cat('Sophie')
# print(kitty.name)             # Sophie
# kitty.rename('Chloe')
# print(kitty.name)             # Chloe

# Identify Yourself Part 1
# Add a method named identify that returns the calling object

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def identify(self):
        return self

# Comments show expected output
# kitty = Cat('Sophie')
# print(kitty.identify())
# <__main__.Cat object at 0x10508c8d0>
# The object ID (0x105...) may vary

# Generic Greeting Part 2
# Using the following code, add two methods: generic_greeting and personal_greeting. The first method should be a class method and print a greeting that's generic to the class. The second method should be an instance method and print a greeting that's custom to the object.

class Cat:

    @classmethod
    def generic_greeting(self):
        print('Hello! I am a cat!')
    
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def personal_greeting(self):
        print(f"Hello, My name is {self.name}!")

#kitty = Cat('Sophie')

# Comments show expected output
# Cat.generic_greeting()        # Hello! I'm a cat!
# kitty.personal_greeting()     # Hello! My name is Sophie!

# Counting Cats

# Create a class named Cat that tracks the number of times a new Cat object is instantiated. The total number of Cat instances should be printed when total is invoked

class Cat:

    cat_counter = 0

    def __init__(self) -> None:
        Cat.cat_counter += 1
    
    @classmethod
    def total(cls):
        print(cls.cat_counter)
    
# Cat.total()         # 0

# kitty1 = Cat()
# Cat.total()         # 1

# kitty2 = Cat()
# Cat.total()         # 2

# print(Cat())        # <__main__.Cat object at 0x104ed7290>
# Cat.total()         # 3

# Create a class named Cat that prints a greeting when the greet instance method is invoked. The greeting should include the name and color of the cat. Use a class constant to define the color.

class Cat:

    COLOR = 'purple'

    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name 

    def greet(self):
        print(f"Hello! My name is {self.name} and I'm a {Cat.COLOR} cat!")

# kitty = Cat('Sophie')
# kitty.greet()

# Update the following code so that it prints I'm Sophie when it invokes print(kitty)

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def __str__(self) -> str:
        return f"I'm {self.name}!"

# Comments show expected output
# kitty = Cat('Sophie')
# print(kitty)        # I'm Sophie!

# Inheritance Problems

# Using the following code, create two classes -- Truck and Car -- that both inherit from Vehicle.

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year
    
class Truck(Vehicle):

    def __init__(self, year) -> None:
        super().__init__(year)

class Car(Vehicle):

    def __init__(self, year) -> None:
        super().__init__(year)

# Comments show expected output
# truck1 = Truck(1994)
# print(truck1.year)            # 1994

# car1 = Car(2006)
# print(car1.year)              # 2006

# Change the following code so that creating a new Truck automatically calls start_engine

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):

    def __init__(self, year):
        super().__init__(year)
        self.start_engine()

    def start_engine(self):
        print('Ready to go!')

# Comments show expected output
# truck1 = Truck(1994)          # Ready to go!
# print(truck1.year)            # 1994

# Using the following code, modify Truck to accept a second argument when instantiating a new Truck object. Name the parameter bed_type. Ensure that the Car constructor contiues to accept only one argument

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):

    def __init__(self, year, bed='Short'):
        super().__init__(year)
        self._bed_type = bed
    
    @property
    def bed_type(self):
        return self._bed_type

class Car(Vehicle):
    pass

# Comments show expected output
# truck1 = Truck(1994, 'Short')
# print(truck1.year)            # 1994
# print(truck1.bed_type)        # Short

# car1 = Car(2006)
# print(car1.year)              # 2006
# print(car1.bed_type)
# AttributeError: 'Car' object has no attribute 'bed_type'

# Given the following code, modify Truck.start_engine by appending 'Drive fast, please!' to the return value of Vehicle.start_engine. The 'fast' in 'Drive fast, please!' should be taken from the value of the speed argument.

class Vehicle:
    def start_engine(self):
        return 'Ready to go!'

class Truck(Vehicle):
    def start_engine(self, speed):
        return super().start_engine() + f" Drive {speed} please!"

# Comments show expected output
# truck1 = Truck()
# print(truck1.start_engine('fast'))
# # Ready to go! Drive fast, please!

# truck2 = Truck()
# print(truck1.start_engine('slow'))
# # Ready to go! Drive slow, please!

# Using the following code, create a mix-in named WalkingMixin that contains a method named walk. This method should print Let's go for a walk! when invoked. Include WalkingMixin in Cat.

class WalkingMixin:

    def walk(self):
        print("Let's go for a walk!")

class Cat(WalkingMixin):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

# Comments show expected output
# kitty = Cat('Sophie')
# kitty.greet()       # Hello! My name is Sophie!
# kitty.walk()        # Let's go for a walk!

# Using the following code, create a Towable mix-in that contains a method named tow. This method should print I can tow a trailer! when invoked. The mix-in should be included in the Truck class.

class TowableMixin:

    def tow(self):
        print("I can tow a trailer!")

class Truck(TowableMixin):
    pass

class Car:
    pass

# Comments show expected output
# truck1 = Truck()
# truck1.tow()        # I can tow a trailer!

# car1 = Car()
# car1.tow()
# AttributeError: 'Car' object has no attribute 'tow'

# Given the following code, create a class named Vehicle that, upon instantiation, assigns the passed-in argument to self.year. Both Truck and Car should inherit from Vehicle.

class TowingMixin:
    def tow(self):
        return 'I can tow a trailer!'
    
class Vehicle:

    def __init__(self, year) -> None:
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(TowingMixin, Vehicle):
    pass

class Car(Vehicle):
    pass

# Comments show expected output
# truck1 = Truck(1994)
# print(truck1.year)            # 1994
# print(truck1.tow())           # I can tow a trailer!

# car1 = Car(2006)
# print(car1.year)              # 2006

# Using the code below, determine the method resolution order (MRO) used when accessing cat1.color. Only list the classes that are checked by Python when searching for the color attribute. Do not use the mro method.

class Animal:
    def __init__(self, color):
        self.color = color

class Cat(Animal):
    pass

class Bird(Animal):
    pass

# cat1 = Cat('Black')
# print(cat1.color)

# Cat -> Animal

# determine MRO on cat1.color

class Animal:
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

# cat1 = Cat()
# cat1.color

# Cat -> Animal -> Object -> raises AttributeError

# Determine bird1.color MRO

class FlyingMixin:
    def fly(self):
        return "I'm flying!"

class Animal:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Cat(Animal):
    pass

class Bird(FlyingMixin, Animal):
    pass

# bird1 = Bird('Red')
# print(bird1.color)

# Bird -> FlyingMixin -> Animal

# Easy OO Problems

# Banner Class

class Banner:
    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self._message

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return '|' + ' '*len(self.message) + '  |'

    def _horizontal_rule(self):
        return '+' + '-'*len(self.message) + '--+'

    def _message_line(self):
        return f"| {self.message} |"
    

# Comments show expected output

# banner = Banner('To boldly go where no one has gone before.')
# print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

# banner = Banner('')
# print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+

# Rectangle

# Create a rectangle class whose initializer takes two arguments that represent the rectangle's width and height, respectively. Use the following code to test:

class Rectangle:

    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @property
    def area(self):
        return self._width * self._height

# rect = Rectangle(4, 5)

# print(rect.width == 4)        # True
# print(rect.height == 5)       # True
# print(rect.area == 20)        # True

# Rectangles and Squares

# Given the class from previous problem, write a class called Square that inherits from Rectangle class. The Square class is used like this:

class Square(Rectangle):

    def __init__(self, size) -> None:
        super().__init__(size, size)

# square = Square(5)
# print(square.area == 25)      # True

# Complete the Program - Cats

class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color

    @property
    def color(self):
        return self._color
    
    @property
    def info(self):
        return f"My cat {self.name} is {self.age} years old and has {self.color} fur."


# My cat Cocoa is 3 years old and has black fur.
# My cat Cheddar is 4 years old and has yellow and white fur.

# cocoa = Cat('Cocoa', 3, 'black')
# cheddar = Cat('Cheddar', 4, 'yellow and white')

# print(cocoa.info)
# print(cheddar.info)

# Given the following Animal class, create two more classes Cat and Dog that inherit from it

class Animal:
    def __init__(self, name, age, legs, species, status):
        self.name = name
        self.age = age
        self.legs = legs
        self.species = species
        self.status = status

    def introduce(self):
        return (f"Hello, my name is {self.name} and I am "
                f"{self.age} years old and {self.status}.")
    
class Cat(Animal):
    LEGS = 4
    SPECIES = 'cat'
    def __init__(self, name, age, status) -> None:
        super().__init__(name, age, self.LEGS, self.SPECIES, status)

    def introduce(self):
        return super().introduce() + ' Meow meow!'

class Dog(Animal):
    LEGS = 4
    SPECIES = 'dog'

    def __init__(self, name, age, status, owner) -> None:
        super().__init__(name, age, self.LEGS, self.SPECIES, status)
        self._owner = owner

    @property
    def owner(self):
        return self._owner

    def introduce(self):
        return super().introduce() + ' Woof! Woof!'

    def greet_owner(self):
        return f"Hi {self.owner}! Woof! Woof!"

    
# cat = Cat("Pepe", 4, "happy")
# expected = ("Hello, my name is Pepe and I am 4 years old "
#             "and happy. Meow meow!")

# print(cat.introduce() == expected)      # True

# dog = Dog("Bobo", 9, "hungry", "Daddy")
# expected = ("Hello, my name is Bobo and I am 9 years old "
#             "and hungry. Woof! Woof!")
# print(dog.introduce() == expected)                  # True
# print(dog.greet_owner() == "Hi Daddy! Woof! Woof!") # True

# Consider the following code:

class Pet:
    def __init__(self, species, name) -> None:
        self._species = species
        self._name = name

    @property
    def species(self):
        return self._species
    
    @property
    def name(self):
        return self._name

class Owner:

    def __init__(self, name) -> None:
        self._name = name
        self._number_of_pets = 0

    def number_of_pets(self):
        return self._number_of_pets

    def adopted_a_pet(self):
        self._number_of_pets += 1

    @property
    def name(self):
        return self._name 
    
class Shelter:
    def __init__(self) -> None:
        self._owners = {}

    @property
    def owners(self):
        return self._owners

    def adopt(self, owner, pet):
        if owner in self.owners.keys():
            self.owners[owner].append(pet)
        else:
            self.owners[owner] = [pet]
        owner.adopted_a_pet()

    def print_adoptions(self):
        for owner in self.owners.keys():
            print(f"{owner.name} has adopted the following pets")
            for pet in self.owners[owner]:
                print(f"a {pet.species} named {pet.name}")


# cocoa   = Pet('cat', 'Cocoa')
# cheddar = Pet('cat', 'Cheddar')
# darwin  = Pet('bearded dragon', 'Darwin')
# kennedy = Pet('dog', 'Kennedy')
# sweetie = Pet('parakeet', 'Sweetie Pie')
# molly   = Pet('dog', 'Molly')
# chester = Pet('fish', 'Chester')

# phanson = Owner('P Hanson')
# bholmes = Owner('B Holmes')

# shelter = Shelter()
# shelter.adopt(phanson, cocoa)
# shelter.adopt(phanson, cheddar)
# shelter.adopt(phanson, darwin)
# shelter.adopt(bholmes, kennedy)
# shelter.adopt(bholmes, sweetie)
# shelter.adopt(bholmes, molly)
# shelter.adopt(bholmes, chester)

# shelter.print_adoptions()
# print(f"{phanson.name} has {phanson.number_of_pets()} "
#       "adopted pets.")
# print(f"{bholmes.name} has {bholmes.number_of_pets()} "
#       "adopted pets.")

# Write the classes and methods to make this code run and log the following output:

# P Hanson has adopted the following pets:
# a cat named Cocoa
# a cat named Cheddar
# a bearded dragon named Darwin

# B Holmes has adopted the following pets:
# a dog named Molly
# a parakeet named Sweetie Pie
# a dog named Kennedy
# a fish named Chester

# P Hanson has 3 adopted pets.
# B Holmes has 4 adopted pets.

# Refactor so they all use a common superclass:

class Vehicle:

    def __init__(self, make, model) -> None:
        self._make = make
        self._model = model

    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    
    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def get_wheels(self):
        return 4

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def get_wheels(self):
        return 2

    def info(self):
        return f"{self.make} {self.model}"

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload

    def get_wheels(self):
        return 6

# Given the following classes, modify the code to makke the desired output

class WalkMixin:

    def walk(self):
        return f"{self.name} {self.gait()} forward"

class Person(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"

# mike = Person("Mike")
# print(mike.walk())  # Expected: "Mike strolls forward"

# kitty = Cat("Kitty")
# print(kitty.walk())  # Expected: "Kitty saunters forward"

# flash = Cheetah("Flash")
# print(flash.walk())  # Expected: "Flash runs forward"

# Now that we have a WalkMixin mix-in, we are given a new challenge. Apparently some of our users are nobility, and the regular way of walking simply isn't good enough. Nobility struts.

# We need a new class Noble that shows the title and name when walk is called. We also require access to name and title; they are needed for other purposes that we aren't showing here.

class Noble(WalkMixin):
    def __init__(self, name, title) -> None:
        self._name = name
        self._title = title

    @property
    def name(self):
        return self._name
    
    @property
    def title(self):
        return self._title
    
    def walk(self):
        return self.title + " "+ WalkMixin.walk(self)

    def gait(self):
        return "struts"
    
# LS: the better way to do this is to define __str__ methods for each class and in the Noble class have the __str__ method return the name combined with the noble status, so when printing "self" in the walk method it uses the modified __str__ method.

# byron = Noble("Byron", "Lord")
# print(byron.walk())  # "Lord Byron struts forward"
# print(byron.name)    # "Byron"
# print(byron.title)   # "Lord"

# Modify class to get the output

class House:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __lt__(self, other):
        return self.price < other.price
    
    def __gt__(self, other):
        return self.price > other.price
    
    # need to implement type checking here, reference LS's solution

# def __gt__(self, other):
#         if isinstance(other, House):
#             return self._price > other._price

#         return NotImplemented

# home1 = House(100000)
# home2 = House(150000)
# if home1 < home2:
#     print("Home 1 is cheaper")
# if home2 > home1:
#     print("Home 2 is more expensive")

# Home 1 is cheaper
# Home 2 is more expensive


# Implement a Wallet class that represents a wallet with a certain amount of money. You want to be able to combine (add) two wallets together to get a new wallet with the combined total amount from both wallets.

# And Wallet pt 2 with str

class Wallet:
    
    def __init__(self, value) -> None:
        self._value = value

    @property
    def amount(self):
        return self._value
    
    def __add__(self, other):
        if isinstance(other, Wallet):
            return Wallet(self.amount + other.amount)

    def __str__(self):
        return f"Wallet with ${self.amount}"
    
# wallet1 = Wallet(50)
# wallet2 = Wallet(30)
# merged_wallet = wallet1 + wallet2
# print(merged_wallet.amount == 80)       # True
# print(merged_wallet)

# Write a class such that the following code prints the results indicated by the comments:

class Transform:

    def __init__(self, phrase: str) -> None:
        self._phrase = phrase

    @classmethod
    def lowercase(cls, phrase):
        return phrase.lower()

    @property
    def phrase(self):
        return self._phrase
    
    def uppercase(self):
        return self.phrase.upper()

# From LS: lowercase could also be a static method since it doens't interact wiht or depend on class-specific details. It's essentially a utility function related to the class.

# my_data = Transform('abc')
# print(my_data.uppercase())              # ABC
# print(Transform.lowercase('XYZ'))       # xyz

#--------------------------------Medium Problems-------------------------------#

# Implement Circular Buffer

# This first implementation did not work...

# class CircularBuffer:

#     def __init__(self, size) -> None:
#         self._max_buffer_size = size
#         self._buffer = []
#         self._oldest_obj_idx = 0 # value changes

#     def buffer_full(self):
#         if len(self._buffer) == self.max_buffer_size:
#             return True
#         return False

#     @property
#     def max_buffer_size(self):
#         return self._max_buffer_size
    
#     def put(self, obj):
#         # if the buffer is not full, append the element to the list
#         # if the buffer is full:
#             # remove the oldest object from the buffer
#             # replace the removed oldest object with the new object
#             # if the oldest obj idx is less than the length, increment it
#             # else, set the oldest obj idx back to 0

#         if self.buffer_full():
#             current_oldest_idx = copy.copy(self._oldest_obj_idx)
#             self.get()
#             self._buffer.insert(current_oldest_idx, obj)
            
#         else:
#             self._buffer.append(obj)

#     def get(self): # remove and return the oldest object, Return None if empty
#         # if the buffer lenght is 0, return None
#         # remove and then return the object at the oldest obj idx
#         if len(self._buffer) == 0:
#             return None
#         oldest = self._buffer.pop(self._oldest_obj_idx)
        
        
#         return oldest
    
        '''
        If the buffer started out not full, leave the oldest idx alone
        If the buffer was full, increment the oldest idx by 1
if len(self._buffer) == self._max_buffer_size - 1 and self._oldest_obj_idx < self._max_buffer_size - 1:
                self._oldest_obj_idx += 1
                print('executed')
        else:
            self._oldest_obj_idx = 0
        '''

# other solution from user submitted:

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self._buffer = []

    def put(self, object):
        if len(self._buffer) == self.size:
            self._buffer.pop(0)                       

        self._buffer.append(object)

    def get(self):
        return self._buffer.pop(0) if self._buffer else None
    
# LS's solution...confusing af

class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size
        self.next = 0
        self.oldest = 0

    def put(self, obj):
        next_item = (self.next + 1) % len(self.buffer)

        if self.buffer[self.next] is not None:
            self.oldest = next_item

        self.buffer[self.next] = obj
        self.next = next_item

    def get(self):
        value = self.buffer[self.oldest]
        self.buffer[self.oldest] = None
        if value is not None:
            self.oldest += 1
            self.oldest %= len(self.buffer)

        return value
        

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)

buffer.put(2)

print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True