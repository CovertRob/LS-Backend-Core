# Problem sets from the lessons

# Inheritance

# Create a subclass from Dog called Bulldog overriding the sleep method to return "snoring!"

# Create a new class called Cat, which can do everything a dog can except fetch. Come up with a class hierarchy.

class Animal:

    def speak():
        pass

    def sleep(self):
        return 'sleeping!'
    
    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Animal):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Bulldog(Dog):

    def sleep(self):
        return "snoring!"
    
class Cat(Animal):
    def speak(self):
        return 'meow!'

# teddy = Dog()
# print(teddy.speak())      # bark!
# print(teddy.sleep())       # sleeping!

# karl = Bulldog()
# print(karl.speak())       # bark!
# print(karl.sleep())        # snoring!

pet = Animal()
dave = Dog()
bud = Bulldog()
kitty = Cat()

# 
# try:print(pet.run())              # running!
# # print(kitty.run())            # running!
# # print(kitty.speak())          # meow!
#     kitty.fetch()
# except Exception as exception:
#     print(exception.__class__.__name__, exception, "\n")
    # AttributeError: 'Cat' object has no attribute 'fetch'

# print(dave.speak())           # bark!

# print(bud.run())              # running!
# print(bud.sleep())             # "snoring!"

# Class hierarchy

#       Pet
#   Dog      Cat
#  Bulldog

# What is the method resolution order and why is it important?
# The MRO is the order in which Python searches through a class and its superclasses for applicable instance methods. It determines which instance method will be executed when overriding them in subclasses. AKA it is how Python traverses the class hierarchy to look for methods.

# Use the following list comprehension to pretty print MRO
# print([ cls.__name__ for cls in Bulldog.mro() ])
# ['Bulldog', 'Dog', 'Pet', 'object']

# Name the method used to customize each operator

# > uses __gt__
# * uses __mul__
# <= uses __le__
# != uses __ne__
# += uses __iadd__
# **= uses __ipow__
# // uses __floordiv__

# Consider the following class:

class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, value: Cat) -> bool:
        if not isinstance(value, Cat):
            return NotImplemented
        return self.name.casefold() == value.name.casefold()

    def __ne__(self, value: object) -> bool:
        if not isinstance(value, Cat):
            return NotImplemented
        return self.name.casefold() != value.name.casefold()
    
    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() < other.name.casefold()
    
    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() <= other.name.casefold()

    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() > other.name.casefold()

    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() >= other.name.casefold()

# Create the methods needed so you can compare Cat objects for equality and inequality by their name value. The comparisons should ignore case and should work for the == and !=operators. If the right-hand operand is not a Cat object, the methods should return NotImplemented.

# Be sure to write test cases to demonstrate that your methods work as intended.

# bugs = Cat('Bugs')
# bugs2 = Cat('Bugs')
# elmer = Cat('Elmer')

# print(bugs == elmer)                # False
# print(bugs == bugs2)                # True

# print(bugs != elmer)                # True
# print(bugs != bugs2)                # False

# print(bugs == 'Bugs')               # False
# print(bugs != 'Bugs')               # True

# Implementation note: use casefold() because lower() does not handle certain unicode characters correctly.

# Implement the rest of the comparison operator methods

# Given the following Vector class:
# Implement addition, subtraction, and multipllication

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)
    
    def __isub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Vector(self.x * other, self.y * other)
    
    # Needed when the left operand is an integer
    def __rmul__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        return Vector(self.x * other, self.y * other)


# print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
# print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
# print(Vector(5, 12) * 2)              # Vector(10, 24)
# print(3 * Vector(5, 12))              # Vector(15, 36)

# my_vector = Vector(5, 7)
# my_vector += Vector(3, 9)             # Vector(8, 16)
# print(my_vector)

# my_vector -= Vector(1, 7)
# print(my_vector)                      # Vector(7, 9)

# print(Vector(3, 2) + 5)
# TypeError: unsupported operand type(s) for +: 'Vector'
# and 'int'

# If both x and y can be expressed an integers, compute the sum of the integer values of x and y.
# otherwise, concatenate the string values of x and y

class Silly:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Silly({repr(self.value)})'

    def _is_numeric(self, value):
        if isinstance(value, int):
            return True

        return value.isdigit()

    def __add__(self, other):
        if not isinstance(other, int):
            if not isinstance(other, str):
                return NotImplemented

        both_numeric = (self._is_numeric(self.value) and
                        self._is_numeric(other))
        if both_numeric:
            return Silly(int(self.value) + int(other))
        else:
            return Silly(str(self.value) + str(other))
        
# Properties problem set

# 1. Create a Person class with a "private" attribute _name. Use properties to create a getter and setter for the _name attribute. The _name attribute must be a string. Test code

class Person:
    def __init__(self, name) -> None:
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
           raise TypeError('Name must be a string')
        if name.strip() == '':
            raise ValueError('Name must not be empty')
        self._name = name

# rob = Person('Rob')
# print(rob.name)
# rob.name = 'mike'
# print(rob.name)
#rob.name = 123

# Update to disallow empty strings. Raise a ValueError

# rob.name = '    '
# print(rob.name)

# 3. Create a Rectangle class with attributes _width and _height. Add properties to get the width and height but to disallow modification after the object is created (i.e. no setters)

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
    
# rec = Rectangle(3, 7)
# rec.width = 8

# Write a brightness property for the class

class SmartLamp:
    def __init__(self, color, brightness):
        self.color = color
        self.brightness = brightness

    def glow(self):
        return (f'The lamp glows {self.color} with '
                f'brightness {self.brightness}%.')

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('Color must be a color name.')
        self._color = color

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        if isinstance(brightness, int):
            if 0 <= brightness <= 100: # This expression shorthand is unique to Python, Fortran, Julia, and Perl 6
                self._brightness = brightness
                return

        raise ValueError('Brightness must be between 0 and 100.')

# Problem Set: Scope

# Define a Dog class that has a breed instance variable. Instantiate two objects from this class, one with the breed 'Golden Retriever' and another with the breed 'Poodle'. Print the breed of each dog.

class Dog:
    def __init__(self, breed):
        self.breed = breed

# dog1 = Dog('Golden Retriever')
# dog2 = Dog('Poodle')

# print(dog1.breed)  # Golden Retriever
# print(dog2.breed)  # Poodle

# 2 Create a getter and mark for internal use
class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

# dog1 = Dog('Golden Retriever')
# dog2 = Dog('Poodle')

# print(dog1.get_breed())  # Golden Retriever
# print(dog2.get_breed())  # Poodle

# 3. Create a Cat class that has a single method named get_name that returns the name instance variable. Without initializing name, try to instantiate a Cat object and call get_name. Print Name not set! when the error occurs.

class Cat:
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return "Name not set!"

# cat = Cat()
# print(cat.get_name())  # Name not set!    
# # Problem Sets Exceptions:

# 1. Write a program that asks the user for two numbers and divides the first number by the second number. Handle any potential ZeroDivisionError or ValueError exceptions

def divide_nums():
    print('Enter two numbers')
    try:
        num1 = int(input('Enter number 1: '))
        num2 = int(input('Enter number 2: '))
        divide = num1 / num2
    except ZeroDivisionError:
        print('Cannot divide by 0')
    except ValueError:
        print('Value must be an integer')
    else:
        print(divide)
    finally:
        print('End of program')

# divide_nums()

# Print only when no exceptions raised

# Modify to  handle on single exception line

def divide_nums():
    print('Enter two numbers')
    try:
        num1 = int(input('Enter number 1: '))
        num2 = int(input('Enter number 2: '))
        divide = num1 / num2
    except (ZeroDivisionError, ValueError) as e:
        print(e)
    else:
        print(divide)
    finally:
        print('End of program')

# divide_nums()

# Write a program that asks the user for a number. If the input isn't a number, let Python raise an appropriate exception. If the number is negative, raise a ValueError with an appropriate error message. If the number isn't negative, print a message that shows its value.

def prob_3():
    num = float(input('Enter a number: '))
    if num < 0:
        raise ValueError('Negative numbers are not allowed!')
    print(f'You entered {num}')

# prob_3()

# 5. Modify your answer from the previous problem to raise a custom exception named NegativeNumberError instead of an ordinary ValueError exception.

class NegativeNumberError(ValueError):
    pass

def prob_5():
    num = float(input('Enter a number: '))
    if num < 0:
        raise NegativeNumberError('Negative numbers are not allowed!')
    print(f'You entered {num}')

def inverse(numbers):
    result = []
    for num in numbers:
        try:
            result.append(1 / num)
        except ZeroDivisionError:
            result.append(float('inf'))
    return result

# In some cases, a floating point number divided by 0 can be treated as infinity. In Python, infinity is represented by the name inf. This name can't be access directly; if you want an infinite value, you need to use float('inf') or float('infinity'). That's one possible solution to what happens when you divide by 0.

#print(inverse([1, 2, 0, 3, 4]))

# Write two functions to fetch the sixth element from the list: one using the LBYL approach and another using the AFNP approach. In both cases, the function should return None when the element isn't found.

numbers = [1, 2, 3, 4, 5]

# LBYL approach
def get_sixth_element_lbyl():
    if len(numbers) > 5:
        return numbers[5]

    return None

# AFNP approach
def get_sixth_element_afnp():
    try:
        return numbers[5]
    except IndexError:
        return None

# 'hello'.upper()
# #[1, 2, 3].push(4)
# {'key': 'value'}.get('key')
# (12345).length()

class Point:
    def __init__(self, x, y):
        self.coordinates = {'x': x, 'y': y}

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        print(self.coordinates)
        print(other.coordinates)
        return self.coordinates == other.coordinates

# point1 = Point(5, 10)
# point2 = Point(5, 10)
# point3 = point1
# point1.coordinates['x'] = 4

# print(point1 == point2)
# print(point2 == point3)
# print(point1 == point3)
# print(point3 is point1)


# Practice Problems

# 1.
# print(True.__class__.__name__)                      # bool
# print('hello'.__class__.__name__)                   # str
# print([1, 2, 3, 'happy days'].__class__.__name__)   # list
# print({1, 2, 3}.__class__.__name__)                 # set
# print((142).__class__.__name__)                     # int
# print(1.2345.__class__.__name__)                    # float

# How does self.__class__.__name__ work

# We use self.__class__.__name__ in the method. It works like so:

# self refers to the object referenced by small_car. In this case, that's a Car object.
# self.__class__ returns a reference to the Car class, which is an object of type class.
# Finally, self.__class__.__name__ returns the name of the Car class as a string: 'Car'.

# Which of the following classes create objects with instance vars?

class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

#         Pizza class instances will have instance variables by virtue of assigning a value to self.my_name in the Pizza.__init__ method. Fruit class instances don't have instance variables since none are defined. my_name is a local variable only defined inside Fruit.__init__.

# You can verify this by using the vars function to see what instance variables exist in Pizza and Fruit objects:

# print(vars(Fruit('orange')))     # {}
# print(vars(Pizza('pepperoni')))  # {'my_name': 'pepperoni'}

# 8

# Suppose you have an object named my_obj and that you want to call a method named foo using my_obj as the caller. How can you see where Python will look for the method. You don't need to determine the actual method location; just identifying the search sequence is sufficient.

# use print(my_obj.__class__.mro()) method
# MRO is also called the lookup chain

# List the type of variable

# excited_dog = 'excited dog' : local var
# self.excited_dog = 'excited dog' : instance var
# self.__class__.excited_dog = 'excited dog' : class var
# BigDog.excited_dog = 'excited dog' : class var

# You can tell based on the prefixes

# Explain _catsc_count

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count
    
# Increments how many Cat objects have been created
    
# cat1 = Cat('or')
# cat2 = Cat('or')
# cat3 = Cat('or')
# print(Cat.cats_count())

# Easy 2 problem set

# Benefits of using OOP in Python
# Encapsulation of code
# Using polymorphism to define features
# Custom behaviors defined
# Manages program complexity
# Allows programmers to think about code at a more abstract level
# Different kinds of data

# 4
# Hello
# AttributeError
# TypeError
# Goodbye
# TypeError because not defined as a class method

# If you have an instance method and a class method named the same, using an instance of the class, Python will call the class method instead

# 6
class Cat:
    def __init__(self, type):
        self.type = type

    def __str__(self) -> str:
        return f"I am a {self.type}"
#print(Cat('hairball'))
# <__main__.Cat object at 0x10695eb10>

# 7
# You can call class methods with class instances but cannot call instance methods with the class name

# Medium problem set

# 1.
class BankAccount:
    def __init__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance
    
# Using self.balance is fine here because it is defined as a property getter

# 2 Update InvoiceEntry so it functions as shown

class InvoiceEntry:
    def __init__(self, product_name, number_purchased):
        self._product_name = product_name
        self._quantity = number_purchased

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        self._quantity = value

# entry = InvoiceEntry('Marbles', 5000)
# print(entry.quantity)         # 5000

# entry.quantity = 10_000
# print(entry.quantity)         # 10_000

class Animal:
    def speak(self, argv):
        print(argv)

class Cat(Animal):
    def meow(self):
        self.speak('Meow')

class Dog(Animal):
    def bark(self):
        self.speak('Woof! Woof! Woof!')

# Given the following code, write additional code fro KrispyKreme such that the print invocations will work as shown

class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing

    def __str__(self) -> str:
        if self.filling == None:
            fill = 'Plain'
        else:
            fill = self.filling
        if self.glazing == None:
            return fill
        return f"{fill} with {self.glazing}"
        

# donut1 = KrispyKreme(None, None)
# donut2 = KrispyKreme('Vanilla', None)
# donut3 = KrispyKreme(None, 'sugar')
# donut4 = KrispyKreme(None, 'chocolate sprinkles')
# donut5 = KrispyKreme('Custard', 'icing')

# print(donut1)       # Plain
# print(donut2)       # Vanilla
# print(donut3)       # Plain with sugar
# print(donut4)       # Plain with chocolate sprinkles
# print(donut5)       # Custard with icing

# LS solution:

# Put this code in the KrispyKreme class
def __str__(self):
    options = []
    options.append(self.filling or 'Plain')
    if self.glazing is not None:
        options.append(self.glazing)

    return ' with '.join(options)


# Catamaran is being added in. Modify the class definitions and move code into a mix-in, as necessary, to share code among Catamaran and the wheeled vehicles.

class FuelStatsMixin:

    def fuel_params(self, kilometers_per_liter, liters_of_fuel_capacity):
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class WheeledVehicle(FuelStatsMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_params(kilometers_per_liter, liters_of_fuel_capacity)

    def tire_pressure(self, tire_index):
        self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)

class Watercraft(FuelStatsMixin):
    def __init__(self,
                 number_propellers,
                 number_hulls,
                 fuel_efficiency,
                 fuel_capacity):
        self.propellers = number_propellers
        self.hulls = number_hulls
        self.fuel_params(fuel_efficiency, fuel_capacity)

    def range(self):
        return super().range() + 10

class Motorboat(Watercraft):
    def __init__(self, kilometers_per_liter, liters_of_fuel_capacity) -> None:
        super().__init__(1, 1, kilometers_per_liter, liters_of_fuel_capacity)

class Catamaran(Watercraft):
  def __init__(self,
               number_propellers,
               number_hulls,
               kilometers_per_liter,
               liters_of_fuel_capacity):
      super().__init__(number_propellers, number_hulls, 
                       kilometers_per_liter, liters_of_fuel_capacity)
      

# auto = Auto()
# motorcycle = Motorcycle()
# catamaran = Catamaran(2, 2, 1.5, 600)

# print(auto.fuel_efficiency)             # 50
# print(auto.fuel_capacity)               # 25.0
# print(auto.range())                     # 1250.0

# print(motorcycle.fuel_efficiency)       # 80
# print(motorcycle.fuel_capacity)         # 8.0
# print(motorcycle.range())               # 640.0

# print(catamaran.fuel_efficiency)        # 1.5
# print(catamaran.fuel_capacity)          # 600
# print(catamaran.range())                # 900.0